# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import *

    from tests import constants, models, protocols, typings, unit, utilities
    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import test_basic, test_simple_api
    from tests.unit.test_basic import *
    from tests.unit.test_simple_api import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtOracleWmsTestConstants": "tests.constants",
    "FlextDbtOracleWmsTestModels": "tests.models",
    "FlextDbtOracleWmsTestProtocols": "tests.protocols",
    "FlextDbtOracleWmsTestTypes": "tests.typings",
    "FlextDbtOracleWmsTestUtilities": "tests.utilities",
    "c": ["tests.constants", "FlextDbtOracleWmsTestConstants"],
    "constants": "tests.constants",
    "d": "flext_tests",
    "e": "flext_tests",
    "h": "flext_tests",
    "m": ["tests.models", "FlextDbtOracleWmsTestModels"],
    "models": "tests.models",
    "p": ["tests.protocols", "FlextDbtOracleWmsTestProtocols"],
    "protocols": "tests.protocols",
    "r": "flext_tests",
    "s": "flext_tests",
    "t": ["tests.typings", "FlextDbtOracleWmsTestTypes"],
    "test_basic": "tests.unit.test_basic",
    "test_basic_import": "tests.unit.test_basic",
    "test_package_import": "tests.unit.test_basic",
    "test_package_structure": "tests.unit.test_basic",
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result": "tests.unit.test_simple_api",
    "test_simple_api": "tests.unit.test_simple_api",
    "test_validate_wms_connection_uses_client_result": "tests.unit.test_simple_api",
    "typings": "tests.typings",
    "u": ["tests.utilities", "FlextDbtOracleWmsTestUtilities"],
    "unit": "tests.unit",
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
