"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import FlextLogger, r
from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from flext_dbt_oracle_wms import t
from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels as m

_logger = FlextLogger(__name__)
_PERFORMANCE_RECOMMENDATION_THRESHOLD = 20


class FlextDbtOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms:
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""

        @staticmethod
        def extract_wms_inventory_data(
            extraction_config: Mapping[str, t.ContainerValue | None],
        ) -> r[
            Mapping[
                str,
                Mapping[str, t.ContainerValue | None]
                | Sequence[t.ContainerValue | None],
            ]
        ]:
            """Return basic extraction metadata for inventory loads."""
            return r[
                Mapping[
                    str,
                    Mapping[str, t.ContainerValue | None]
                    | Sequence[t.ContainerValue | None],
                ]
            ].ok({
                "extraction_config": extraction_config,
                "inventory_records": [],
            })

        class WmsDimensionalModeling:
            """DBT SQL generation helpers for dimensional models."""

            @staticmethod
            def generate_wms_inventory_dimension(
                inventory_config: Mapping[str, t.ContainerValue | None],
            ) -> r[str]:
                """Generate SQL for inventory dimension model."""
                _ = inventory_config
                return r[str].ok("select * from {{ ref('stg_wms_inventory') }}")

        class Service:
            """Workflow and monitoring service helpers — u.DbtOracleWms.Service.*."""

            def __init__(
                self,
                config: m.DbtOracleWms.FlextDbtOracleWmsSettings | None = None,
            ) -> None:
                """Initialize service state and default settings."""
                super().__init__()
                self.config = (
                    config
                    if config is not None
                    else m.DbtOracleWms.FlextDbtOracleWmsSettings.get_global()
                )

            def generate_workflow_recommendations(
                self,
                entities: Sequence[t.ConfigurationMapping] | None = None,
            ) -> r[t.Dict]:
                """Generate simple workflow recommendations for entity processing."""
                entity_list = entities or []
                total = len(entity_list)
                recommendation_message = ""
                if total > _PERFORMANCE_RECOMMENDATION_THRESHOLD:
                    recommendation_message = "Process entities in smaller batches"
                return r[t.Dict].ok(
                    t.Dict.model_validate({
                        "total_entities": total,
                        "recommendation": recommendation_message,
                        "dbt_threads": str(self.config.dbt_threads),
                        "target": str(self.config.dbt_target),
                    }),
                )

            def log_workflow_completion(
                self,
                tracking_info: t.ConfigurationMapping,
                result: r[t.Dict],
            ) -> None:
                """Log workflow completion status."""
                _logger.info(
                    "Workflow completion",
                    tracking_id=str(tracking_info.get("tracking_id", "")),
                    is_success=result.is_success,
                )

            def track_workflow_execution(
                self,
                workflow_name: str,
                workflow_type: str,
                entity_names: t.StrSequence | None = None,
                additional_data: Mapping[str, str | int | float] | None = None,
            ) -> t.Dict:
                """Return tracking payload for workflow instrumentation."""
                _logger.info("Tracking workflow execution")
                return t.Dict.model_validate({
                    "workflow_name": workflow_name,
                    "workflow_type": workflow_type,
                    "entity_names": ",".join(entity_names or []),
                    "additional_data": str(additional_data or {}),
                    "tracking_id": f"{workflow_name}:{workflow_type}",
                    "status": "running",
                })


__all__ = ["FlextDbtOracleWmsUtilities", "u"]

u = FlextDbtOracleWmsUtilities
