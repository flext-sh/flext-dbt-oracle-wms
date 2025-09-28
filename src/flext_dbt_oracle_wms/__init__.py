"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core import FlextResult
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
from flext_dbt_oracle_wms.services import (
    FlextDbtOracleWmsMonitoringService,
    FlextDbtOracleWmsWorkflowService,
)
from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsUtilities

__version__ = importlib.metadata.version("flext-dbt-oracle-wms")

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

__all__ = [
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
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsUtilities",
    "FlextDbtOracleWmsValidationError",
    "FlextDbtOracleWmsWorkflowService",
    "FlextResult",
    "__version__",
    "__version_info__",
]
