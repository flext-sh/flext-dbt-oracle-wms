"""FLEXT DBT Oracle WMS Constants extending flext-core platform constants.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

DBT Oracle WMS-specific constants that extend flext-core patterns.
"""

from __future__ import annotations

from typing import ClassVar

from flext_core.constants import FlextConstants
from flext_oracle_wms.wms_constants import (
    FlextOracleWmsSemanticConstants as _WmsConstants,
    OracleWMSEntityType as _OracleWMSEntityType,
)

# =============================================================================
# DBT ORACLE WMS-SPECIFIC SEMANTIC CONSTANTS - Modern Python 3.13 Structure
# =============================================================================


class FlextDbtOracleWmsSemanticConstants(FlextConstants):
    """DBT Oracle WMS semantic constants extending FlextConstants.

    Modern Python 3.13 constants following semantic grouping patterns.
    Extends the FLEXT ecosystem constants with DBT Oracle WMS-specific
    values while maintaining full backward compatibility.
    """

    class Core:
        """Core DBT Oracle WMS system constants."""

        NAME = "flext-dbt-oracle-wms"
        VERSION = "0.9.0"
        # CONSUME from single source - NO DUPLICATION
        ECOSYSTEM_SIZE = FlextConstants.Core.ECOSYSTEM_SIZE

    class Dbt:
        """DBT-specific configuration constants."""

        PROJECT_NAME = "flext_dbt_oracle_wms"
        PROFILE = "flext_oracle_wms"
        SCHEMA_PREFIX = "wms"

        # Materialization types
        MATERIALIZATIONS: ClassVar[list[str]] = [
            "table",
            "view",
            "incremental",
            "snapshot",
            "ephemeral",
        ]

        # Test types
        TEST_TYPES: ClassVar[list[str]] = [
            "unique",
            "not_null",
            "relationships",
            "accepted_values",
            "data_quality",
        ]

        # Macro types
        MACRO_TYPES: ClassVar[list[str]] = [
            "utility",
            "transformation",
            "audit",
            "oracle_specific",
        ]

        # Documentation types
        DOCUMENTATION_TYPES: ClassVar[list[str]] = [
            "model",
            "source",
            "macro",
            "analysis",
        ]

    class Entities:
        """Oracle WMS entity type constants - consumed from flext-oracle-wms."""

        # CONSUME Oracle WMS entities from single source (flext-oracle-wms)
        WMS_ENTITIES: ClassVar[list[str]] = (
            _WmsConstants.Entities.CORE_ENTITIES
            + _WmsConstants.Entities.ORDER_ENTITIES
            + _WmsConstants.Entities.INVENTORY_ENTITIES
            + _WmsConstants.Entities.MOVEMENT_ENTITIES
            + _WmsConstants.Entities.SHIPMENT_ENTITIES
        )

        # Entity priority levels
        PRIORITY_LEVELS: ClassVar[list[str]] = ["high", "medium", "low"]

    class Processing:
        """Data processing configuration constants."""

        # Batch processing - CONSUME from single source
        DEFAULT_BATCH_SIZE = FlextConstants.Performance.DEFAULT_BATCH_SIZE
        INCREMENTAL_LOOKBACK_DAYS = 7

        # Data quality
        DATA_QUALITY_THRESHOLD = 0.95

        # Processing status
        PROCESSING_STATUSES: ClassVar[list[str]] = [
            "pending",
            "processing",
            "completed",
            "failed",
        ]

        # Validation modes
        VALIDATION_MODES: ClassVar[list[str]] = [
            "strict",
            "normal",
            "relaxed",
        ]

    class Configuration:
        """Configuration management constants."""

        DEFAULT_CONFIG: ClassVar[dict[str, object]] = {
            "project_name": "flext_dbt_oracle_wms",
            "profile": "flext_oracle_wms",
            "schema_prefix": "wms",
            "batch_size": 1000,
            "incremental_lookback_days": 7,
            "data_quality_threshold": 0.95,
        }


class FlextDbtOracleWmsConstants(FlextDbtOracleWmsSemanticConstants):
    """DBT Oracle WMS constants with backward compatibility.

    Legacy compatibility layer providing both modern semantic access
    and traditional flat constant access patterns for smooth migration.
    """

    # Modern semantic access (Primary API) - direct references
    Core = FlextDbtOracleWmsSemanticConstants.Core
    Dbt = FlextDbtOracleWmsSemanticConstants.Dbt
    Entities = FlextDbtOracleWmsSemanticConstants.Entities
    Processing = FlextDbtOracleWmsSemanticConstants.Processing
    Configuration = FlextDbtOracleWmsSemanticConstants.Configuration

    # Legacy compatibility - flat access patterns (DEPRECATED - use semantic access)
    PROJECT_NAME = FlextDbtOracleWmsSemanticConstants.Dbt.PROJECT_NAME
    VERSION = FlextDbtOracleWmsSemanticConstants.Core.VERSION
    PROFILE = FlextDbtOracleWmsSemanticConstants.Dbt.PROFILE
    SCHEMA_PREFIX = FlextDbtOracleWmsSemanticConstants.Dbt.SCHEMA_PREFIX
    BATCH_SIZE = FlextDbtOracleWmsSemanticConstants.Processing.DEFAULT_BATCH_SIZE
    INCREMENTAL_LOOKBACK_DAYS = (
        FlextDbtOracleWmsSemanticConstants.Processing.INCREMENTAL_LOOKBACK_DAYS
    )
    DATA_QUALITY_THRESHOLD = (
        FlextDbtOracleWmsSemanticConstants.Processing.DATA_QUALITY_THRESHOLD
    )


