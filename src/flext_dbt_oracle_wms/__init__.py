# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
from flext_dbt_oracle_wms.__version__ import __version__

if TYPE_CHECKING:
    from flext_meltano import d, h, r, x
    from flext_oracle_wms import e

    from flext_dbt_oracle_wms import (
        _constants,
        _models,
        _protocols,
        _typings,
        _utilities,
        services,
    )
    from flext_dbt_oracle_wms.__version__ import (
        FlextDbtOracleWmsVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version_info__,
    )
    from flext_dbt_oracle_wms._config import FlextDbtOracleWmsConfig, config
    from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings, settings
    from flext_dbt_oracle_wms.api import FlextDbtOracleWms, dbt_oracle_wms
    from flext_dbt_oracle_wms.base import FlextDbtOracleWmsServiceBase, s
    from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
    from flext_dbt_oracle_wms.constants import FlextDbtOracleWmsConstants, c
    from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels, m
    from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols, p
    from flext_dbt_oracle_wms.typings import FlextDbtOracleWmsTypes, t
    from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsUtilities, u


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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_constants",
    "_models",
    "_protocols",
    "_typings",
    "_utilities",
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
    "services",
    "settings",
    "t",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleWms": ".api",
        "FlextDbtOracleWmsCliService": ".cli",
        "FlextDbtOracleWmsConfig": "._config",
        "FlextDbtOracleWmsConstants": ".constants",
        "FlextDbtOracleWmsModels": ".models",
        "FlextDbtOracleWmsProtocols": ".protocols",
        "FlextDbtOracleWmsServiceBase": ".base",
        "FlextDbtOracleWmsSettings": "._settings",
        "FlextDbtOracleWmsTypes": ".typings",
        "FlextDbtOracleWmsUtilities": ".utilities",
        "FlextDbtOracleWmsVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "_constants": "._constants",
        "_models": "._models",
        "_protocols": "._protocols",
        "_typings": "._typings",
        "_utilities": "._utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "dbt_oracle_wms": ".api",
        "e": "flext_oracle_wms",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": ".base",
        "services": ".services",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
