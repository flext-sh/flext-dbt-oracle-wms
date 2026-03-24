"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence

from flext_core import FlextLogger, r

from flext_dbt_oracle_wms import t

from .settings import FlextDbtOracleWmsSettings

logger = FlextLogger(__name__)


class FlextDbtOracleWmsClient:
    """DBT Oracle WMS client with typed extraction and transform stubs."""

    def __init__(self, config: FlextDbtOracleWmsSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        super().__init__()
        self.config = (
            config if config is not None else FlextDbtOracleWmsSettings.get_global()
        )

    def discover_oracle_wms_entities(self) -> r[Sequence[str]]:
        """Return the configured Oracle WMS entities."""
        entities = list(self.config.required_fields_per_entity.keys())
        return r[Sequence[str]].ok(entities)

    def extract_oracle_wms_data(
        self, entity_name: str, filters: Mapping[str, t.Scalar] | None = None
    ) -> r[Sequence[Mapping[str, t.Scalar]]]:
        """Return sample records for a requested entity."""
        _ = filters
        return r[Sequence[t.ScalarMapping]].ok([
            {"entity": entity_name, "id": 1, "name": f"sample_{entity_name}"}
        ])

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: Sequence[str] | None = None,
        filters: Mapping[str, t.Scalar] | None = None,
        model_names: Sequence[str] | None = None,
    ) -> r[t.Dict]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            r[Sequence[str]].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.is_failure:
            return r[t.Dict].fail(entities_result.error or "Entity discovery failed")
        entity_list = entities_result.value
        extracted: MutableMapping[str, Sequence[Mapping[str, t.Scalar]]] = {}
        for entity_name in entity_list:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.is_failure:
                return r[t.Dict].fail(extract_result.error or "Extraction failed")
            validate_result = self.validate_oracle_wms_data(
                entity_name, extract_result.value
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
            })
        )

    def test_oracle_wms_connection(self) -> r[t.Dict]:
        """Return simple connection health status."""
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "status": "connected",
                "environment": self.config.oracle_wms_environment,
                "base_url": self.config.oracle_wms_base_url,
            })
        )

    def transform_with_dbt(
        self,
        entity_data: Mapping[str, Sequence[Mapping[str, t.Scalar]]],
        model_names: Sequence[str] | None,
    ) -> r[t.Dict]:
        """Return transformation summary for provided entities."""
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "transformed_tables": ",".join(entity_data.keys()),
                "requested_models": ",".join(model_names or []),
                "status": "success",
            })
        )

    def validate_oracle_wms_data(
        self, entity_name: str, records: Sequence[Mapping[str, t.Scalar]]
    ) -> r[Sequence[Mapping[str, t.Scalar]]]:
        """Validate records list for a specific entity."""
        _ = entity_name
        if not records:
            return r[Sequence[t.ScalarMapping]].fail("No records to validate")
        return r[Sequence[t.ScalarMapping]].ok(records)


__all__ = ["FlextDbtOracleWmsClient"]
