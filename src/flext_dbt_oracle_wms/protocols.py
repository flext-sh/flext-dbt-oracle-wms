"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import p
from flext_oracle_wms import FlextOracleWmsProtocols

if TYPE_CHECKING:
    from collections.abc import (
        Sequence,
    )

    from flext_dbt_oracle_wms import m, t


class FlextDbtOracleWmsProtocols(p, FlextOracleWmsProtocols):
    """Namespace for DBT Oracle WMS protocol contracts."""

    class DbtOracleWms:
        """DBT Oracle WMS protocol namespace."""

        @runtime_checkable
        class Client(Protocol):
            """Protocol for the public Oracle WMS workflow client surface."""

            def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
                """Discover available Oracle WMS entities."""
                ...

            def extract_oracle_wms_data(
                self,
                entity_name: str,
                filters: t.ConfigurationMapping | None = None,
            ) -> p.Result[Sequence[t.ConfigurationMapping]]:
                """Extract records for a specific Oracle WMS entity."""
                ...

            def run_full_oracle_wms_to_dbt_pipeline(
                self,
                entity_names: t.StrSequence | None = None,
                filters: t.ConfigurationMapping | None = None,
                model_names: t.StrSequence | None = None,
            ) -> p.Result[m.DbtOracleWms.PipelineResult]:
                """Run the full Oracle WMS to DBT workflow."""
                ...

            def test_oracle_wms_connection(
                self,
            ) -> p.Result[m.DbtOracleWms.ConnectionStatus]:
                """Validate Oracle WMS connectivity."""
                ...

            def transform_with_dbt(
                self,
                entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
                model_names: t.StrSequence | None,
            ) -> p.Result[m.Meltano.CommandExecutionResult]:
                """Run DBT transformations for extracted entity data."""
                ...

        @runtime_checkable
        class Service(Protocol):
            """Protocol for the workflow/monitoring service surface."""

            def generate_workflow_recommendations(
                self,
                entities: t.SequenceOf[t.ConfigurationMapping] | None = None,
            ) -> p.Result[m.DbtOracleWms.WorkflowRecommendation]:
                """Generate workflow recommendations for entity processing."""
                ...

            def track_workflow_execution(
                self,
                workflow_name: str,
                workflow_type: str,
                entity_names: t.StrSequence | None = None,
                additional_data: t.ConfigValueMapping | None = None,
            ) -> m.DbtOracleWms.WorkflowTracking:
                """Return a typed tracking model for workflow instrumentation."""
                ...


p = FlextDbtOracleWmsProtocols

__all__: list[str] = ["FlextDbtOracleWmsProtocols", "p"]
