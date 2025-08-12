"""DBT client for Oracle WMS operations.

Provides high-level interface for DBT Oracle WMS transformations.
Integrates flext-oracle-wms and flext-meltano for complete data pipeline operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core import FlextResult, get_logger
from flext_meltano import create_dbt_hub
from flext_oracle_wms import (
    FlextOracleWmsClient,
    create_oracle_wms_client,
)

from .dbt_config import FlextDbtOracleWmsConfig
from .dbt_exceptions import (
    FlextDbtOracleWmsConnectionError,
    FlextDbtOracleWmsProcessingError,
    FlextDbtOracleWmsValidationError,
)

if TYPE_CHECKING:
    from flext_meltano import FlextDbtHub
    from flext_oracle_wms import FlextOracleWmsEntity

logger = get_logger(__name__)


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
            meltano_config = self.config.get_meltano_config()
            self._dbt_hub = create_dbt_hub(meltano_config)
        return self._dbt_hub

    @property
    def oracle_wms_client(self) -> FlextOracleWmsClient:
        """Get Oracle WMS client instance."""
        return self._oracle_wms_client

    def test_oracle_wms_connection(self) -> FlextResult[dict[str, Any]]:
        """Test Oracle WMS connection.

        Returns:
            FlextResult containing connection test results

        """
        try:
            logger.info("Testing Oracle WMS connection...")

            # Use flext-oracle-wms client to test connection
            # This would typically be a health check or simple entity discovery
            discovery_result = self._oracle_wms_client.discover_entities()

            if discovery_result.is_success:
                connection_info = {
                    "status": "connected",
                    "discovered_entities": len(discovery_result.data or []),
                    "environment": self.config.oracle_wms_environment,
                    "base_url": self.config.oracle_wms_base_url,
                }
                logger.info("Oracle WMS connection test successful")
                return FlextResult.ok(connection_info)
            logger.error("Oracle WMS connection test failed: %s", discovery_result.error)
            return FlextResult.failure(
                FlextDbtOracleWmsConnectionError(
                    f"Oracle WMS connection test failed: {discovery_result.error}",
                ),
            )

        except Exception as e:
            logger.exception("Unexpected error during Oracle WMS connection test")
            return FlextResult.failure(
                FlextDbtOracleWmsConnectionError(f"Oracle WMS connection error: {e}"),
            )

    def discover_oracle_wms_entities(
        self,
        entity_types: list[str] | None = None,
    ) -> FlextResult[list[FlextOracleWmsEntity]]:
        """Discover Oracle WMS entities for DBT processing.

        Args:
            entity_types: Specific entity types to discover (None = all)

        Returns:
            FlextResult containing list of Oracle WMS entities

        """
        try:
            logger.info("Discovering Oracle WMS entities: types=%s", entity_types)

            # Use flext-oracle-wms client for entity discovery
            discovery_result = self._oracle_wms_client.discover_entities()

            if discovery_result.is_success:
                entities = discovery_result.data or []

                # Filter by entity types if specified
                if entity_types:
                    entities = [
                        entity for entity in entities
                        if entity.entity_type in entity_types
                    ]

                logger.info(
                    "Successfully discovered %d Oracle WMS entities",
                    len(entities),
                )
                return FlextResult.ok(entities)
            logger.error("Oracle WMS entity discovery failed: %s", discovery_result.error)
            return FlextResult.failure(
                FlextDbtOracleWmsConnectionError(
                    f"Oracle WMS entity discovery failed: {discovery_result.error}",
                ),
            )

        except Exception as e:
            logger.exception("Unexpected error during Oracle WMS entity discovery")
            return FlextResult.failure(
                FlextDbtOracleWmsConnectionError(f"Oracle WMS entity discovery error: {e}"),
            )

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: dict[str, Any] | None = None,
        limit: int | None = None,
    ) -> FlextResult[list[dict[str, Any]]]:
        """Extract Oracle WMS data for DBT processing.

        Args:
            entity_name: Name of Oracle WMS entity to extract
            filters: Optional filters to apply
            limit: Maximum number of records to extract

        Returns:
            FlextResult containing list of Oracle WMS records

        """
        try:
            logger.info(
                "Extracting Oracle WMS data: entity=%s, filters=%s, limit=%s",
                entity_name,
                filters,
                limit,
            )

            # Use flext-oracle-wms client for data extraction
            # This is a simplified example - the actual API would depend on flext-oracle-wms implementation

            # For now, we'll simulate the extraction result
            # In real implementation, this would call the appropriate method from flext-oracle-wms
            extraction_result = FlextResult.ok([])  # Placeholder

            if extraction_result.is_success:
                records = extraction_result.data or []
                logger.info(
                    "Successfully extracted %d records from Oracle WMS entity '%s'",
                    len(records),
                    entity_name,
                )
                return extraction_result
            logger.error("Oracle WMS data extraction failed: %s", extraction_result.error)
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(
                    f"Oracle WMS data extraction failed: {extraction_result.error}",
                ),
            )

        except Exception as e:
            logger.exception("Unexpected error during Oracle WMS data extraction")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(f"Oracle WMS data extraction error: {e}"),
            )

    def validate_oracle_wms_data(
        self,
        entity_name: str,
        records: list[dict[str, Any]],
    ) -> FlextResult[dict[str, Any]]:
        """Validate Oracle WMS data quality for DBT processing.

        Args:
            entity_name: Name of Oracle WMS entity
            records: List of Oracle WMS records to validate

        Returns:
            FlextResult containing validation metrics

        """
        try:
            logger.info(
                "Validating %d Oracle WMS records for entity '%s'",
                len(records),
                entity_name,
            )

            quality_config = self.config.get_oracle_wms_quality_config()
            required_fields = self.config.get_required_fields(entity_name)
            business_rules = quality_config.get("business_rules", {})

            # Validate required fields
            validation_errors = []
            valid_records = 0

            for i, record in enumerate(records):

                # Check required fields
                record_errors = [f"Missing required field: {field}" for field in required_fields if field not in record or record[field] is None or record[field] == ""]

                # Apply business rules validation
                if entity_name == "inventory" and quality_config.get("validate_business_rules"):
                    inventory_rules = business_rules.get("inventory_thresholds", {})
                    quantity = record.get("quantityOnHand", 0)

                    if quantity < inventory_rules.get("min_quantity", 0):
                        record_errors.append(f"Quantity below minimum: {quantity}")
                    elif quantity > inventory_rules.get("max_quantity", 999999):
                        record_errors.append(f"Quantity above maximum: {quantity}")

                if not record_errors:
                    valid_records += 1
                else:
                    validation_errors.extend([f"Record {i}: {error}" for error in record_errors])

            # Calculate quality metrics
            total_records = len(records)
            quality_score = valid_records / total_records if total_records > 0 else 0.0

            validation_metrics = {
                "entity_name": entity_name,
                "total_records": total_records,
                "valid_records": valid_records,
                "invalid_records": total_records - valid_records,
                "quality_score": quality_score,
                "validation_errors": validation_errors[:10],  # Limit to first 10 errors
                "total_errors": len(validation_errors),
            }

            # Check if quality meets threshold
            min_threshold = quality_config.get("min_quality_threshold", 0.85)
            if quality_score < min_threshold:
                return FlextResult.failure(
                    FlextDbtOracleWmsValidationError(
                        f"Oracle WMS data quality below threshold for {entity_name}: "
                        f"{quality_score:.2f} < {min_threshold}",
                        validation_details=validation_metrics,
                    ),
                )

            logger.info(
                "Oracle WMS data validation completed: entity=%s, quality_score=%.2f",
                entity_name,
                quality_score,
            )
            return FlextResult.ok(validation_metrics)

        except Exception as e:
            logger.exception("Unexpected error during Oracle WMS data validation")
            return FlextResult.failure(
                FlextDbtOracleWmsValidationError(f"Oracle WMS data validation error: {e}"),
            )

    def transform_with_dbt(
        self,
        entity_data: dict[str, list[dict[str, Any]]],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Transform Oracle WMS data using DBT models.

        Args:
            entity_data: Dictionary of entity name -> records
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation results

        """
        try:
            logger.info(
                "Running DBT transformations on Oracle WMS data: entities=%s, models=%s",
                list(entity_data.keys()),
                model_names,
            )

            # Prepare Oracle WMS data for DBT (convert using field mappings)
            transformed_data = self._prepare_oracle_wms_data_for_dbt(entity_data)

            # Use flext-meltano DBT hub for execution
            hub = self.dbt_hub

            if model_names:
                # Run specific models
                result = hub.run_models(model_names, data=transformed_data)
            else:
                # Run all models
                result = hub.run_project(data=transformed_data)

            if result.is_success:
                logger.info("DBT transformation completed successfully")
            else:
                logger.error("DBT transformation failed: %s", result.error)
                return FlextResult.failure(
                    FlextDbtOracleWmsProcessingError(f"DBT transformation failed: {result.error}"),
                )

            return result

        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(f"DBT transformation error: {e}"),
            )

    def run_full_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: dict[str, dict[str, Any]] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run complete Oracle WMS to DBT transformation pipeline.

        Args:
            entity_names: Oracle WMS entities to process (None = all discovered)
            filters: Filters per entity
            model_names: DBT models to run

        Returns:
            FlextResult containing complete pipeline results

        """
        logger.info("Starting full Oracle WMS-to-DBT pipeline")

        # Step 1: Discover entities if not specified
        if entity_names is None:
            discover_result = self.discover_oracle_wms_entities()
            if discover_result.is_failure:
                return discover_result

            entities = discover_result.data or []
            entity_names = [entity.entity_type for entity in entities]

        # Step 2: Extract data for each entity
        entity_data = {}
        for entity_name in entity_names:
            entity_filters = filters.get(entity_name, {}) if filters else {}
            extract_result = self.extract_oracle_wms_data(entity_name, entity_filters)

            if extract_result.is_failure:
                return extract_result

            records = extract_result.data or []

            # Step 3: Validate data quality
            validate_result = self.validate_oracle_wms_data(entity_name, records)
            if validate_result.is_failure:
                return validate_result

            entity_data[entity_name] = records

        # Step 4: Transform with DBT
        transform_result = self.transform_with_dbt(entity_data, model_names)
        if transform_result.is_failure:
            return transform_result

        # Combine results
        pipeline_results = {
            "processed_entities": list(entity_data.keys()),
            "total_records": sum(len(records) for records in entity_data.values()),
            "transformation_results": transform_result.data,
            "pipeline_status": "completed",
        }

        logger.info("Full Oracle WMS-to-DBT pipeline completed successfully")
        return FlextResult.ok(pipeline_results)

    def _prepare_oracle_wms_data_for_dbt(
        self,
        entity_data: dict[str, list[dict[str, Any]]],
    ) -> dict[str, Any]:
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


__all__: list[str] = [
    "FlextDbtOracleWmsClient",
]
