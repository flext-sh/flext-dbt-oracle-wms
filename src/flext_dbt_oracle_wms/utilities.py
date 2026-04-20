"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from collections.abc import (
    Mapping,
    Sequence,
)
from typing import ClassVar

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import u

from flext_dbt_oracle_wms import m, p, r, t


class FlextDbtOracleWmsUtilities(FlextMeltanoUtilities, u):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms:
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""

        PERFORMANCE_RECOMMENDATION_THRESHOLD: ClassVar[int] = 20

        @staticmethod
        def extract_wms_inventory_data(
            extraction_config: Mapping[str, t.Container | None],
        ) -> p.Result[
            Mapping[
                str,
                Mapping[str, t.Container | None] | Sequence[t.Container | None],
            ]
        ]:
            """Return basic extraction metadata for inventory loads."""
            return r[
                Mapping[
                    str,
                    Mapping[str, t.Container | None] | Sequence[t.Container | None],
                ]
            ].ok({
                "extraction_config": extraction_config,
                "inventory_records": [],
            })

        class WmsDimensionalModeling:
            """DBT SQL generation helpers for dimensional models."""

            @staticmethod
            def generate_wms_inventory_dimension(
                inventory_config: Mapping[str, t.Container | None],
            ) -> p.Result[str]:
                """Generate SQL for inventory dimension model."""
                _ = inventory_config
                return r[str].ok("select * from {{ ref('stg_wms_inventory') }}")

        class Service:
            """Workflow and monitoring service helpers — u.DbtOracleWms.Service.*."""

            def __init__(
                self,
                settings: m.DbtOracleWms.FlextDbtOracleWmsSettings | None = None,
            ) -> None:
                """Initialize service state and default settings."""
                super().__init__()
                self.settings = (
                    settings
                    if settings is not None
                    else m.DbtOracleWms.FlextDbtOracleWmsSettings.fetch_global()
                )

            def generate_workflow_recommendations(
                self,
                entities: Sequence[t.ConfigurationMapping] | None = None,
            ) -> p.Result[m.Dict]:
                """Generate simple workflow recommendations for entity processing."""
                entity_list = entities or []
                total = len(entity_list)
                recommendation_message = ""
                if (
                    total
                    > FlextDbtOracleWmsUtilities.DbtOracleWms.PERFORMANCE_RECOMMENDATION_THRESHOLD
                ):
                    recommendation_message = "Process entities in smaller batches"
                return r[m.Dict].ok(
                    m.Dict.model_validate({
                        "total_entities": total,
                        "recommendation": recommendation_message,
                        "dbt_threads": str(self.settings.dbt_threads),
                        "target": str(self.settings.dbt_target),
                    }),
                )

            def log_workflow_completion(
                self,
                tracking_info: t.ConfigurationMapping,
                result: p.Result[m.Dict],
            ) -> None:
                """Log workflow completion status."""
                u.fetch_logger(__name__).info(
                    "Workflow completion",
                    tracking_id=str(tracking_info.get("tracking_id", "")),
                    success=result.success,
                )

            def track_workflow_execution(
                self,
                workflow_name: str,
                workflow_type: str,
                entity_names: t.StrSequence | None = None,
                additional_data: t.ConfigValueMapping | None = None,
            ) -> m.Dict:
                """Return tracking payload for workflow instrumentation."""
                u.fetch_logger(__name__).info("Tracking workflow execution")
                return m.Dict.model_validate({
                    "workflow_name": workflow_name,
                    "workflow_type": workflow_type,
                    "entity_names": ",".join(entity_names or []),
                    "additional_data": str(additional_data or {}),
                    "tracking_id": f"{workflow_name}:{workflow_type}",
                    "status": "running",
                })


__all__: list[str] = ["FlextDbtOracleWmsUtilities", "u"]

u = FlextDbtOracleWmsUtilities
