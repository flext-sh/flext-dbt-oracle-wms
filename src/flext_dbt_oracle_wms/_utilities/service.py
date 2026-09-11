"""Workflow and monitoring service helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_meltano import u

from flext_core import r
from flext_dbt_oracle_wms import m, t
from flext_dbt_oracle_wms._settings import settings

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class FlextDbtOracleWmsUtilitiesService(u.DbtOracleWms.Service):
    """Workflow and monitoring service helpers — u.DbtOracleWms.Service.*."""

    def generate_workflow_recommendations(
        self, entities: t.SequenceOf[t.ConfigurationMapping] | None = None
    ) -> p.Result[m.DbtOracleWms.WorkflowRecommendation]:
        """Generate simple workflow recommendations for entity processing."""
        entity_list = entities or []
        total = len(entity_list)
        recommendation_message = ""
        if total > self.PERFORMANCE_RECOMMENDATION_THRESHOLD:
            recommendation_message = "Process entities in smaller batches"
        return r[m.DbtOracleWms.WorkflowRecommendation].ok(
            m.DbtOracleWms.WorkflowRecommendation(
                total_entities=total,
                recommendation=recommendation_message,
                dbt_threads=str(settings.DbtOracleWms.dbt_threads),
                target=settings.DbtOracleWms.dbt_target,
            )
        )

    def log_workflow_completion(
        self,
        tracking_info: m.DbtOracleWms.WorkflowTracking,
        result: p.Result[m.DbtOracleWms.WorkflowResult],
    ) -> None:
        """Log workflow completion status."""
        u.fetch_logger(__name__).info(
            "Workflow completion",
            tracking_id=tracking_info.tracking_id,
            success=result.success,
        )

    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: t.StrSequence | None = None,
        additional_data: t.ConfigValueMapping | None = None,
    ) -> m.DbtOracleWms.WorkflowTracking:
        """Return typed tracking model for workflow instrumentation."""
        _ = additional_data
        u.fetch_logger(__name__).info("Tracking workflow execution")
        return m.DbtOracleWms.WorkflowTracking(
            workflow_name=workflow_name,
            workflow_type=workflow_type,
            entity_names=tuple(entity_names or ()),
            tracking_id=f"{workflow_name}:{workflow_type}",
            status="running",
        )


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesService"]
