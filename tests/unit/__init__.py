# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from tests.unit import test_basic, test_simple_api
    from tests.unit.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )
    from tests.unit.test_simple_api import (
        test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result,
        test_validate_wms_connection_uses_client_result,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "test_basic": "tests.unit.test_basic",
    "test_basic_import": "tests.unit.test_basic",
    "test_package_import": "tests.unit.test_basic",
    "test_package_structure": "tests.unit.test_basic",
    "test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result": "tests.unit.test_simple_api",
    "test_simple_api": "tests.unit.test_simple_api",
    "test_validate_wms_connection_uses_client_result": "tests.unit.test_simple_api",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
