# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td as td, tf as tf, tk as tk, tv as tv

    from flext_dbt_oracle_wms import d as d, e as e, h as h, r as r, x as x
    from tests.base import (
        TestsFlextDbtOracleWmsServiceBase as TestsFlextDbtOracleWmsServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextDbtOracleWmsConstants as TestsFlextDbtOracleWmsConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextDbtOracleWmsModels as TestsFlextDbtOracleWmsModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextDbtOracleWmsProtocols as TestsFlextDbtOracleWmsProtocols,
        p as p,
    )
    from tests.settings import (
        TestsFlextDbtOracleWmsSettings as TestsFlextDbtOracleWmsSettings,
    )
    from tests.typings import (
        TestsFlextDbtOracleWmsTypes as TestsFlextDbtOracleWmsTypes,
        t as t,
    )
    from tests.unit.test_cli import (
        TestsFlextDbtOracleWmsCli as TestsFlextDbtOracleWmsCli,
    )
    from tests.unit.test_module_governance import (
        TestsFlextDbtOracleWmsModuleGovernance as TestsFlextDbtOracleWmsModuleGovernance,
    )
    from tests.unit.test_simple_api import (
        TestsFlextDbtOracleWmsSimpleApi as TestsFlextDbtOracleWmsSimpleApi,
    )
    from tests.utilities import (
        TestsFlextDbtOracleWmsUtilities as TestsFlextDbtOracleWmsUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextDbtOracleWmsServiceBase",
                "s",
            ),
            ".constants": (
                "TestsFlextDbtOracleWmsConstants",
                "c",
            ),
            ".models": (
                "TestsFlextDbtOracleWmsModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextDbtOracleWmsProtocols",
                "p",
            ),
            ".settings": ("TestsFlextDbtOracleWmsSettings",),
            ".typings": (
                "TestsFlextDbtOracleWmsTypes",
                "t",
            ),
            ".unit.test_cli": ("TestsFlextDbtOracleWmsCli",),
            ".unit.test_module_governance": ("TestsFlextDbtOracleWmsModuleGovernance",),
            ".unit.test_simple_api": ("TestsFlextDbtOracleWmsSimpleApi",),
            ".utilities": (
                "TestsFlextDbtOracleWmsUtilities",
                "u",
            ),
            "flext_dbt_oracle_wms": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tv",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextDbtOracleWmsCli",
    "TestsFlextDbtOracleWmsConstants",
    "TestsFlextDbtOracleWmsModels",
    "TestsFlextDbtOracleWmsModuleGovernance",
    "TestsFlextDbtOracleWmsProtocols",
    "TestsFlextDbtOracleWmsServiceBase",
    "TestsFlextDbtOracleWmsSettings",
    "TestsFlextDbtOracleWmsSimpleApi",
    "TestsFlextDbtOracleWmsTypes",
    "TestsFlextDbtOracleWmsUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tv",
    "u",
    "x",
]
