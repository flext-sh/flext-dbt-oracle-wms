"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from flext_core import r
from flext_dbt_oracle_wms._settings import settings
from flext_dbt_oracle_wms.typings import t
from flext_meltano import m, u
from flext_oracle_wms import FlextOracleWmsUtilities

if TYPE_CHECKING:
    from flext_dbt_oracle_wms.protocols import p


class FlextDbtOracleWmsUtilities(u, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms:
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""

        PERFORMANCE_RECOMMENDATION_THRESHOLD: ClassVar[int] = 20

        @staticmethod
        def extract_wms_inventory_data(
            extraction_config: t.MappingKV[str, t.JsonValue | None],
        ) -> p.Result[
            t.MappingKV[
                str,
                t.MappingKV[str, t.JsonValue | None] | t.SequenceOf[t.JsonValue | None],
            ]
        ]:
            """Return basic extraction metadata for inventory loads."""
            inventory_records: t.SequenceOf[t.JsonValue | None] = ()
            return r[
                t.MappingKV[
                    str,
                    t.MappingKV[str, t.JsonValue | None]
                    | t.SequenceOf[t.JsonValue | None],
                ]
            ].ok({
                "extraction_config": extraction_config,
                "inventory_records": inventory_records,
            })

        class Service:
            """Workflow and monitoring service helpers — u.DbtOracleWms.Service.*."""

            def generate_workflow_recommendations(
                self,
                entities: t.SequenceOf[t.ConfigurationMapping] | None = None,
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
                        "dbt_threads": str(settings.DbtOracleWms.dbt_threads),
                        "target": settings.DbtOracleWms.dbt_target,
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
