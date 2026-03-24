# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_dbt_oracle_wms.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_dbt_oracle_wms.cli import (
        FlextDbtOracleWmsCliService,
        discover,
        extract,
        info,
        logger,
        main,
        pipeline,
    )
    from flext_dbt_oracle_wms.client import FlextDbtOracleWmsClient
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
    from flext_dbt_oracle_wms.services import FlextDbtOracleWmsServices
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsTypes as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities,
        FlextDbtOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, tuple[str, str]] = {
    "FlextDbtOracleWms": ("flext_dbt_oracle_wms.simple_api", "FlextDbtOracleWms"),
    "FlextDbtOracleWmsCliService": (
        "flext_dbt_oracle_wms.cli",
        "FlextDbtOracleWmsCliService",
    ),
    "FlextDbtOracleWmsClient": (
        "flext_dbt_oracle_wms.client",
        "FlextDbtOracleWmsClient",
    ),
    "FlextDbtOracleWmsConstants": (
        "flext_dbt_oracle_wms.constants",
        "FlextDbtOracleWmsConstants",
    ),
    "FlextDbtOracleWmsModels": (
        "flext_dbt_oracle_wms.models",
        "FlextDbtOracleWmsModels",
    ),
    "FlextDbtOracleWmsProtocols": (
        "flext_dbt_oracle_wms.protocols",
        "FlextDbtOracleWmsProtocols",
    ),
    "FlextDbtOracleWmsServices": (
        "flext_dbt_oracle_wms.services",
        "FlextDbtOracleWmsServices",
    ),
    "FlextDbtOracleWmsTypes": (
        "flext_dbt_oracle_wms.typings",
        "FlextDbtOracleWmsTypes",
    ),
    "FlextDbtOracleWmsUtilities": (
        "flext_dbt_oracle_wms.utilities",
        "FlextDbtOracleWmsUtilities",
    ),
    "__all__": ("flext_dbt_oracle_wms.__version__", "__all__"),
    "__author__": ("flext_dbt_oracle_wms.__version__", "__author__"),
    "__author_email__": ("flext_dbt_oracle_wms.__version__", "__author_email__"),
    "__description__": ("flext_dbt_oracle_wms.__version__", "__description__"),
    "__license__": ("flext_dbt_oracle_wms.__version__", "__license__"),
    "__title__": ("flext_dbt_oracle_wms.__version__", "__title__"),
    "__url__": ("flext_dbt_oracle_wms.__version__", "__url__"),
    "__version__": ("flext_dbt_oracle_wms.__version__", "__version__"),
    "__version_info__": ("flext_dbt_oracle_wms.__version__", "__version_info__"),
    "c": ("flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsConstants"),
    "d": ("flext_meltano", "d"),
    "discover": ("flext_dbt_oracle_wms.cli", "discover"),
    "e": ("flext_meltano", "e"),
    "extract": ("flext_dbt_oracle_wms.cli", "extract"),
    "h": ("flext_meltano", "h"),
    "info": ("flext_dbt_oracle_wms.cli", "info"),
    "logger": ("flext_dbt_oracle_wms.cli", "logger"),
    "m": ("flext_dbt_oracle_wms.models", "FlextDbtOracleWmsModels"),
    "main": ("flext_dbt_oracle_wms.cli", "main"),
    "p": ("flext_dbt_oracle_wms.protocols", "FlextDbtOracleWmsProtocols"),
    "pipeline": ("flext_dbt_oracle_wms.cli", "pipeline"),
    "r": ("flext_meltano", "r"),
    "s": ("flext_meltano", "s"),
    "t": ("flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTypes"),
    "u": ("flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsUtilities"),
    "x": ("flext_meltano", "x"),
}

__all__ = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServices",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "__all__",
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
    "discover",
    "e",
    "extract",
    "h",
    "info",
    "logger",
    "m",
    "main",
    "p",
    "pipeline",
    "r",
    "s",
    "t",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
