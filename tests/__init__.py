# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests import (
        conftest,
        constants,
        models,
        protocols,
        test_module_governance,
        typings,
        unit,
        utilities,
    )
    from tests.constants import (
        TestsFlextDbtOracleWmsConstants,
        TestsFlextDbtOracleWmsConstants as c,
    )
    from tests.models import (
        TestsFlextDbtOracleWmsModels,
        TestsFlextDbtOracleWmsModels as m,
    )
    from tests.protocols import (
        TestsFlextDbtOracleWmsProtocols,
        TestsFlextDbtOracleWmsProtocols as p,
    )
    from tests.typings import (
        TestsFlextDbtOracleWmsTypes,
        TestsFlextDbtOracleWmsTypes as t,
    )
    from tests.utilities import (
        TestsFlextDbtOracleWmsUtilities,
        TestsFlextDbtOracleWmsUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "TestsFlextDbtOracleWmsConstants": (
            "tests.constants",
            "TestsFlextDbtOracleWmsConstants",
        ),
        "TestsFlextDbtOracleWmsModels": (
            "tests.models",
            "TestsFlextDbtOracleWmsModels",
        ),
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
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "TestsFlextDbtOracleWmsModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "TestsFlextDbtOracleWmsProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "TestsFlextDbtOracleWmsTypes"),
        "test_module_governance": "tests.test_module_governance",
        "typings": "tests.typings",
        "u": ("tests.utilities", "TestsFlextDbtOracleWmsUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
    "c",
    "conftest",
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
    "test_module_governance",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
