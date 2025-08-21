"""DBT services for Oracle WMS workflow orchestration.

Provides high-level services for orchestrating complete Oracle WMS-to-DBT workflows.
Integrates all components for end-to-end data transformation pipelines.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import cast

from flext_core import FlextResult, get_logger

from flext_dbt_oracle_wms.dbt_client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.dbt_config import FlextDbtOracleWmsConfig
from flext_dbt_oracle_wms.models import FlextDbtOracleWmsTransformer

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

    async def run_entity_discovery_workflow(
        self,
        entity_types: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run Oracle WMS entity discovery workflow.

        Args:
            entity_types: Specific entity types to discover (None = all)

        Returns:
            FlextResult containing discovery workflow results

        """
        try:
            logger.info("Starting Oracle WMS entity discovery workflow...")

            # Step 1: Test Oracle WMS connection
            logger.info("Testing Oracle WMS connection...")
            connection_result = await self.client.test_oracle_wms_connection()
            if connection_result.is_failure:
                return FlextResult[None].fail(
                    connection_result.error or "Connection failed",
                )

            # Step 2: Discover Oracle WMS entities
            logger.info("Discovering Oracle WMS entities...")
            discovery_result = await self.client.discover_oracle_wms_entities(
                entity_types,
            )
            if discovery_result.is_failure:
                return FlextResult[None].fail(
                    discovery_result.error or "Discovery failed"
                )

            entities = discovery_result.data or []
            logger.info("Discovered %d Oracle WMS entities", len(entities))

            # Collect discovery workflow results
            workflow_results: dict[str, object] = {
                "connection_status": connection_result.data,
                "discovered_entities": len(entities),
                "entity_types": list({entity.get("name") for entity in entities}),
                "entities_by_type": {
                    entity_type: len(
                        [e for e in entities if e.get("name") == entity_type],
                    )
                    for entity_type in {entity.get("name") for entity in entities}
                },
                "workflow_status": "completed",
            }

            logger.info(
                "Oracle WMS entity discovery workflow completed successfully: %s",
                workflow_results,
            )
            return FlextResult[None].ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in Oracle WMS entity discovery workflow")
            return FlextResult[None].fail(
                f"Oracle WMS entity discovery workflow failed: {e}",
            )

    async def run_data_extraction_workflow(
        self,
        entity_names: list[str],
        filters: dict[str, dict[str, str | int | float | bool]] | None = None,
        limits: dict[str, int] | None = None,
    ) -> FlextResult[dict[str, object]]:
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

                extract_result = await self.client.extract_oracle_wms_data(
                    entity_name,
                    entity_filters,
                    entity_limit,
                )

                if extract_result.is_failure:
                    return FlextResult[None].fail(
                        extract_result.error or "Extraction failed",
                    )

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

            workflow_results: dict[str, object] = {
                "extraction_data": extraction_results,
                "total_records": total_records,
                "entities_processed": len(entity_names),
                "workflow_status": "completed",
            }

            logger.info(
                "Oracle WMS data extraction workflow completed successfully: %s",
                workflow_results,
            )
            return FlextResult[None].ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in Oracle WMS data extraction workflow")
            return FlextResult[None].fail(
                f"Oracle WMS data extraction workflow failed: {e}",
            )

    async def run_data_transformation_workflow(
        self,
        entity_names: list[str],
        entity_data: dict[str, list[dict[str, str | int | float | bool]]],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run Oracle WMS data transformation workflow.

        Args:
            entity_names: Specific DBT models to run (None = all)
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

            # Step 1: Validate data quality
            logger.info("Validating Oracle WMS data quality...")
            validation_results = {}
            for entity_name in entity_names:
                records = entity_data.get(entity_name, [])
                validate_result = await self.client.validate_oracle_wms_data(
                    entity_name,
                    records,
                )
                if validate_result.is_failure:
                    return validate_result
                validation_results[entity_name] = validate_result.data

            # Step 2: Transform with DBT
            logger.info("Running DBT transformations...")
            transform_result = await self.client.transform_with_dbt(
                entity_data,
                model_names,
            )
            if transform_result.is_failure:
                return transform_result

            # Step 3: Use transformer for additional processing
            logger.info("Running additional transformations...")
            entity_data_cast = cast("dict[str, list[dict[str, object]]]", entity_data)
            transformed_models = self.transformer.transform_all_entities(
                entity_data_cast,
            )

            # Collect transformation workflow results
            workflow_results: dict[str, object] = {
                "validation_results": validation_results,
                "transformation_results": transform_result.data,
                "transformed_models": transformed_models,
                "entities_processed": len(entity_names),
                "workflow_status": "completed",
            }

            logger.info(
                "Oracle WMS data transformation workflow completed successfully",
            )
            return FlextResult[None].ok(workflow_results)

        except Exception as e:
            logger.exception(
                "Unexpected error in Oracle WMS data transformation workflow",
            )
            return FlextResult[None].fail(
                f"Oracle WMS data transformation workflow failed: {e}",
            )

    async def run_full_transformation_pipeline(
        self,
        entity_names: list[str] | None = None,
        filters: dict[str, dict[str, str | int | float | bool]] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run complete Oracle WMS to DBT transformation pipeline.

        Args:
            entity_names: Oracle WMS entities to process (None = all discovered)
            filters: Optional filters per entity
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing complete pipeline results

        """
        try:
            logger.info("Starting Oracle WMS full transformation pipeline...")

            # Step 1: Discover entities if not specified
            if entity_names is None:
                discovery_result = await self.run_entity_discovery_workflow()
                if discovery_result.is_failure:
                    return discovery_result

                pipeline_results = discovery_result.data or {}
                discovered_entities = pipeline_results.get("entity_types", [])
                if isinstance(discovered_entities, list):
                    entity_names = discovered_entities[
                        :10
                    ]  # Limit to first 10 for safety
                else:
                    entity_names = []

            # Step 2: Extract data
            logger.info("Extracting Oracle WMS data...")
            extraction_result = await self.run_data_extraction_workflow(
                entity_names,
                filters,
                None,
            )
            if extraction_result.is_failure:
                return extraction_result

            pipeline_results = extraction_result.data or {}
            pipeline_results["extraction"] = extraction_result.data

            # Step 3: Transform data
            logger.info("Running Oracle WMS data transformations...")
            extraction_data = pipeline_results.get("extraction_data", {})
            extraction_dict: dict[str, list[dict[str, str | int | float | bool]]] = (
                extraction_data if isinstance(extraction_data, dict) else {}
            )
            transformation_result = await self.run_data_transformation_workflow(
                entity_names,
                extraction_dict,
                model_names,
            )
            if transformation_result.is_failure:
                return transformation_result

            pipeline_results["transformation"] = transformation_result.data

            # Collect final results
            extraction_info = cast("dict[str, object]", pipeline_results["extraction"])
            transformation_info = cast(
                "dict[str, object]",
                pipeline_results["transformation"],
            )

            full_results: dict[str, object] = {
                "discovery": {
                    "entities_processed": len(entity_names),
                    "total_records_extracted": extraction_info.get("total_records", 0),
                    "entities_transformed": transformation_info.get(
                        "entities_processed",
                        0,
                    ),
                },
                "extraction": extraction_info,
                "transformation": transformation_info,
                "pipeline_status": "completed",
            }

            logger.info(
                "Oracle WMS full transformation pipeline completed successfully: %s",
                full_results,
            )
            return FlextResult[None].ok(full_results)

        except Exception as e:
            logger.exception(
                "Unexpected error in Oracle WMS full transformation pipeline",
            )
            return FlextResult[None].fail(
                f"Oracle WMS full transformation pipeline failed: {e}",
            )

    async def validate_workflow_prerequisites(
        self,
    ) -> FlextResult[dict[str, object]]:
        """Validate all prerequisites for running Oracle WMS-to-DBT workflows.

        Returns:
            FlextResult containing validation results

        """
        try:
            logger.info("Validating Oracle WMS workflow prerequisites...")

            validation_results: dict[str, object] = {}

            # Step 1: Validate Oracle WMS connection
            logger.info("Validating Oracle WMS connection...")
            try:
                connection_result = await self.client.test_oracle_wms_connection()
                if connection_result.is_failure:
                    return FlextResult[None].fail(
                        connection_result.error or "Connection failed",
                    )
                validation_results["oracle_wms_connection"] = cast(
                    "dict[str, object]",
                    connection_result.data,
                )

                # Step 3: Validate DBT setup
                try:
                    _ = self.client.dbt_hub
                    dbt_validation: dict[str, object] = {
                        "status": "available",
                        "hub_initialized": True,
                    }
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
                return FlextResult[None].ok(final_results)

            except Exception as e:
                logger.exception("Oracle WMS connection validation failed")
                return FlextResult[None].fail(
                    f"Oracle WMS connection validation failed: {e}",
                )

        except Exception as e:
            logger.exception(
                "Unexpected error during Oracle WMS prerequisites validation",
            )
            return FlextResult[None].fail(
                f"Oracle WMS prerequisites validation failed: {e}",
            )

    async def get_workflow_recommendations(
        self,
        entities: list[dict[str, object]] | None = None,
    ) -> FlextResult[dict[str, object]]:
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
                discovery_result = await self.client.discover_oracle_wms_entities()
                if discovery_result.is_failure:
                    return FlextResult[None].fail(
                        discovery_result.error or "Discovery failed",
                    )
                entities = discovery_result.data or []

            if not entities:
                return FlextResult[None].ok(
                    {
                        "message": "No Oracle WMS entities found for analysis",
                        "recommendations": [],
                    },
                )

            # Analyze entities and generate recommendations
            recommendations = []

            # Analyze entity distribution
            entity_counts: dict[str, int] = {}
            for entity in entities:
                if isinstance(entity, dict) and "name" in entity:
                    entity_type = entity["name"]
                    if isinstance(entity_type, str):
                        entity_counts[entity_type] = (
                            entity_counts.get(entity_type, 0) + 1
                        )

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
            if (
                "inventory" in entity_counts
                and entity_counts["inventory"] > inventory_threshold
            ):
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

            results: dict[str, object] = {
                "analysis": {
                    "total_entities": total_entities,
                    "entity_type_distribution": entity_counts,
                    "most_common_entity_type": max(
                        entity_counts,
                        key=lambda k: entity_counts[k],
                    )
                    if entity_counts
                    else None,
                },
                "recommendations": recommendations,
                "suggested_config": {
                    "dbt_threads": min(8, max(4, total_entities // 5))
                    if total_entities > config_threads_threshold
                    else 4,
                    "oracle_wms_page_size": 2000
                    if total_entities > config_threads_threshold
                    else 1000,
                    "batch_processing": total_entities > entity_count_threshold,
                },
            }

            logger.info(
                "Generated %d Oracle WMS workflow recommendations",
                len(recommendations),
            )
            return FlextResult[None].ok(results)

        except Exception as e:
            logger.exception(
                "Unexpected error generating Oracle WMS workflow recommendations",
            )
            return FlextResult[None].fail(
                f"Oracle WMS workflow recommendations generation failed: {e}",
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
        workflow_name: str,
        workflow_type: str,
        entity_names: list[str] | None = None,
        additional_data: dict[str, str | int | float | bool] | None = None,
    ) -> dict[str, object]:
        """Track Oracle WMS workflow execution metrics.

        Args:
            workflow_name: Name of the workflow being executed
            workflow_type: Type of workflow being executed
            entity_names: Names of entities being processed
            additional_data: Additional data for tracking

        Returns:
            Dictionary containing execution tracking information

        """
        # Create tracking info
        tracking_info: dict[str, object] = {
            "workflow_name": workflow_name,
            "workflow_type": workflow_type,
            "start_time": time.time(),
            "entity_names": entity_names or [],
            "additional_data": additional_data or {},
            "status": "running",
        }

        logger.info(
            "Started tracking Oracle WMS workflow execution: %s",
            tracking_info["tracking_id"],
        )
        return tracking_info

    def log_workflow_completion(
        self,
        tracking_info: dict[str, str | int | float | bool],
        result: FlextResult[dict[str, str | int | float | bool]],
    ) -> None:
        """Log Oracle WMS workflow completion metrics.

        Args:
            tracking_info: Tracking information from track_workflow_execution
            result: Workflow execution result

        """
        end_time = time.time()
        start_time = tracking_info["start_time"]
        duration = (
            end_time - start_time if isinstance(start_time, (int, float)) else 0.0
        )

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
            logger.info(
                "Oracle WMS workflow completed successfully: %s",
                completion_info,
            )
        else:
            logger.error("Oracle WMS workflow failed: %s", completion_info)


__all__: list[str] = [
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsWorkflowService",
]
