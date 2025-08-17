"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Version 0.9.0 - Consolidated DBT Oracle WMS following the established DBT pattern:
- Uses flext-meltano for DBT integration and orchestration
- Built on flext-core foundation with flext-oracle-wms maximum composition
- Follows consolidated DBT architecture with dbt_config, dbt_client, dbt_models, dbt_services
- Implements Oracle WMS-specific business logic and transformations

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

# Core imports from flext-core
from flext_core import FlextResult, get_logger

try:
    __version__ = importlib.metadata.version("flext-dbt-oracle-wms")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# ================================
# CONSOLIDATED DBT ORACLE WMS API
# ================================

# Configuration - Essential for setup
from flext_dbt_oracle_wms.dbt_config import FlextDbtOracleWmsConfig

# Client - Main interface for Oracle WMS DBT operations
from flext_dbt_oracle_wms.dbt_client import FlextDbtOracleWmsClient

# Models - Oracle WMS DBT data models and transformers
from flext_dbt_oracle_wms.models import (
    FlextDbtOracleWmsInventoryFact,
    FlextDbtOracleWmsItemDimension,
    FlextDbtOracleWmsLocationDimension,
    FlextDbtOracleWmsShipmentFact,
    FlextDbtOracleWmsTransformer,
)

# Services - High-level workflow orchestration
from flext_dbt_oracle_wms.dbt_services import (
    FlextDbtOracleWmsMonitoringService,
    FlextDbtOracleWmsWorkflowService,
)

# Exceptions - Comprehensive error handling using flext-core factory patterns
from flext_dbt_oracle_wms.exceptions import (
    FlextDbtOracleWmsError,
    FlextDbtOracleWmsValidationError,
    FlextDbtOracleWmsConfigurationError,
    FlextDbtOracleWmsConnectionError,
    FlextDbtOracleWmsProcessingError,
    FlextDbtOracleWmsAuthenticationError,
    FlextDbtOracleWmsTimeoutError,
    # Domain-specific exceptions
    FlextDbtOracleWmsInventoryError,
    FlextDbtOracleWmsModelError,
    FlextDbtOracleWmsShipmentError,
    FlextDbtOracleWmsTestError,
)

# ================================
# CONVENIENCE FACTORY FUNCTIONS
# ================================

logger = get_logger(__name__)


def create_oracle_wms_dbt_client(
    config: FlextDbtOracleWmsConfig | None = None,
) -> FlextDbtOracleWmsClient:
    """Create Oracle WMS DBT client with configuration.

    Args:
      config: Optional configuration (defaults to FlextDbtOracleWmsConfig())

    Returns:
      Configured Oracle WMS DBT client

    """
    logger.info("Creating Oracle WMS DBT client")
    return FlextDbtOracleWmsClient(config)


def create_oracle_wms_workflow_service(
    config: FlextDbtOracleWmsConfig | None = None,
) -> FlextDbtOracleWmsWorkflowService:
    """Create Oracle WMS workflow service with configuration.

    Args:
      config: Optional configuration (defaults to FlextDbtOracleWmsConfig())

    Returns:
      Configured Oracle WMS workflow service

    """
    logger.info("Creating Oracle WMS workflow service")
    return FlextDbtOracleWmsWorkflowService(config)


# ================================
# BACKWARD COMPATIBILITY ALIASES
# ================================

# Maintain compatibility with existing imports
OracleWMSDBTClient = FlextDbtOracleWmsClient
OracleWMSDBTConfig = FlextDbtOracleWmsConfig
OracleWMSTransformer = FlextDbtOracleWmsTransformer
ItemDimension = FlextDbtOracleWmsItemDimension
LocationDimension = FlextDbtOracleWmsLocationDimension
InventoryFact = FlextDbtOracleWmsInventoryFact
ShipmentFact = FlextDbtOracleWmsShipmentFact

# ================================
# PUBLIC API EXPORTS
# ================================

__all__: list[str] = [
    # Configuration
    "FlextDbtOracleWmsConfig",
    # Client & Services - Primary interfaces
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsWorkflowService",
    # Models & Transformers - Data structures
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
    # Exceptions - Error handling
    "FlextDbtOracleWmsAuthenticationError",
    "FlextDbtOracleWmsConfigurationError",
    "FlextDbtOracleWmsConnectionError",
    "FlextDbtOracleWmsError",
    "FlextDbtOracleWmsInventoryError",
    "FlextDbtOracleWmsModelError",
    "FlextDbtOracleWmsProcessingError",
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsValidationError",
    # Core patterns (from flext-core)
    "FlextResult",
    # Factory functions
    "create_oracle_wms_dbt_client",
    "create_oracle_wms_workflow_service",
    # Backward compatibility aliases
    "InventoryFact",
    "ItemDimension",
    "LocationDimension",
    "OracleWMSDBTClient",
    "OracleWMSDBTConfig",
    "OracleWMSTransformer",
    "ShipmentFact",
    # Metadata
    "__version__",
    "__version_info__",
]
