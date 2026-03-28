"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence

from flext_core import FlextLogger, r
from flext_meltano import FlextMeltanoLibraryRunner
from flext_oracle_wms import FlextOracleWmsClient, FlextOracleWmsSettings
from pydantic import ValidationError

from flext_dbt_oracle_wms import t
from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels as m

logger = FlextLogger(__name__)


class FlextDbtOracleWmsClient:
    """DBT Oracle WMS client backed by real WMS and Meltano integrations."""

    def __init__(
        self, config: m.DbtOracleWms.FlextDbtOracleWmsSettings | None = None
    ) -> None:
        """Initialize client with explicit or global settings."""
        super().__init__()
        self.config = (
            config
            if config is not None
            else m.DbtOracleWms.FlextDbtOracleWmsSettings.get_global()
        )
        self._meltano_runner = FlextMeltanoLibraryRunner()
        self._transformer = m.DbtOracleWms.FlextDbtOracleWmsTransformer()
        self._wms_client: FlextOracleWmsClient | None = None

    def discover_oracle_wms_entities(self) -> r[t.StrSequence]:
        """Discover Oracle WMS entities through the owning domain client."""
        client_result = self._get_wms_client()
        if client_result.is_failure:
            return r[t.StrSequence].fail(
                client_result.error or "WMS client unavailable"
            )
        return client_result.value.discover_entities()

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> r[Sequence[t.ConfigurationMapping]]:
        """Extract entity records from Oracle WMS using the real domain client."""
        client_result = self._get_wms_client()
        if client_result.is_failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                client_result.error or "WMS client unavailable",
            )
        extract_result = client_result.value.get_entity_data(
            entity_name,
            filters=filters,
        )
        if extract_result.is_failure:
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
    ) -> r[t.Dict]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            r[t.StrSequence].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.is_failure:
            return r[t.Dict].fail(entities_result.error or "Entity discovery failed")
        entity_list = entities_result.value
        extracted: MutableMapping[str, Sequence[t.ConfigurationMapping]] = {}
        for entity_name in entity_list:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.is_failure:
                return r[t.Dict].fail(extract_result.error or "Extraction failed")
            validate_result = self.validate_oracle_wms_data(
                entity_name,
                extract_result.value,
            )
            if validate_result.is_failure:
                return r[t.Dict].fail(validate_result.error or "Validation failed")
            extracted[entity_name] = list(validate_result.value)
        transform_result = self.transform_with_dbt(extracted, model_names)
        if transform_result.is_failure:
            return r[t.Dict].fail(transform_result.error or "Transformation failed")
        logger.info("Completed Oracle WMS to DBT pipeline")
        tr_val = transform_result.value
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "processed_entities": ",".join(extracted.keys()),
                "total_records": sum(len(records) for records in extracted.values()),
                "transformation_status": str(tr_val.get("status", "")),
                "pipeline_status": "completed",
            }),
        )

    def test_oracle_wms_connection(self) -> r[t.Dict]:
        """Validate Oracle WMS connectivity using the real health endpoint."""
        client_result = self._get_wms_client()
        if client_result.is_failure:
            return r[t.Dict].fail(client_result.error or "WMS client unavailable")
        health_result = client_result.value.health_check()
        if health_result.is_failure:
            return r[t.Dict].fail(
                health_result.error or "Oracle WMS health check failed"
            )
        response = health_result.value
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "status": "connected",
                "environment": self.config.oracle_wms_environment,
                "base_url": self.config.oracle_wms_base_url,
                "status_code": response.status_code,
            }),
        )

    def transform_with_dbt(
        self,
        entity_data: Mapping[str, Sequence[t.ConfigurationMapping]],
        model_names: t.StrSequence | None,
    ) -> r[t.Dict]:
        """Run DBT transformations through flext-meltano."""
        transformed_entities = self._transformer.transform_all_entities(entity_data)
        dbt_result = self._meltano_runner.run_dbt_transformation(model_names)
        if dbt_result.is_failure:
            return r[t.Dict].fail(dbt_result.error or "DBT transformation failed")
        execution_result = dbt_result.value
        return r[t.Dict].ok(
            t.Dict.model_validate({
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
    ) -> r[Sequence[t.ConfigurationMapping]]:
        """Validate extracted records against configured entity requirements."""
        if not records:
            return r[Sequence[t.ScalarMapping]].fail("No records to validate")
        required_fields = self.config.required_fields_per_entity.get(entity_name, ())
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
        if validation_result.is_failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                validation_result.error or "Oracle WMS validation failed",
            )
        return r[Sequence[t.ScalarMapping]].ok(records)

    def _get_wms_client(self) -> r[FlextOracleWmsClient]:
        """Create and cache the real Oracle WMS client."""
        if self._wms_client is not None:
            return r[FlextOracleWmsClient].ok(self._wms_client)
        try:
            settings = FlextOracleWmsSettings.model_validate({
                "base_url": self.config.oracle_wms_base_url,
            })
            validation_result = settings.validate_config()
            if validation_result.is_failure:
                return r[FlextOracleWmsClient].fail(
                    validation_result.error or "Invalid Oracle WMS settings",
                )
            self._wms_client = FlextOracleWmsClient(config=settings)
            return r[FlextOracleWmsClient].ok(self._wms_client)
        except (ValidationError, TypeError, ValueError) as exc:
            return r[FlextOracleWmsClient].fail(
                f"Oracle WMS client initialization failed: {exc}",
            )


__all__ = ["FlextDbtOracleWmsClient"]
