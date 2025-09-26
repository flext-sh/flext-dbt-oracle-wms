"""Module docstring."""

from __future__ import annotations

"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import importlib.metadata

from flext_core import FlextResult

__version__ = importlib.metadata.version("flext-dbt-oracle-wms")

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# ================================
# CONSOLIDATED DBT ORACLE WMS API
# ================================

# Configuration - Essential for setup
# Client - Main interface for Oracle WMS DBT operations
# Compatibility imports temporarily disabled - modules not implemented yet
from flext_dbt_oracle_wms.dbt_client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.dbt_config import FlextDbtOracleWmsConfig

# Services - High-level workflow orchestration
from flext_dbt_oracle_wms.dbt_services import (
    FlextDbtOracleWmsMonitoringService,
    FlextDbtOracleWmsWorkflowService,
)

# Exceptions - Comprehensive error handling using flext-core factory patterns
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

# Factory functions and compatibility imports
# Factory functions temporarily disabled - modules not implemented yet
# Models - Oracle WMS DBT unified models collection
from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    # Exceptions - Error handling
    "FlextDbtOracleWmsAuthenticationError",
    # Client & Services - Primary interfaces
    "FlextDbtOracleWmsClient",
    # Configuration
    "FlextDbtOracleWmsConfig",
    "FlextDbtOracleWmsConfigurationError",
    "FlextDbtOracleWmsConnectionError",
    "FlextDbtOracleWmsError",
    "FlextDbtOracleWmsInventoryError",
    "FlextDbtOracleWmsModelError",
    # Models - Unified models collection
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsProcessingError",
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsValidationError",
    "FlextDbtOracleWmsWorkflowService",
    # Core patterns (from flext-core)
    "FlextResult",
    # Backward compatibility aliases - temporarily disabled
    # Metadata
    "__version__",
    "__version_info__",
    # Factory functions - temporarily disabled
]
