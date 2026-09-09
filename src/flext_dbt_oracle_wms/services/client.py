"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from collections.abc import MutableMapping, Sequence
from typing import ClassVar

from flext_meltano import FlextMeltanoLibraryRunner
from flext_oracle_wms import FlextOracleWmsSettings, r, u as oracle_wms_u

from flext_dbt_oracle_wms import c, m, p, t, u

from .._settings import FlextDbtOracleWmsSettings


class FlextDbtOracleWmsClient:
    """DBT Oracle WMS client backed by real WMS and Meltano integrations."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        *,
        wms_client: p.DbtOracleWms.WmsClient | None = None,
        meltano_runner: p.DbtOracleWms.DbtRunner | None = None,
    ) -> None:
        """Initialize client with explicit settings and optional injected boundaries."""
        super().__init__()
        # NOTE (multi-agent): mro-rn88 — hold the effective settings (injected override or
        # global singleton) and read it via self.settings, never a bare module global.
        self._settings = settings or FlextDbtOracleWmsSettings.fetch_global()
        self._meltano_runner = meltano_runner or FlextMeltanoLibraryRunner()
        self._transformer = u.DbtOracleWms.Transformer()
        self._wms_client: p.DbtOracleWms.WmsClient | None = wms_client

    @property
    def settings(self) -> FlextDbtOracleWmsSettings:
        """The effective dbt Oracle WMS settings for this client."""
        return self._settings

    def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
        """Discover Oracle WMS entities through the owning domain client."""
        client_result = self._get_wms_client()
        if client_result.failure:
            return r[t.StrSequence].from_failure(client_result)
        return client_result.value.discover_entities()

    def extract_oracle_wms_data(
        self, entity_name: str, filters: t.ConfigurationMapping | None = None
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        """Extract entity records from Oracle WMS using the real domain client."""
        client_result = self._get_wms_client()
        if client_result.failure:
            return r[Sequence[t.ConfigurationMapping]].from_failure(client_result)
        extract_result = client_result.value.get_entity_data(
            entity_name, filters=filters
        )
        if extract_result.failure:
            return r[Sequence[t.ConfigurationMapping]].from_failure(extract_result)
        records = [dict(record) for record in extract_result.value]
        return r[Sequence[t.ConfigurationMapping]].ok(records)

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.DbtOracleWms.PipelineResult]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            r[t.StrSequence].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.failure:
            return r[m.DbtOracleWms.PipelineResult].from_failure(entities_result)
        entity_list = entities_result.value
        extracted: MutableMapping[str, t.SequenceOf[t.ConfigurationMapping]] = {}
        for entity_name in entity_list:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.failure:
                return r[m.DbtOracleWms.PipelineResult].from_failure(extract_result)
            validate_result = self.validate_oracle_wms_data(
                entity_name, extract_result.value
            )
            if validate_result.failure:
                return r[m.DbtOracleWms.PipelineResult].from_failure(validate_result)
            extracted[entity_name] = list(validate_result.value)
        transform_result = self.transform_with_dbt(extracted, model_names)
        if transform_result.failure:
            return r[m.DbtOracleWms.PipelineResult].from_failure(transform_result)
        self.logger.info("Completed Oracle WMS to DBT pipeline")
        command_result = transform_result.value
        return r[m.DbtOracleWms.PipelineResult].ok(
            m.DbtOracleWms.PipelineResult(
                processed_entities=tuple(extracted.keys()),
                total_records=sum(len(records) for records in extracted.values()),
                transformation_status=(
                    "success" if command_result.success else "failed"
                ),
                pipeline_status="completed",
            )
        )

    def test_oracle_wms_connection(self) -> p.Result[m.DbtOracleWms.ConnectionStatus]:
        """Validate Oracle WMS connectivity using the real health endpoint."""
        client_result = self._get_wms_client()
        if client_result.failure:
            return r[m.DbtOracleWms.ConnectionStatus].from_failure(client_result)
        start_result = client_result.value.start()
        if start_result.failure:
            return r[m.DbtOracleWms.ConnectionStatus].from_failure(start_result)
        health_result = client_result.value.health_check()
        if health_result.failure:
            return r[m.DbtOracleWms.ConnectionStatus].from_failure(health_result)
        response = health_result.value
        return r[m.DbtOracleWms.ConnectionStatus].ok(
            m.DbtOracleWms.ConnectionStatus(
                status="connected",
                environment=self.settings.DbtOracleWms.oracle_wms_environment,
                base_url=self.settings.DbtOracleWms.oracle_wms_base_url,
                status_code=response.status_code,
            )
        )

    def transform_with_dbt(
        self,
        entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
        model_names: t.StrSequence | None,
    ) -> p.Result[m.Meltano.CommandExecutionResult]:
        """Run DBT transformations through flext-meltano."""
        transformed_entities_result = self._transformer.transform_all_entities(
            entity_data
        )
        if transformed_entities_result.failure:
            return r[m.Meltano.CommandExecutionResult].from_failure(
                transformed_entities_result
            )
        dbt_result = self._meltano_runner.run_dbt_transformation(model_names)
        if dbt_result.failure:
            return r[m.Meltano.CommandExecutionResult].from_failure(dbt_result)
        # NOTE (multi-agent, bead mro-wfc8.3): return the typed meltano command result
        # directly (no generic wrapper, no fabricated models_run/execution_method keys).
        return dbt_result

    def validate_oracle_wms_data(
        self, entity_name: str, records: t.SequenceOf[t.ConfigurationMapping]
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        """Validate extracted records against configured entity requirements."""
        if not records:
            return r[Sequence[t.ScalarMapping]].fail("No records to validate")
        required_fields = self.settings.DbtOracleWms.required_fields_per_entity.get(
            entity_name, ()
        )
        for index, record in enumerate(records):
            missing_fields = [
                field
                for field in required_fields
                if not str(record.get(field, "")).strip()
            ]
            if missing_fields:
                return r[Sequence[t.ConfigurationMapping]].fail(
                    f"{entity_name} record {index} missing required fields: {missing_fields}"
                )
        validation_result = self._transformer.validate_business_rules(records)
        if validation_result.failure:
            return r[Sequence[t.ConfigurationMapping]].from_failure(validation_result)
        return r[Sequence[t.ScalarMapping]].ok(records)

    def _get_wms_client(self) -> p.Result[p.DbtOracleWms.WmsClient]:
        """Create and cache the real Oracle WMS client."""
        if self._wms_client is not None:
            return r[p.DbtOracleWms.WmsClient].ok(self._wms_client)
        try:
            settings_overrides: t.ConfigurationMapping = (
                {"base_url": self.settings.DbtOracleWms.oracle_wms_base_url}
                if self.settings.DbtOracleWms.oracle_wms_base_url
                else {}
            )
            # NOTE (multi-agent): mro-rn88 — fetch_global already validates via pydantic on
            # construction; the removed validate_config() method no longer exists.
            wms_settings = FlextOracleWmsSettings.fetch_global(
                overrides=settings_overrides
            )
            self._wms_client = oracle_wms_u.OracleWms.Client(settings=wms_settings)
            return r[p.DbtOracleWms.WmsClient].ok(self._wms_client)
        except c.EXC_VALIDATION_TYPE_VALUE as exc:
            return r[p.DbtOracleWms.WmsClient].fail_op(
                "Oracle WMS client initialization", exc
            )


__all__: list[str] = ["FlextDbtOracleWmsClient"]
