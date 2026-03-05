"""Client orchestration for Oracle WMS to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import FlextLogger, FlextResult, t

from .settings import FlextDbtOracleWmsSettings

logger = FlextLogger(__name__)


class FlextDbtOracleWmsClient:
    """DBT Oracle WMS client with typed extraction and transform stubs."""

    def __init__(self, config: FlextDbtOracleWmsSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        super().__init__()
        self.config = config or FlextDbtOracleWmsSettings.get_global_instance()

    def discover_oracle_wms_entities(self) -> FlextResult[list[str]]:
        """Return the configured Oracle WMS entities."""
        entities = list(self.config.required_fields_per_entity.keys())
        return FlextResult[list[str]].ok(entities)

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: Mapping[str, t.ContainerValue] | None = None,
    ) -> FlextResult[Sequence[Mapping[str, t.ContainerValue]]]:
        """Return sample records for a requested entity."""
        _ = filters
        return FlextResult[list[t.ConfigurationMapping]].ok([
            {"entity": entity_name, "id": 1, "name": f"sample_{entity_name}"},
        ])

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: Mapping[str, t.ContainerValue] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Run discover, extract, validate, and transform pipeline."""
        entities_result = (
            FlextResult[list[str]].ok(entity_names)
            if entity_names is not None
            else self.discover_oracle_wms_entities()
        )
        if entities_result.is_failure:
            return FlextResult[t.ConfigurationMapping].fail(
                entities_result.error or "Entity discovery failed",
            )
        entity_list = entities_result.value

        extracted: dict[str, list[dict[str, t.ContainerValue]]] = {}
        for entity_name in entity_list:
            extract_result = self.extract_oracle_wms_data(entity_name, filters)
            if extract_result.is_failure:
                return FlextResult[t.ConfigurationMapping].fail(
                    extract_result.error or "Extraction failed",
                )
            validate_result = self.validate_oracle_wms_data(
                entity_name,
                extract_result.value,
            )
            if validate_result.is_failure:
                return FlextResult[t.ConfigurationMapping].fail(
                    validate_result.error or "Validation failed",
                )
            extracted[entity_name] = [dict(record) for record in validate_result.value]

        transform_result = self.transform_with_dbt(extracted, model_names)
        if transform_result.is_failure:
            return FlextResult[t.ConfigurationMapping].fail(
                transform_result.error or "Transformation failed",
            )

        logger.info("Completed Oracle WMS to DBT pipeline")
        tr_val = transform_result.value
        return FlextResult[t.ConfigurationMapping].ok({
            "processed_entities": list(extracted.keys()),
            "total_records": sum(len(records) for records in extracted.values()),
            "transformation_results": tr_val,
            "pipeline_status": "completed",
        })

    def test_oracle_wms_connection(
        self,
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Return simple connection health status."""
        return FlextResult[t.ConfigurationMapping].ok({
            "status": "connected",
            "environment": self.config.oracle_wms_environment,
            "base_url": self.config.oracle_wms_base_url,
        })

    def transform_with_dbt(
        self,
        entity_data: Mapping[str, Sequence[Mapping[str, t.ContainerValue]]],
        model_names: list[str] | None,
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Return transformation summary for provided entities."""
        return FlextResult[t.ConfigurationMapping].ok({
            "transformed_tables": list(entity_data.keys()),
            "requested_models": model_names or [],
            "status": "success",
        })

    def validate_oracle_wms_data(
        self,
        entity_name: str,
        records: Sequence[Mapping[str, t.ContainerValue]],
    ) -> FlextResult[Sequence[Mapping[str, t.ContainerValue]]]:
        """Validate records list for a specific entity."""
        _ = entity_name
        if not records:
            return FlextResult[list[t.ConfigurationMapping]].fail(
                "No records to validate",
            )
        return FlextResult[list[t.ConfigurationMapping]].ok(records)


__all__ = ["FlextDbtOracleWmsClient"]
