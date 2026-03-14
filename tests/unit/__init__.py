# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from tests.unit.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "test_basic_import": ("tests.unit.test_basic", "test_basic_import"),
    "test_package_import": ("tests.unit.test_basic", "test_package_import"),
    "test_package_structure": ("tests.unit.test_basic", "test_package_structure"),
}

__all__ = [
    "test_basic_import",
    "test_package_import",
    "test_package_structure",
]


def __getattr__(name: str):
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
