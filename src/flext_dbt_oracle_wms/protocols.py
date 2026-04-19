"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_dbt_oracle_wms import m, t
from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms import p


class FlextDbtOracleWmsProtocols(FlextMeltanoProtocols, p):
    """Namespace for DBT Oracle WMS protocol contracts."""

    class DbtOracleWms:
        """DBT Oracle WMS protocol namespace."""

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
