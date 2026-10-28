"""Service helpers for DBT Oracle WMS utilities.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_utilities/service
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from flext_meltano import u

from flext_dbt_oracle_wms import m, r, t

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class FlextDbtOracleWmsUtilitiesService:
    """Service helpers for workflow recommendations and tracking."""

    class Service:
        """Workflow and monitoring service helpers."""

        PERFORMANCE_RECOMMENDATION_THRESHOLD: int = 20
        logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

        def __init__(self, settings: p.DbtOracleWms.SettingsGroup) -> None:
            """Bind the service to the injected dbt Oracle WMS settings.

            Args:
                settings: Settings snapshot providing dbt thread and
                    target knobs.

            """
            self._settings = settings

        def generate_workflow_recommendations(
            self,
            entities: t.SequenceOf[t.ConfigurationMapping] | None = None,
        ) -> p.Result[m.DbtOracleWms.WorkflowRecommendation]:
            """Generate simple workflow recommendations for entity processing.

            Args:
                entities: Entity records in scope; batching advice is
                    emitted when their count exceeds the recommendation
                    threshold.

            Returns:
                Result wrapping the recommendation payload with the
                configured dbt threads and target.

            """
            entity_list = entities or []
            total = len(entity_list)
            recommendation_message = ""
            if total > self.PERFORMANCE_RECOMMENDATION_THRESHOLD:
                recommendation_message = "Process entities in smaller batches"
            return r[m.DbtOracleWms.WorkflowRecommendation].ok(
                m.DbtOracleWms.WorkflowRecommendation(
                    total_entities=total,
                    recommendation=recommendation_message,
                    dbt_threads=str(self._settings.dbt_threads),
                    target=self._settings.dbt_target,
                ),
            )

        def log_workflow_completion(
            self,
            tracking_info: m.DbtOracleWms.WorkflowTracking,
            result: p.Result[m.DbtOracleWms.WorkflowResult],
        ) -> None:
            """Log workflow completion status.

            Args:
                tracking_info: Tracking payload identifying the workflow.
                result: Final workflow result whose success flag is
                    logged.

            """
            self.logger.info(
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
            """Return typed tracking model for workflow instrumentation.

            Args:
                workflow_name: Name recorded in the tracking payload.
                workflow_type: Type recorded in the tracking payload.
                entity_names: Entities in scope for the workflow.
                additional_data: Reserved for extra instrumentation
                    context; currently unused.

            Returns:
                Tracking payload in the initial ``running`` state.

            """
            _ = additional_data
            self.logger.info("Tracking workflow execution")
            return m.DbtOracleWms.WorkflowTracking(
                workflow_name=workflow_name,
                workflow_type=workflow_type,
                entity_names=tuple(entity_names or ()),
                tracking_id=f"{workflow_name}:{workflow_type}",
                status="running",
            )


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesService"]
