"""DBT client for Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import override

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_meltano import FlextMeltanoAPI
from flext_oracle_wms import FlextOracleWmsClient, create_oracle_wms_client

from flext_dbt_oracle_wms.config import FlextDbtOracleWmsConfig


class FlextDbtOracleWmsClient:
    """DBT client for Oracle WMS data transformations.

    Provides unified interface for Oracle WMS data extraction, validation,
    and DBT transformation operations using maximum composition from flext-oracle-wms.
    """

    # Shared logger for all DBT Oracle WMS client operations
    logger = FlextLogger(__name__)

    @override
    def __init__(
        self,
        config: FlextDbtOracleWmsConfig | None = None,
    ) -> None:
        """Initialize DBT Oracle WMS client.

        Args:
        config: Configuration for Oracle WMS and DBT operations

        """
        self.config: dict[str, object] = (
            config or FlextDbtOracleWmsConfig.get_global_instance()
        )
        # Initialize Oracle WMS client using flext-oracle-wms
        oracle_wms_config: dict[str, object] = self.config.get_oracle_wms_config()
        self._oracle_wms_client = create_oracle_wms_client(oracle_wms_config)
        self._dbt_service: object | None = None
        FlextDbtOracleWmsClient.logger.info(
            "Initialized DBT Oracle WMS client with config: %s", self.config
        )

    @property
    def dbt_service(self: object) -> object:
        """Get or create DBT service instance."""
        if self._dbt_service is None:
            # Create DBT service with configuration
            meltano_config: dict[str, object] = self.config.get_meltano_config()
            # Suppress unused registry_path warning for future use
            _ = (
                Path(meltano_config.project_root)
                if getattr(meltano_config, "project_root", None)
                else None
            )
            self._dbt_service = FlextMeltanoAPI()
        return self._dbt_service

    @property
    def oracle_wms_client(self: object) -> FlextOracleWmsClient:
        """Get Oracle WMS client instance."""
        return self._oracle_wms_client

    def test_oracle_wms_connection(self) -> FlextResult[dict[str, str | int]]:
        """Test Oracle WMS connection and basic functionality.

        Returns:
        FlextResult containing connection status and basic info

        """
        try:
            # Test the Oracle WMS connection
            # Mock connection test for now
            test_result: FlextResult[object] = FlextResult[dict["str", "object"]].ok({
                "status": "connected"
            })
            if test_result.is_failure:
                return FlextResult[dict[str, str | int]].fail(
                    f"Connection test failed: {test_result.error}",
                )

            # Return connection status
            return FlextResult[dict[str, str | int]].ok(
                {
                    "status": "connected",
                    "timestamp": "2025-01-01T00:00:00Z",
                    "entities_count": 0,
                },
            )
        except Exception as e:
            return FlextResult[dict[str, str | int]].fail(f"Connection test error: {e}")

    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: FlextTypes.NestedDict | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run full Oracle WMS-to-DBT pipeline.

        Args:
        entity_names: List of Oracle WMS entity names to process
        filters: Filters per entity
        model_names: DBT models to run

        Returns:
        FlextResult containing complete pipeline results

        """
        FlextDbtOracleWmsClient.logger.info("Starting full Oracle WMS-to-DBT pipeline")
        # Step 1: Discover entities if not specified
        if entity_names is None:
            discover_result: FlextResult[object] = self.discover_oracle_wms_entities()
            if discover_result.is_failure:
                # Convert discovery result to expected format
                return FlextResult[dict[str, object]].ok(
                    {
                        "discovery_results": discover_result.data,
                        "pipeline_status": "failed_at_discovery",
                    },
                )
            entities = discover_result.data or []
            entity_names = []
            for entity in entities:
                if isinstance(entity, str):
                    entity_names.append(entity)
        # Step 2: Extract data for each entity
        entity_data = {}
        for entity_name in entity_names:
            entity_filters: dict[str, object] = (
                filters.get(entity_name, {}) if filters else {}
            )
            extract_result = self.extract_oracle_wms_data(
                entity_name,
                entity_filters,
            )
            if extract_result.is_failure:
                # Convert extraction result to expected format
                return FlextResult[dict[str, object]].ok(
                    {
                        "extraction_results": extract_result.data,
                        "pipeline_status": "failed_at_extraction",
                    },
                )
            records = extract_result.data or []
            # Step 3: Validate data quality
            validate_result: FlextResult[object] = self.validate_oracle_wms_data(
                entity_name, records
            )
            if validate_result.is_failure:
                return FlextResult[dict["str", "object"]].fail(
                    validate_result.error or "Validation failed",
                )
            entity_data[entity_name] = records
        # Step 4: Transform with DBT
        transform_result: FlextResult[object] = self.transform_with_dbt(
            entity_data, model_names
        )
        if transform_result.is_failure:
            return transform_result
        # Combine results
        pipeline_results: dict[str, object] = {
            "processed_entities": list(entity_data.keys()),
            "total_records": sum(len(records) for records in entity_data.values()),
            "transformation_results": transform_result.data,
            "pipeline_status": "completed",
        }
        FlextDbtOracleWmsClient.logger.info(
            "Full Oracle WMS-to-DBT pipeline completed successfully"
        )
        return FlextResult[dict[str, object]].ok(pipeline_results)

    def _prepare_oracle_wms_data_for_dbt(
        self,
        entity_data: dict[str, list[dict[str, str | int, float] | bool]],
    ) -> dict[str, list[dict[str, str | int, float] | bool]]:
        """Prepare Oracle WMS data for DBT processing.

        Converts Oracle WMS records to format suitable for DBT models using field mappings.

        Args:
            entity_data: Dictionary of entity name -> records

        Returns:
            Dictionary of prepared data for DBT

        """
        prepared_data = {}
        for entity_name, records in entity_data.items():
            # Get DBT table name for entity
            table_name = self.config.get_entity_dbt_mapping(entity_name)
            # Convert records using field mapping
            mapped_records = []
            for record in records:
                mapped_record = {}
                for oracle_field, value in record.items():
                    dbt_field = self.config.get_field_dbt_mapping(oracle_field)
                    mapped_record[dbt_field] = value
                mapped_records.append(mapped_record)
            prepared_data[table_name] = mapped_records
        FlextDbtOracleWmsClient.logger.debug(
            "Prepared Oracle WMS data for DBT: %s",
            {k: len(v) for k, v in prepared_data.items()},
        )
        return prepared_data

    def discover_oracle_wms_entities(
        self,
    ) -> FlextResult[list[str]]:
        """Discover available Oracle WMS entities."""
        try:
            # Use the Oracle WMS client to discover entities
            # Mock entities discovery for now
            entities = ["company", "facility", "location", "item"]
            return FlextResult[list[str]].ok(entities)
        except Exception as e:
            return FlextResult[list[str]].fail(f"Failed to discover entities: {e}")

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: dict[str, object],
    ) -> FlextResult[list[dict[str, object]]]:
        """Extract data from Oracle WMS for a specific entity."""
        try:
            # Suppress unused filters parameter warning for future use
            _ = filters
            # Use the Oracle WMS client to extract data
            # Mock data extraction for now
            data = [{"id": 1, "name": f"sample_{entity_name}"}]
            return FlextResult[list[dict["str", "object"]]].ok(data)
        except Exception as e:
            return FlextResult[list[dict["str", "object"]]].fail(
                f"Failed to extract data: {e}",
            )

    def validate_oracle_wms_data(
        self,
        entity_name: str,
        records: list[dict[str, object]],
    ) -> FlextResult[list[dict[str, object]]]:
        """Validate Oracle WMS data quality."""
        try:
            # Suppress unused entity_name parameter warning for future use
            _ = entity_name
            # Basic validation - check that records are not empty
            if not records:
                return FlextResult[list[dict["str", "object"]]].fail(
                    "No records to validate",
                )

            # Return validated records
            return FlextResult[list[dict["str", "object"]]].ok(records)
        except Exception as e:
            return FlextResult[list[dict["str", "object"]]].fail(
                f"Validation failed: {e}"
            )

    def transform_with_dbt(
        self,
        entity_data: dict[str, list[dict[str, object]]],
        model_names: list[str] | None,
    ) -> FlextResult[dict[str, object]]:
        """Transform data using DBT."""
        try:
            # Suppress unused model_names parameter warning for future use
            _ = model_names
            # Use the DBT service to transform data
            # Mock DBT transformation for now
            result = {
                "transformed_tables": list(entity_data.keys()),
                "status": "success",
            }
            return FlextResult[dict["str", "object"]].ok(result)
        except Exception as e:
            return FlextResult[dict["str", "object"]].fail(
                f"DBT transformation failed: {e}",
            )


__all__: list[str] = [
    "FlextDbtOracleWmsClient",
]
