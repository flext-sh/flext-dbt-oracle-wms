# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_tests import d, e, h, r, td, tf, tk, tm, tv, x

    from tests.base import TestsFlextDbtOracleWmsServiceBase, s
    from tests.constants import TestsFlextDbtOracleWmsConstants, c
    from tests.models import TestsFlextDbtOracleWmsModels, m
    from tests.protocols import TestsFlextDbtOracleWmsProtocols, p
    from tests.settings import TestsFlextDbtOracleWmsSettings
    from tests.typings import TestsFlextDbtOracleWmsTypes, t
    from tests.unit.test_cli import TestsFlextDbtOracleWmsCli
    from tests.unit.test_module_governance import TestsFlextDbtOracleWmsModuleGovernance
    from tests.unit.test_simple_api import TestsFlextDbtOracleWmsSimpleApi
    from tests.utilities import TestsFlextDbtOracleWmsUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextDbtOracleWmsServiceBase",
                "s",
            ),
            ".conftest": ("conftest",),
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
            ".unit": ("unit",),
            ".unit.test_cli": ("TestsFlextDbtOracleWmsCli",),
            ".unit.test_module_governance": ("TestsFlextDbtOracleWmsModuleGovernance",),
            ".unit.test_simple_api": ("TestsFlextDbtOracleWmsSimpleApi",),
            ".utilities": (
                "TestsFlextDbtOracleWmsUtilities",
                "u",
            ),
            "flext_tests": (
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
