# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms.services package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .base import FlextDbtOracleWmsBase
    from .client import FlextDbtOracleWmsClient
    from .generation import FlextDbtOracleWmsGeneration
    from .metadata import FlextDbtOracleWmsMetadata
    from .workflow import FlextDbtOracleWmsWorkflow
__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsBase", "FlextDbtOracleWmsClient", "FlextDbtOracleWmsGeneration", "FlextDbtOracleWmsMetadata",
    "FlextDbtOracleWmsWorkflow",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("FlextDbtOracleWmsBase",),
            ".client": ("FlextDbtOracleWmsClient",),
            ".generation": ("FlextDbtOracleWmsGeneration",),
            ".metadata": ("FlextDbtOracleWmsMetadata",),
            ".workflow": ("FlextDbtOracleWmsWorkflow",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
