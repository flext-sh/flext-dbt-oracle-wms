# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_dbt_oracle_wms.__version__ import *

if _t.TYPE_CHECKING:
    from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms.base import FlextDbtOracleWmsServiceBase
    from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
    from flext_dbt_oracle_wms.constants import FlextDbtOracleWmsConstants, c
    from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels, m
    from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols, p
    from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import FlextDbtOracleWmsTypes, t
    from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsUtilities, u
    from flext_meltano import d, e, h, r, s, x
_LAZY_IMPORTS = merge_lazy_imports(
    ("._utilities",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            "._utilities.client": ("FlextDbtOracleWmsClient",),
            ".base": ("FlextDbtOracleWmsServiceBase",),
            ".cli": (
                "FlextDbtOracleWmsCliService",
                "main",
            ),
            ".constants": (
                "FlextDbtOracleWmsConstants",
                "c",
            ),
            ".models": (
                "FlextDbtOracleWmsModels",
                "m",
            ),
            ".protocols": (
                "FlextDbtOracleWmsProtocols",
                "p",
            ),
            ".settings": ("FlextDbtOracleWmsSettings",),
            ".simple_api": ("FlextDbtOracleWms",),
            ".typings": (
                "FlextDbtOracleWmsTypes",
                "t",
            ),
            ".utilities": (
                "FlextDbtOracleWmsUtilities",
                "u",
            ),
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServiceBase",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]
