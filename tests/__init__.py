# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

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
    from tests.test_module_governance import (
        test_public_cli_module_exposes_canonical_entrypoints,
    )

    typings = _tests_typings
    import tests.unit as _tests_unit
    from tests.typings import (
        FlextDbtOracleWmsTestTypes,
        FlextDbtOracleWmsTestTypes as t,
    )

    unit = _tests_unit
    import tests.utilities as _tests_utilities
    from tests.unit import (
        test_basic,
        test_basic_import,
        test_cli,
        test_cli_executes_discover_command,
        test_cli_executes_extract_command_through_public_client,
        test_cli_main_defaults_to_info,
        test_cli_returns_failure_for_pipeline_errors,
        test_cli_returns_failure_for_unknown_command,
        test_cli_uses_default_extract_entity,
        test_module_main_uses_public_cli_entrypoint,
        test_package_import,
        test_package_structure,
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_simple_api,
        test_validate_wms_connection_uses_client_result,
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
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
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
        "test_public_cli_module_exposes_canonical_entrypoints": (
            "tests.test_module_governance",
            "test_public_cli_module_exposes_canonical_entrypoints",
        ),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtOracleWmsTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

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
    "test_basic",
    "test_basic_import",
    "test_cli",
    "test_cli_executes_discover_command",
    "test_cli_executes_extract_command_through_public_client",
    "test_cli_main_defaults_to_info",
    "test_cli_returns_failure_for_pipeline_errors",
    "test_cli_returns_failure_for_unknown_command",
    "test_cli_uses_default_extract_entity",
    "test_module_governance",
    "test_module_main_uses_public_cli_entrypoint",
    "test_package_import",
    "test_package_structure",
    "test_public_cli_module_exposes_canonical_entrypoints",
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
