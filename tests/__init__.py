# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests for flext-dbt-oracle-wms.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
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

# Lazy import mapping: export_name -> (module_path, attr_name)
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
]


def __getattr__(name: str):
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
