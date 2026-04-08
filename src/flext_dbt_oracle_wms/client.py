"""Lazy re-export from internal module."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextDbtOracleWmsClient": (
        "flext_dbt_oracle_wms._utilities.client",
        "FlextDbtOracleWmsClient",
    ),
}
FlextDbtOracleWmsClient: object

__all__ = ["FlextDbtOracleWmsClient"]

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
