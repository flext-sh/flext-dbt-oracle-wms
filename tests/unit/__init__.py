# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms.tests.unit.test_cli import (
        TestsFlextDbtOracleWmsCli as TestsFlextDbtOracleWmsCli,
    )
    from flext_dbt_oracle_wms.tests.unit.test_module_governance import (
        TestsFlextDbtOracleWmsModuleGovernance as TestsFlextDbtOracleWmsModuleGovernance,
    )
    from flext_dbt_oracle_wms.tests.unit.test_simple_api import (
        TestsFlextDbtOracleWmsSimpleApi as TestsFlextDbtOracleWmsSimpleApi,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_cli": ("TestsFlextDbtOracleWmsCli",),
        ".test_module_governance": ("TestsFlextDbtOracleWmsModuleGovernance",),
        ".test_simple_api": ("TestsFlextDbtOracleWmsSimpleApi",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
