# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_oracle_wms import d as d
    from flext_oracle_wms import e as e
    from flext_oracle_wms import h as h
    from flext_oracle_wms import r as r
    from flext_oracle_wms import x as x

    from ._config import FlextDbtOracleWmsConfig as FlextDbtOracleWmsConfig
    from ._config import config as config
    from ._settings import FlextDbtOracleWmsSettings as FlextDbtOracleWmsSettings
    from ._settings import settings as settings
    from .api import FlextDbtOracleWms as FlextDbtOracleWms
    from .api import dbt_oracle_wms as dbt_oracle_wms
    from .base import FlextDbtOracleWmsServiceBase as FlextDbtOracleWmsServiceBase

    s: type[FlextDbtOracleWmsServiceBase]
    from .cli import FlextDbtOracleWmsCliService as FlextDbtOracleWmsCliService
    from .cli import main as main
    from .constants import FlextDbtOracleWmsConstants as FlextDbtOracleWmsConstants

    c: type[FlextDbtOracleWmsConstants]
    from .models import FlextDbtOracleWmsModels as FlextDbtOracleWmsModels

    m: type[FlextDbtOracleWmsModels]
    from .protocols import FlextDbtOracleWmsProtocols as FlextDbtOracleWmsProtocols

    p: type[FlextDbtOracleWmsProtocols]
    from .typings import FlextDbtOracleWmsTypes as FlextDbtOracleWmsTypes

    t: type[FlextDbtOracleWmsTypes]
    from .utilities import FlextDbtOracleWmsUtilities as FlextDbtOracleWmsUtilities

    u: type[FlextDbtOracleWmsUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextDbtOracleWmsConfig", "config"),
    "._settings": ("FlextDbtOracleWmsSettings", "settings"),
    ".api": ("FlextDbtOracleWms", "dbt_oracle_wms"),
    ".base": ("FlextDbtOracleWmsServiceBase", "s"),
    ".cli": ("FlextDbtOracleWmsCliService", "main"),
    ".constants": ("FlextDbtOracleWmsConstants", "c"),
    ".models": ("FlextDbtOracleWmsModels", "m"),
    ".protocols": ("FlextDbtOracleWmsProtocols", "p"),
    ".typings": ("FlextDbtOracleWmsTypes", "t"),
    ".utilities": ("FlextDbtOracleWmsUtilities", "u"),
    "flext_oracle_wms": ("d", "e", "h", "r", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
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
    "u",
    "x",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
