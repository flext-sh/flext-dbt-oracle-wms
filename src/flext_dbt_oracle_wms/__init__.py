"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_dbt_oracle_wms.__version__ import __version__, __version_info__
    from flext_dbt_oracle_wms.client import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants,
        FlextDbtOracleWmsConstants as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels,
        FlextDbtOracleWmsModels as m,
    )
    from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols
    from flext_dbt_oracle_wms.services import FlextDbtOracleWmsServices
    from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsUtilities

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextDbtOracleWms": ("flext_dbt_oracle_wms.simple_api", "FlextDbtOracleWms"),
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
    "FlextDbtOracleWmsSettings": (
        "flext_dbt_oracle_wms.settings",
        "FlextDbtOracleWmsSettings",
    ),
    "u": ("flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsUtilities"),
    "__version__": ("flext_dbt_oracle_wms.__version__", "__version__"),
    "__version_info__": ("flext_dbt_oracle_wms.__version__", "__version_info__"),
    "c": ("flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsConstants"),
    "m": ("flext_dbt_oracle_wms.models", "FlextDbtOracleWmsModels"),
}

__all__ = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServices",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsUtilities",
    "__version__",
    "__version_info__",
    "c",
    "m",
    "u",
]


def __getattr__(name: str) -> Any:  # noqa: ANN401
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
