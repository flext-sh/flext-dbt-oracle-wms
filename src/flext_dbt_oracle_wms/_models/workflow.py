"""Workflow and transformation result models."""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m, u

from flext_dbt_oracle_wms import t


class FlextDbtOracleWmsModelsWorkflow(m):
    """Workflow result and transformation models."""

    class DbtOracleWms:
        """DBT Oracle WMS workflow namespace."""

        # NOTE (multi-agent, bead mro-wfc8.3): typed result models replacing the banned
        # generic RootModel[dict] (model-less). CSV strings become typed sequences.
        class EntityTransformationSet(m.ImmutableValueModel):
            """Typed outcome of transforming WMS entities into item models."""

            entity_names: Annotated[
                t.StrSequence,
                u.Field(description="Entity names present in the transformed set"),
            ]
            items: Annotated[
                t.SequenceOf[FlextDbtOracleWmsModelsWorkflow.DbtOracleWms.WmsItem],
                u.Field(description="Transformed WMS item models"),
            ]

        class TransformationResult(m.ImmutableValueModel):
            """Typed dbt-transformation summary composed from the meltano command result."""

            transformed_tables: Annotated[
                t.StrSequence,
                u.Field(description="Tables produced by the transformation"),
            ]
            requested_models: Annotated[
                t.StrSequence, u.Field(description="dbt models requested for the run")
            ]
            command_result: Annotated[
                m.Meltano.CommandExecutionResult,
                u.Field(description="Typed meltano dbt command execution result"),
            ]

            @u.computed_field
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
                str, u.Field(default="running", description="Tracking status")
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
                t.StrSequence, u.Field(description="Discovered WMS entities")
            ]
            inventory_count: Annotated[
                int, u.Field(description="Inventory record count")
            ]
            shipment_count: Annotated[int, u.Field(description="Shipment record count")]
            include_inventory_details: Annotated[
                bool, u.Field(description="Inventory detail flag")
            ]
            include_shipment_tracking: Annotated[
                bool, u.Field(description="Shipment tracking flag")
            ]
            status: Annotated[str, u.Field(description="Extraction status")]

        class DbtModelGenerationResult(m.ImmutableValueModel):
            """Typed dbt model-generation summary."""

            model_names: Annotated[
                t.StrSequence, u.Field(description="Generated dbt model names")
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
                bool, u.Field(description="Transformation flag")
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
                int, u.Field(default=0, description="Total records processed")
            ]
            transformation_status: Annotated[
                str, u.Field(default="", description="Transformation status")
            ]
            workflow_status: Annotated[
                str, u.Field(description="Overall workflow status")
            ]

        class DbtExecutionResult(m.ImmutableValueModel):
            """Typed dbt execution monitoring result."""

            command: Annotated[str, u.Field(description="dbt command")]
            dbt_subcommand: Annotated[str, u.Field(description="dbt subcommand")]
            requested_timeout_seconds: Annotated[
                int, u.Field(description="Requested timeout in seconds")
            ]
            transformation: Annotated[
                FlextDbtOracleWmsModelsWorkflow.DbtOracleWms.TransformationResult,
                u.Field(description="Underlying transformation result"),
            ]


__all__: list[str] = ["FlextDbtOracleWmsModelsWorkflow"]
