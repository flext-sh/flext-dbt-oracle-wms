"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms.protocols import FlextOracleWmsProtocols





class FlextDbtOracleWmsProtocols(FlextMeltanoProtocols, FlextOracleWmsProtocols):
    """Namespace for DBT Oracle WMS protocol contracts."""

    class DbtOracleWms:
        """DBT Oracle WMS protocol namespace."""

        @runtime_checkable
        class DbtProtocol(Protocol):
            """Protocol for DBT operation execution."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
                config: m.Dict | None = None,
            ) -> FlextResult[m.Dict]:
                """Run DBT models and return execution metadata."""
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: m.Dict | None = None,
            ) -> FlextResult[m.Dict]:
                """Run DBT tests and return status metadata."""
                ...

        @runtime_checkable
        class WmsIntegrationProtocol(Protocol):
            """Protocol for Oracle WMS data extraction and transform stages."""

            def extract_wms_inventory_data(
                self,
                wms_config: m.Dict,
                extraction_config: m.Dict,
            ) -> FlextResult[list[m.Dict]]:
                """Extract inventory records from Oracle WMS."""
                ...


p = FlextDbtOracleWmsProtocols

__all__ = ["FlextDbtOracleWmsProtocols", "p"]
