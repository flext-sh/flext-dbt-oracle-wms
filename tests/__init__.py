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
    from tests.unit import (
        test_basic,
        test_basic_import,
        test_package_import,
        test_package_structure,
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_simple_api,
        test_validate_wms_connection_uses_client_result,
    )
    from tests.utilities import (
        FlextDbtOracleWmsTestUtilities,
        FlextDbtOracleWmsTestUtilities as u,
    )

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
