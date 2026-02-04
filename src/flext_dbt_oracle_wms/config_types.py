"""Configuration types for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextSettings, FlextTypes as t
from flext_oracle_wms.wms_constants import (
    FlextOracleWmsSemanticConstants as WmsConstants,
)
from pydantic import BaseModel, ConfigDict, Field

# Simple type aliases for dbt Oracle WMS
NonEmptyStr = str
PositiveInt = int
ProjectName = str
Version = str


# Helper function - defined outside class to avoid forward reference
def _get_default_wms_entities() -> list[str]:
    """Get default WMS entities from flext-oracle-wms API.

    Returns:
    list[str]: List of default WMS entity names.

    """
    entities: list[str] = []
    entities.extend(WmsConstants.OracleWmsEntities.CORE_ENTITIES)
    entities.extend(WmsConstants.OracleWmsEntities.ORDER_ENTITIES)
    entities.extend(list(WmsConstants.OracleWmsEntities.INVENTORY_ENTITIES)[:2])
    return entities


class FlextDBTOracleWMSSettings(FlextSettings):
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


# DBT Oracle WMS Pydantic Models using unified core types
class DBTOracleWMSConfiguration(BaseModel):
    """DBT Oracle WMS configuration using core types."""

    model_config = ConfigDict(frozen=False, extra="forbid")

    project_name: ProjectName
    version: Version
    profile: NonEmptyStr


class DBTOracleWMSModelConfiguration(BaseModel):
    """DBT model configuration using core types."""

    model_config = ConfigDict(frozen=False, extra="forbid")

    materialized: Literal["table", "view", "incremental"]
    schema_name: NonEmptyStr = Field(alias="schema")
    tags: list[NonEmptyStr]


class DBTOracleWMSSourceConfiguration(BaseModel):
    """DBT source configuration using core types."""

    model_config = ConfigDict(frozen=False, extra="forbid")

    name: NonEmptyStr
    schema_name: NonEmptyStr = Field(alias="schema")
    tables: list[dict[str, t.GeneralValueType]]


class DBTOracleWMSTestConfiguration(BaseModel):
    """DBT test configuration using core types."""

    model_config = ConfigDict(frozen=False, extra="forbid")

    store_failures: bool
    schema_name: NonEmptyStr = Field(alias="schema")


class DBTOracleWMSMacroConfiguration(BaseModel):
    """DBT macro configuration using core types."""

    model_config = ConfigDict(frozen=False, extra="forbid")

    name: NonEmptyStr
    description: NonEmptyStr
    arguments: list[NonEmptyStr]


class DBTOracleWMSProfileConfiguration(BaseModel):
    """DBT profile configuration using core types."""

    model_config = ConfigDict(frozen=False, extra="forbid")

    target: NonEmptyStr
    outputs: dict[str, t.GeneralValueType]


# ==============================================================================
# EXPORTS - ALL DBT ORACLE WMS CONFIG TYPES
# ==============================================================================

__all__: list[str] = [
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTestConfiguration",
    # Main configuration classes
    "FlextDBTOracleWMSSettings",
]
