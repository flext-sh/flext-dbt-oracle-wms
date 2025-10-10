"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_core import FlextResult

from flext_dbt_oracle_wms.__version__ import __version__, __version_info__
from flext_dbt_oracle_wms.client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.config import FlextDbtOracleWmsConfig
from flext_dbt_oracle_wms.exceptions import (
    FlextDbtOracleWmsAuthenticationError,
    FlextDbtOracleWmsConfigurationError,
    FlextDbtOracleWmsConnectionError,
    FlextDbtOracleWmsError,
    FlextDbtOracleWmsInventoryError,
    FlextDbtOracleWmsModelError,
    FlextDbtOracleWmsProcessingError,
    FlextDbtOracleWmsShipmentError,
    FlextDbtOracleWmsTestError,
    FlextDbtOracleWmsTimeoutError,
    FlextDbtOracleWmsValidationError,
)
from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels
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
    "FlextDbtOracleWmsAuthenticationError",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsConfig",
    "FlextDbtOracleWmsConfigurationError",
    "FlextDbtOracleWmsConnectionError",
    "FlextDbtOracleWmsError",
    "FlextDbtOracleWmsInventoryError",
    "FlextDbtOracleWmsModelError",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsProcessingError",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsUtilities",
    "FlextDbtOracleWmsValidationError",
    "FlextDbtOracleWmsVersion",
    "FlextDbtOracleWmsWorkflowService",
    "FlextResult",
    "__version__",
    "__version_info__",
]
