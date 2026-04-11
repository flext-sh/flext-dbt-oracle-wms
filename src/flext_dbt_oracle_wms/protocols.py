"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_core import r
from flext_dbt_oracle_wms import t
from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms import FlextOracleWmsProtocols


class FlextDbtOracleWmsProtocols(FlextMeltanoProtocols, FlextOracleWmsProtocols):
    """Namespace for DBT Oracle WMS protocol contracts."""

    class DbtOracleWms:
        """DBT Oracle WMS protocol namespace."""

        @runtime_checkable
        class Dbt(Protocol):
            """Protocol for DBT operation execution."""

            def run_dbt_models(
                self,
                models: t.StrSequence | None = None,
                settings: t.Dict | None = None,
            ) -> r[t.Dict]:
                """Run DBT models and return execution metadata."""
                ...

            def test_dbt_models(
                self,
                models: t.StrSequence | None = None,
                settings: t.Dict | None = None,
            ) -> r[t.Dict]:
                """Run DBT tests and return status metadata."""
                ...

        @runtime_checkable
        class WmsIntegration(Protocol):
            """Protocol for Oracle WMS data extraction and transform stages."""

            def extract_wms_inventory_data(
                self,
                wms_config: t.Dict,
                extraction_config: t.Dict,
            ) -> r[Sequence[t.Dict]]:
                """Extract inventory records from Oracle WMS."""
                ...


__all__ = ["FlextDbtOracleWmsProtocols", "p"]

p = FlextDbtOracleWmsProtocols
