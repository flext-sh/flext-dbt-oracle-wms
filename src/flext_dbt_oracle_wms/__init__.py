# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports
from flext_dbt_oracle_wms.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)
from flext_dbt_oracle_wms._exports import FLEXT_DBT_ORACLE_WMS_LAZY_IMPORTS

_LAZY_IMPORTS = FLEXT_DBT_ORACLE_WMS_LAZY_IMPORTS


_EAGER_EXPORTS = (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServiceBase",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=_PUBLIC_EXPORTS,
)
