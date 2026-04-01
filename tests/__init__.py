# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
    ("tests.unit",),
    {
        "FlextDbtOracleWmsTestConstants": "tests.constants",
        "FlextDbtOracleWmsTestModels": "tests.models",
        "FlextDbtOracleWmsTestProtocols": "tests.protocols",
        "FlextDbtOracleWmsTestTypes": "tests.typings",
        "FlextDbtOracleWmsTestUtilities": "tests.utilities",
        "c": ("tests.constants", "FlextDbtOracleWmsTestConstants"),
        "constants": "tests.constants",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ("tests.models", "FlextDbtOracleWmsTestModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "FlextDbtOracleWmsTestProtocols"),
        "protocols": "tests.protocols",
        "r": "flext_tests",
        "s": "flext_tests",
        "t": ("tests.typings", "FlextDbtOracleWmsTestTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtOracleWmsTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": "flext_tests",
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
