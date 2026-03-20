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
    from flext_meltano import d, e, h, r, x

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
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants,
        FlextDbtOracleWmsConstants as c,
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
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels,
        FlextDbtOracleWmsModels as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsProtocols,
        FlextDbtOracleWmsProtocols as p,
    )
    from flext_dbt_oracle_wms.services import FlextDbtOracleWmsServices
    from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsTypes as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities,
        FlextDbtOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "DBTOracleWMSAnalysis": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSAnalysis",
    ),
    "DBTOracleWMSCompilation": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSCompilation",
    ),
    "DBTOracleWMSConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSConfiguration",
    ),
    "DBTOracleWMSDocumentation": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSDocumentation",
    ),
    "DBTOracleWMSExecution": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSExecution",
    ),
    "DBTOracleWMSMacro": ("flext_dbt_oracle_wms.domain_types", "DBTOracleWMSMacro"),
    "DBTOracleWMSMacroConfiguration": (
        "flext_dbt_oracle_wms.config_types",
        "DBTOracleWMSMacroConfiguration",
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
    "DBTOracleWMSSnapshot": (
        "flext_dbt_oracle_wms.domain_types",
        "DBTOracleWMSSnapshot",
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
    "FlextDbtOracleWmsConstants": (
        "flext_dbt_oracle_wms.constants",
        "FlextDbtOracleWmsConstants",
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
    "c": ("flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsConstants"),
    "d": ("flext_meltano", "d"),
    "discover": ("flext_dbt_oracle_wms.cli", "discover"),
    "e": ("flext_meltano", "e"),
    "extract": ("flext_dbt_oracle_wms.cli", "extract"),
    "h": ("flext_meltano", "h"),
    "info": ("flext_dbt_oracle_wms.cli", "info"),
    "logger": ("flext_dbt_oracle_wms.cli", "logger"),
    "m": ("flext_dbt_oracle_wms.models", "FlextDbtOracleWmsModels"),
    "main": ("flext_dbt_oracle_wms.cli", "main"),
    "p": ("flext_dbt_oracle_wms.protocols", "FlextDbtOracleWmsProtocols"),
    "pipeline": ("flext_dbt_oracle_wms.cli", "pipeline"),
    "r": ("flext_meltano", "r"),
    "s": ("flext_dbt_oracle_wms.cli", "FlextDbtOracleWmsCliService"),
    "t": ("flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTypes"),
    "u": ("flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsUtilities"),
    "x": ("flext_meltano", "x"),
}

__all__ = [
    "DBTOracleWMSAnalysis",
    "DBTOracleWMSCompilation",
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSDocumentation",
    "DBTOracleWMSExecution",
    "DBTOracleWMSMacro",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSModel",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSProject",
    "DBTOracleWMSSnapshot",
    "DBTOracleWMSSource",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTest",
    "DBTOracleWMSTestConfiguration",
    "FlextDBTOracleWMSSettings",
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsConstants",
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
    "c",
    "d",
    "discover",
    "e",
    "extract",
    "h",
    "info",
    "logger",
    "m",
    "main",
    "p",
    "pipeline",
    "r",
    "s",
    "t",
    "u",
    "x",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
