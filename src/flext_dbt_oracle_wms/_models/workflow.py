"""Workflow and transformation result models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_models/workflow
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated

from flext_meltano import m

from flext_dbt_oracle_wms._models import FlextDbtOracleWmsModelsItems


class FlextDbtOracleWmsModelsWorkflow(m):
    """Workflow result and transformation models."""

    # NOTE (multi-agent, bead mro-wfc8.3): typed result models replacing the banned
    # generic RootModel[dict] (model-less). CSV strings become typed sequences.
    class EntityTransformationSet(m.ImmutableValueModel):
        """Typed outcome of transforming WMS entities into item models."""

        entity_names: Annotated[
            Sequence[str],
            m.Field(description="Entity names present in the transformed set"),
        ]
        items: Annotated[
            Sequence[FlextDbtOracleWmsModelsItems.WmsItem],
            m.Field(description="Transformed WMS item models"),
        ]

    class TransformationResult(m.ImmutableValueModel):
        """Typed dbt-transformation summary composed from the meltano command result."""

        transformed_tables: Annotated[
            Sequence[str],
            m.Field(description="Tables produced by the transformation"),
        ]
        requested_models: Annotated[
            Sequence[str],
            m.Field(description="dbt models requested for the run"),
        ]
        command_result: Annotated[
            m.Meltano.CommandExecutionResult,
            m.Field(description="Typed meltano dbt command execution result"),
        ]

        @m.computed_field
        @property
        def status(self) -> str:
            """Overall status derived from the command result."""
            return "success" if self.command_result.success else "failed"

    class WorkflowTracking(m.ImmutableValueModel):
        """Typed workflow-execution tracking payload."""

        workflow_name: Annotated[str, m.Field(description="Workflow name")]
        workflow_type: Annotated[str, m.Field(description="Workflow type")]
        tracking_id: Annotated[str, m.Field(description="Tracking identifier")]
        entity_names: Annotated[
            Sequence[str],
            m.Field(default_factory=tuple, description="Entities in scope"),
        ]
        status: Annotated[
            str,
            m.Field(default="running", description="Tracking status"),
        ]

    class WorkflowRecommendation(m.ImmutableValueModel):
        """Typed workflow recommendation payload."""

        total_entities: Annotated[int, m.Field(description="Entity count")]
        recommendation: Annotated[str, m.Field(description="Recommendation text")]
        dbt_threads: Annotated[str, m.Field(description="Configured dbt threads")]
        target: Annotated[str, m.Field(description="dbt target profile")]

    class WmsMetadataResult(m.ImmutableValueModel):
        """Typed WMS metadata extraction summary."""

        available_entities: Annotated[
            Sequence[str],
            m.Field(description="Discovered WMS entities"),
        ]
        inventory_count: Annotated[int, m.Field(description="Inventory record count")]
        shipment_count: Annotated[int, m.Field(description="Shipment record count")]
        include_inventory_details: Annotated[
            bool,
            m.Field(description="Inventory detail flag"),
        ]
        include_shipment_tracking: Annotated[
            bool,
            m.Field(description="Shipment tracking flag"),
        ]
        status: Annotated[str, m.Field(description="Extraction status")]

    class DbtModelGenerationResult(m.ImmutableValueModel):
        """Typed dbt model-generation summary."""

        model_names: Annotated[
            Sequence[str],
            m.Field(description="Generated dbt model names"),
        ]
        models_generated: Annotated[int, m.Field(description="Generated model count")]
        output_dir: Annotated[str, m.Field(description="Output directory")]
        recommendation: Annotated[str, m.Field(description="Recommendation text")]
        status: Annotated[str, m.Field(description="Generation status")]

    class WorkflowResult(m.ImmutableValueModel):
        """Typed end-to-end workflow result."""

        tracking_id: Annotated[str, m.Field(description="Tracking identifier")]
        generate_models: Annotated[bool, m.Field(description="Model generation flag")]
        run_transformations: Annotated[bool, m.Field(description="Transformation flag")]
        generated_models: Annotated[
            Sequence[str],
            m.Field(default_factory=tuple, description="Generated models"),
        ]
        entity_names: Annotated[
            Sequence[str],
            m.Field(default_factory=tuple, description="Entities processed"),
        ]
        total_records: Annotated[
            int,
            m.Field(default=0, description="Total records processed"),
        ]
        transformation_status: Annotated[
            str,
            m.Field(default="", description="Transformation status"),
        ]
        workflow_status: Annotated[str, m.Field(description="Overall workflow status")]

    class DbtExecutionResult(m.ImmutableValueModel):
        """Typed dbt execution monitoring result."""

        command: Annotated[str, m.Field(description="dbt command")]
        dbt_subcommand: Annotated[str, m.Field(description="dbt subcommand")]
        requested_timeout_seconds: Annotated[
            int,
            m.Field(description="Requested timeout in seconds"),
        ]
        transformation: Annotated[
            FlextDbtOracleWmsModelsWorkflow.TransformationResult,
            m.Field(description="Underlying transformation result"),
        ]


__all__: list[str] = ["FlextDbtOracleWmsModelsWorkflow"]
