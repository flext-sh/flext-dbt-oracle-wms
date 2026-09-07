# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import FlextDbtOracleWmsConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x

    from . import unit as unit
    from .base import (
        TestsFlextDbtOracleWmsServiceBase,
        TestsFlextDbtOracleWmsServiceBase as s,
    )
    from .constants import (
        TestsFlextDbtOracleWmsConstants,
        TestsFlextDbtOracleWmsConstants as c,
    )
    from .models import TestsFlextDbtOracleWmsModels, TestsFlextDbtOracleWmsModels as m
    from .protocols import (
        TestsFlextDbtOracleWmsProtocols,
        TestsFlextDbtOracleWmsProtocols as p,
    )
    from .settings import TestsFlextDbtOracleWmsSettings
    from .typings import TestsFlextDbtOracleWmsTypes, TestsFlextDbtOracleWmsTypes as t
    from .utilities import (
        TestsFlextDbtOracleWmsUtilities,
        TestsFlextDbtOracleWmsUtilities as u,
    )
__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsConstants",
    "FlextTestsConstants",
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsServiceBase",
    "TestsFlextDbtOracleWmsSettings",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
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
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextDbtOracleWmsServiceBase", "s"),
            ".constants": ("TestsFlextDbtOracleWmsConstants", "c"),
            ".models": ("TestsFlextDbtOracleWmsModels", "m"),
            ".protocols": ("TestsFlextDbtOracleWmsProtocols", "p"),
            ".settings": ("TestsFlextDbtOracleWmsSettings",),
            ".typings": ("TestsFlextDbtOracleWmsTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtOracleWmsUtilities", "u"),
            "flext_dbt_oracle_wms": ("FlextDbtOracleWmsConstants",),
            "flext_tests": (
                "FlextTestsConstants",
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
