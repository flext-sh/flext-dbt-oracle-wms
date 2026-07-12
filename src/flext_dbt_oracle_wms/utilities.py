"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import TYPE_CHECKING, ClassVar

from flext_core import r
from flext_dbt_oracle_wms._settings import settings
from flext_dbt_oracle_wms.constants import c
from flext_dbt_oracle_wms.models import m
from flext_dbt_oracle_wms.typings import t
from flext_meltano import u
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

        class Transformer:
            """Transformer for WMS entity data to DBT models."""

            def transform_all_entities(
                self,
                entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
            ) -> p.Result[t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]]]:
                """Transform all WMS entities to DBT-compatible format."""
                items_result = self.transform_items(entity_data.get("items", []))
                if items_result.failure:
                    return r[
                        t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]]
                    ].fail(
                        items_result.error or "Item transformation failed",
                    )
                return r[t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]]].ok({
                    "items": [item.model_dump() for item in items_result.value],
                })

            def transform_items(
                self,
                records: t.SequenceOf[t.ConfigurationMapping],
            ) -> p.Result[Sequence[m.DbtOracleWms.FlextDbtOracleWmsItemDimension]]:
                """Transform item records to item dimension models."""
                transformed: MutableSequence[
                    m.DbtOracleWms.FlextDbtOracleWmsItemDimension
                ] = []
                for index, record in enumerate(records):
                    try:
                        raw_record = m.DbtOracleWms.RawItemRecord.model_validate(
                            record,
                        )
                    except c.ValidationError as exc:
                        return r[
                            Sequence[m.DbtOracleWms.FlextDbtOracleWmsItemDimension]
                        ].fail(f"Invalid item record at index {index}: {exc}")
                    transformed.append(
                        m.DbtOracleWms.FlextDbtOracleWmsItemDimension(
                            item_id=raw_record.item_id,
                            item_number=raw_record.item_number,
                            item_description=raw_record.item_description,
                        ),
                    )
                return r[Sequence[m.DbtOracleWms.FlextDbtOracleWmsItemDimension]].ok(
                    transformed
                )

            def validate_business_rules(
                self,
                records: t.SequenceOf[t.ConfigurationMapping],
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
            ) -> p.Result[Sequence[m.DbtOracleWms.DbtModel]]:
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
                return r[Sequence[m.DbtOracleWms.DbtModel]].ok(
                    models,
                )


__all__: list[str] = ["FlextDbtOracleWmsUtilities", "u"]

u = FlextDbtOracleWmsUtilities
