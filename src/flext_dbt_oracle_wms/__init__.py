# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

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
    from . import services as services
    from enum import StrEnum, unique
    from flext_oracle_wms import FlextOracleWmsConstants, d, e, h, r, x
    from typing import Final

    from ._config import FlextDbtOracleWmsConfig, config
    from ._settings import FlextDbtOracleWmsSettings, settings
    from .api import FlextDbtOracleWms, dbt_oracle_wms
    from .base import FlextDbtOracleWmsServiceBase, FlextDbtOracleWmsServiceBase as s
    from .cli import FlextDbtOracleWmsCliService, main
    from .constants import FlextDbtOracleWmsConstants, FlextDbtOracleWmsConstants as c
    from .models import FlextDbtOracleWmsModels, FlextDbtOracleWmsModels as m
    from .protocols import FlextDbtOracleWmsProtocols, FlextDbtOracleWmsProtocols as p
    from .services.base import FlextDbtOracleWmsBase
    from .services.metadata import FlextDbtOracleWmsMetadata
    from .services.models import FlextDbtOracleWmsModelsApi
    from .services.workflow import FlextDbtOracleWmsWorkflow
    from .typings import FlextDbtOracleWmsTypes, FlextDbtOracleWmsTypes as t
    from .utilities import FlextDbtOracleWmsUtilities, FlextDbtOracleWmsUtilities as u
__all__: tuple[str, ...] = (
    "Final",
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsBase",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsConfig",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsMetadata",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsModelsApi",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServiceBase",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "FlextDbtOracleWmsWorkflow",
    "FlextOracleWmsConstants",
    "StrEnum",
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
    "services",
    "settings",
    "t",
    "u",
    "unique",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextDbtOracleWmsConfig", "config"),
            "._settings": ("FlextDbtOracleWmsSettings", "settings"),
            ".api": ("FlextDbtOracleWms", "dbt_oracle_wms"),
            ".base": ("FlextDbtOracleWmsServiceBase", "s"),
            ".cli": ("FlextDbtOracleWmsCliService", "main"),
            ".constants": ("FlextDbtOracleWmsConstants", "c"),
            ".models": ("FlextDbtOracleWmsModels", "m"),
            ".protocols": ("FlextDbtOracleWmsProtocols", "p"),
            ".services": ("services",),
            ".services.base": ("FlextDbtOracleWmsBase",),
            ".services.metadata": ("FlextDbtOracleWmsMetadata",),
            ".services.models": ("FlextDbtOracleWmsModelsApi",),
            ".services.workflow": ("FlextDbtOracleWmsWorkflow",),
            ".typings": ("FlextDbtOracleWmsTypes", "t"),
            ".utilities": ("FlextDbtOracleWmsUtilities", "u"),
            "enum": ("StrEnum", "unique"),
            "flext_oracle_wms": ("FlextOracleWmsConstants", "d", "e", "h", "r", "x"),
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