# =============================================================================
# LEGACY CLASSES - Backward compatibility (DEPRECATED - use semantic access)
# =============================================================================


class DBTOracleWMSEntityTypes:
    """Oracle WMS entity types for DBT models (DEPRECATED - use FlextDbtOracleWmsConstants.Entities.WMS_ENTITIES)."""

    # CONSUME from flext-oracle-wms API - NO DUPLICATION
    ALLOCATION = _OracleWMSEntityType.ALLOCATION
    ORDER_HDR = _OracleWMSEntityType.ORDER_HDR
    ORDER_DTL = _OracleWMSEntityType.ORDER_DTL
    INVENTORY = _OracleWMSEntityType.INVENTORY
    LOCATION = _OracleWMSEntityType.LOCATION
    ITEM = _OracleWMSEntityType.ITEM
    SHIPMENT = _OracleWMSEntityType.SHIPMENT
    # Additional entities not in base enum
    RECEIPT = "receipt"
    TASK = "task"
    WAVE = "wave"


class DBTOracleWMSMaterializations:
    """DBT materialization types (DEPRECATED - use FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS)."""

    TABLE = "table"
    VIEW = "view"
    INCREMENTAL = "incremental"
    SNAPSHOT = "snapshot"
    EPHEMERAL = "ephemeral"


class DBTOracleWMSTestTypes:
    """DBT test types (DEPRECATED - use FlextDbtOracleWmsConstants.Dbt.TEST_TYPES)."""

    UNIQUE = "unique"
    NOT_NULL = "not_null"
    RELATIONSHIPS = "relationships"
    ACCEPTED_VALUES = "accepted_values"
    DATA_QUALITY = "data_quality"


class DBTOracleWMSMacroTypes:
    """DBT macro types (DEPRECATED - use FlextDbtOracleWmsConstants.Dbt.MACRO_TYPES)."""

    UTILITY = "utility"
    TRANSFORMATION = "transformation"
    AUDIT = "audit"
    ORACLE_SPECIFIC = "oracle_specific"


class DBTOracleWMSDocumentationTypes:
    """DBT documentation types (DEPRECATED - use FlextDbtOracleWmsConstants.Dbt.DOCUMENTATION_TYPES)."""

    MODEL = "model"
    SOURCE = "source"
    MACRO = "macro"
    ANALYSIS = "analysis"


class DBTOracleWMSDefaults:
    """Default values for DBT Oracle WMS (DEPRECATED - use FlextDbtOracleWmsConstants.Configuration.DEFAULT_CONFIG)."""

    PROJECT_NAME = FlextDbtOracleWmsSemanticConstants.Dbt.PROJECT_NAME
    VERSION = FlextDbtOracleWmsSemanticConstants.Core.VERSION
    PROFILE = FlextDbtOracleWmsSemanticConstants.Dbt.PROFILE
    SCHEMA_PREFIX = FlextDbtOracleWmsSemanticConstants.Dbt.SCHEMA_PREFIX
    BATCH_SIZE = FlextDbtOracleWmsSemanticConstants.Processing.DEFAULT_BATCH_SIZE
    INCREMENTAL_LOOKBACK_DAYS = (
        FlextDbtOracleWmsSemanticConstants.Processing.INCREMENTAL_LOOKBACK_DAYS
    )
    DATA_QUALITY_THRESHOLD = (
        FlextDbtOracleWmsSemanticConstants.Processing.DATA_QUALITY_THRESHOLD
    )


class WMSConstants:
    """Core WMS constants (DEPRECATED - use FlextDbtOracleWmsConstants.Entities and Processing)."""

    # Entity levels
    HIGH_LEVEL = "high"
    MEDIUM_LEVEL = "medium"
    LOW_LEVEL = "low"

    # Processing status
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    # Validation modes
    STRICT_VALIDATION = "strict"
    NORMAL_VALIDATION = "normal"
    RELAXED_VALIDATION = "relaxed"


# =============================================================================
# EXPORTS - DBT Oracle WMS constants API
# =============================================================================

__all__: list[str] = [
    # Legacy classes (deprecated)
    "DBTOracleWMSDefaults",
    "DBTOracleWMSDocumentationTypes",
    "DBTOracleWMSEntityTypes",
    "DBTOracleWMSMacroTypes",
    "DBTOracleWMSMaterializations",
    "DBTOracleWMSTestTypes",
    # Legacy Compatibility (Backward Compatibility)
    "FlextDbtOracleWmsConstants",
    # Modern Semantic Constants (Primary API)
    "FlextDbtOracleWmsSemanticConstants",
    "WMSConstants",
]
