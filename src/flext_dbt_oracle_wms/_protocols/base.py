"""Base protocols for DBT Oracle WMS integration points.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_protocols/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols, p
from flext_oracle_wms import p as _oracle_wms_p

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import t
    from flext_dbt_oracle_wms._protocols import (
        FlextDbtOracleWmsProtocolsConnection,
        FlextDbtOracleWmsProtocolsWorkflow,
    )


class FlextDbtOracleWmsProtocolsBase(p, _oracle_wms_p):
    """Namespace for DBT Oracle WMS protocol contracts."""

    class DbtOracleWms:
        """DBT Oracle WMS protocol namespace."""

        @runtime_checkable
        class SettingsGroup(Protocol):
            """Runtime knobs supplied by the validated DbtOracleWms namespace."""

            @property
            def required_fields_per_entity(self) -> Mapping[str, Sequence[str]]:
                """Required fields of each configured WMS entity."""
                ...

            @property
            def oracle_wms_environment(self) -> str:
                """Selected Oracle WMS deployment environment."""
                ...

            @property
            def oracle_wms_base_url(self) -> str:
                """Selected Oracle WMS API endpoint."""
                ...

            @property
            def dbt_threads(self) -> int:
                """Configured dbt worker count."""
                ...

            @property
            def dbt_target(self) -> str:
                """Configured dbt profile target."""
                ...

        @runtime_checkable
        class Client(Protocol):
            """Protocol for the public Oracle WMS workflow client surface."""

            def discover_oracle_wms_entities(self) -> p.Result[Sequence[str]]:
                """Discover available Oracle WMS entities."""
                ...

            def extract_oracle_wms_data(
                self,
                entity_name: str,
                filters: t.ConfigurationMapping | None = None,
            ) -> p.Result[Sequence[t.ConfigurationMapping]]:
                """Extract records for a specific Oracle WMS entity.

                Args:
                    entity_name: WMS entity to fetch records for.
                    filters: Optional fetch filters applied by the
                        implementation.

                """
                ...

            def run_full_oracle_wms_to_dbt_pipeline(
                self,
                entity_names: Sequence[str] | None = None,
                filters: t.ConfigurationMapping | None = None,
                model_names: Sequence[str] | None = None,
            ) -> p.Result[FlextDbtOracleWmsProtocolsConnection.PipelineResult]:
                """Run the full Oracle WMS to DBT workflow.

                Args:
                    entity_names: Entities to process; implementations
                        discover entities when omitted.
                    filters: Optional fetch filters applied to every
                        extraction.
                    model_names: dbt models for the transformation step.

                """
                ...

            def test_oracle_wms_connection(
                self,
            ) -> p.Result[FlextDbtOracleWmsProtocolsConnection.ConnectionStatus]:
                """Validate Oracle WMS connectivity."""
                ...

            def transform_with_dbt(
                self,
                entity_data: Mapping[str, Sequence[t.ConfigurationMapping]],
                model_names: Sequence[str] | None,
            ) -> p.Result[p.Meltano.CommandExecutionResult]:
                """Run DBT transformations for extracted entity data.

                Args:
                    entity_data: Extracted entity records transformed
                        before the dbt run.
                    model_names: dbt models to run.

                """
                ...

        @runtime_checkable
        class Service(Protocol):
            """Protocol for the workflow/monitoring service surface."""

            def generate_workflow_recommendations(
                self,
                entities: Sequence[t.ConfigurationMapping] | None = None,
            ) -> p.Result[FlextDbtOracleWmsProtocolsWorkflow.WorkflowRecommendation]:
                """Generate workflow recommendations for entity processing.

                Args:
                    entities: Entity records in scope for the
                        recommendation.

                """
                ...

            def track_workflow_execution(
                self,
                workflow_name: str,
                workflow_type: str,
                entity_names: Sequence[str] | None = None,
                additional_data: t.ConfigValueMapping | None = None,
            ) -> FlextDbtOracleWmsProtocolsWorkflow.WorkflowTracking:
                """Return a typed tracking model for workflow instrumentation.

                Args:
                    workflow_name: Name recorded in the tracking payload.
                    workflow_type: Type recorded in the tracking payload.
                    entity_names: Entities in scope for the workflow.
                    additional_data: Optional extra instrumentation
                        context.

                """
                ...

            def log_workflow_completion(
                self,
                tracking_info: FlextDbtOracleWmsProtocolsWorkflow.WorkflowTracking,
                result: p.Result[FlextDbtOracleWmsProtocolsWorkflow.WorkflowResult],
            ) -> None:
                """Record the completion outcome of a tracked workflow.

                Args:
                    tracking_info: Tracking payload identifying the
                        workflow.
                    result: Final workflow result whose outcome is
                        recorded.

                """
                ...

    @runtime_checkable
    class DbtConnectionProfile(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def type(self) -> str:
            """Dbt adapter type identifier."""
            ...

        @property
        def base_url(self) -> str:
            """Oracle WMS base URL."""
            ...

        @property
        def environment(self) -> str:
            """Oracle WMS environment."""
            ...

        @property
        def target(self) -> str:
            """Dbt target profile."""
            ...

        @property
        def threads(self) -> int:
            """Dbt parallel threads."""
            ...

        @property
        def project(self) -> str:
            """Dbt project name owning this profile."""
            ...


__all__: list[str] = ["FlextDbtOracleWmsProtocolsBase"]
