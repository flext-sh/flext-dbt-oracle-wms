# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT Oracle WMS utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._utilities import client as client
    from flext_dbt_oracle_wms._utilities.client import (
        FlextDbtOracleWmsClient as FlextDbtOracleWmsClient,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracleWmsClient": [
        "flext_dbt_oracle_wms._utilities.client",
        "FlextDbtOracleWmsClient",
    ],
    "client": ["flext_dbt_oracle_wms._utilities.client", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextDbtOracleWmsClient",
    "client",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
