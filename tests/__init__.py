# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_wms import e
    from flext_tests import api, td, tf, tk, tm

    from flext_dbt_oracle_wms import d, h, r, x
    from tests import unit
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
    "u",
    "unit",
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
        "c": ".constants",
        "d": "flext_dbt_oracle_wms",
        "e": "flext_oracle_wms",
        "h": "flext_dbt_oracle_wms",
        "m": ".models",
        "p": ".protocols",
        "r": "flext_dbt_oracle_wms",
        "s": ".base",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "unit": ".unit",
        "x": "flext_dbt_oracle_wms",
    }),
    public_exports=__all__,
)
