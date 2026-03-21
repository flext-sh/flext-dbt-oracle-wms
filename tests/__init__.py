# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from . import unit as unit
    from .constants import (
        TestsFlextDbtOracleWmsConstants,
        TestsFlextDbtOracleWmsConstants as c,
    )
    from .models import (
        TestsFlextDbtOracleWmsModels,
        TestsFlextDbtOracleWmsModels as m,
        tm,
    )
    from .protocols import (
        TestsFlextDbtOracleWmsProtocols,
        TestsFlextDbtOracleWmsProtocols as p,
    )
    from .typings import TestsFlextDbtOracleWmsTypes, TestsFlextDbtOracleWmsTypes as t
    from .unit.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )
    from .utilities import (
        TestsFlextDbtOracleWmsUtilities,
        TestsFlextDbtOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestsFlextDbtOracleWmsConstants": ("tests.constants", "TestsFlextDbtOracleWmsConstants"),
    "TestsFlextDbtOracleWmsModels": ("tests.models", "TestsFlextDbtOracleWmsModels"),
    "TestsFlextDbtOracleWmsProtocols": ("tests.protocols", "TestsFlextDbtOracleWmsProtocols"),
    "TestsFlextDbtOracleWmsTypes": ("tests.typings", "TestsFlextDbtOracleWmsTypes"),
    "TestsFlextDbtOracleWmsUtilities": ("tests.utilities", "TestsFlextDbtOracleWmsUtilities"),
    "c": ("tests.constants", "TestsFlextDbtOracleWmsConstants"),
    "m": ("tests.models", "TestsFlextDbtOracleWmsModels"),
    "p": ("tests.protocols", "TestsFlextDbtOracleWmsProtocols"),
    "t": ("tests.typings", "TestsFlextDbtOracleWmsTypes"),
    "test_basic_import": ("tests.unit.test_basic", "test_basic_import"),
    "test_package_import": ("tests.unit.test_basic", "test_package_import"),
    "test_package_structure": ("tests.unit.test_basic", "test_package_structure"),
    "tm": ("tests.models", "tm"),
    "u": ("tests.utilities", "TestsFlextDbtOracleWmsUtilities"),
    "unit": ("tests.unit", ""),
}

__all__ = [
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
    "c",
    "m",
    "p",
    "t",
    "test_basic_import",
    "test_package_import",
    "test_package_structure",
    "tm",
    "u",
    "unit",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
