# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._utilities.client import (
        FlextDbtOracleWmsClient as FlextDbtOracleWmsClient,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".client": ("FlextDbtOracleWmsClient",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
