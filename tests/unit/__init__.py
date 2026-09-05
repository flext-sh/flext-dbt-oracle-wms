# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import c, d, e, h, m, p, r, s, t, td, tf, tk, tm, tv, u, x

    from .test_api import TestsFlextDbtOracleWmsApi
    from .test_cli import TestsFlextDbtOracleWmsCli
    from .test_connection_profile import (
        test_connection_profile_returns_typed_oracle_wms_wire_shape,
    )
    from .test_module_governance import TestsFlextDbtOracleWmsModuleGovernance
__all__: tuple[str, ...] = (
    "TestsFlextDbtOracleWmsApi",
    "TestsFlextDbtOracleWmsCli",
    "TestsFlextDbtOracleWmsModuleGovernance",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "test_connection_profile_returns_typed_oracle_wms_wire_shape",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".test_api": ("TestsFlextDbtOracleWmsApi",),
            ".test_cli": ("TestsFlextDbtOracleWmsCli",),
            ".test_connection_profile": (
                "test_connection_profile_returns_typed_oracle_wms_wire_shape",
            ),
            ".test_module_governance": ("TestsFlextDbtOracleWmsModuleGovernance",),
            "flext_tests": (
                "c",
                "d",
                "e",
                "h",
                "m",
                "p",
                "r",
                "s",
                "t",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "u",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
