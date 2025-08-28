"""FLEXT DBT Oracle WMS Configuration Types - Unified typing system using flext-core.

This module imports from the unified typing system in flext-core and defines
DBT Oracle WMS configuration types using modern Python 3.13 patterns and Pydantic v2.

IMPORTANT: This module is for Oracle WMS API integration, NOT Oracle Database.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal, TypedDict

from flext_oracle_wms.wms_constants import (
    FlextOracleWmsSemanticConstants as WmsConstants,
)
from pydantic import BaseModel, Field

# Simple type aliases for dbt Oracle WMS
NonEmptyStr = str
PositiveInt = int
ProjectName = str
Version = str


# Helper function - defined outside class to avoid forward reference
def _get_default_wms_entities() -> list[str]:
    """Get default WMS entities from flext-oracle-wms API.

    Returns:
      list[str]: Description.

    """  # Avoid object by building a new list explicitly
    entities: list[str] = []
    entities.extend(WmsConstants.Entities.CORE_ENTITIES)
    entities.extend(WmsConstants.Entities.ORDER_ENTITIES)
    entities.extend(list(WmsConstants.Entities.INVENTORY_ENTITIES)[:2])
    return entities


class FlextDBTOracleWMSConfig(BaseModel):
    """FLEXT DBT Oracle WMS configuration using core types."""

    project_name: ProjectName = Field(
        default="flext-dbt-oracle-wms",
        description="DBT Oracle WMS project name",
    )
    version: Version = Field(default="0.9.0", description="Project version")
    profile: NonEmptyStr = Field(
        default="flext_oracle_wms",
        description="DBT profile name",
    )

    # DBT configurations
    model_paths: list[str] = Field(default_factory=lambda: ["models"])
    analysis_paths: list[str] = Field(default_factory=lambda: ["analyses"])
    test_paths: list[str] = Field(default_factory=lambda: ["tests"])
    seed_paths: list[str] = Field(default_factory=lambda: ["seeds"])
    macro_paths: list[str] = Field(default_factory=lambda: ["macros"])

    # Oracle WMS specific - consuming from flext-oracle-wms API
    oracle_wms_schema: str = Field(default="wms_raw")

    wms_entities: list[str] = Field(
        default_factory=_get_default_wms_entities,
    )

    # Performance settings using core types
    enable_incremental_models: bool = Field(default=True)
    incremental_lookback_days: PositiveInt = Field(
        default=7,
        description="Days to look back for incremental models",
    )

    # Data quality
    enable_audit_logging: bool = Field(default=True)
    enable_lineage_tracking: bool = Field(default=True)


# DBT Oracle WMS TypedDicts using unified core types
class DBTOracleWMSConfiguration(TypedDict):
    """DBT Oracle WMS configuration using core types."""

    project_name: ProjectName
    version: Version
    profile: NonEmptyStr


class DBTOracleWMSModelConfiguration(TypedDict):
    """DBT model configuration using core types."""

    materialized: Literal["table", "view", "incremental"]
    schema: NonEmptyStr
    tags: list[NonEmptyStr]


class DBTOracleWMSSourceConfiguration(TypedDict):
    """DBT source configuration using core types."""

    name: NonEmptyStr
    schema: NonEmptyStr
    tables: list[dict[str, object]]


class DBTOracleWMSTestConfiguration(TypedDict):
    """DBT test configuration using core types."""

    store_failures: bool
    schema: NonEmptyStr


class DBTOracleWMSMacroConfiguration(TypedDict):
    """DBT macro configuration using core types."""

    name: NonEmptyStr
    description: NonEmptyStr
    arguments: list[NonEmptyStr]


class DBTOracleWMSProfileConfiguration(TypedDict):
    """DBT profile configuration using core types."""

    target: NonEmptyStr
    outputs: dict[str, object]


# ==============================================================================
# EXPORTS - ALL DBT ORACLE WMS CONFIG TYPES
# ==============================================================================

__all__: list[str] = [
    # TypedDict configurations
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTestConfiguration",
    # Main configuration classes
    "FlextDBTOracleWMSConfig",
]
