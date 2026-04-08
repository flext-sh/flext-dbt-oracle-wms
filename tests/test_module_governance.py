"""Public contract checks for DBT Oracle WMS CLI entrypoints."""

from __future__ import annotations

from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main


def test_public_cli_module_exposes_canonical_entrypoints() -> None:
    assert callable(main)
    assert FlextDbtOracleWmsCliService.__name__ == "FlextDbtOracleWmsCliService"
