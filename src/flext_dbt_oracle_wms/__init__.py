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
from flext_dbt_oracle_wms.compatibility import (
    InventoryFact,
    ItemDimension,
    LocationDimension,
    OracleWMSDBTClient,
    OracleWMSDBTConfig,
    OracleWMSTransformer,
    ShipmentFact,
)
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
from flext_dbt_oracle_wms.factory import (
    create_oracle_wms_dbt_client,
    create_oracle_wms_workflow_service,
)

# Models - Oracle WMS DBT data models and transformers
from flext_dbt_oracle_wms.models import (
    FlextDbtOracleWmsInventoryFact,
    FlextDbtOracleWmsItemDimension,
    FlextDbtOracleWmsLocationDimension,
    FlextDbtOracleWmsShipmentFact,
    FlextDbtOracleWmsTransformer,
)

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
    # Models & Transformers - Data structures
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsModelError",
    "FlextDbtOracleWmsMonitoringService",
    "FlextDbtOracleWmsProcessingError",
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsTransformer",
    "FlextDbtOracleWmsValidationError",
    "FlextDbtOracleWmsWorkflowService",
    # Core patterns (from flext-core)
    "FlextResult",
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
    # Factory functions
    "create_oracle_wms_dbt_client",
    "create_oracle_wms_workflow_service",
]
