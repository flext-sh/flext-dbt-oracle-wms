"""DBT services for Oracle WMS workflow orchestration.

Provides high-level services for orchestrating complete Oracle WMS-to-DBT workflows.
Integrates all components for end-to-end data transformation pipelines.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

from flext_core import FlextResult, get_logger

from .dbt_client import FlextDbtOracleWmsClient
from .dbt_config import FlextDbtOracleWmsConfig
from .dbt_exceptions import (
    FlextDbtOracleWmsProcessingError,
    FlextDbtOracleWmsValidationError,
)
from .dbt_models import FlextDbtOracleWmsTransformer

if TYPE_CHECKING:
    from flext_oracle_wms import FlextOracleWmsEntity

logger = get_logger(__name__)


class FlextDbtOracleWmsWorkflowService:
    """Service for orchestrating complete Oracle WMS-to-DBT workflows.

    Provides high-level workflow orchestration that combines entity discovery,
    data extraction, model transformation, and DBT execution into cohesive
    Oracle WMS data transformation pipelines.
    """

    def __init__(
        self,
        config: FlextDbtOracleWmsConfig | None = None,
    ) -> None:
        """Initialize workflow service.

        Args:
            config: Configuration for Oracle WMS and DBT operations

        """
        self.config = config or FlextDbtOracleWmsConfig()
        self.client = FlextDbtOracleWmsClient(self.config)
        self.transformer = FlextDbtOracleWmsTransformer()

        logger.info("Initialized Oracle WMS DBT workflow service")

    def run_entity_discovery_workflow(
        self,
        entity_types: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run Oracle WMS entity discovery workflow.

        Args:
            entity_types: Specific entity types to discover (None = all)

        Returns:
            FlextResult containing discovery workflow results

        """
        try:
            logger.info(
                "Starting Oracle WMS entity discovery workflow: types=%s",
                entity_types,
            )

            # Step 1: Test Oracle WMS connection
            logger.info("Testing Oracle WMS connection...")
            connection_result = self.client.test_oracle_wms_connection()
            if connection_result.is_failure:
                return connection_result

            # Step 2: Discover Oracle WMS entities
            logger.info("Discovering Oracle WMS entities...")
            discovery_result = self.client.discover_oracle_wms_entities(entity_types)
            if discovery_result.is_failure:
                return discovery_result

            entities = discovery_result.data or []
            logger.info("Discovered %d Oracle WMS entities", len(entities))

            # Collect discovery workflow results
            workflow_results = {
                "connection_status": connection_result.data,
                "discovered_entities": len(entities),
                "entity_types": list({entity.entity_type for entity in entities}),
                "entities_by_type": {
                    entity_type: len([e for e in entities if e.entity_type == entity_type])
                    for entity_type in {entity.entity_type for entity in entities}
                },
                "workflow_status": "completed",
            }

            logger.info(
                "Oracle WMS entity discovery workflow completed successfully: %s",
                workflow_results,
            )
            return FlextResult.ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in Oracle WMS entity discovery workflow")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(
                    f"Oracle WMS entity discovery workflow failed: {e}",
                ),
            )

    def run_data_extraction_workflow(
        self,
        entity_names: list[str],
        filters: dict[str, dict[str, Any]] | None = None,
        limits: dict[str, int] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run Oracle WMS data extraction workflow.

        Args:
            entity_names: Names of Oracle WMS entities to extract
            filters: Optional filters per entity
            limits: Optional limits per entity

        Returns:
            FlextResult containing extraction workflow results

        """
        try:
            logger.info(
                "Starting Oracle WMS data extraction workflow: entities=%s",
                entity_names,
            )

            extraction_results = {}
            total_records = 0

            # Extract data for each entity
            for entity_name in entity_names:
                logger.info("Extracting data for entity: %s", entity_name)

                entity_filters = filters.get(entity_name, {}) if filters else {}
                entity_limit = limits.get(entity_name) if limits else None

                extract_result = self.client.extract_oracle_wms_data(
                    entity_name,
                    entity_filters,
                    entity_limit,
                )

                if extract_result.is_failure:
                    return extract_result

                records = extract_result.data or []
                extraction_results[entity_name] = {
                    "record_count": len(records),
                    "records": records,
                }
                total_records += len(records)

                logger.info(
                    "Extracted %d records for entity: %s",
                    len(records),
                    entity_name,
                )

            workflow_results = {
                "extracted_entities": list(extraction_results.keys()),
                "total_records": total_records,
                "records_per_entity": {
                    entity: result["record_count"]
                    for entity, result in extraction_results.items()
                },
                "extraction_data": extraction_results,
                "workflow_status": "completed",
            }

            logger.info("Oracle WMS data extraction workflow completed successfully")
            return FlextResult.ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in Oracle WMS data extraction workflow")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(
                    f"Oracle WMS data extraction workflow failed: {e}",
                ),
            )

    def run_data_transformation_workflow(
        self,
        entity_data: dict[str, list[dict[str, Any]]],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run Oracle WMS data transformation workflow.

        Args:
            entity_data: Dictionary of entity name -> records
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation workflow results

        """
        try:
            logger.info(
                "Starting Oracle WMS data transformation workflow: entities=%s, models=%s",
                list(entity_data.keys()),
                model_names,
            )

            # Step 1: Validate all entity data
            validation_results = {}
            for entity_name, records in entity_data.items():
                logger.info("Validating data for entity: %s", entity_name)

                validate_result = self.client.validate_oracle_wms_data(
                    entity_name,
                    records,
                )

                if validate_result.is_failure:
                    return validate_result

                validation_results[entity_name] = validate_result.data

            # Step 2: Transform data using DBT models
            logger.info("Running DBT transformation...")
            transform_result = self.client.transform_with_dbt(entity_data, model_names)

            if transform_result.is_failure:
                return transform_result

            # Step 3: Transform data using local transformers
            logger.info("Running local data transformations...")
            transformed_models = self.transformer.transform_all_entities(entity_data)

            workflow_results = {
                "validation_results": validation_results,
                "dbt_transformation": transform_result.data,
                "local_transformations": {
                    entity: len(models) for entity, models in transformed_models.items()
                },
                "total_transformed_entities": len(transformed_models),
                "workflow_status": "completed",
            }

            logger.info("Oracle WMS data transformation workflow completed successfully")
            return FlextResult.ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in Oracle WMS data transformation workflow")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(
                    f"Oracle WMS data transformation workflow failed: {e}",
                ),
            )

    def run_full_transformation_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: dict[str, dict[str, Any]] | None = None,
        limits: dict[str, int] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run complete Oracle WMS transformation pipeline.

        Args:
            entity_names: Oracle WMS entities to process (None = all discovered)
            filters: Filters per entity
            limits: Limits per entity
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing complete pipeline results

        """
        try:
            logger.info("Starting full Oracle WMS transformation pipeline")
            pipeline_results = {}

            # Step 1: Discover entities if not specified
            if entity_names is None:
                logger.info("Discovering Oracle WMS entities...")
                discovery_result = self.run_entity_discovery_workflow()
                if discovery_result.is_failure:
                    return discovery_result

                pipeline_results["discovery"] = discovery_result.data

                # Extract entity names from discovery results
                discovered_entities = pipeline_results["discovery"].get("entity_types", [])
                entity_names = discovered_entities[:10]  # Limit to first 10 for safety
                logger.info("Using discovered entities: %s", entity_names)

            # Step 2: Extract data
            logger.info("Extracting Oracle WMS data...")
            extraction_result = self.run_data_extraction_workflow(
                entity_names, filters, limits,
            )
            if extraction_result.is_failure:
                return extraction_result

            pipeline_results["extraction"] = extraction_result.data
            entity_data = {
                entity: result["records"]
                for entity, result in extraction_result.data["extraction_data"].items()
            }

            # Step 3: Transform data
            logger.info("Running Oracle WMS data transformations...")
            transformation_result = self.run_data_transformation_workflow(
                entity_data, model_names,
            )
            if transformation_result.is_failure:
                return transformation_result

            pipeline_results["transformation"] = transformation_result.data

            # Combine results
            full_results = {
                "pipeline_type": "full_oracle_wms_transformation",
                "processed_entities": entity_names,
                "results": pipeline_results,
                "pipeline_status": "completed",
                "summary": {
                    "entities_processed": len(entity_names),
                    "total_records_extracted": pipeline_results["extraction"]["total_records"],
                    "entities_transformed": pipeline_results["transformation"]["total_transformed_entities"],
                },
            }

            logger.info("Full Oracle WMS transformation pipeline completed successfully")
            return FlextResult.ok(full_results)

        except Exception as e:
            logger.exception("Unexpected error in full Oracle WMS transformation pipeline")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(
                    f"Full Oracle WMS transformation pipeline failed: {e}",
                ),
            )

    def validate_workflow_prerequisites(self) -> FlextResult[dict[str, Any]]:
        """Validate all prerequisites for running Oracle WMS-to-DBT workflows.

        Returns:
            FlextResult containing validation results

        """
        try:
            logger.info("Validating Oracle WMS workflow prerequisites...")
            validation_results = {}

            # Step 1: Validate configuration
            if not self.config.validate_oracle_wms_connection():
                return FlextResult.failure(
                    FlextDbtOracleWmsValidationError(
                        "Invalid Oracle WMS connection configuration",
                    ),
                )
            validation_results["config_validation"] = "passed"

            # Step 2: Test Oracle WMS connection
            connection_result = self.client.test_oracle_wms_connection()
            if connection_result.is_failure:
                return connection_result
            validation_results["oracle_wms_connection"] = connection_result.data

            # Step 3: Validate DBT setup
            try:
                _ = self.client.dbt_hub
                dbt_validation = {"status": "available", "hub_initialized": True}
            except Exception as e:
                logger.warning("DBT hub validation failed: %s", e)
                dbt_validation = {"status": "error", "error": str(e)}

            validation_results["dbt_setup"] = dbt_validation

            # Step 4: Check required directories and permissions
            try:
                project_dir = Path(self.config.dbt_project_dir)
                if not project_dir.exists():
                    project_dir.mkdir(parents=True)

                validation_results["directory_access"] = {
                    "project_dir": str(project_dir),
                    "writable": project_dir.is_dir(),
                }
            except Exception as e:
                validation_results["directory_access"] = {"error": str(e)}

            overall_status = "passed"
            if any(
                result.get("status") == "error" or "error" in result
                for result in validation_results.values()
                if isinstance(result, dict)
            ):
                overall_status = "failed"

            final_results = {
                "overall_status": overall_status,
                "validations": validation_results,
                "prerequisites_met": overall_status == "passed",
            }

            logger.info(
                "Oracle WMS workflow prerequisites validation completed: %s",
                overall_status,
            )
            return FlextResult.ok(final_results)

        except Exception as e:
            logger.exception("Unexpected error during Oracle WMS prerequisites validation")
            return FlextResult.failure(
                FlextDbtOracleWmsValidationError(
                    f"Oracle WMS prerequisites validation failed: {e}",
                ),
            )

    def get_workflow_recommendations(
        self,
        entities: list[FlextOracleWmsEntity] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Get recommendations for optimal Oracle WMS workflow configuration.

        Args:
            entities: Oracle WMS entities to analyze (None = discover from system)

        Returns:
            FlextResult containing workflow recommendations

        """
        try:
            logger.info("Generating Oracle WMS workflow recommendations...")

            # Discover entities if not provided
            if entities is None:
                discovery_result = self.client.discover_oracle_wms_entities()
                if discovery_result.is_failure:
                    return discovery_result
                entities = discovery_result.data or []

            if not entities:
                return FlextResult.ok(
                    {
                        "message": "No Oracle WMS entities found for analysis",
                        "recommendations": [],
                    },
                )

            # Analyze entities and generate recommendations
            recommendations = []

            # Analyze entity distribution
            entity_counts = {}
            for entity in entities:
                entity_type = entity.entity_type
                entity_counts[entity_type] = entity_counts.get(entity_type, 0) + 1

            # Performance recommendations
            total_entities = len(entities)
            entity_count_threshold = 20
            if total_entities > entity_count_threshold:
                recommendations.append(
                    {
                        "type": "performance",
                        "priority": "high",
                        "message": f"Large number of entities ({total_entities}). Consider processing in batches.",
                        "suggestion": "Use limits parameter to process entities in smaller batches",
                    },
                )

            # Oracle WMS specific recommendations
            inventory_threshold = 1000
            if "inventory" in entity_counts and entity_counts["inventory"] > inventory_threshold:
                recommendations.append(
                    {
                        "type": "oracle_wms_specific",
                        "priority": "medium",
                        "message": "Large inventory dataset detected. Consider date-based filtering.",
                        "suggestion": "Filter inventory by lastMovementDate to reduce data volume",
                    },
                )

            # Configuration recommendations based on data volume
            config_threads_threshold = 10
            if total_entities > config_threads_threshold:
                recommendations.append(
                    {
                        "type": "configuration",
                        "priority": "medium",
                        "message": "Multiple entities detected. Consider performance optimizations.",
                        "suggestion": f"Increase threads to {min(8, max(4, total_entities // 5))} and page_size to 2000",
                    },
                )

            results = {
                "analysis": {
                    "total_entities": total_entities,
                    "entity_type_distribution": entity_counts,
                    "most_common_entity_type": max(entity_counts, key=entity_counts.get)
                    if entity_counts
                    else None,
                },
                "recommendations": recommendations,
                "suggested_config": {
                    "dbt_threads": min(8, max(4, total_entities // 5))
                    if total_entities > config_threads_threshold
                    else 4,
                    "oracle_wms_page_size": 2000 if total_entities > config_threads_threshold else 1000,
                    "batch_processing": total_entities > entity_count_threshold,
                },
            }

            logger.info("Generated %d Oracle WMS workflow recommendations", len(recommendations))
            return FlextResult.ok(results)

        except Exception as e:
            logger.exception("Unexpected error generating Oracle WMS workflow recommendations")
            return FlextResult.failure(
                FlextDbtOracleWmsProcessingError(
                    f"Oracle WMS recommendations generation failed: {e}",
                ),
            )


class FlextDbtOracleWmsMonitoringService:
    """Service for monitoring Oracle WMS-to-DBT workflow execution.

    Provides monitoring, logging, and metrics collection for workflow execution.
    """

    def __init__(
        self,
        config: FlextDbtOracleWmsConfig,
    ) -> None:
        """Initialize monitoring service.

        Args:
            config: Configuration for monitoring settings

        """
        self.config = config
        logger.info("Initialized Oracle WMS DBT monitoring service")

    def track_workflow_execution(
        self,
        workflow_type: str,
        workflow_params: dict[str, Any],
    ) -> dict[str, Any]:
        """Track Oracle WMS workflow execution metrics.

        Args:
            workflow_type: Type of workflow being executed
            workflow_params: Parameters passed to workflow

        Returns:
            Dictionary containing execution tracking information

        """
        tracking_info = {
            "workflow_type": workflow_type,
            "start_time": time.time(),
            "parameters": workflow_params,
            "tracking_id": f"oracle_wms_{workflow_type}_{int(time.time())}",
            "oracle_wms_environment": self.config.oracle_wms_environment,
        }

        logger.info(
            "Started tracking Oracle WMS workflow execution: %s",
            tracking_info["tracking_id"],
        )
        return tracking_info

    def log_workflow_completion(
        self,
        tracking_info: dict[str, Any],
        result: FlextResult[Any],
    ) -> None:
        """Log Oracle WMS workflow completion metrics.

        Args:
            tracking_info: Tracking information from track_workflow_execution
            result: Workflow execution result

        """
        end_time = time.time()
        duration = end_time - tracking_info["start_time"]

        completion_info = {
            "tracking_id": tracking_info["tracking_id"],
            "workflow_type": tracking_info["workflow_type"],
            "duration_seconds": round(duration, 2),
            "success": result.is_success,
            "oracle_wms_environment": tracking_info.get("oracle_wms_environment"),
            "result_summary": str(result.data)[:200] if result.data else None,
            "error_summary": str(result.error)[:200] if result.error else None,
        }

        if result.is_success:
            logger.info("Oracle WMS workflow completed successfully: %s", completion_info)
        else:
            logger.error("Oracle WMS workflow failed: %s", completion_info)


__all__: list[str] = [
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsWorkflowService",
]
