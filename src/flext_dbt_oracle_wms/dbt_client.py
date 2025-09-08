"""DBT client for Oracle WMS operations.

Provides high-level interface for DBT Oracle WMS transformations.
Integrates flext-oracle-wms and flext-meltano for complete data pipeline operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_meltano import FlextDbtHub, create_dbt_hub
from flext_oracle_wms import (
    FlextOracleWmsClient,
    create_oracle_wms_client,
)

from flext_dbt_oracle_wms.dbt_config import FlextDbtOracleWmsConfig

logger = FlextLogger(__name__)


class FlextDbtOracleWmsClient:
    """DBT client for Oracle WMS data transformations.

    Provides unified interface for Oracle WMS data extraction, validation,
    and DBT transformation operations using maximum composition from flext-oracle-wms.
    """

    def __init__(
        self,
        config: FlextDbtOracleWmsConfig | None = None,
    ) -> None:
        """Initialize DBT Oracle WMS client.

        Args:
            config: Configuration for Oracle WMS and DBT operations

        """
        self.config = config or FlextDbtOracleWmsConfig()
        # Initialize Oracle WMS client using flext-oracle-wms
        oracle_wms_config = self.config.get_oracle_wms_config()
        self._oracle_wms_client = create_oracle_wms_client(oracle_wms_config)
        self._dbt_hub: FlextDbtHub | None = None
        logger.info("Initialized DBT Oracle WMS client with config: %s", self.config)

    @property
    def dbt_hub(self) -> FlextDbtHub:
        """Get or create DBT hub instance."""
        if self._dbt_hub is None:
            # create_dbt_hub expects a Path, not a config object
            meltano_config = self.config.get_meltano_config()
            registry_path = (
                Path(meltano_config.project_root)
                if getattr(meltano_config, "project_root", None)
                else None
            )
            self._dbt_hub = create_dbt_hub(registry_path)
        return self._dbt_hub

    @property
    def oracle_wms_client(self) -> FlextOracleWmsClient:
        """Get Oracle WMS client instance."""
        return self._oracle_wms_client

    async def test_oracle_wms_connection(self) -> FlextResult[dict[str, str | int]]:
        """Test Oracle WMS connection and basic functionality.

        Returns:
            FlextResult containing connection status and basic info

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS entities

            entity_types: Specific entity types to discover (None = all)

        Returns:
            FlextResult containing list of Oracle WMS entities

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing list of Oracle WMS records

            filters: Optional filters to apply
            limit: Maximum number of records to extract
        Returns:
            FlextResult containing list of Oracle WMS records

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing validation metrics

            records: List of Oracle WMS records to validate
            quality_config: Optional quality configuration
        Returns:
            FlextResult containing validation metrics

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing transformation results

            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

        Returns:
            FlextResult containing complete pipeline results

            filters: Filters per entity
            model_names: DBT models to run
        Returns:
            FlextResult containing complete pipeline results

        """

    async def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: FlextTypes.Core.StringList | None = None,
        filters: dict[str, FlextTypes.Core.Dict] | None = None,
        model_names: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Run full Oracle WMS-to-DBT pipeline.

        Args:
            entity_names: List of Oracle WMS entity names to process
            filters: Filters per entity
            model_names: DBT models to run

        Returns:
            FlextResult containing complete pipeline results

        """
        logger.info("Starting full Oracle WMS-to-DBT pipeline")
        # Step 1: Discover entities if not specified
        if entity_names is None:
            discover_result = await self.discover_oracle_wms_entities()
            if discover_result.is_failure:
                # Convert discovery result to expected format
                return FlextResult[FlextTypes.Core.Dict].ok(
                    {
                        "discovery_results": discover_result.data,
                        "pipeline_status": "failed_at_discovery",
                    },
                )
            entities = discover_result.data or []
            entity_names = []
            for entity in entities:
                if isinstance(entity, dict) and "name" in entity:
                    name = entity.get("name")
                    if isinstance(name, str):
                        entity_names.append(name)
        # Step 2: Extract data for each entity
        entity_data = {}
        for entity_name in entity_names:
            entity_filters = filters.get(entity_name, {}) if filters else {}
            extract_result = await self.extract_oracle_wms_data(
                entity_name,
                entity_filters,
            )
            if extract_result.is_failure:
                # Convert extraction result to expected format
                return FlextResult[FlextTypes.Core.Dict].ok(
                    {
                        "extraction_results": extract_result.data,
                        "pipeline_status": "failed_at_extraction",
                    },
                )
            records = extract_result.data or []
            # Step 3: Validate data quality
            validate_result = await self.validate_oracle_wms_data(entity_name, records)
            if validate_result.is_failure:
                return validate_result
            entity_data[entity_name] = records
        # Step 4: Transform with DBT
        transform_result = await self.transform_with_dbt(entity_data, model_names)
        if transform_result.is_failure:
            return transform_result
        # Combine results
        pipeline_results: FlextTypes.Core.Dict = {
            "processed_entities": list(entity_data.keys()),
            "total_records": sum(len(records) for records in entity_data.values()),
            "transformation_results": transform_result.data,
            "pipeline_status": "completed",
        }
        logger.info("Full Oracle WMS-to-DBT pipeline completed successfully")
        return FlextResult[FlextTypes.Core.Dict].ok(pipeline_results)

    def _prepare_oracle_wms_data_for_dbt(
        self,
        entity_data: dict[str, list[dict[str, str | int | float | bool]]],
    ) -> dict[str, list[dict[str, str | int | float | bool]]]:
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
        logger.debug(
            "Prepared Oracle WMS data for DBT: %s",
            {k: len(v) for k, v in prepared_data.items()},
        )
        return prepared_data


__all__: FlextTypes.Core.StringList = [
    "FlextDbtOracleWmsClient",
]
