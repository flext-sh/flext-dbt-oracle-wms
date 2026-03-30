# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_dbt_oracle_wms.__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import (
        _utilities as _utilities,
        cli as cli,
        client as client,
        constants as constants,
        models as models,
        protocols as protocols,
        simple_api as simple_api,
        typings as typings,
        utilities as utilities,
    )
    from flext_dbt_oracle_wms._utilities.client import (
        FlextDbtOracleWmsClient as FlextDbtOracleWmsClient,
    )
    from flext_dbt_oracle_wms.cli import (
        FlextDbtOracleWmsCliService as FlextDbtOracleWmsCliService,
        discover as discover,
        extract as extract,
        info as info,
        logger as logger,
        main as main,
        pipeline as pipeline,
    )
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants as FlextDbtOracleWmsConstants,
        FlextDbtOracleWmsConstants as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels as FlextDbtOracleWmsModels,
        FlextDbtOracleWmsModels as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsProtocols as FlextDbtOracleWmsProtocols,
        FlextDbtOracleWmsProtocols as p,
    )
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms as FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes as FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsTypes as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities as FlextDbtOracleWmsUtilities,
        FlextDbtOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracleWms": ["flext_dbt_oracle_wms.simple_api", "FlextDbtOracleWms"],
    "FlextDbtOracleWmsCliService": [
        "flext_dbt_oracle_wms.cli",
        "FlextDbtOracleWmsCliService",
    ],
    "FlextDbtOracleWmsClient": [
        "flext_dbt_oracle_wms._utilities.client",
        "FlextDbtOracleWmsClient",
    ],
    "FlextDbtOracleWmsConstants": [
        "flext_dbt_oracle_wms.constants",
        "FlextDbtOracleWmsConstants",
    ],
    "FlextDbtOracleWmsModels": [
        "flext_dbt_oracle_wms.models",
        "FlextDbtOracleWmsModels",
    ],
    "FlextDbtOracleWmsProtocols": [
        "flext_dbt_oracle_wms.protocols",
        "FlextDbtOracleWmsProtocols",
    ],
    "FlextDbtOracleWmsTypes": [
        "flext_dbt_oracle_wms.typings",
        "FlextDbtOracleWmsTypes",
    ],
    "FlextDbtOracleWmsUtilities": [
        "flext_dbt_oracle_wms.utilities",
        "FlextDbtOracleWmsUtilities",
    ],
    "_utilities": ["flext_dbt_oracle_wms._utilities", ""],
    "c": ["flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsConstants"],
    "cli": ["flext_dbt_oracle_wms.cli", ""],
    "client": ["flext_dbt_oracle_wms.client", ""],
    "constants": ["flext_dbt_oracle_wms.constants", ""],
    "d": ["flext_meltano", "d"],
    "discover": ["flext_dbt_oracle_wms.cli", "discover"],
    "e": ["flext_meltano", "e"],
    "extract": ["flext_dbt_oracle_wms.cli", "extract"],
    "h": ["flext_meltano", "h"],
    "info": ["flext_dbt_oracle_wms.cli", "info"],
    "logger": ["flext_dbt_oracle_wms.cli", "logger"],
    "m": ["flext_dbt_oracle_wms.models", "FlextDbtOracleWmsModels"],
    "main": ["flext_dbt_oracle_wms.cli", "main"],
    "models": ["flext_dbt_oracle_wms.models", ""],
    "p": ["flext_dbt_oracle_wms.protocols", "FlextDbtOracleWmsProtocols"],
    "pipeline": ["flext_dbt_oracle_wms.cli", "pipeline"],
    "protocols": ["flext_dbt_oracle_wms.protocols", ""],
    "r": ["flext_meltano", "r"],
    "s": ["flext_meltano", "s"],
    "simple_api": ["flext_dbt_oracle_wms.simple_api", ""],
    "t": ["flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTypes"],
    "typings": ["flext_dbt_oracle_wms.typings", ""],
    "u": ["flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsUtilities"],
    "utilities": ["flext_dbt_oracle_wms.utilities", ""],
    "x": ["flext_meltano", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
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
    "_utilities",
    "c",
    "cli",
    "client",
    "constants",
    "d",
    "discover",
    "e",
    "extract",
    "h",
    "info",
    "logger",
    "m",
    "main",
    "models",
    "p",
    "pipeline",
    "protocols",
    "r",
    "s",
    "simple_api",
    "t",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
