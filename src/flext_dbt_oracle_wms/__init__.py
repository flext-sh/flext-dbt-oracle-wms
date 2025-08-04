"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using flext-meltano.

Version 0.9.0 - DBT Oracle WMS plugin using flext-meltano architecture:
- Uses flext-meltano for DBT integration and orchestration
- Built on flext-core foundation for robust Oracle WMS transformations
- Follows FLEXT architecture where DBT components are centralized in flext-meltano

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings
from typing import Any, Optional

from flext_core import FlextResult
from flext_meltano.dbt import (
    FlextMeltanoDbtManager,
    FlextMeltanoDbtProject,
    FlextMeltanoDbtRunner,
)
from pydantic import BaseModel

try:
    __version__ = importlib.metadata.version("flext-dbt-oracle-wms")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


# Create local orchestrator implementation - the orchestration.dbt module doesn't exist
class FlextOracleWMSDbtOrchestrator:
    """Oracle WMS DBT orchestrator placeholder."""


# Base classes for configuration
class WMSBaseConfig(BaseModel):
    """Base configuration for WMS operations."""


class WMSError(Exception):
    """Base exception for WMS-specific errors."""


class ValidationError(ValueError):
    """Validation error for WMS data."""


class FlextDbtOracleWmsDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT DBT ORACLE WMS import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT DBT ORACLE WMS docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextDbtOracleWmsDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# DBT Oracle WMS Configuration exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_oracle_wms.config.types import (
        DBTOracleWMSConfiguration,
        FlextDBTOracleWMSConfig,
    )

# DBT Oracle WMS Domain exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_oracle_wms.domain.types import (
        DBTOracleWMSAnalysis,
        DBTOracleWMSExecution,
        DBTOracleWMSModel,
        DBTOracleWMSProject,
    )

# DBT Oracle WMS Constants exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_oracle_wms.constants import (
        DBTOracleWMSDefaults,
        DBTOracleWMSEntityTypes,
        DBTOracleWMSMaterializations,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__: list[str] = [
    "BaseModel",  # from flext_dbt_oracle_wms import BaseModel
    # DBT Oracle WMS Analysis (simplified access)
    "DBTOracleWMSAnalysis",  # from flext_dbt_oracle_wms import DBTOracleWMSAnalysis
    # DBT Oracle WMS Configuration (simplified access)
    "DBTOracleWMSConfiguration",  # from flext_dbt_oracle_wms import DBTOracleWMSConfiguration
    # DBT Oracle WMS Constants (simplified access)
    "DBTOracleWMSDefaults",  # from flext_dbt_oracle_wms import DBTOracleWMSDefaults
    "DBTOracleWMSEntityTypes",  # from flext_dbt_oracle_wms import DBTOracleWMSEntityTypes
    # DBT Oracle WMS Execution (simplified access)
    "DBTOracleWMSExecution",  # from flext_dbt_oracle_wms import DBTOracleWMSExecution
    "DBTOracleWMSMaterializations",  # from flext_dbt_oracle_wms import DBTOracleWMSMaterializations
    # DBT Oracle WMS Models (simplified access)
    "DBTOracleWMSModel",  # from flext_dbt_oracle_wms import DBTOracleWMSModel
    "DBTOracleWMSProject",  # from flext_dbt_oracle_wms import DBTOracleWMSProject
    "FlextDBTOracleWMSConfig",  # from flext_dbt_oracle_wms import FlextDBTOracleWMSConfig
    # Deprecation utilities
    "FlextDbtOracleWmsDeprecationWarning",
    # Consolidated Orchestrator (from flext-meltano)
    "FlextOracleWMSDbtOrchestrator",  # DBT orchestration for Oracle WMS
    "FlextResult",  # from flext_dbt_oracle_wms import FlextResult
    "ValidationError",  # from flext_dbt_oracle_wms import ValidationError
    # Core Patterns (from flext-core)
    "WMSBaseConfig",  # from flext_dbt_oracle_wms import WMSBaseConfig
    "WMSError",  # from flext_dbt_oracle_wms import WMSError
    # Version
    "__version__",
    "__version_info__",
]
