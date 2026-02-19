"""Protocols for DBT Oracle WMS integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, FlextTypes as t


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
                config: dict[str, t.GeneralValueType] | None = None,
            ) -> FlextResult[dict[str, t.GeneralValueType]]:
                """Run DBT models and return execution metadata."""
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, t.GeneralValueType] | None = None,
            ) -> FlextResult[dict[str, t.GeneralValueType]]:
                """Run DBT tests and return status metadata."""
                ...

        @runtime_checkable
        class WmsIntegrationProtocol(Protocol):
            """Protocol for Oracle WMS data extraction and transform stages."""

            def extract_wms_inventory_data(
                self,
                wms_config: dict[str, t.GeneralValueType],
                extraction_config: dict[str, t.GeneralValueType],
            ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
                """Extract inventory records from Oracle WMS."""
                ...


p = FlextDbtOracleWmsProtocols

__all__ = ["FlextDbtOracleWmsProtocols", "p"]
