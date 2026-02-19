"""Workflow and monitoring services for DBT Oracle WMS."""

from __future__ import annotations

from flext_core import FlextLogger, FlextResult, FlextTypes as t

from .settings import FlextDbtOracleWmsSettings

logger = FlextLogger(__name__)
PERFORMANCE_RECOMMENDATION_THRESHOLD = 20


class FlextDbtOracleWmsServices:
    """Service facade with recommendation and monitoring helpers."""

    def __init__(self, config: FlextDbtOracleWmsSettings | None = None) -> None:
        """Initialize service state and default settings."""
        self.config = config or FlextDbtOracleWmsSettings.get_global_instance()

    def generate_workflow_recommendations(
        self,
        entities: list[dict[str, t.GeneralValueType]] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Generate simple workflow recommendations for entity processing."""
        entity_list = entities or []
        total = len(entity_list)
        recommendations: list[dict[str, t.GeneralValueType]] = []
        if total > PERFORMANCE_RECOMMENDATION_THRESHOLD:
            recommendations.append({
                "type": "performance",
                "priority": "high",
                "message": "Process entities in smaller batches",
            })
        return FlextResult[dict[str, t.GeneralValueType]].ok({
            "analysis": {
                "total_entities": total,
            },
            "recommendations": recommendations,
            "summary": {
                "dbt_threads": self.config.dbt_threads,
                "target": self.config.dbt_target,
            },
        })

    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: list[str] | None = None,
        additional_data: dict[str, str | int | float] | None = None,
    ) -> dict[str, t.GeneralValueType]:
        """Return tracking payload for workflow instrumentation."""
        logger.info("Tracking workflow execution")
        return {
            "workflow_name": workflow_name,
            "workflow_type": workflow_type,
            "entity_names": entity_names or [],
            "additional_data": additional_data or {},
            "tracking_id": f"{workflow_name}:{workflow_type}",
            "status": "running",
        }

    def log_workflow_completion(
        self,
        tracking_info: dict[str, t.GeneralValueType],
        result: FlextResult[dict[str, t.GeneralValueType]],
    ) -> None:
        """Log workflow completion status."""
        logger.info(
            "Workflow completion",
            extra={
                "tracking_id": tracking_info.get("tracking_id"),
                "is_success": result.is_success,
            },
        )


FlextDbtOracleWmsWorkflowService = FlextDbtOracleWmsServices
FlextDbtOracleWmsMonitoringService = FlextDbtOracleWmsServices

__all__ = [
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsServices",
    "FlextDbtOracleWmsWorkflowService",
]
