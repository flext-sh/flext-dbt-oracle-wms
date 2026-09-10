# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Utilities package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .base import FlextDbtOracleWmsUtilitiesBase
    from .model_builder import FlextDbtOracleWmsUtilitiesModelBuilder
    from .service import FlextDbtOracleWmsUtilitiesService
    from .transformer import FlextDbtOracleWmsUtilitiesTransformer
__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsUtilitiesBase",
    "FlextDbtOracleWmsUtilitiesModelBuilder",
    "FlextDbtOracleWmsUtilitiesService",
    "FlextDbtOracleWmsUtilitiesTransformer",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("FlextDbtOracleWmsUtilitiesBase",),
            ".model_builder": ("FlextDbtOracleWmsUtilitiesModelBuilder",),
            ".service": ("FlextDbtOracleWmsUtilitiesService",),
            ".transformer": ("FlextDbtOracleWmsUtilitiesTransformer",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
