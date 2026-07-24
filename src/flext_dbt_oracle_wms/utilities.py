"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import ClassVar

from flext_core import r
from flext_dbt_oracle_wms import c, m, p, t
from flext_dbt_oracle_wms._settings import settings
from flext_meltano import u
from flext_oracle_wms import FlextOracleWmsUtilities


class FlextDbtOracleWmsUtilities(u, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms:
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""

        PERFORMANCE_RECOMMENDATION_THRESHOLD: ClassVar[int] = 20

        # NOTE (multi-agent, bead mro-wfc8.3): dead extract_wms_inventory_data removed
        # (only reference was the deleted p.DbtOracleWms.WmsIntegration protocol).

        class Service:
            """Workflow and monitoring service helpers — u.DbtOracleWms.Service.*."""

            def generate_workflow_recommendations(
                self, entities: t.SequenceOf[t.ConfigurationMapping] | None = None
            ) -> p.Result[p.DbtOracleWms.WorkflowRecommendation]:
                """Generate simple workflow recommendations for entity processing."""
                entity_list = entities or []
                total = len(entity_list)
                recommendation_message = ""
                if (
                    total
                    > FlextDbtOracleWmsUtilities.DbtOracleWms.PERFORMANCE_RECOMMENDATION_THRESHOLD
                ):
                    recommendation_message = "Process entities in smaller batches"
                return r[p.DbtOracleWms.WorkflowRecommendation].ok(
                    m.DbtOracleWms.WorkflowRecommendation(
                        total_entities=total,
                        recommendation=recommendation_message,
                        dbt_threads=str(settings.DbtOracleWms.dbt_threads),
                        target=settings.DbtOracleWms.dbt_target,
                    )
                )

            def log_workflow_completion(
                self,
                tracking_info: p.DbtOracleWms.WorkflowTracking,
                result: p.Result[p.DbtOracleWms.WorkflowResult],
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
            ) -> p.DbtOracleWms.WorkflowTracking:
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

        class Transformer:
            """Transformer for WMS entity data to DBT models."""

            def transform_all_entities(
                self,
                entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
            ) -> p.Result[p.DbtOracleWms.EntityTransformationSet]:
                """Transform WMS entities into a typed transformation set."""
                # NOTE (multi-agent, bead mro-wfc8.3): returns a typed model (no
                # item.model_dump() roundtrip; WmsItems are surfaced directly).
                return self.transform_items(entity_data.get("items", [])).map(
                    lambda items: p.DbtOracleWms.EntityTransformationSet(
                        entity_names=("items",), items=tuple(items)
                    )
                )

            def transform_items(
                self, records: t.SequenceOf[t.ConfigurationMapping]
            ) -> p.Result[Sequence[p.DbtOracleWms.WmsItem]]:
                """Transform item records to typed WmsItem models."""
                transformed: MutableSequence[p.DbtOracleWms.WmsItem] = []
                for index, record in enumerate(records):
                    try:
                        item = m.DbtOracleWms.WmsItem.model_validate(record)
                    except c.ValidationError as exc:
                        return r[Sequence[p.DbtOracleWms.WmsItem]].fail(
                            f"Invalid item record at index {index}: {exc}"
                        )
                    transformed.append(item)
                return r[Sequence[p.DbtOracleWms.WmsItem]].ok(transformed)

            def validate_business_rules(
                self, records: t.SequenceOf[t.ConfigurationMapping]
            ) -> p.Result[bool]:
                """Validate business rules for WMS records."""
                if not records:
                    return r[bool].fail("No records to validate")
                return r[bool].ok(True)

        class ModelBuilder:
            """Deterministic DBT staging-model generation for WMS sources."""

            @staticmethod
            def generate_wms_staging_models(
                oracle_sources: t.StrSequence,
            ) -> p.Result[Sequence[p.DbtOracleWms.DbtModel]]:
                """Create one staging model per source name."""
                models = [
                    m.DbtOracleWms.DbtModel(
                        name=f"stg_wms_{source}",
                        dbt_model_type="staging",
                        wms_entity_type=source,
                        schema_name="wms_staging",
                        table_name=f"stg_{source}",
                        columns=[],
                        materialization=c.DbtOracleWms.Dbt.Materialization.VIEW.value,
                        sql_content=f"select * from {{{{ source('oracle_wms', '{source}') }}}}",  # nosec B608
                        description=f"Staging model for {source}",
                        oracle_source=source,
                        dependencies=[],
                        wms_business_rules=[],
                    )
                    for source in oracle_sources
                ]
                return r[Sequence[p.DbtOracleWms.DbtModel]].ok(models)


__all__: list[str] = ["FlextDbtOracleWmsUtilities", "u"]

u = FlextDbtOracleWmsUtilities
