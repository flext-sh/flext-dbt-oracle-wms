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
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import *

    from flext_dbt_oracle_wms import (
        cli,
        client,
        constants,
        models,
        protocols,
        simple_api,
        typings,
        utilities,
    )
    from flext_dbt_oracle_wms._utilities import *
    from flext_dbt_oracle_wms.cli import *
    from flext_dbt_oracle_wms.constants import *
    from flext_dbt_oracle_wms.models import *
    from flext_dbt_oracle_wms.protocols import *
    from flext_dbt_oracle_wms.simple_api import *
    from flext_dbt_oracle_wms.typings import *
    from flext_dbt_oracle_wms.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtOracleWms": "flext_dbt_oracle_wms.simple_api",
    "FlextDbtOracleWmsCliService": "flext_dbt_oracle_wms.cli",
    "FlextDbtOracleWmsClient": "flext_dbt_oracle_wms._utilities.client",
    "FlextDbtOracleWmsConstants": "flext_dbt_oracle_wms.constants",
    "FlextDbtOracleWmsModels": "flext_dbt_oracle_wms.models",
    "FlextDbtOracleWmsProtocols": "flext_dbt_oracle_wms.protocols",
    "FlextDbtOracleWmsTypes": "flext_dbt_oracle_wms.typings",
    "FlextDbtOracleWmsUtilities": "flext_dbt_oracle_wms.utilities",
    "_utilities": "flext_dbt_oracle_wms._utilities",
    "c": ["flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsConstants"],
    "cli": "flext_dbt_oracle_wms.cli",
    "client": "flext_dbt_oracle_wms.client",
    "constants": "flext_dbt_oracle_wms.constants",
    "d": "flext_meltano",
    "discover": "flext_dbt_oracle_wms.cli",
    "e": "flext_meltano",
    "extract": "flext_dbt_oracle_wms.cli",
    "h": "flext_meltano",
    "info": "flext_dbt_oracle_wms.cli",
    "logger": "flext_dbt_oracle_wms.cli",
    "m": ["flext_dbt_oracle_wms.models", "FlextDbtOracleWmsModels"],
    "main": "flext_dbt_oracle_wms.cli",
    "models": "flext_dbt_oracle_wms.models",
    "p": ["flext_dbt_oracle_wms.protocols", "FlextDbtOracleWmsProtocols"],
    "pipeline": "flext_dbt_oracle_wms.cli",
    "protocols": "flext_dbt_oracle_wms.protocols",
    "r": "flext_meltano",
    "s": "flext_meltano",
    "simple_api": "flext_dbt_oracle_wms.simple_api",
    "t": ["flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTypes"],
    "typings": "flext_dbt_oracle_wms.typings",
    "u": ["flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsUtilities"],
    "utilities": "flext_dbt_oracle_wms.utilities",
    "x": "flext_meltano",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
