"""Constants for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import Final, Literal

from flext_oracle_wms.constants import FlextOracleWmsConstants

from flext import FlextConstants
from flext_dbt_oracle_wms.__version__ import __version__


class FlextDbtOracleWmsSemanticConstants(FlextConstants):
    """DBT Oracle WMS semantic constants extending FlextConstants."""

    class Core:
        """Core DBT Oracle WMS system constants."""

        NAME: Final[str] = "flext-dbt-oracle-wms"
        VERSION: Final[str] = (
            __version__  # Use single source of truth from pyproject.toml
        )
        # CONSUME from single source
        ECOSYSTEM_SIZE: Final[int] = 33  # Total FLEXT ecosystem projects

    class Dbt:
        """DBT-specific configuration constants."""

        PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"
        PROFILE: Final[str] = "flext_oracle_wms"
        SCHEMA_PREFIX: Final[str] = "wms"

        class Materialization(StrEnum):
            """DBT materialization types.

            DRY Pattern: This StrEnum is the single source of truth for materialization types.
            All materialization-related constants and Literal types MUST reference this enum.
            """

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"
            SNAPSHOT = "snapshot"
            EPHEMERAL = "ephemeral"

        # Generate list from StrEnum for backward compatibility
        MATERIALIZATIONS: Final[tuple[str, ...]] = tuple(
            member.value for member in Materialization.__members__.values()
        )

        class TestType(StrEnum):
            """DBT test types.

            DRY Pattern: This StrEnum is the single source of truth for test types.
            All test type-related constants and Literal types MUST reference this enum.
            """

            UNIQUE = "unique"
            NOT_NULL = "not_null"
            RELATIONSHIPS = "relationships"
            ACCEPTED_VALUES = "accepted_values"
            DATA_QUALITY = "data_quality"
            CUSTOM = "custom"

        # Generate list from StrEnum for backward compatibility
        TEST_TYPES: Final[tuple[str, ...]] = tuple(
            member.value for member in TestType.__members__.values()
        )

        class MacroType(StrEnum):
            """DBT macro types.

            DRY Pattern: This StrEnum is the single source of truth for macro types.
            All macro type-related constants and Literal types MUST reference this enum.
            """

            UTILITY = "utility"
            TRANSFORMATION = "transformation"
            AUDIT = "audit"
            ORACLE_SPECIFIC = "oracle_specific"

        # Generate list from StrEnum for backward compatibility
        MACRO_TYPES: Final[tuple[str, ...]] = tuple(
            member.value for member in MacroType.__members__.values()
        )

        class DocumentationType(StrEnum):
            """DBT documentation types.

            DRY Pattern: This StrEnum is the single source of truth for documentation types.
            All documentation type-related constants and Literal types MUST reference this enum.
            """

            MODEL = "model"
            SOURCE = "source"
            MACRO = "macro"
            ANALYSIS = "analysis"

        # Generate list from StrEnum for backward compatibility
        DOCUMENTATION_TYPES: Final[tuple[str, ...]] = tuple(
            member.value for member in DocumentationType.__members__.values()
        )

        # PEP 695 Literal types referencing StrEnum members
        type MaterializationLiteral = Literal[
            Materialization.TABLE,
            Materialization.VIEW,
            Materialization.INCREMENTAL,
            Materialization.SNAPSHOT,
            Materialization.EPHEMERAL,
        ]

        type TestTypeLiteral = Literal[
            TestType.UNIQUE,
            TestType.NOT_NULL,
            TestType.RELATIONSHIPS,
            TestType.ACCEPTED_VALUES,
            TestType.DATA_QUALITY,
        ]

        type MacroTypeLiteral = Literal[
            MacroType.UTILITY,
            MacroType.TRANSFORMATION,
            MacroType.AUDIT,
            MacroType.ORACLE_SPECIFIC,
        ]

        type DocumentationTypeLiteral = Literal[
            DocumentationType.MODEL,
            DocumentationType.SOURCE,
            DocumentationType.MACRO,
            DocumentationType.ANALYSIS,
        ]

    class Entities:
        """Oracle WMS entity type constants - consumed from flext-oracle-wms."""

        class WmsEntityType(StrEnum):
            """Oracle WMS entity types.

            DRY Pattern: This StrEnum is the single source of truth for WMS entity types.
            All entity type-related constants and Literal types MUST reference this enum.
            Note: Some values are consumed from FlextOracleWmsConstants, others are project-specific.
            """

            INVENTORY = "inventory"
            LOCATION = "location"
            ALLOCATION = "allocation"
            ORDER = "order"
            ITEM = "item"
            SHIPMENT = "shipment"
            RECEIPT = "receipt"
            TASK = "task"
            WAVE = "wave"

        # Generate list from StrEnum for backward compatibility
        WMS_ENTITIES: Final[tuple[str, ...]] = tuple(
            member.value for member in WmsEntityType.__members__.values()
        )

        class PriorityLevel(StrEnum):
            """Entity priority levels.

            DRY Pattern: This StrEnum is the single source of truth for priority levels.
            All priority-related constants and Literal types MUST reference this enum.
            """

            HIGH = "high"
            MEDIUM = "medium"
            LOW = "low"

        # Generate list from StrEnum for backward compatibility
        PRIORITY_LEVELS: Final[tuple[str, ...]] = tuple(
            member.value for member in PriorityLevel.__members__.values()
        )

        # PEP 695 Literal types referencing StrEnum members
        type WmsEntityTypeLiteral = Literal[
            WmsEntityType.INVENTORY,
            WmsEntityType.LOCATION,
            WmsEntityType.ALLOCATION,
            WmsEntityType.ORDER,
            WmsEntityType.ITEM,
            WmsEntityType.SHIPMENT,
            WmsEntityType.RECEIPT,
            WmsEntityType.TASK,
            WmsEntityType.WAVE,
        ]

        type PriorityLevelLiteral = Literal[
            PriorityLevel.HIGH,
            PriorityLevel.MEDIUM,
            PriorityLevel.LOW,
        ]

    class DbtOracleWmsProcessing:
        """Data processing configuration constants.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """

        # Batch processing - CONSUME from single source
        DEFAULT_BATCH_SIZE: Final[int] = 1000  # Default batch size for WMS operations
        INCREMENTAL_LOOKBACK_DAYS: Final[int] = 7

        # Data quality thresholds
        DATA_QUALITY_THRESHOLD: Final[float] = 0.95
        HIGH_QUALITY_THRESHOLD: Final[int] = 95  # High quality score threshold
        GOOD_QUALITY_THRESHOLD: Final[int] = 92  # Good quality score threshold
        ACCEPTABLE_QUALITY_THRESHOLD: Final[int] = (
            90  # Acceptable quality score threshold
        )
        MINIMUM_QUALITY_THRESHOLD: Final[int] = 88  # Minimum quality score threshold
        LOW_QUALITY_THRESHOLD: Final[int] = 85  # Low quality score threshold

        # Data volume thresholds
        HIGH_VOLUME_THRESHOLD: Final[int] = 100  # High volume threshold for WMS data
        MEDIUM_VOLUME_THRESHOLD: Final[int] = 10  # Medium volume threshold for WMS data

        # Query frequency thresholds
        HIGH_FREQUENCY_THRESHOLD: Final[int] = (
            1000  # High frequency threshold for queries
        )

        class ProcessingStatus(StrEnum):
            """Processing status values.

            DRY Pattern: This StrEnum is the single source of truth for processing statuses.
            All status-related constants and Literal types MUST reference this enum.
            """

            PENDING = "pending"
            PROCESSING = "processing"
            COMPLETED = "completed"
            FAILED = "failed"

        class RunStatus(StrEnum):
            """DBT run status values.

            DRY Pattern: This StrEnum is the single source of truth for run statuses.
            All run status-related constants and Literal types MUST reference this enum.
            """

            SUCCESS = "success"
            ERROR = "error"
            SKIPPED = "skipped"
            RUNNING = "running"
            QUEUED = "queued"

        # Generate list from StrEnum for backward compatibility
        PROCESSING_STATUSES: Final[tuple[str, ...]] = tuple(
            member.value for member in ProcessingStatus.__members__.values()
        )

        class ValidationMode(StrEnum):
            """Validation mode values.

            DRY Pattern: This StrEnum is the single source of truth for validation modes.
            All validation mode-related constants and Literal types MUST reference this enum.
            """

            STRICT = "strict"
            NORMAL = "normal"
            RELAXED = "relaxed"

        # Generate list from StrEnum for backward compatibility
        VALIDATION_MODES: Final[tuple[str, ...]] = tuple(
            member.value for member in ValidationMode.__members__.values()
        )

        # PEP 695 Literal types referencing StrEnum members
        type ProcessingStatusLiteral = Literal[
            ProcessingStatus.PENDING,
            ProcessingStatus.PROCESSING,
            ProcessingStatus.COMPLETED,
            ProcessingStatus.FAILED,
        ]

        type ValidationModeLiteral = Literal[
            ValidationMode.STRICT,
            ValidationMode.NORMAL,
            ValidationMode.RELAXED,
        ]

        type RunStatusLiteral = Literal[
            RunStatus.SUCCESS,
            RunStatus.ERROR,
            RunStatus.SKIPPED,
            RunStatus.RUNNING,
            RunStatus.QUEUED,
        ]

    class Configuration:
        """Configuration management constants."""

        DEFAULT_CONFIG: Final[dict[str, object]] = {
            "project_name": "flext_dbt_oracle_wms",
            "profile": "flext_oracle_wms",
            "schema_prefix": "wms",
            "batch_size": 1000,
            "incremental_lookback_days": 7,
            "data_quality_threshold": 0.95,
        }


class FlextDbtOracleWmsConstants(FlextDbtOracleWmsSemanticConstants):
    """DBT Oracle WMS constants with backward compatibility."""

    # Modern semantic access (Primary API) - real inheritance classes
    class Core(FlextDbtOracleWmsSemanticConstants.Core):
        """Core constants - real inheritance."""

    class Dbt(FlextDbtOracleWmsSemanticConstants.Dbt):
        """DBT constants - real inheritance."""

    class Entities(FlextDbtOracleWmsSemanticConstants.Entities):
        """Entities constants - real inheritance."""

    class DbtOracleWmsProcessing(
        FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing,
    ):
        """Processing constants - real inheritance.

        Note: Cannot use 'Processing' name due to conflict with parent FlextConstants.Processing.
        All references should use DbtOracleWmsProcessing.
        """

    class Configuration(FlextDbtOracleWmsSemanticConstants.Configuration):
        """Configuration constants - real inheritance."""

    # Legacy compatibility - flat access patterns (DEPRECATED - use semantic access)
    # PROJECT_NAME = FlextDbtOracleWmsSemanticConstants.Dbt.PROJECT_NAME  # Disabled: Final override violation
    VERSION: Final[str] = FlextDbtOracleWmsSemanticConstants.Core.VERSION
    PROFILE: Final[str] = FlextDbtOracleWmsSemanticConstants.Dbt.PROFILE
    SCHEMA_PREFIX: Final[str] = FlextDbtOracleWmsSemanticConstants.Dbt.SCHEMA_PREFIX
    BATCH_SIZE: Final[int] = (
        FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing.DEFAULT_BATCH_SIZE
    )
    INCREMENTAL_LOOKBACK_DAYS: Final[int] = (
        FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing.INCREMENTAL_LOOKBACK_DAYS
    )
    DATA_QUALITY_THRESHOLD: Final[float] = (
        FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing.DATA_QUALITY_THRESHOLD
    )


class DBTOracleWMSEntityTypes:
    """Oracle WMS entity types for DBT models (DEPRECATED - use FlextDbtOracleWmsConstants.Entities.WMS_ENTITIES)."""

    # CONSUME from flext-oracle-wms API
    # Note: These are enum values, not classes - cannot use inheritance
    # Keep as aliases since enum values cannot be inherited
    INVENTORY = FlextOracleWmsConstants.WmsEntityType.INVENTORY
    ORDER = (
        FlextOracleWmsConstants.WmsEntityType.ORDERS
    )  # Note: parent uses ORDERS (plural)
    SHIPMENT = (
        FlextOracleWmsConstants.WmsEntityType.SHIPMENTS
    )  # Note: parent uses SHIPMENTS (plural)
    PICKING = FlextOracleWmsConstants.WmsEntityType.PICKING
    LOCATION = (
        FlextOracleWmsConstants.WmsEntityType.LOCATIONS
    )  # Note: parent uses LOCATIONS (plural)
    ITEM = (
        FlextOracleWmsConstants.WmsEntityType.ITEMS
    )  # Note: parent uses ITEMS (plural)
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
    BATCH_SIZE = (
        FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing.DEFAULT_BATCH_SIZE
    )
    INCREMENTAL_LOOKBACK_DAYS = FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing.INCREMENTAL_LOOKBACK_DAYS
    DATA_QUALITY_THRESHOLD = (
        FlextDbtOracleWmsSemanticConstants.DbtOracleWmsProcessing.DATA_QUALITY_THRESHOLD
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


c = FlextDbtOracleWmsConstants

__all__: list[str] = [
    "DBTOracleWMSDefaults",
    "DBTOracleWMSDocumentationTypes",
    "DBTOracleWMSEntityTypes",
    "DBTOracleWMSMacroTypes",
    "DBTOracleWMSMaterializations",
    "DBTOracleWMSTestTypes",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsSemanticConstants",
    "FlextWmsConstants",
    "c",
]
