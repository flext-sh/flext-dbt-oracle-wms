"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Final

from flext_dbt_oracle_wms.client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.config import FlextDbtOracleWmsSettings
from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels, m, m_dbt_oracle_wms
from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols
from flext_dbt_oracle_wms.services import (
    FlextDbtOracleWmsMonitoringService,
    FlextDbtOracleWmsWorkflowService,
)
from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms, FlextDbtOracleWmsAPI
from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsUtilities
from flext_dbt_oracle_wms.version import VERSION, FlextDbtOracleWmsVersion

PROJECT_VERSION: Final[FlextDbtOracleWmsVersion] = VERSION

__version__: str = VERSION.version
__version_info__: tuple[int | str, ...] = VERSION.version_info

__all__ = [
    "PROJECT_VERSION",
    "VERSION",
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsAPI",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsUtilities",
    "FlextDbtOracleWmsVersion",
    "FlextDbtOracleWmsWorkflowService",
    "__version__",
    "__version_info__",
    "m",
    "m_dbt_oracle_wms",
]
