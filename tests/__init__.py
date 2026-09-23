# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_cli import cli
    from flext_meltano import meltano
    from flext_oracle_wms import e, oracle_wms
    from flext_tests import (
        active_rules,
        api,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )
    from flext_web import web

    from flext_core import core, d, h, lazy_attribute, r, x
    from flext_dbt_oracle_wms import config, dbt_oracle_wms, main, s, settings

    from . import unit
    from .base import TestsFlextDbtOracleWmsServiceBase
    from .constants import TestsFlextDbtOracleWmsConstants, c
    from .models import TestsFlextDbtOracleWmsModels, m
    from .protocols import TestsFlextDbtOracleWmsProtocols, p
    from .settings import TestsFlextDbtOracleWmsSettings
    from .typings import TestsFlextDbtOracleWmsTypes, t
    from .utilities import TestsFlextDbtOracleWmsUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsServiceBase",
    "TestsFlextDbtOracleWmsSettings",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
    "active_rules",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "dbt_oracle_wms",
    "discover_repository_root",
    "e",
    "h",
    "install_local_packages",
    "lazy_attribute",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "oracle_wms",
    "p",
    "r",
    "s",
    "settings",
    "split_csv",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "web",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextDbtOracleWmsServiceBase",),
            ".constants": ("TestsFlextDbtOracleWmsConstants", "c"),
            ".models": ("TestsFlextDbtOracleWmsModels", "m"),
            ".protocols": ("TestsFlextDbtOracleWmsProtocols", "p"),
            ".settings": ("TestsFlextDbtOracleWmsSettings",),
            ".typings": ("TestsFlextDbtOracleWmsTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtOracleWmsUtilities", "u"),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "h", "lazy_attribute", "r", "x"),
            "flext_dbt_oracle_wms": (
                "config",
                "dbt_oracle_wms",
                "main",
                "s",
                "settings",
            ),
            "flext_meltano": ("meltano",),
            "flext_oracle_wms": ("e", "oracle_wms"),
            "flext_tests": (
                "active_rules",
                "api",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
            "flext_web": ("web",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
