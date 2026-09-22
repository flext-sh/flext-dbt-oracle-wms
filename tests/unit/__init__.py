# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .test_cli import TestsFlextDbtOracleWmsCli
    from .test_connection_profile import TestsFlextDbtOracleWmsConnectionProfile
    from .test_module_governance import TestsFlextDbtOracleWmsModuleGovernance
__all__: tuple[str, ...] = (
    "TestsFlextDbtOracleWmsCli",
    "TestsFlextDbtOracleWmsConnectionProfile",
    "TestsFlextDbtOracleWmsModuleGovernance",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".test_cli": ("TestsFlextDbtOracleWmsCli",),
            ".test_connection_profile": ("TestsFlextDbtOracleWmsConnectionProfile",),
            ".test_module_governance": ("TestsFlextDbtOracleWmsModuleGovernance",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
