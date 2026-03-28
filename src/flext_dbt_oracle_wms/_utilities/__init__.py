# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT Oracle WMS utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

    from flext_dbt_oracle_wms._utilities.cli import (
        FlextDbtOracleWmsCliService,
        discover,
        extract,
        info,
        logger,
        main,
        pipeline,
    )
    from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms._utilities.simple_api import FlextDbtOracleWms

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracleWms": [
        "flext_dbt_oracle_wms._utilities.simple_api",
        "FlextDbtOracleWms",
    ],
    "FlextDbtOracleWmsCliService": [
        "flext_dbt_oracle_wms._utilities.cli",
        "FlextDbtOracleWmsCliService",
    ],
    "FlextDbtOracleWmsClient": [
        "flext_dbt_oracle_wms._utilities.client",
        "FlextDbtOracleWmsClient",
    ],
    "discover": ["flext_dbt_oracle_wms._utilities.cli", "discover"],
    "extract": ["flext_dbt_oracle_wms._utilities.cli", "extract"],
    "info": ["flext_dbt_oracle_wms._utilities.cli", "info"],
    "logger": ["flext_dbt_oracle_wms._utilities.cli", "logger"],
    "main": ["flext_dbt_oracle_wms._utilities.cli", "main"],
    "pipeline": ["flext_dbt_oracle_wms._utilities.cli", "pipeline"],
}

__all__ = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
    "discover",
    "extract",
    "info",
    "logger",
    "main",
    "pipeline",
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
