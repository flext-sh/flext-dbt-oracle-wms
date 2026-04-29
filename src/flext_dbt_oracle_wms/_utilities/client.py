"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from collections.abc import (
    Mapping,
    MutableMapping,
    Sequence,
)
from typing import ClassVar

from flext_dbt_oracle_wms import c, m, p, t, u
from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
from flext_meltano import FlextMeltanoLibraryRunner
from flext_oracle_wms import FlextOracleWmsSettings, FlextOracleWmsUtilitiesClient, r


class FlextDbtOracleWmsClient:
    """DBT Oracle WMS client backed by real WMS and Meltano integrations."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

    def __init__(self, settings: FlextDbtOracleWmsSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        super().__init__()
        self.settings = (
            settings
            if settings is not None
            else FlextDbtOracleWmsSettings.fetch_global()
        )
        self._meltano_runner = FlextMeltanoLibraryRunner()
        self._transformer = m.DbtOracleWms.FlextDbtOracleWmsTransformer()
        self._wms_client: FlextOracleWmsUtilitiesClient.Client | None = None

    def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
        """Discover Oracle WMS entities through the owning domain client."""
        client_result = self._get_wms_client()
        if client_result.failure:
            return r[t.StrSequence].fail(
                client_result.error or "WMS client unavailable"
            )
        return client_result.value.discover_entities()

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        """Extract entity records from Oracle WMS using the real domain client."""
        client_result = self._get_wms_client()
        if client_result.failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                client_result.error or "WMS client unavailable",
            )
        extract_result = client_result.value.get_entity_data(
            entity_name,
            filters=filters,
        )
        if extract_result.failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                extract_result.error or "Oracle WMS extraction failed",
            )
        records = [dict(record) for record in extract_result.value]
        return r[Sequence[t.ConfigurationMapping]].ok(records)

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.Dict]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            r[t.StrSequence].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.failure:
            return r[m.Dict].fail(entities_result.error or "Entity discovery failed")
        entity_list = entities_result.value
        extracted: MutableMapping[str, Sequence[t.ConfigurationMapping]] = {}
        for entity_name in entity_list:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.failure:
                return r[m.Dict].fail(extract_result.error or "Extraction failed")
            validate_result = self.validate_oracle_wms_data(
                entity_name,
                extract_result.value,
            )
            if validate_result.failure:
                return r[m.Dict].fail(validate_result.error or "Validation failed")
            extracted[entity_name] = list(validate_result.value)
        transform_result = self.transform_with_dbt(extracted, model_names)
        if transform_result.failure:
            return r[m.Dict].fail(transform_result.error or "Transformation failed")
        self.logger.info("Completed Oracle WMS to DBT pipeline")
        tr_val = transform_result.value
        return r[m.Dict].ok(
            m.Dict.model_validate({
                "processed_entities": ",".join(extracted.keys()),
                "total_records": sum(len(records) for records in extracted.values()),
                "transformation_status": str(tr_val.get("status", "")),
                "pipeline_status": "completed",
            }),
        )

    def test_oracle_wms_connection(self) -> p.Result[m.Dict]:
        """Validate Oracle WMS connectivity using the real health endpoint."""
        client_result = self._get_wms_client()
        if client_result.failure:
            return r[m.Dict].fail(client_result.error or "WMS client unavailable")
        start_result = client_result.value.start()
        if start_result.failure:
            return r[m.Dict].fail(
                start_result.error or "Oracle WMS client startup failed",
            )
        health_result = client_result.value.health_check()
        if health_result.failure:
            return r[m.Dict].fail(
                health_result.error or "Oracle WMS health check failed"
            )
        response = health_result.value
        return r[m.Dict].ok(
            m.Dict.model_validate({
                "status": "connected",
                "environment": self.settings.oracle_wms_environment,
                "base_url": self.settings.oracle_wms_base_url,
                "status_code": response.status_code,
            }),
        )

    def transform_with_dbt(
        self,
        entity_data: Mapping[str, Sequence[t.ConfigurationMapping]],
        model_names: t.StrSequence | None,
    ) -> p.Result[m.Dict]:
        """Run DBT transformations through flext-meltano."""
        transformed_entities = self._transformer.transform_all_entities(entity_data)
        dbt_result = self._meltano_runner.run_dbt_transformation(model_names)
        if dbt_result.failure:
            return r[m.Dict].fail(dbt_result.error or "DBT transformation failed")
        execution_result = dbt_result.value
        return r[m.Dict].ok(
            m.Dict.model_validate({
                "transformed_tables": ",".join(sorted(transformed_entities.keys())),
                "requested_models": ",".join(model_names or []),
                "models_run": str(execution_result.get("models_run", "")),
                "execution_method": str(
                    execution_result.get("execution_method", ""),
                ),
                "status": "success" if execution_result.get("success") else "failed",
            }),
        )

    def validate_oracle_wms_data(
        self,
        entity_name: str,
        records: Sequence[t.ConfigurationMapping],
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        """Validate extracted records against configured entity requirements."""
        if not records:
            return r[Sequence[t.ScalarMapping]].fail("No records to validate")
        required_fields = self.settings.required_fields_per_entity.get(entity_name, ())
        for index, record in enumerate(records):
            missing_fields = [
                field
                for field in required_fields
                if not str(record.get(field, "")).strip()
            ]
            if missing_fields:
                return r[Sequence[t.ConfigurationMapping]].fail(
                    f"{entity_name} record {index} missing required fields: {missing_fields}",
                )
        validation_result = self._transformer.validate_business_rules(records)
        if validation_result.failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                validation_result.error or "Oracle WMS validation failed",
            )
        return r[Sequence[t.ScalarMapping]].ok(records)

    def _get_wms_client(self) -> p.Result[FlextOracleWmsUtilitiesClient.Client]:
        """Create and cache the real Oracle WMS client."""
        if self._wms_client is not None:
            return r[FlextOracleWmsUtilitiesClient.Client].ok(self._wms_client)
        try:
            settings_overrides: t.ConfigurationMapping = (
                {"base_url": self.settings.oracle_wms_base_url}
                if self.settings.oracle_wms_base_url
                else {}
            )
            settings = FlextOracleWmsSettings.fetch_global(overrides=settings_overrides)
            validation_result = settings.validate_config()
            if validation_result.failure:
                return r[FlextOracleWmsUtilitiesClient.Client].fail(
                    validation_result.error or "Invalid Oracle WMS settings",
                )
            self._wms_client = FlextOracleWmsUtilitiesClient.Client(settings=settings)
            return r[FlextOracleWmsUtilitiesClient.Client].ok(self._wms_client)
        except (c.ValidationError, TypeError, ValueError) as exc:
            return r[FlextOracleWmsUtilitiesClient.Client].fail(
                f"Oracle WMS client initialization failed: {exc}",
            )


__all__: list[str] = ["FlextDbtOracleWmsClient"]
