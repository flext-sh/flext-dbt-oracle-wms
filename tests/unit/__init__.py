# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

    from tests.unit.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )
    from tests.unit.test_simple_api import (
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_validate_wms_connection_uses_client_result,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "test_basic_import": ["tests.unit.test_basic", "test_basic_import"],
    "test_package_import": ["tests.unit.test_basic", "test_package_import"],
    "test_package_structure": ["tests.unit.test_basic", "test_package_structure"],
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result": ["tests.unit.test_simple_api", "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result"],
    "test_validate_wms_connection_uses_client_result": ["tests.unit.test_simple_api", "test_validate_wms_connection_uses_client_result"],
}

__all__ = [
    "test_basic_import",
    "test_package_import",
    "test_package_structure",
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result",
    "test_validate_wms_connection_uses_client_result",
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
