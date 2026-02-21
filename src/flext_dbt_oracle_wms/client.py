"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from flext_core import FlextLogger, FlextResult, t

from .settings import FlextDbtOracleWmsSettings

logger = FlextLogger(__name__)


class FlextDbtOracleWmsClient:
    """DBT Oracle WMS client with typed extraction and transform stubs."""

    def __init__(self, config: FlextDbtOracleWmsSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        self.config = config or FlextDbtOracleWmsSettings.get_global_instance()

    def test_oracle_wms_connection(self) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Return simple connection health status."""
        return FlextResult[dict[str, t.GeneralValueType]].ok({
            "status": "connected",
            "environment": self.config.oracle_wms_environment,
            "base_url": self.config.oracle_wms_base_url,
        })

    def discover_oracle_wms_entities(self) -> FlextResult[list[str]]:
        """Return the configured Oracle WMS entities."""
        entities = list(self.config.required_fields_per_entity.keys())
        return FlextResult[list[str]].ok(entities)

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Return sample records for a requested entity."""
        _ = filters
        return FlextResult[list[dict[str, t.GeneralValueType]]].ok([
            {"entity": entity_name, "id": 1, "name": f"sample_{entity_name}"}
        ])

    def validate_oracle_wms_data(
        self,
        entity_name: str,
        records: list[dict[str, t.GeneralValueType]],
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Validate records list for a specific entity."""
        _ = entity_name
        if not records:
            return FlextResult[list[dict[str, t.GeneralValueType]]].fail(
                "No records to validate",
            )
        return FlextResult[list[dict[str, t.GeneralValueType]]].ok(records)

    def transform_with_dbt(
        self,
        entity_data: dict[str, list[dict[str, t.GeneralValueType]]],
        model_names: list[str] | None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Return transformation summary for provided entities."""
        return FlextResult[dict[str, t.GeneralValueType]].ok({
            "transformed_tables": list(entity_data.keys()),
            "requested_models": model_names or [],
            "status": "success",
        })

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: dict[str, t.GeneralValueType] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            FlextResult[list[str]].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.is_failure or entities_result.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                entities_result.error or "Entity discovery failed",
            )

        extracted: dict[str, list[dict[str, t.GeneralValueType]]] = {}
        for entity_name in entities_result.value:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.is_failure or extract_result.value is None:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    extract_result.error or "Extraction failed",
                )
            validate_result = self.validate_oracle_wms_data(
                entity_name, extract_result.value
            )
            if validate_result.is_failure or validate_result.value is None:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    validate_result.error or "Validation failed",
                )
            extracted[entity_name] = validate_result.value

        transform_result = self.transform_with_dbt(extracted, model_names)
        if transform_result.is_failure or transform_result.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                transform_result.error or "Transformation failed",
            )

        logger.info("Completed Oracle WMS to DBT pipeline")
        return FlextResult[dict[str, t.GeneralValueType]].ok({
            "processed_entities": list(extracted.keys()),
            "total_records": sum(len(records) for records in extracted.values()),
            "transformation_results": transform_result.value,
            "pipeline_status": "completed",
        })


__all__ = ["FlextDbtOracleWmsClient"]
