# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Models package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .base import FlextDbtOracleWmsModelsBase
    from .connection import FlextDbtOracleWmsModelsConnection
    from .dbt import FlextDbtOracleWmsModelsDbt
    from .items import FlextDbtOracleWmsModelsItems
    from .workflow import FlextDbtOracleWmsModelsWorkflow
__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsModelsBase",
    "FlextDbtOracleWmsModelsConnection",
    "FlextDbtOracleWmsModelsDbt",
    "FlextDbtOracleWmsModelsItems",
    "FlextDbtOracleWmsModelsWorkflow",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("FlextDbtOracleWmsModelsBase",),
            ".connection": ("FlextDbtOracleWmsModelsConnection",),
            ".dbt": ("FlextDbtOracleWmsModelsDbt",),
            ".items": ("FlextDbtOracleWmsModelsItems",),
            ".workflow": ("FlextDbtOracleWmsModelsWorkflow",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
