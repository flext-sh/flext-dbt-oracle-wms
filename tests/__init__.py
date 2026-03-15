# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from tests import unit
    from tests.constants import (
        TestsFlextDbtOracleWmsConstants,
        TestsFlextDbtOracleWmsConstants as c,
    )
    from tests.models import TestsFlextDbtOracleWmsModels, m, tm
    from tests.protocols import TestsFlextDbtOracleWmsProtocols, p
    from tests.typings import (
        TestsFlextDbtOracleWmsTypes,
        TestsFlextDbtOracleWmsTypes as t,
    )
    from tests.unit.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )
    from tests.utilities import (
        TestsFlextDbtOracleWmsUtilities,
        TestsFlextDbtOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestsFlextDbtOracleWmsConstants": (
        "tests.constants",
        "TestsFlextDbtOracleWmsConstants",
    ),
    "TestsFlextDbtOracleWmsModels": ("tests.models", "TestsFlextDbtOracleWmsModels"),
    "TestsFlextDbtOracleWmsProtocols": (
        "tests.protocols",
        "TestsFlextDbtOracleWmsProtocols",
    ),
    "TestsFlextDbtOracleWmsTypes": ("tests.typings", "TestsFlextDbtOracleWmsTypes"),
    "TestsFlextDbtOracleWmsUtilities": (
        "tests.utilities",
        "TestsFlextDbtOracleWmsUtilities",
    ),
    "c": ("tests.constants", "TestsFlextDbtOracleWmsConstants"),
    "m": ("tests.models", "m"),
    "p": ("tests.protocols", "p"),
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


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
