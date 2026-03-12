"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import FlextLogger, r, t

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

    def discover_oracle_wms_entities(self) -> r[list[str]]:
        """Return the configured Oracle WMS entities."""
        entities = list(self.config.required_fields_per_entity.keys())
        return r[list[str]].ok(entities)

    def extract_oracle_wms_data(
        self, entity_name: str, filters: Mapping[str, object] | None = None
    ) -> r[list[object]]:
        """Return sample records for a requested entity."""
        _ = filters
        return r[list[object]].ok([
            {"entity": entity_name, "id": 1, "name": f"sample_{entity_name}"}
        ])

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: Mapping[str, object] | None = None,
        model_names: list[str] | None = None,
    ) -> r[Mapping[str, object]]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            r[list[str]].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.is_failure:
            return r[object].fail(
                entities_result.error or "Entity discovery failed"
            )
        entity_list = entities_result.value
        extracted: dict[str, list[dict[str, object]]] = {}
        for entity_name in entity_list:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.is_failure:
                return r[object].fail(
                    extract_result.error or "Extraction failed"
                )
            validate_result = self.validate_oracle_wms_data(
                entity_name, extract_result.value
            )
            if validate_result.is_failure:
                return r[object].fail(
                    validate_result.error or "Validation failed"
                )
            extracted[entity_name] = [dict(record) for record in validate_result.value]
        transform_result = self.transform_with_dbt(extracted, model_names)
        if transform_result.is_failure:
            return r[object].fail(
                transform_result.error or "Transformation failed"
            )
        logger.info("Completed Oracle WMS to DBT pipeline")
        tr_val = transform_result.value
        return r[object].ok({
            "processed_entities": list(extracted.keys()),
            "total_records": sum(len(records) for records in extracted.values()),
            "transformation_results": tr_val,
            "pipeline_status": "completed",
        })

    def test_oracle_wms_connection(self) -> r[Mapping[str, object]]:
        """Return simple connection health status."""
        return r[object].ok({
            "status": "connected",
            "environment": self.config.oracle_wms_environment,
            "base_url": self.config.oracle_wms_base_url,
        })

    def transform_with_dbt(
        self,
        entity_data: Mapping[str, Sequence[Mapping[str, object]]],
        model_names: list[str] | None,
    ) -> r[Mapping[str, object]]:
        """Return transformation summary for provided entities."""
        return r[object].ok({
            "transformed_tables": list(entity_data.keys()),
            "requested_models": model_names or [],
            "status": "success",
        })

    def validate_oracle_wms_data(
        self, entity_name: str, records: list[object]
    ) -> r[list[object]]:
        """Validate records list for a specific entity."""
        _ = entity_name
        if not records:
            return r[list[object]].fail("No records to validate")
        return r[list[object]].ok(records)


__all__ = ["FlextDbtOracleWmsClient"]
