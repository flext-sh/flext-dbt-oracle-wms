# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import (
        build_lazy_import_map,
        cleanup_submodule_namespace,
        cli,
        core,
        d,
        h,
        install_lazy_exports,
        lazy,
        lazy_getattr,
        lazy_member,
        meltano,
        merge_lazy_imports,
        normalize_lazy_imports,
        r,
        resolve_lazy_members,
        x,
    )
    from flext_oracle_wms import api, e, oracle_wms, web

    from flext_dbt_oracle_wms.__version__ import (
        FlextDbtOracleWmsVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
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
    "u",
    "web",
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
        "api": "flext_oracle_wms",
        "build_lazy_import_map": "flext_meltano",
        "c": ".constants",
        "cleanup_submodule_namespace": "flext_meltano",
        "cli": "flext_meltano",
        "config": "._config",
        "core": "flext_meltano",
        "d": "flext_meltano",
        "dbt_oracle_wms": ".api",
        "e": "flext_oracle_wms",
        "h": "flext_meltano",
        "install_lazy_exports": "flext_meltano",
        "lazy": "flext_meltano",
        "lazy_getattr": "flext_meltano",
        "lazy_member": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "meltano": "flext_meltano",
        "merge_lazy_imports": "flext_meltano",
        "normalize_lazy_imports": "flext_meltano",
        "oracle_wms": "flext_oracle_wms",
        "p": ".protocols",
        "r": "flext_meltano",
        "resolve_lazy_members": "flext_meltano",
        "s": ".base",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "web": "flext_oracle_wms",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)

if not TYPE_CHECKING:
    from flext_dbt_oracle_wms.__version__ import __version__
