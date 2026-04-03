# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_core.mixins import FlextMixins as x
from flext_core.result import FlextResult as r
from flext_core.service import FlextService as s
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

if _t.TYPE_CHECKING:
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.models as _tests_models

    models = _tests_models
    import tests.protocols as _tests_protocols

    protocols = _tests_protocols
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.unit as _tests_unit

    unit = _tests_unit
    import tests.unit.test_basic as _tests_unit_test_basic

    test_basic = _tests_unit_test_basic
    import tests.unit.test_simple_api as _tests_unit_test_simple_api

    test_simple_api = _tests_unit_test_simple_api
    import tests.utilities as _tests_utilities

    utilities = _tests_utilities

    _ = (
        FlextDbtOracleWmsTestConstants,
        FlextDbtOracleWmsTestModels,
        FlextDbtOracleWmsTestProtocols,
        FlextDbtOracleWmsTestTypes,
        FlextDbtOracleWmsTestUtilities,
        c,
        constants,
        d,
        e,
        h,
        m,
        models,
        p,
        protocols,
        r,
        s,
        t,
        test_basic,
        test_basic_import,
        test_package_import,
        test_package_structure,
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_simple_api,
        test_validate_wms_connection_uses_client_result,
        typings,
        u,
        unit,
        utilities,
        x,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "FlextDbtOracleWmsTestConstants": "tests.constants",
        "FlextDbtOracleWmsTestModels": "tests.models",
        "FlextDbtOracleWmsTestProtocols": "tests.protocols",
        "FlextDbtOracleWmsTestTypes": "tests.typings",
        "FlextDbtOracleWmsTestUtilities": "tests.utilities",
        "c": ("tests.constants", "FlextDbtOracleWmsTestConstants"),
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "FlextDbtOracleWmsTestModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "FlextDbtOracleWmsTestProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "FlextDbtOracleWmsTestTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtOracleWmsTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
