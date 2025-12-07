"""FLEXT DBT Oracle WMS Types - Domain-specific DBT Oracle WMS type definitions.

This module provides DBT Oracle WMS-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated, Literal, TypedDict

from flext_core import FlextTypes

# =============================================================================
# DBT ORACLE WMS MODULE-LEVEL TYPE ALIASES
# =============================================================================


# Simple type aliases for dbt Oracle WMS
EntityId = str
ProjectName = str
TimeoutSeconds = int
TimestampISO = str
Version = str

type CreatedAt = Annotated[datetime, "Timestamp of when entity was created"]
type UpdatedAt = Annotated[datetime, "Timestamp of when entity was last updated"]

# ==============================================================================
# DBT ORACLE WMS TYPE ALIASES USING CORE TYPES
# ==============================================================================

# Oracle WMS specific IDs using core types
type OracleWMSOperationId = EntityId
type OracleWMSConnectionId = EntityId
type OracleWMSSchemaId = EntityId
type OracleWMSQueryId = EntityId

# DBT specific timeout type aliases using core timeout types
type DBTOracleWMSProjectTimeout = TimeoutSeconds
type DBTOracleWMSModelTimeout = TimeoutSeconds
type DBTOracleWMSSourceTimeout = TimeoutSeconds
type DBTOracleWMSTestTimeout = TimeoutSeconds
type DBTOracleWMSMacroTimeout = TimeoutSeconds
type DBTOracleWMSSnapshotTimeout = TimeoutSeconds
type DBTOracleWMSAnalysisTimeout = TimeoutSeconds
type DBTOracleWMSCompilationTimeout = TimeoutSeconds
type DBTOracleWMSExecutionTimeout = TimeoutSeconds
type DBTOracleWMSDocumentationTimeout = TimeoutSeconds

# ==============================================================================
# DBT ORACLE WMS ENUMS
# ==============================================================================


class DBTOracleWMSMaterialization(StrEnum):
    """DBT Oracle WMS materialization types."""

    TABLE = "table"
    VIEW = "view"
    INCREMENTAL = "incremental"
    EPHEMERAL = "ephemeral"
    SNAPSHOT = "snapshot"


class DBTOracleWMSTestType(StrEnum):
    """DBT Oracle WMS test types."""

    UNIQUE = "unique"
    NOT_NULL = "not_null"
    ACCEPTED_VALUES = "accepted_values"
    RELATIONSHIPS = "relationships"
    CUSTOM = "custom"


class DBTOracleWMSRunStatus(StrEnum):
    """DBT Oracle WMS run status using StrEnum."""

    SUCCESS = "success"
    ERROR = "error"
    SKIPPED = "skipped"
    RUNNING = "running"
    QUEUED = "queued"


# =============================================================================
# DBT ORACLE WMS-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle WMS operations
# =============================================================================


# DBT Oracle WMS domain TypeVars
class FlextDbtOracleWmsTypes(FlextTypes):
    """DBT Oracle WMS-specific type definitions extending t.

    Domain-specific type system for DBT Oracle WMS data transformation operations.
    Contains ONLY complex DBT Oracle WMS-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types for Oracle WMS
    # =========================================================================

    class DbtProject:
        """DBT Oracle WMS project complex types."""

        type ProjectConfiguration = dict[str, object | dict[str, object]]
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type SourceConfiguration = dict[str, str | list[dict[str, object]]]
        type ProfileConfiguration = dict[str, object]
        type MacroConfiguration = dict[str, str | dict[str, object]]
        type TestConfiguration = dict[str, str | bool | list[str]]

    # =========================================================================
    # ORACLE WMS CONNECTION TYPES - Oracle WMS database connection configuration
    # =========================================================================

    class OracleWmsConnection:
        """Oracle WMS connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | dict[str, object]]
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type PoolingConfig = dict[str, int | bool | dict[str, object]]
        type SecurityConfig = dict[str, bool | str | dict[str, object]]
        type SessionConfig = dict[str, str | int | dict[str, object]]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # WMS DATA TYPES - Oracle WMS warehouse management data types
    # =========================================================================

    class WmsData:
        """Oracle WMS data complex types."""

        type InventoryData = dict[
            str, str | int | float | dict[str, FlextTypes.Json.JsonValue]
        ]
        type LocationData = dict[
            str, str | list[str] | dict[str, FlextTypes.Json.JsonValue]
        ]
        type AllocationData = dict[str, str | int | bool | dict[str, object]]
        type OrderData = dict[str, str | list[dict[str, FlextTypes.Json.JsonValue]]]
        type TaskData = dict[str, str | int | dict[str, FlextTypes.Json.JsonValue]]
        type ShipmentData = dict[str, str | list[str] | dict[str, object]]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle WMS
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle WMS transformation complex types."""

        type TransformationConfig = dict[
            str, FlextTypes.Json.JsonValue | dict[str, object]
        ]
        type WmsTransformation = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type DataValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type MaterializationConfig = dict[
            str, str | dict[str, FlextTypes.Json.JsonValue]
        ]
        type OutputFormat = dict[str, str | dict[str, object]]
        type ProcessingStep = dict[
            str, str | int | dict[str, FlextTypes.Json.JsonValue]
        ]

    # =========================================================================
    # DIMENSIONAL MODELING TYPES - WMS dimensional model types
    # =========================================================================

    class DimensionalModeling:
        """WMS dimensional modeling complex types."""

        type DimensionModel = dict[
            str, str | list[dict[str, FlextTypes.Json.JsonValue]]
        ]
        type FactModel = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type BridgeModel = dict[str, str | list[str] | dict[str, object]]
        type StarSchema = dict[str, list[dict[str, FlextTypes.Json.JsonValue]]]
        type ScdConfiguration = dict[str, str | bool | dict[str, object]]
        type GrainDefinition = dict[str, str | list[str]]

    # =========================================================================
    # WMS BUSINESS LOGIC TYPES - Warehouse management business rule types
    # =========================================================================

    class WmsBusinessLogic:
        """WMS business logic complex types."""

        type InventoryRules = dict[str, bool | str | float | dict[str, object]]
        type AllocationRules = dict[
            str, str | int | bool | dict[str, FlextTypes.Json.JsonValue]
        ]
        type PickingRules = dict[str, str | list[str] | dict[str, object]]
        type ReceivingRules = dict[
            str, bool | str | dict[str, FlextTypes.Json.JsonValue]
        ]
        type ShippingRules = dict[str, str | int | dict[str, object]]
        type QualityRules = dict[
            str, bool | float | dict[str, FlextTypes.Json.JsonValue]
        ]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle WMS
    # =========================================================================

    class DbtModel:
        """DBT Oracle WMS model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | dict[str, object]]
        type ModelDependency = dict[str, str | list[str] | dict[str, object]]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.Json.JsonValue]]
        type ModelDocumentation = dict[str, str | dict[str, object]]
        type ModelMaterialization = dict[str, str | dict[str, object]]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle WMS
    # =========================================================================

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type SourceConnection = dict[str, object | dict[str, object]]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.Json.JsonValue]]]
        type SourceFreshness = dict[str, str | int | dict[str, object]]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]

    # =========================================================================
    # ORACLE WMS ADAPTER TYPES - Oracle WMS-specific adapter configuration
    # =========================================================================

    class OracleWmsAdapter:
        """Oracle WMS adapter complex types."""

        type AdapterConfiguration = dict[str, object | dict[str, object]]
        type ConnectionAdapter = dict[str, str | int | bool | dict[str, object]]
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.Json.JsonValue]]
        type SchemaAdapter = dict[str, str | list[str] | dict[str, object]]
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextTypes.Json.JsonValue]
        ]
        type WmsAdapter = dict[str, str | int | dict[str, object]]

    # =========================================================================
    # PERFORMANCE OPTIMIZATION TYPES - Oracle WMS performance optimization
    # =========================================================================

    class PerformanceOptimization:
        """Oracle WMS performance optimization complex types."""

        type PartitionStrategy = dict[str, str | list[str] | dict[str, object]]
        type IndexStrategy = dict[
            str, str | bool | dict[str, FlextTypes.Json.JsonValue]
        ]
        type MaterializationStrategy = dict[str, str | dict[str, object]]
        type CacheStrategy = dict[
            str, bool | int | dict[str, FlextTypes.Json.JsonValue]
        ]
        type ParallelProcessing = dict[str, int | bool | dict[str, object]]
        type OracleHints = dict[str, str | list[str]]

    # =========================================================================
    # DBT ORACLE WMS PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """DBT Oracle WMS-specific project types.

        Adds DBT Oracle WMS transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle WMS domain owns Oracle WMS data transformation-specific types.
        """

        # DBT Oracle WMS-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from t
            "library",
            "application",
            "service",
            # DBT Oracle WMS-specific types
            "dbt-oracle-wms",
            "wms-transform",
            "wms-analytics",
            "wms-dbt-models",
            "dbt-wms-project",
            "wms-dimensional",
            "wms-warehouse",
            "wms-etl",
            "dbt-wms-pipeline",
            "wms-reporting",
            "wms-dbt",
            "wms-data-warehouse",
            "wms-inventory-analytics",
            "wms-allocation-analytics",
            "wms-operational-reporting",
            "wms-performance-analytics",
            "warehouse-bi",
            "wms-compliance-reporting",
        ]

        # DBT Oracle WMS-specific project configurations
        type DbtOracleWmsProjectConfig = dict[str, object]
        type WmsTransformConfig = dict[str, str | int | bool | list[str]]
        type WmsAnalyticsConfig = dict[str, bool | str | dict[str, object]]
        type DbtWmsPipelineConfig = dict[str, object]

    class DbtOracleWms:
        """DBT Oracle WMS types namespace for cross-project access.

        Provides organized access to all DBT Oracle WMS types for other FLEXT projects.
        Usage: Other projects can reference `t.DbtOracleWms.WmsData.*`, `t.DbtOracleWms.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_dbt_oracle_wms.typings import t
            config: t.DbtOracleWms.Project.DbtOracleWmsProjectConfig = ...
            data: t.DbtOracleWms.WmsData.InventoryData = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """

    # =========================================================================
    # DBT ORACLE WMS DOMAIN OBJECTS - TypedDict definitions for domain objects
    # =========================================================================

    class DomainObjects:
        """DBT Oracle WMS domain object TypedDict definitions."""

        # Domain objects using the configurations above
        class DBTOracleWMSProject(TypedDict):
            """DBT Oracle WMS project domain object using core types."""

            id: EntityId
            name: ProjectName
            version: Version
            configuration: DBTOracleWMSProjectConfiguration
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSModel(TypedDict):
            """DBT Oracle WMS model domain object using core types."""

            id: EntityId
            project_id: EntityId
            name: str
            configuration: dict[str, object]  # Using dict for model config
            sql_content: str
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSSource(TypedDict):
            """DBT Oracle WMS source domain object using core types."""

            id: EntityId
            project_id: EntityId
            name: str
            configuration: dict[str, object]  # Using dict for source config
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSTest(TypedDict):
            """DBT Oracle WMS test domain object using core types."""

            id: EntityId
            project_id: EntityId
            model_id: EntityId | None
            name: str
            configuration: dict[str, object]  # Using dict for test config
            sql_content: str | None
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSMacro(TypedDict):
            """DBT Oracle WMS macro domain object using core types."""

            id: EntityId
            project_id: EntityId
            name: str
            configuration: dict[str, object]  # Using dict for macro config
            sql_content: str
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSSnapshot(TypedDict):
            """DBT Oracle WMS snapshot domain object using core types."""

            id: EntityId
            project_id: EntityId
            name: str
            configuration: DBTOracleWMSSnapshotConfiguration
            sql_content: str
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSAnalysis(TypedDict):
            """DBT Oracle WMS analysis domain object using core types."""

            id: EntityId
            project_id: EntityId
            name: str
            configuration: DBTOracleWMSAnalysisConfiguration
            sql_content: str
            created_at: CreatedAt
            updated_at: UpdatedAt

        class DBTOracleWMSCompilation(TypedDict):
            """DBT Oracle WMS compilation domain object using core types."""

            id: EntityId
            project_id: EntityId
            configuration: DBTOracleWMSCompilationConfiguration
            status: DBTOracleWMSRunStatus
            output: str | None
            error: str | None
            created_at: CreatedAt
            completed_at: UpdatedAt | None

        class DBTOracleWMSExecution(TypedDict):
            """DBT Oracle WMS execution domain object using core types."""

            id: EntityId
            project_id: EntityId
            configuration: DBTOracleWMSExecutionConfiguration
            status: DBTOracleWMSRunStatus
            output: str | None
            error: str | None
            created_at: CreatedAt
            completed_at: UpdatedAt | None

        class DBTOracleWMSDocumentation(TypedDict):
            """DBT Oracle WMS documentation domain object using core types."""

            id: EntityId
            project_id: EntityId
            configuration: DBTOracleWMSDocumentationConfiguration
            status: DBTOracleWMSRunStatus
            output_path: str | None
            error: str | None
            created_at: CreatedAt
            completed_at: UpdatedAt | None


# Moved TypedDict classes to module level to avoid F821 issues
class DBTOracleWMSProjectConfiguration(TypedDict):
    """DBT Oracle WMS project configuration using core types."""

    name: ProjectName
    version: Version
    profile: str
    model_paths: list[str]
    analysis_paths: list[str]
    test_paths: list[str]
    seed_paths: list[str]
    macro_paths: list[str]
    snapshot_paths: list[str]
    target_path: str
    clean_targets: list[str]
    require_dbt_version: str
    dbt_version: str


class DBTOracleWMSSnapshotConfiguration(TypedDict):
    """DBT Oracle WMS snapshot configuration using core types."""

    name: str
    strategy: str
    unique_key: str
    updated_at: str
    dbt_version: str


class DBTOracleWMSAnalysisConfiguration(TypedDict):
    """DBT Oracle WMS analysis configuration using core types."""

    name: str
    depends_on: list[str]


class DBTOracleWMSCompilationConfiguration(TypedDict):
    """DBT Oracle WMS compilation configuration using core types."""

    name: str
    depends_on: list[str]


class DBTOracleWMSExecutionConfiguration(TypedDict):
    """DBT Oracle WMS execution configuration using core types."""

    name: str
    depends_on: list[str]


class DBTOracleWMSDocumentationConfiguration(TypedDict):
    """DBT Oracle WMS documentation configuration using core types."""

    name: str
    depends_on: list[str]


# Alias for simplified usage
t = FlextDbtOracleWmsTypes

# Namespace composition via class inheritance
# DbtOracleWms namespace provides access to nested classes through inheritance
# Access patterns:
# - t.DbtOracleWms.* for DBT Oracle WMS-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle WMS TypeVars and types
# =============================================================================

__all__ = [
    "CreatedAt",
    "DBTOracleWMSAnalysisConfiguration",
    "DBTOracleWMSAnalysisTimeout",
    "DBTOracleWMSCompilationConfiguration",
    "DBTOracleWMSCompilationTimeout",
    "DBTOracleWMSDocumentationConfiguration",
    "DBTOracleWMSDocumentationTimeout",
    "DBTOracleWMSExecutionConfiguration",
    "DBTOracleWMSExecutionTimeout",
    "DBTOracleWMSMacroTimeout",
    # Enums
    "DBTOracleWMSMaterialization",
    "DBTOracleWMSModelTimeout",
    "DBTOracleWMSProjectConfiguration",
    "DBTOracleWMSProjectTimeout",
    "DBTOracleWMSRunStatus",
    "DBTOracleWMSSnapshotConfiguration",
    "DBTOracleWMSSnapshotTimeout",
    "DBTOracleWMSSourceTimeout",
    "DBTOracleWMSTestTimeout",
    "DBTOracleWMSTestType",
    # Module-level aliases
    "EntityId",
    # Core types
    "FlextDbtOracleWmsTypes",
    "OracleWMSConnectionId",
    # Type aliases
    "OracleWMSOperationId",
    "OracleWMSQueryId",
    "OracleWMSSchemaId",
    "ProjectName",
    "TimeoutSeconds",
    "TimestampISO",
    "UpdatedAt",
    "Version",
    "t",
]
