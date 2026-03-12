"""Workflow and monitoring services for DBT Oracle WMS."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextLogger, r, t

from .settings import FlextDbtOracleWmsSettings

logger = FlextLogger(__name__)
PERFORMANCE_RECOMMENDATION_THRESHOLD = 20


class FlextDbtOracleWmsServices:
    """Service facade with recommendation and monitoring helpers."""

    def __init__(self, config: FlextDbtOracleWmsSettings | None = None) -> None:
        """Initialize service state and default settings."""
        super().__init__()
        self.config = (
            config if config is not None else FlextDbtOracleWmsSettings.get_global()
        )

    def generate_workflow_recommendations(
        self, entities: list[Mapping[str, object]] | None = None
    ) -> r[Mapping[str, object]]:
        """Generate simple workflow recommendations for entity processing."""
        entity_list = entities or []
        total = len(entity_list)
        recommendations: list[dict[str, object]] = []
        if total > PERFORMANCE_RECOMMENDATION_THRESHOLD:
            recommendations.append({
                "type": "performance",
                "priority": "high",
                "message": "Process entities in smaller batches",
            })
        return r[object].ok({
            "analysis": {"total_entities": total},
            "recommendations": recommendations,
            "summary": {
                "dbt_threads": self.config.dbt_threads,
                "target": self.config.dbt_target,
            },
        })

    def log_workflow_completion(
        self,
        tracking_info: Mapping[str, object],
        result: r[Mapping[str, object]],
    ) -> None:
        """Log workflow completion status."""
        logger.info(
            "Workflow completion",
            extra={
                "tracking_id": tracking_info.get("tracking_id"),
                "is_success": result.is_success,
            },
        )

    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: list[str] | None = None,
        additional_data: Mapping[str, str | int | float] | None = None,
    ) -> Mapping[str, object]:
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


__all__ = ["FlextDbtOracleWmsServices"]
