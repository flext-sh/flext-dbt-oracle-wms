# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from flext_dbt_oracle_wms.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_dbt_oracle_wms.cli import (
        FlextDbtOracleWmsCliService,
        FlextDbtOracleWmsCliService as s,
        discover,
        extract,
        info,
        logger,
        main,
        pipeline,
    )
    from flext_dbt_oracle_wms.client import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms.config_types import (
        DBTOracleWMSConfiguration,
        DBTOracleWMSMacroConfiguration,
        DBTOracleWMSModelConfiguration,
        DBTOracleWMSProfileConfiguration,
        DBTOracleWMSSourceConfiguration,
        DBTOracleWMSTestConfiguration,
        FlextDBTOracleWMSSettings,
    )
    from flext_dbt_oracle_wms.dbt_models import (
        FlextDbtOracleWmsInventoryFact,
        FlextDbtOracleWmsItemDimension,
        FlextDbtOracleWmsLocationDimension,
        FlextDbtOracleWmsShipmentFact,
        FlextDbtOracleWmsTransformer,
    )
    from flext_dbt_oracle_wms.domain_types import (
        DBTOracleWMSAnalysis,
        DBTOracleWMSCompilation,
        DBTOracleWMSDocumentation,
        DBTOracleWMSExecution,
        DBTOracleWMSMacro,
        DBTOracleWMSModel,
        DBTOracleWMSProject,
        DBTOracleWMSSnapshot,
        DBTOracleWMSSource,
        DBTOracleWMSTest,
    )
    from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels, m
    from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols, p
    from flext_dbt_oracle_wms.services import FlextDbtOracleWmsServices
    from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        DBTOracleWMSAnalysisConfiguration,
        DBTOracleWMSCompilationConfiguration,
        DBTOracleWMSDocumentationConfiguration,
        DBTOracleWMSExecutionConfiguration,
        DBTOracleWMSMaterialization,
        DBTOracleWMSProjectConfiguration,
        DBTOracleWMSRunStatus,
        DBTOracleWMSSnapshotConfiguration,
        DBTOracleWMSTestType,
        FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsTypes as t,
    )
    from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsUtilities, u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "DBTOracleWMSAnalysis": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSAnalysis",
    ),
    "DBTOracleWMSAnalysisConfiguration": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSAnalysisConfiguration",
    ),
    "DBTOracleWMSCompilation": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSCompilation",
    ),
    "DBTOracleWMSCompilationConfiguration": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSCompilationConfiguration",
    ),
    "DBTOracleWMSConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSConfiguration",
    ),
    "DBTOracleWMSDocumentation": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSDocumentation",
    ),
    "DBTOracleWMSDocumentationConfiguration": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSDocumentationConfiguration",
    ),
    "DBTOracleWMSExecution": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSExecution",
    ),
    "DBTOracleWMSExecutionConfiguration": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSExecutionConfiguration",
    ),
    "DBTOracleWMSMacro": ("flext_dbt_oracle_wms.domain_types", "DBTOracleWMSMacro"),
    "DBTOracleWMSMacroConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSMacroConfiguration",
    ),
    "DBTOracleWMSMaterialization": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSMaterialization",
    ),
    "DBTOracleWMSModel": ("flext_dbt_oracle_wms.domain_types", "DBTOracleWMSModel"),
    "DBTOracleWMSModelConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSModelConfiguration",
    ),
    "DBTOracleWMSProfileConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSProfileConfiguration",
    ),
    "DBTOracleWMSProject": ("flext_dbt_oracle_wms.domain_types", "DBTOracleWMSProject"),
    "DBTOracleWMSProjectConfiguration": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSProjectConfiguration",
    ),
    "DBTOracleWMSRunStatus": ("flext_dbt_oracle_wms.typings", "DBTOracleWMSRunStatus"),
    "DBTOracleWMSSnapshot": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSSnapshot",
    ),
    "DBTOracleWMSSnapshotConfiguration": (
        "flext_dbt_oracle_wms.typings",
        "DBTOracleWMSSnapshotConfiguration",
    ),
    "DBTOracleWMSSource": ("flext_dbt_oracle_wms.domain_types", "DBTOracleWMSSource"),
    "DBTOracleWMSSourceConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSSourceConfiguration",
    ),
    "DBTOracleWMSTest": ("flext_dbt_oracle_wms.domain_types", "DBTOracleWMSTest"),
    "DBTOracleWMSTestConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSTestConfiguration",
    ),
    "DBTOracleWMSTestType": ("flext_dbt_oracle_wms.typings", "DBTOracleWMSTestType"),
    "FlextDBTOracleWMSSettings": (
        "flext_dbt_oracle_wms.config_types",
        "FlextDBTOracleWMSSettings",
    ),
    "FlextDbtOracleWms": ("flext_dbt_oracle_wms.simple_api", "FlextDbtOracleWms"),
    "FlextDbtOracleWmsCliService": (
        "flext_dbt_oracle_wms.cli",
        "FlextDbtOracleWmsCliService",
    ),
    "FlextDbtOracleWmsClient": (
        "flext_dbt_oracle_wms.client",
        "FlextDbtOracleWmsClient",
    ),
    "FlextDbtOracleWmsInventoryFact": (
        "flext_dbt_oracle_wms.dbt_models",
        "FlextDbtOracleWmsInventoryFact",
    ),
    "FlextDbtOracleWmsItemDimension": (
        "flext_dbt_oracle_wms.dbt_models",
        "FlextDbtOracleWmsItemDimension",
    ),
    "FlextDbtOracleWmsLocationDimension": (
        "flext_dbt_oracle_wms.dbt_models",
        "FlextDbtOracleWmsLocationDimension",
    ),
    "FlextDbtOracleWmsModels": (
        "flext_dbt_oracle_wms.models",
        "FlextDbtOracleWmsModels",
    ),
    "FlextDbtOracleWmsProtocols": (
        "flext_dbt_oracle_wms.protocols",
        "FlextDbtOracleWmsProtocols",
    ),
    "FlextDbtOracleWmsServices": (
        "flext_dbt_oracle_wms.services",
        "FlextDbtOracleWmsServices",
    ),
    "FlextDbtOracleWmsSettings": (
        "flext_dbt_oracle_wms.settings",
        "FlextDbtOracleWmsSettings",
    ),
    "FlextDbtOracleWmsShipmentFact": (
        "flext_dbt_oracle_wms.dbt_models",
        "FlextDbtOracleWmsShipmentFact",
    ),
    "FlextDbtOracleWmsTransformer": (
        "flext_dbt_oracle_wms.dbt_models",
        "FlextDbtOracleWmsTransformer",
    ),
    "FlextDbtOracleWmsTypes": (
        "flext_dbt_oracle_wms.typings",
        "FlextDbtOracleWmsTypes",
    ),
    "FlextDbtOracleWmsUtilities": (
        "flext_dbt_oracle_wms.utilities",
        "FlextDbtOracleWmsUtilities",
    ),
    "__all__": ("flext_dbt_oracle_wms.__version__", "__all__"),
    "__author__": ("flext_dbt_oracle_wms.__version__", "__author__"),
    "__author_email__": ("flext_dbt_oracle_wms.__version__", "__author_email__"),
    "__description__": ("flext_dbt_oracle_wms.__version__", "__description__"),
    "__license__": ("flext_dbt_oracle_wms.__version__", "__license__"),
    "__title__": ("flext_dbt_oracle_wms.__version__", "__title__"),
    "__url__": ("flext_dbt_oracle_wms.__version__", "__url__"),
    "__version__": ("flext_dbt_oracle_wms.__version__", "__version__"),
    "__version_info__": ("flext_dbt_oracle_wms.__version__", "__version_info__"),
    "discover": ("flext_dbt_oracle_wms.cli", "discover"),
    "extract": ("flext_dbt_oracle_wms.cli", "extract"),
    "info": ("flext_dbt_oracle_wms.cli", "info"),
    "logger": ("flext_dbt_oracle_wms.cli", "logger"),
    "m": ("flext_dbt_oracle_wms.models", "m"),
    "main": ("flext_dbt_oracle_wms.cli", "main"),
    "p": ("flext_dbt_oracle_wms.protocols", "p"),
    "pipeline": ("flext_dbt_oracle_wms.cli", "pipeline"),
    "s": ("flext_dbt_oracle_wms.cli", "FlextDbtOracleWmsCliService"),
    "t": ("flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTypes"),
    "u": ("flext_dbt_oracle_wms.utilities", "u"),
}

__all__ = [
    "DBTOracleWMSAnalysis",
    "DBTOracleWMSAnalysisConfiguration",
    "DBTOracleWMSCompilation",
    "DBTOracleWMSCompilationConfiguration",
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSDocumentation",
    "DBTOracleWMSDocumentationConfiguration",
    "DBTOracleWMSExecution",
    "DBTOracleWMSExecutionConfiguration",
    "DBTOracleWMSMacro",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSMaterialization",
    "DBTOracleWMSModel",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSProject",
    "DBTOracleWMSProjectConfiguration",
    "DBTOracleWMSRunStatus",
    "DBTOracleWMSSnapshot",
    "DBTOracleWMSSnapshotConfiguration",
    "DBTOracleWMSSource",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTest",
    "DBTOracleWMSTestConfiguration",
    "DBTOracleWMSTestType",
    "FlextDBTOracleWMSSettings",
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsServices",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "discover",
    "extract",
    "info",
    "logger",
    "m",
    "main",
    "p",
    "pipeline",
    "s",
    "t",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
