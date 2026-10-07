"""Service helpers for DBT Oracle WMS utilities.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_utilities/service
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from flext_meltano import u

from flext_core import r
from flext_dbt_oracle_wms import m, t

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p
    from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings


class FlextDbtOracleWmsUtilitiesService:
    """Service helpers for workflow recommendations and tracking."""

    class Service:
        """Workflow and monitoring service helpers."""

        PERFORMANCE_RECOMMENDATION_THRESHOLD: int = 20
        logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

        def __init__(self, settings: FlextDbtOracleWmsSettings) -> None:
            """Bind the service to the injected dbt Oracle WMS settings."""
            self._settings = settings

        def generate_workflow_recommendations(
            self,
            entities: t.SequenceOf[t.ConfigurationMapping] | None = None,
        ) -> p.Result[m.DbtOracleWms.WorkflowRecommendation]:
            """Generate simple workflow recommendations for entity processing.

            Returns:
                The resulting ``p.Result[m.DbtOracleWms.WorkflowRecommendation]``.
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
                    dbt_threads=str(self._settings.DbtOracleWms.dbt_threads),
                    target=self._settings.DbtOracleWms.dbt_target,
                ),
            )

        def log_workflow_completion(
            self,
            tracking_info: m.DbtOracleWms.WorkflowTracking,
            result: p.Result[m.DbtOracleWms.WorkflowResult],
        ) -> None:
            """Log workflow completion status."""
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
            """Return typed tracking model for workflow instrumentation."""
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
