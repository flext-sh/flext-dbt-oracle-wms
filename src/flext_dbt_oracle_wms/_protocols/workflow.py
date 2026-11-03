# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_protocols/workflow
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_meltano import p

    from flext_dbt_oracle_wms._protocols import FlextDbtOracleWmsProtocolsItems


class FlextDbtOracleWmsProtocolsWorkflow:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class EntityTransformationSet(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def entity_names(self) -> Sequence[str]:
            """Entity names present in the transformed set."""
            ...

        @property
        def items(self) -> Sequence[FlextDbtOracleWmsProtocolsItems.WmsItem]:
            """Transformed WMS item models."""
            ...

    @runtime_checkable
    class TransformationResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def transformed_tables(self) -> Sequence[str]:
            """Tables produced by the transformation."""
            ...

        @property
        def requested_models(self) -> Sequence[str]:
            """Dbt models requested for the run."""
            ...

        @property
        def command_result(self) -> p.Meltano.CommandExecutionResult:
            """Typed meltano dbt command execution result."""
            ...

        @property
        def status(self) -> str:
            """Overall status derived from the command result."""
            ...

    @runtime_checkable
    class WorkflowTracking(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def workflow_name(self) -> str:
            """Workflow name."""
            ...

        @property
        def workflow_type(self) -> str:
            """Workflow type."""
            ...

        @property
        def tracking_id(self) -> str:
            """Tracking identifier."""
            ...

        @property
        def entity_names(self) -> Sequence[str]:
            """Entities in scope."""
            ...

        @property
        def status(self) -> str:
            """Tracking status."""
            ...

    @runtime_checkable
    class WorkflowRecommendation(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def total_entities(self) -> int:
            """Entity count."""
            ...

        @property
        def recommendation(self) -> str:
            """Recommendation text."""
            ...

        @property
        def dbt_threads(self) -> str:
            """Configured dbt threads."""
            ...

        @property
        def target(self) -> str:
            """Dbt target profile."""
            ...

    @runtime_checkable
    class WmsMetadataResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def available_entities(self) -> Sequence[str]:
            """Discovered WMS entities."""
            ...

        @property
        def inventory_count(self) -> int:
            """Inventory record count."""
            ...

        @property
        def shipment_count(self) -> int:
            """Shipment record count."""
            ...

        @property
        def include_inventory_details(self) -> bool:
            """Inventory detail flag."""
            ...

        @property
        def include_shipment_tracking(self) -> bool:
            """Shipment tracking flag."""
            ...

        @property
        def status(self) -> str:
            """Extraction status."""
            ...

    @runtime_checkable
    class DbtModelGenerationResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def model_names(self) -> Sequence[str]:
            """Generated dbt model names."""
            ...

        @property
        def models_generated(self) -> int:
            """Generated model count."""
            ...

        @property
        def output_dir(self) -> str:
            """Output directory."""
            ...

        @property
        def recommendation(self) -> str:
            """Recommendation text."""
            ...

        @property
        def status(self) -> str:
            """Generation status."""
            ...

    @runtime_checkable
    class WorkflowResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def tracking_id(self) -> str:
            """Tracking identifier."""
            ...

        @property
        def generate_models(self) -> bool:
            """Model generation flag."""
            ...

        @property
        def run_transformations(self) -> bool:
            """Transformation flag."""
            ...

        @property
        def generated_models(self) -> Sequence[str]:
            """Generated models."""
            ...

        @property
        def entity_names(self) -> Sequence[str]:
            """Entities processed."""
            ...

        @property
        def total_records(self) -> int:
            """Total records processed."""
            ...

        @property
        def transformation_status(self) -> str:
            """Transformation status."""
            ...

        @property
        def workflow_status(self) -> str:
            """Overall workflow status."""
            ...

    @runtime_checkable
    class DbtExecutionResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def command(self) -> str:
            """Dbt command."""
            ...

        @property
        def dbt_subcommand(self) -> str:
            """Dbt subcommand."""
            ...

        @property
        def requested_timeout_seconds(self) -> int:
            """Requested timeout in seconds."""
            ...

        @property
        def transformation(
            self,
        ) -> FlextDbtOracleWmsProtocolsWorkflow.TransformationResult:
            """Underlying transformation result."""
            ...


__all__: list[str] = [
    "FlextDbtOracleWmsProtocolsWorkflow",
]
