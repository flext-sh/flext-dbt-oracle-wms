"""Workflow and monitoring services for DBT Oracle WMS."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import FlextLogger, r

from flext_dbt_oracle_wms import t

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
        self, entities: Sequence[t.ConfigurationMapping] | None = None
    ) -> r[t.Dict]:
        """Generate simple workflow recommendations for entity processing."""
        entity_list = entities or []
        total = len(entity_list)
        recommendation_message = ""
        if total > PERFORMANCE_RECOMMENDATION_THRESHOLD:
            recommendation_message = "Process entities in smaller batches"
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "total_entities": total,
                "recommendation": recommendation_message,
                "dbt_threads": str(self.config.dbt_threads),
                "target": str(self.config.dbt_target),
            })
        )

    def log_workflow_completion(
        self,
        tracking_info: t.ConfigurationMapping,
        result: r[t.Dict],
    ) -> None:
        """Log workflow completion status."""
        logger.info(
            "Workflow completion",
            tracking_id=str(tracking_info.get("tracking_id", "")),
            is_success=result.is_success,
        )

    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: Sequence[str] | None = None,
        additional_data: Mapping[str, str | int | float] | None = None,
    ) -> t.Dict:
        """Return tracking payload for workflow instrumentation."""
        logger.info("Tracking workflow execution")
        return t.Dict.model_validate({
            "workflow_name": workflow_name,
            "workflow_type": workflow_type,
            "entity_names": ",".join(entity_names or []),
            "additional_data": str(additional_data or {}),
            "tracking_id": f"{workflow_name}:{workflow_type}",
            "status": "running",
        })


__all__ = ["FlextDbtOracleWmsServices"]
