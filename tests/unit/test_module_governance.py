"""Public contract checks for DBT Oracle WMS entrypoints."""

from __future__ import annotations

from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms


def test_package_root_exposes_canonical_public_entrypoints() -> None:
    assert FlextDbtOracleWms.__name__ == "FlextDbtOracleWms"
    assert callable(main)
    assert FlextDbtOracleWmsCliService.__name__ == "FlextDbtOracleWmsCliService"
