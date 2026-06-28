# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_dbt_oracle_wms.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _t.TYPE_CHECKING:
    from flext_dbt_oracle_wms._utilities.client import (
        FlextDbtOracleWmsClient as FlextDbtOracleWmsClient,
    )
    from flext_dbt_oracle_wms.cli import (
        FlextDbtOracleWmsCliService as FlextDbtOracleWmsCliService,
        main as main,
    )
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants as FlextDbtOracleWmsConstants,
        c as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels as FlextDbtOracleWmsModels,
        m as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsProtocols as FlextDbtOracleWmsProtocols,
        p as p,
    )
    from flext_dbt_oracle_wms.settings import (
        FlextDbtOracleWmsSettings as FlextDbtOracleWmsSettings,
    )
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms as FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes as FlextDbtOracleWmsTypes,
        t as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities as FlextDbtOracleWmsUtilities,
        u as u,
    )
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
_LAZY_IMPORTS = merge_lazy_imports(
    ("._utilities",),
    build_lazy_import_map(
        {
            "._utilities.client": ("FlextDbtOracleWmsClient",),
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)

__all__: list[str] = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
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
