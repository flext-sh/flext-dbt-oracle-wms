# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests import (
        constants as constants,
        models as models,
        protocols as protocols,
        typings as typings,
        unit as unit,
        utilities as utilities,
    )
    from tests.constants import (
        FlextDbtOracleWmsTestConstants as FlextDbtOracleWmsTestConstants,
        FlextDbtOracleWmsTestConstants as c,
    )
    from tests.models import (
        FlextDbtOracleWmsTestModels as FlextDbtOracleWmsTestModels,
        FlextDbtOracleWmsTestModels as m,
    )
    from tests.protocols import (
        FlextDbtOracleWmsTestProtocols as FlextDbtOracleWmsTestProtocols,
        FlextDbtOracleWmsTestProtocols as p,
    )
    from tests.typings import (
        FlextDbtOracleWmsTestTypes as FlextDbtOracleWmsTestTypes,
        FlextDbtOracleWmsTestTypes as t,
    )
    from tests.unit import test_basic as test_basic, test_simple_api as test_simple_api
    from tests.unit.test_basic import (
        test_basic_import as test_basic_import,
        test_package_import as test_package_import,
        test_package_structure as test_package_structure,
    )
    from tests.unit.test_simple_api import (
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result as test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_validate_wms_connection_uses_client_result as test_validate_wms_connection_uses_client_result,
    )
    from tests.utilities import (
        FlextDbtOracleWmsTestUtilities as FlextDbtOracleWmsTestUtilities,
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

_EXPORTS: Sequence[str] = [
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
