# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_dbt_oracle_wms.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import d
    from flext_core.exceptions import e
    from flext_core.handlers import h
    from flext_core.mixins import x
    from flext_core.result import r
    from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms.base import (
        FlextDbtOracleWmsServiceBase,
        FlextDbtOracleWmsServiceBase as s,
    )
    from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants,
        FlextDbtOracleWmsConstants as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels,
        FlextDbtOracleWmsModels as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsProtocols,
        FlextDbtOracleWmsProtocols as p,
    )
    from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsTypes as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities,
        FlextDbtOracleWmsUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("._utilities",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".base": ("FlextDbtOracleWmsServiceBase",),
            ".cli": (
                "FlextDbtOracleWmsCliService",
                "main",
            ),
            ".constants": ("FlextDbtOracleWmsConstants",),
            ".models": ("FlextDbtOracleWmsModels",),
            ".protocols": ("FlextDbtOracleWmsProtocols",),
            ".settings": ("FlextDbtOracleWmsSettings",),
            ".simple_api": ("FlextDbtOracleWms",),
            ".typings": ("FlextDbtOracleWmsTypes",),
            ".utilities": ("FlextDbtOracleWmsUtilities",),
            "flext_core.decorators": ("d",),
            "flext_core.exceptions": ("e",),
            "flext_core.handlers": ("h",),
            "flext_core.mixins": ("x",),
            "flext_core.result": ("r",),
        },
        alias_groups={
            ".base": (("s", "FlextDbtOracleWmsServiceBase"),),
            ".constants": (("c", "FlextDbtOracleWmsConstants"),),
            ".models": (("m", "FlextDbtOracleWmsModels"),),
            ".protocols": (("p", "FlextDbtOracleWmsProtocols"),),
            ".typings": (("t", "FlextDbtOracleWmsTypes"),),
            ".utilities": (("u", "FlextDbtOracleWmsUtilities"),),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)

__all__ = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
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
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
