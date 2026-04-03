# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports
from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient

if _t.TYPE_CHECKING:
    import flext_dbt_oracle_wms._utilities.client as _flext_dbt_oracle_wms__utilities_client

    client = _flext_dbt_oracle_wms__utilities_client

    _ = (
        FlextDbtOracleWmsClient,
        client,
    )
_LAZY_IMPORTS = {
    "FlextDbtOracleWmsClient": "flext_dbt_oracle_wms._utilities.client",
    "client": "flext_dbt_oracle_wms._utilities.client",
}

__all__ = [
    "FlextDbtOracleWmsClient",
    "client",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
