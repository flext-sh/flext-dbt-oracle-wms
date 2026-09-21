# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Protocols package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .base import FlextDbtOracleWmsProtocolsBase
    from .contracts import FlextDbtOracleWmsProtocolsContracts
    from .dbt_runner import FlextDbtOracleWmsProtocolsDbtRunner
    from .wms_client import FlextDbtOracleWmsProtocolsWmsClient
__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsProtocolsBase", "FlextDbtOracleWmsProtocolsContracts", "FlextDbtOracleWmsProtocolsDbtRunner", "FlextDbtOracleWmsProtocolsWmsClient",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("FlextDbtOracleWmsProtocolsBase",),
            ".contracts": ("FlextDbtOracleWmsProtocolsContracts",),
            ".dbt_runner": ("FlextDbtOracleWmsProtocolsDbtRunner",),
            ".wms_client": ("FlextDbtOracleWmsProtocolsWmsClient",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
