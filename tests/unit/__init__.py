# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

import typing as _t

from flext_core.constants import FlextConstants as c
from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports
from flext_core.mixins import FlextMixins as x
from flext_core.models import FlextModels as m
from flext_core.protocols import FlextProtocols as p
from flext_core.result import FlextResult as r
from flext_core.service import FlextService as s
from flext_core.typings import FlextTypes as t
from flext_core.utilities import FlextUtilities as u
from tests.unit.test_basic import (
    test_basic_import,
    test_package_import,
    test_package_structure,
)
from tests.unit.test_simple_api import (
    test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
    test_validate_wms_connection_uses_client_result,
)

if _t.TYPE_CHECKING:
    import tests.unit.test_basic as _tests_unit_test_basic

    test_basic = _tests_unit_test_basic
    import tests.unit.test_simple_api as _tests_unit_test_simple_api

    test_simple_api = _tests_unit_test_simple_api

    _ = (
        c,
        d,
        e,
        h,
        m,
        p,
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
        u,
        x,
    )
_LAZY_IMPORTS = {
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("flext_core.typings", "FlextTypes"),
    "test_basic": "tests.unit.test_basic",
    "test_basic_import": "tests.unit.test_basic",
    "test_package_import": "tests.unit.test_basic",
    "test_package_structure": "tests.unit.test_basic",
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result": "tests.unit.test_simple_api",
    "test_simple_api": "tests.unit.test_simple_api",
    "test_validate_wms_connection_uses_client_result": "tests.unit.test_simple_api",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
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
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
