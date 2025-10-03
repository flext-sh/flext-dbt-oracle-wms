"""Constants for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_oracle_wms.wms_constants import OracleWMSEntityType

from flext_core import FlextConstants, FlextTypes


class FlextDbtOracleWmsSemanticConstants(FlextConstants):
    """DBT Oracle WMS semantic constants extending FlextConstants."""

    class Core:
        """Core DBT Oracle WMS system constants."""

        NAME = "flext-dbt-oracle-wms"
        VERSION = "0.9.0"
        # CONSUME from single source
        ECOSYSTEM_SIZE = 33  # Total FLEXT ecosystem projects

    class Dbt:
        """DBT-specific configuration constants."""

        PROJECT_NAME = "flext_dbt_oracle_wms"
        PROFILE = "flext_oracle_wms"
        SCHEMA_PREFIX = "wms"

        # Materialization types
        MATERIALIZATIONS: ClassVar[FlextTypes.StringList] = [
            "table",
            "view",
            "incremental",
            "snapshot",
            "ephemeral",
        ]

        # Test types
        TEST_TYPES: ClassVar[FlextTypes.StringList] = [
            "unique",
            "not_null",
            "relationships",
            "accepted_values",
            "data_quality",
        ]

        # Macro types
        MACRO_TYPES: ClassVar[FlextTypes.StringList] = [
            "utility",
            "transformation",
            "audit",
            "oracle_specific",
        ]

        # Documentation types
        DOCUMENTATION_TYPES: ClassVar[FlextTypes.StringList] = [
            "model",
            "source",
            "macro",
            "analysis",
        ]

    class Entities:
        """Oracle WMS entity type constants - consumed from flext-oracle-wms."""

        # CONSUME Oracle WMS entities from single source (flext-oracle-wms)
        WMS_ENTITIES: ClassVar[FlextTypes.StringList] = [
            "inventory",
            "location",
            "allocation",
            "order",
            "item",
            "shipment",
            "receipt",
            "task",
            "wave",
        ]

        # Entity priority levels
        PRIORITY_LEVELS: ClassVar[FlextTypes.StringList] = [
            "high",
            "medium",
            "low",
        ]

    class Processing:
        """Data processing configuration constants."""

        # Batch processing - CONSUME from single source
        DEFAULT_BATCH_SIZE = 1000  # Default batch size for WMS operations
        INCREMENTAL_LOOKBACK_DAYS = 7

        # Data quality thresholds
        DATA_QUALITY_THRESHOLD = 0.95
        HIGH_QUALITY_THRESHOLD = 95  # High quality score threshold
        GOOD_QUALITY_THRESHOLD = 92  # Good quality score threshold
        ACCEPTABLE_QUALITY_THRESHOLD = 90  # Acceptable quality score threshold
        MINIMUM_QUALITY_THRESHOLD = 88  # Minimum quality score threshold
        LOW_QUALITY_THRESHOLD = 85  # Low quality score threshold

        # Data volume thresholds
        HIGH_VOLUME_THRESHOLD = 100  # High volume threshold for WMS data
        MEDIUM_VOLUME_THRESHOLD = 10  # Medium volume threshold for WMS data

        # Query frequency thresholds
        HIGH_FREQUENCY_THRESHOLD = 1000  # High frequency threshold for queries

        # Processing status
        PROCESSING_STATUSES: ClassVar[FlextTypes.StringList] = [
            "pending",
            "processing",
            "completed",
            "failed",
        ]

        # Validation modes
        VALIDATION_MODES: ClassVar[FlextTypes.StringList] = [
            "strict",
            "normal",
            "relaxed",
        ]

    class Configuration:
        """Configuration management constants."""

        DEFAULT_CONFIG: ClassVar[FlextTypes.Dict] = {
            "project_name": "flext_dbt_oracle_wms",
            "profile": "flext_oracle_wms",
            "schema_prefix": "wms",
            "batch_size": 1000,
            "incremental_lookback_days": 7,
            "data_quality_threshold": 0.95,
        }


class FlextDbtOracleWmsConstants(FlextDbtOracleWmsSemanticConstants):
    """DBT Oracle WMS constants with backward compatibility."""

    # Modern semantic access (Primary API) - direct references
    Core = FlextDbtOracleWmsSemanticConstants.Core
    Dbt = FlextDbtOracleWmsSemanticConstants.Dbt
    Entities = FlextDbtOracleWmsSemanticConstants.Entities
    Processing = FlextDbtOracleWmsSemanticConstants.Processing
    Configuration = FlextDbtOracleWmsSemanticConstants.Configuration

    # Legacy compatibility - flat access patterns (DEPRECATED - use semantic access)
    # PROJECT_NAME = FlextDbtOracleWmsSemanticConstants.Dbt.PROJECT_NAME  # Disabled: Final override violation
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


class DBTOracleWMSEntityTypes:
    """Oracle WMS entity types for DBT models (DEPRECATED - use FlextDbtOracleWmsConstants.Entities.WMS_ENTITIES)."""

    # CONSUME from flext-oracle-wms API
    INVENTORY = OracleWMSEntityType.INVENTORY
    ORDER = OracleWMSEntityType.ORDER
    SHIPMENT = OracleWMSEntityType.SHIPMENT
    PICKING = OracleWMSEntityType.PICKING
    LOCATION = OracleWMSEntityType.LOCATION
    ITEM = OracleWMSEntityType.ITEM
    # Additional entities not in base enum
    ALLOCATION = "allocation"
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


class FlextWmsConstants(FlextConstants):
    """Core WMS constants extending FlextConstants (DEPRECATED - use FlextDbtOracleWmsConstants.Entities and Processing)."""

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


__all__: FlextTypes.StringList = [
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
    "FlextWmsConstants",
]
