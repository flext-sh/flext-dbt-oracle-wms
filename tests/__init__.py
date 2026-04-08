# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
    from tests.conftest import pytest_plugins

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextDbtOracleWmsTestConstants,
        FlextDbtOracleWmsTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import (
        FlextDbtOracleWmsTestModels,
        FlextDbtOracleWmsTestModels as m,
    )

    protocols = _tests_protocols
    import tests.test_module_governance as _tests_test_module_governance
    from tests.protocols import (
        FlextDbtOracleWmsTestProtocols,
        FlextDbtOracleWmsTestProtocols as p,
    )

    test_module_governance = _tests_test_module_governance
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import (
        FlextDbtOracleWmsTestTypes,
        FlextDbtOracleWmsTestTypes as t,
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextDbtOracleWmsTestUtilities,
        FlextDbtOracleWmsTestUtilities as u,
    )
_LAZY_IMPORTS = {
    "FlextDbtOracleWmsTestConstants": (
        "tests.constants",
        "FlextDbtOracleWmsTestConstants",
    ),
    "FlextDbtOracleWmsTestModels": ("tests.models", "FlextDbtOracleWmsTestModels"),
    "FlextDbtOracleWmsTestProtocols": (
        "tests.protocols",
        "FlextDbtOracleWmsTestProtocols",
    ),
    "FlextDbtOracleWmsTestTypes": ("tests.typings", "FlextDbtOracleWmsTestTypes"),
    "FlextDbtOracleWmsTestUtilities": (
        "tests.utilities",
        "FlextDbtOracleWmsTestUtilities",
    ),
    "c": ("tests.constants", "FlextDbtOracleWmsTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "FlextDbtOracleWmsTestModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextDbtOracleWmsTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "FlextDbtOracleWmsTestTypes"),
    "test_module_governance": "tests.test_module_governance",
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextDbtOracleWmsTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "FlextDbtOracleWmsTestConstants",
    "FlextDbtOracleWmsTestModels",
    "FlextDbtOracleWmsTestProtocols",
    "FlextDbtOracleWmsTestTypes",
    "FlextDbtOracleWmsTestUtilities",
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
    "pytest_plugins",
    "r",
    "s",
    "t",
    "test_module_governance",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
