"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_dbt_oracle_wms import c, t
from flext_meltano import m, u
from flext_oracle_wms import FlextOracleWmsModels


class FlextDbtOracleWmsModels(m, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms:
        """DBT Oracle WMS domain namespace."""

        # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — typed connection_profile.
        class DbtConnectionProfile(m.ImmutableValueModel):
            """Typed dbt Oracle WMS connection profile (satisfies p.Meltano.DbtConnectionProfile)."""

            type: Annotated[str, u.Field(description="Dbt adapter type identifier")] = (
                "oracle_wms"
            )
            base_url: Annotated[str, u.Field(description="Oracle WMS base URL")]
            environment: Annotated[str, u.Field(description="Oracle WMS environment")]
            target: Annotated[str, u.Field(description="Dbt target profile")]
            threads: Annotated[int, u.Field(description="Dbt parallel threads")]
            project: Annotated[
                str, u.Field(description="Dbt project name owning this profile")
            ]

        # NOTE (multi-agent, bead mro-wfc8.3): WmsItem collapses the former identical
        # RawItemRecord + FlextDbtOracleWmsItemDimension (same 3 fields). extra=ignore keeps
        # ingestion tolerant of extra WMS record keys; model_dump() emits the DBT mapping.
        class WmsItem(m.ImmutableValueModel):
            """WMS item record / dimension (single typed model)."""

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")

            item_id: Annotated[
                str,
                u.Field(default="", description="Unique item identifier"),
            ]
            item_number: Annotated[
                str,
                u.Field(default="", description="Item number code"),
            ]
            item_description: Annotated[
                str,
                u.Field(default="", description="Description of the item"),
            ]

        # NOTE (multi-agent, bead mro-wfc8): FlextDbtOracleWmsTransformer moved to
        # u.DbtOracleWms.Transformer (behavior belongs in utilities, not among models; §2a).

        class DbtModel(m.ArbitraryTypesModel):
            """WMS-specific DBT model metadata."""

            name: Annotated[str, u.Field(description="DBT model name")]
            dbt_model_type: Annotated[
                str,
                u.Field(description="DBT model classification"),
            ] = "staging"
            schema_name: Annotated[
                str,
                u.Field(description="Target schema name"),
            ] = "wms_staging"
            table_name: Annotated[str, u.Field(description="Target table name")]
            materialization: Annotated[
                str,
                u.Field(description="DBT materialization strategy"),
            ] = c.DbtOracleWms.Dbt.Materialization.VIEW.value
            sql_content: Annotated[str, u.Field(description="Model SQL body")]
            description: Annotated[
                str,
                u.Field(description="Human-readable model description"),
            ] = ""
            columns: Annotated[
                t.SequenceOf[t.StrMapping],
                u.Field(description="Column metadata payloads"),
            ] = u.Field(default_factory=tuple)
            dependencies: Annotated[
                t.StrSequence,
                u.Field(description="Upstream model dependencies"),
            ] = u.Field(default_factory=tuple)
            wms_entity_type: Annotated[
                str,
                u.Field(description="Oracle WMS entity represented by this model"),
            ]
            oracle_source: Annotated[
                str,
                u.Field(description="Oracle source for this model"),
            ]
            wms_business_rules: Annotated[
                t.StrSequence,
                u.Field(
                    description="WMS-specific business rules attached to the model",
                ),
            ] = u.Field(default_factory=tuple)

        # NOTE (multi-agent, bead mro-wfc8): ModelGenerator moved to
        # u.DbtOracleWms.ModelBuilder.generate_wms_staging_models (behavior belongs in
        # utilities, not among models; §2a). The unused settings parameter was dropped.

        # NOTE (multi-agent, bead mro-wfc8.3): typed result models replacing the banned
        # generic RootModel[dict] (model-less). CSV strings become typed sequences.
        class EntityTransformationSet(m.ImmutableValueModel):
            """Typed outcome of transforming WMS entities into item models."""

            entity_names: Annotated[
                t.StrSequence,
                u.Field(description="Entity names present in the transformed set"),
            ]
            items: Annotated[
                t.SequenceOf[FlextDbtOracleWmsModels.DbtOracleWms.WmsItem],
                u.Field(description="Transformed WMS item models"),
            ]

        class TransformationResult(m.ImmutableValueModel):
            """Typed dbt-transformation summary composed from the meltano command result."""

            transformed_tables: Annotated[
                t.StrSequence,
                u.Field(description="Tables produced by the transformation"),
            ]
            requested_models: Annotated[
                t.StrSequence,
                u.Field(description="dbt models requested for the run"),
            ]
            command_result: Annotated[
                m.Meltano.CommandExecutionResult,
                u.Field(description="Typed meltano dbt command execution result"),
            ]

            @u.computed_field(return_type=str)
            @property
            def status(self) -> str:
                """Overall status derived from the command result."""
                return "success" if self.command_result.success else "failed"

        class WorkflowTracking(m.ImmutableValueModel):
            """Typed workflow-execution tracking payload."""

            workflow_name: Annotated[str, u.Field(description="Workflow name")]
            workflow_type: Annotated[str, u.Field(description="Workflow type")]
            tracking_id: Annotated[str, u.Field(description="Tracking identifier")]
            entity_names: Annotated[
                t.StrSequence,
                u.Field(default_factory=tuple, description="Entities in scope"),
            ]
            status: Annotated[
                str,
                u.Field(default="running", description="Tracking status"),
            ]

        class WorkflowRecommendation(m.ImmutableValueModel):
            """Typed workflow recommendation payload."""

            total_entities: Annotated[int, u.Field(description="Entity count")]
            recommendation: Annotated[str, u.Field(description="Recommendation text")]
            dbt_threads: Annotated[str, u.Field(description="Configured dbt threads")]
            target: Annotated[str, u.Field(description="dbt target profile")]

        class WmsMetadataResult(m.ImmutableValueModel):
            """Typed WMS metadata extraction summary."""

            available_entities: Annotated[
                t.StrSequence,
                u.Field(description="Discovered WMS entities"),
            ]
            inventory_count: Annotated[
                int, u.Field(description="Inventory record count")
            ]
            shipment_count: Annotated[int, u.Field(description="Shipment record count")]
            include_inventory_details: Annotated[
                bool,
                u.Field(description="Inventory detail flag"),
            ]
            include_shipment_tracking: Annotated[
                bool,
                u.Field(description="Shipment tracking flag"),
            ]
            status: Annotated[str, u.Field(description="Extraction status")]

        class DbtModelGenerationResult(m.ImmutableValueModel):
            """Typed dbt model-generation summary."""

            model_names: Annotated[
                t.StrSequence,
                u.Field(description="Generated dbt model names"),
            ]
            models_generated: Annotated[
                int, u.Field(description="Generated model count")
            ]
            output_dir: Annotated[str, u.Field(description="Output directory")]
            recommendation: Annotated[str, u.Field(description="Recommendation text")]
            status: Annotated[str, u.Field(description="Generation status")]

        class WorkflowResult(m.ImmutableValueModel):
            """Typed end-to-end workflow result."""

            tracking_id: Annotated[str, u.Field(description="Tracking identifier")]
            generate_models: Annotated[
                bool, u.Field(description="Model generation flag")
            ]
            run_transformations: Annotated[
                bool,
                u.Field(description="Transformation flag"),
            ]
            generated_models: Annotated[
                t.StrSequence,
                u.Field(default_factory=tuple, description="Generated models"),
            ]
            entity_names: Annotated[
                t.StrSequence,
                u.Field(default_factory=tuple, description="Entities processed"),
            ]
            total_records: Annotated[
                int,
                u.Field(default=0, description="Total records processed"),
            ]
            transformation_status: Annotated[
                str,
                u.Field(default="", description="Transformation status"),
            ]
            workflow_status: Annotated[
                str, u.Field(description="Overall workflow status")
            ]

        class DbtExecutionResult(m.ImmutableValueModel):
            """Typed dbt execution monitoring result."""

            command: Annotated[str, u.Field(description="dbt command")]
            dbt_subcommand: Annotated[str, u.Field(description="dbt subcommand")]
            requested_timeout_seconds: Annotated[
                int,
                u.Field(description="Requested timeout in seconds"),
            ]
            transformation: Annotated[
                FlextDbtOracleWmsModels.DbtOracleWms.TransformationResult,
                u.Field(description="Underlying transformation result"),
            ]

        class ConnectionStatus(m.ImmutableValueModel):
            """Typed Oracle WMS connection status."""

            status: Annotated[str, u.Field(description="Connection status")]
            environment: Annotated[str, u.Field(description="Environment name")]
            base_url: Annotated[str, u.Field(description="Oracle WMS base URL")]
            status_code: Annotated[int, u.Field(description="HTTP status code")]

        class PipelineResult(m.ImmutableValueModel):
            """Typed full pipeline result."""

            processed_entities: Annotated[
                t.StrSequence,
                u.Field(description="Entities processed by the pipeline"),
            ]
            total_records: Annotated[
                int, u.Field(description="Total records processed")
            ]
            transformation_status: Annotated[
                str,
                u.Field(description="Transformation status"),
            ]
            pipeline_status: Annotated[
                str, u.Field(description="Overall pipeline status")
            ]

    # NOTE (multi-agent, bead mro-wfc8): create_generator removed with ModelGenerator —
    # callers use u.DbtOracleWms.ModelBuilder.generate_wms_staging_models directly (§2a).


m = FlextDbtOracleWmsModels

__all__: list[str] = ["FlextDbtOracleWmsModels", "m"]
