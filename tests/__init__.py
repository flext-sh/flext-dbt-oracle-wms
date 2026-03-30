# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests import constants, models, protocols, typings, unit, utilities
    from tests.constants import (
        FlextDbtOracleWmsTestConstants,
        FlextDbtOracleWmsTestConstants as c,
    )
    from tests.models import (
        FlextDbtOracleWmsTestModels,
        FlextDbtOracleWmsTestModels as m,
    )
    from tests.protocols import (
        FlextDbtOracleWmsTestProtocols,
        FlextDbtOracleWmsTestProtocols as p,
    )
    from tests.typings import (
        FlextDbtOracleWmsTestTypes,
        FlextDbtOracleWmsTestTypes as t,
    )
    from tests.unit import test_basic, test_simple_api
    from tests.unit.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )
    from tests.unit.test_simple_api import (
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_validate_wms_connection_uses_client_result,
    )
    from tests.utilities import (
        FlextDbtOracleWmsTestUtilities,
        FlextDbtOracleWmsTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracleWmsTestConstants": [
        "tests.constants",
        "FlextDbtOracleWmsTestConstants",
    ],
    "FlextDbtOracleWmsTestModels": ["tests.models", "FlextDbtOracleWmsTestModels"],
    "FlextDbtOracleWmsTestProtocols": [
        "tests.protocols",
        "FlextDbtOracleWmsTestProtocols",
    ],
    "FlextDbtOracleWmsTestTypes": ["tests.typings", "FlextDbtOracleWmsTestTypes"],
    "FlextDbtOracleWmsTestUtilities": [
        "tests.utilities",
        "FlextDbtOracleWmsTestUtilities",
    ],
    "c": ["tests.constants", "FlextDbtOracleWmsTestConstants"],
    "constants": ["tests.constants", ""],
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "h": ["flext_tests", "h"],
    "m": ["tests.models", "FlextDbtOracleWmsTestModels"],
    "models": ["tests.models", ""],
    "p": ["tests.protocols", "FlextDbtOracleWmsTestProtocols"],
    "protocols": ["tests.protocols", ""],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "t": ["tests.typings", "FlextDbtOracleWmsTestTypes"],
    "test_basic": ["tests.unit.test_basic", ""],
    "test_basic_import": ["tests.unit.test_basic", "test_basic_import"],
    "test_package_import": ["tests.unit.test_basic", "test_package_import"],
    "test_package_structure": ["tests.unit.test_basic", "test_package_structure"],
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result": [
        "tests.unit.test_simple_api",
        "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result",
    ],
    "test_simple_api": ["tests.unit.test_simple_api", ""],
    "test_validate_wms_connection_uses_client_result": [
        "tests.unit.test_simple_api",
        "test_validate_wms_connection_uses_client_result",
    ],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextDbtOracleWmsTestUtilities"],
    "unit": ["tests.unit", ""],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

__all__ = [
    "FlextDbtOracleWmsTestConstants",
    "FlextDbtOracleWmsTestModels",
    "FlextDbtOracleWmsTestProtocols",
    "FlextDbtOracleWmsTestTypes",
    "FlextDbtOracleWmsTestUtilities",
    "c",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_basic",
    "test_basic_import",
    "test_package_import",
    "test_package_structure",
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result",
    "test_simple_api",
    "test_validate_wms_connection_uses_client_result",
    "typings",
    "u",
    "unit",
    "utilities",
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
