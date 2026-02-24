"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, t

type WmsPayload = t.Dict
type WmsPayloadList = list[t.Dict]


class FlextDbtOracleWmsProtocols:
    """Namespace for DBT Oracle WMS protocol contracts."""

    class DbtOracleWms:
        """DBT Oracle WMS protocol namespace."""

        @runtime_checkable
        class DbtProtocol(Protocol):
            """Protocol for DBT operation execution."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
                config: WmsPayload | None = None,
            ) -> FlextResult[WmsPayload]:
                """Run DBT models and return execution metadata."""
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: WmsPayload | None = None,
            ) -> FlextResult[WmsPayload]:
                """Run DBT tests and return status metadata."""
                ...

        @runtime_checkable
        class WmsIntegrationProtocol(Protocol):
            """Protocol for Oracle WMS data extraction and transform stages."""

            def extract_wms_inventory_data(
                self,
                wms_config: WmsPayload,
                extraction_config: WmsPayload,
            ) -> FlextResult[WmsPayloadList]:
                """Extract inventory records from Oracle WMS."""
                ...


p = FlextDbtOracleWmsProtocols

__all__ = ["FlextDbtOracleWmsProtocols", "p"]
