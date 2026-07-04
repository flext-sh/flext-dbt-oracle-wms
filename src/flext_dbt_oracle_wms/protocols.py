"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import p
from flext_oracle_wms import FlextOracleWmsProtocols

if TYPE_CHECKING:
    from collections.abc import (
        Sequence,
    )

    from flext_dbt_oracle_wms.typings import t
    from flext_meltano import m


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
            ) -> p.Result[m.Dict]:
                """Run the full Oracle WMS to DBT workflow."""
                ...

            def test_oracle_wms_connection(self) -> p.Result[m.Dict]:
                """Validate Oracle WMS connectivity."""
                ...

            def transform_with_dbt(
                self,
                entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
                model_names: t.StrSequence | None,
            ) -> p.Result[m.Dict]:
                """Run DBT transformations for extracted entity data."""
                ...

        @runtime_checkable
        class Dbt(Protocol):
            """Protocol for DBT operation execution."""

            def run_dbt_models(
                self,
                models: t.StrSequence | None = None,
                settings: m.Dict | None = None,
            ) -> p.Result[m.Dict]:
                """Run DBT models and return execution metadata."""
                ...

            def test_dbt_models(
                self,
                models: t.StrSequence | None = None,
                settings: m.Dict | None = None,
            ) -> p.Result[m.Dict]:
                """Run DBT tests and return status metadata."""
                ...

        @runtime_checkable
        class WmsIntegration(Protocol):
            """Protocol for Oracle WMS data extraction and transform stages."""

            def extract_wms_inventory_data(
                self,
                wms_config: m.Dict,
                extraction_config: m.Dict,
            ) -> p.Result[Sequence[m.Dict]]:
                """Extract inventory records from Oracle WMS."""
                ...


p = FlextDbtOracleWmsProtocols

__all__: list[str] = ["FlextDbtOracleWmsProtocols", "p"]
