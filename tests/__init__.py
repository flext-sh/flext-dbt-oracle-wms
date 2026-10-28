# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_wms import e
    from flext_tests import (
        api,
        build_lazy_import_map,
        cleanup_submodule_namespace,
        core,
        install_lazy_exports,
        install_local_packages,
        lazy,
        lazy_getattr,
        lazy_member,
        merge_lazy_imports,
        normalize_lazy_imports,
        resolve_lazy_members,
        td,
        tf,
        tk,
        tm,
    )

    from flext_dbt_oracle_wms import (
        cli,
        config,
        d,
        dbt_oracle_wms,
        h,
        main,
        meltano,
        oracle_wms,
        r,
        settings,
        web,
        x,
    )
    from tests.base import TestsFlextDbtOracleWmsServiceBase, s
    from tests.constants import TestsFlextDbtOracleWmsConstants, c
    from tests.models import TestsFlextDbtOracleWmsModels, m
    from tests.protocols import TestsFlextDbtOracleWmsProtocols, p
    from tests.settings import TestsFlextDbtOracleWmsSettings
    from tests.typings import TestsFlextDbtOracleWmsTypes, t
    from tests.utilities import TestsFlextDbtOracleWmsUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsServiceBase",
    "TestsFlextDbtOracleWmsSettings",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
    "api",
    "build_lazy_import_map",
    "c",
    "cleanup_submodule_namespace",
    "cli",
    "config",
    "core",
    "d",
    "dbt_oracle_wms",
    "e",
    "h",
    "install_lazy_exports",
    "install_local_packages",
    "lazy",
    "lazy_getattr",
    "lazy_member",
    "m",
    "main",
    "meltano",
    "merge_lazy_imports",
    "normalize_lazy_imports",
    "oracle_wms",
    "p",
    "r",
    "resolve_lazy_members",
    "s",
    "settings",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextDbtOracleWmsConstants": ".constants",
        "TestsFlextDbtOracleWmsModels": ".models",
        "TestsFlextDbtOracleWmsProtocols": ".protocols",
        "TestsFlextDbtOracleWmsServiceBase": ".base",
        "TestsFlextDbtOracleWmsSettings": ".settings",
        "TestsFlextDbtOracleWmsTypes": ".typings",
        "TestsFlextDbtOracleWmsUtilities": ".utilities",
        "api": "flext_tests",
        "build_lazy_import_map": "flext_tests",
        "c": ".constants",
        "cleanup_submodule_namespace": "flext_tests",
        "cli": "flext_dbt_oracle_wms",
        "config": "flext_dbt_oracle_wms",
        "core": "flext_tests",
        "d": "flext_dbt_oracle_wms",
        "dbt_oracle_wms": "flext_dbt_oracle_wms",
        "e": "flext_oracle_wms",
        "h": "flext_dbt_oracle_wms",
        "install_lazy_exports": "flext_tests",
        "install_local_packages": "flext_tests",
        "lazy": "flext_tests",
        "lazy_getattr": "flext_tests",
        "lazy_member": "flext_tests",
        "m": ".models",
        "main": "flext_dbt_oracle_wms",
        "meltano": "flext_dbt_oracle_wms",
        "merge_lazy_imports": "flext_tests",
        "normalize_lazy_imports": "flext_tests",
        "oracle_wms": "flext_dbt_oracle_wms",
        "p": ".protocols",
        "r": "flext_dbt_oracle_wms",
        "resolve_lazy_members": "flext_tests",
        "s": ".base",
        "settings": "flext_dbt_oracle_wms",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "web": "flext_dbt_oracle_wms",
        "x": "flext_dbt_oracle_wms",
    }),
    public_exports=__all__,
)
