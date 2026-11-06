# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_wms import e
    from flext_tests import api, td, tf, tk, tm

    from flext_dbt_oracle_wms import (
        FlextDbtOracleWms,
        FlextDbtOracleWmsCliService,
        FlextDbtOracleWmsConfig,
        FlextDbtOracleWmsConstants,
        FlextDbtOracleWmsModels,
        FlextDbtOracleWmsProtocols,
        FlextDbtOracleWmsServiceBase,
        FlextDbtOracleWmsSettings,
        FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsUtilities,
        FlextDbtOracleWmsVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        d,
        dbt_oracle_wms,
        h,
        main,
        r,
        settings,
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
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsConfig",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServiceBase",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "FlextDbtOracleWmsVersion",
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsServiceBase",
    "TestsFlextDbtOracleWmsSettings",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "c",
    "config",
    "d",
    "dbt_oracle_wms",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextDbtOracleWms": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsCliService": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsConfig": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsConstants": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsModels": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsProtocols": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsServiceBase": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsSettings": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsTypes": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsUtilities": "flext_dbt_oracle_wms",
        "FlextDbtOracleWmsVersion": "flext_dbt_oracle_wms",
        "TestsFlextDbtOracleWmsConstants": ".constants",
        "TestsFlextDbtOracleWmsModels": ".models",
        "TestsFlextDbtOracleWmsProtocols": ".protocols",
        "TestsFlextDbtOracleWmsServiceBase": ".base",
        "TestsFlextDbtOracleWmsSettings": ".settings",
        "TestsFlextDbtOracleWmsTypes": ".typings",
        "TestsFlextDbtOracleWmsUtilities": ".utilities",
        "__author__": "flext_dbt_oracle_wms",
        "__author_email__": "flext_dbt_oracle_wms",
        "__description__": "flext_dbt_oracle_wms",
        "__license__": "flext_dbt_oracle_wms",
        "__title__": "flext_dbt_oracle_wms",
        "__url__": "flext_dbt_oracle_wms",
        "__version__": "flext_dbt_oracle_wms",
        "__version_info__": "flext_dbt_oracle_wms",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_dbt_oracle_wms",
        "d": "flext_dbt_oracle_wms",
        "dbt_oracle_wms": "flext_dbt_oracle_wms",
        "e": "flext_oracle_wms",
        "h": "flext_dbt_oracle_wms",
        "m": ".models",
        "main": "flext_dbt_oracle_wms",
        "p": ".protocols",
        "r": "flext_dbt_oracle_wms",
        "s": ".base",
        "settings": "flext_dbt_oracle_wms",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_dbt_oracle_wms",
    },
    public_exports=__all__,
)
