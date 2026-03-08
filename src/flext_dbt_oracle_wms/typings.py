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
from typing import Annotated, Literal

from flext_core import FlextTypes
from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

from flext_dbt_oracle_wms.constants import c

# ==============================================================================
# DBT ORACLE WMS ENUMS - Aliases from constants.py (single source of truth)
# ==============================================================================

DBTOracleWMSMaterialization = c.DbtOracleWms.Dbt.Materialization
DBTOracleWMSTestType = c.DbtOracleWms.Dbt.TestType
type DBTOracleWMSRunStatus = c.DbtOracleWms.DbtOracleWmsProcessing.RunStatus

# =============================================================================
# DBT ORACLE WMS-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle WMS operations
# =============================================================================


# DBT Oracle WMS domain TypeVars
class FlextDbtOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """DBT Oracle WMS-specific type definitions extending t.

    Domain-specific type system for DBT Oracle WMS data transformation operations.
    Contains ONLY complex DBT Oracle WMS-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # BASE TYPES - Foundational type aliases for DBT Oracle WMS
    # =========================================================================

    class Base:
        """Foundational type aliases for DBT Oracle WMS domain."""

        type EntityId = str
        type ProjectName = str
        type TimeoutSeconds = int
        type TimestampISO = str
        type Version = str
        type CreatedAt = Annotated[datetime, "Timestamp of when entity was created"]
        type UpdatedAt = Annotated[
            datetime,
            "Timestamp of when entity was last updated",
        ]

    # =========================================================================
    # ORACLE WMS ID TYPES - Oracle WMS specific identifiers
    # =========================================================================

    class DbtOracleWms:
        """Oracle WMS specific ID type aliases."""

        type OracleWMSOperationId = str
        type OracleWMSConnectionId = str
        type OracleWMSSchemaId = str
        type OracleWMSQueryId = str

    # =========================================================================
    # TIMEOUT TYPES - DBT Oracle WMS operation timeouts
    # =========================================================================

    class Timeouts:
        """DBT Oracle WMS timeout type aliases."""

        type DBTOracleWMSProjectTimeout = int
        type DBTOracleWMSModelTimeout = int
        type DBTOracleWMSSourceTimeout = int
        type DBTOracleWMSTestTimeout = int
        type DBTOracleWMSMacroTimeout = int
        type DBTOracleWMSSnapshotTimeout = int
        type DBTOracleWMSAnalysisTimeout = int
        type DBTOracleWMSCompilationTimeout = int
        type DBTOracleWMSExecutionTimeout = int
        type DBTOracleWMSDocumentationTimeout = int

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types for Oracle WMS
    # =========================================================================

    class DbtProject:
        """DBT Oracle WMS project complex types."""

        type ProjectConfiguration = dict[
            str,
            FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue],
        ]
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConfiguration = dict[
            str,
            str | list[dict[str, FlextTypes.ContainerValue]],
        ]
        type ProfileConfiguration = dict[str, FlextTypes.ContainerValue]
        type MacroConfiguration = dict[
            str,
            str | dict[str, FlextTypes.ContainerValue],
        ]
        type TestConfiguration = dict[str, str | bool | list[str]]

    # =========================================================================
    # ORACLE WMS CONNECTION TYPES - Oracle WMS database connection configuration
    # =========================================================================

    class OracleWmsConnection:
        """Oracle WMS connection complex types."""

        type ConnectionConfig = dict[
            str,
            str | int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type PoolingConfig = dict[
            str,
            int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type SecurityConfig = dict[
            str,
            bool | str | dict[str, FlextTypes.ContainerValue],
        ]
        type SessionConfig = dict[
            str,
            str | int | dict[str, FlextTypes.ContainerValue],
        ]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # WMS DATA TYPES - Oracle WMS warehouse management data types
    # =========================================================================

    class WmsData:
        """Oracle WMS data complex types."""

        type InventoryData = dict[
            str,
            str | int | float | dict[str, FlextTypes.JsonValue],
        ]
        type LocationData = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type AllocationData = dict[
            str,
            str | int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type OrderData = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type TaskData = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type ShipmentData = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle WMS
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle WMS transformation complex types."""

        type TransformationConfig = dict[
            str,
            FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue],
        ]
        type WmsTransformation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DataValidation = dict[
            str,
            bool | str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type MaterializationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type OutputFormat = dict[str, str | dict[str, FlextTypes.ContainerValue]]
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DIMENSIONAL MODELING TYPES - WMS dimensional model types
    # =========================================================================

    class DimensionalModeling:
        """WMS dimensional modeling complex types."""

        type DimensionModel = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type FactModel = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type BridgeModel = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type StarSchema = dict[str, list[dict[str, FlextTypes.JsonValue]]]
        type ScdConfiguration = dict[
            str,
            str | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type GrainDefinition = dict[str, str | list[str]]

    # =========================================================================
    # WMS BUSINESS LOGIC TYPES - Warehouse management business rule types
    # =========================================================================

    class WmsBusinessLogic:
        """WMS business logic complex types."""

        type InventoryRules = dict[
            str,
            bool | str | float | dict[str, FlextTypes.ContainerValue],
        ]
        type AllocationRules = dict[
            str,
            str | int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type PickingRules = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type ReceivingRules = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type ShippingRules = dict[
            str,
            str | int | dict[str, FlextTypes.ContainerValue],
        ]
        type QualityRules = dict[str, bool | float | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle WMS
    # =========================================================================

    class DbtModel:
        """DBT Oracle WMS model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ModelExecution = dict[
            str,
            str | bool | int | dict[str, FlextTypes.ContainerValue],
        ]
        type ModelDependency = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type ModelDocumentation = dict[
            str,
            str | dict[str, FlextTypes.ContainerValue],
        ]
        type ModelMaterialization = dict[
            str,
            str | dict[str, FlextTypes.ContainerValue],
        ]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle WMS
    # =========================================================================

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConnection = dict[
            str,
            FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue],
        ]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SourceFreshness = dict[
            str,
            str | int | dict[str, FlextTypes.ContainerValue],
        ]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ORACLE WMS ADAPTER TYPES - Oracle WMS-specific adapter configuration
    # =========================================================================

    class OracleWmsAdapter:
        """Oracle WMS adapter complex types."""

        type AdapterConfiguration = dict[
            str,
            FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue],
        ]
        type ConnectionAdapter = dict[
            str,
            str | int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SchemaAdapter = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type TransactionAdapter = dict[
            str,
            bool | str | dict[str, FlextTypes.JsonValue],
        ]
        type WmsAdapter = dict[str, str | int | dict[str, FlextTypes.ContainerValue]]

    # =========================================================================
    # PERFORMANCE OPTIMIZATION TYPES - Oracle WMS performance optimization
    # =========================================================================

    class PerformanceOptimization:
        """Oracle WMS performance optimization complex types."""

        type PartitionStrategy = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type IndexStrategy = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type MaterializationStrategy = dict[
            str,
            str | dict[str, FlextTypes.ContainerValue],
        ]
        type CacheStrategy = dict[str, bool | int | dict[str, FlextTypes.JsonValue]]
        type ParallelProcessing = dict[
            str,
            int | bool | dict[str, FlextTypes.ContainerValue],
        ]
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
        type DbtOracleWmsProjectConfig = dict[str, FlextTypes.ContainerValue]
        type WmsTransformConfig = dict[str, str | int | bool | list[str]]
        type WmsAnalyticsConfig = dict[
            str,
            bool | str | dict[str, FlextTypes.ContainerValue],
        ]
        type DbtWmsPipelineConfig = dict[str, FlextTypes.ContainerValue]

    # =========================================================================
    # DBT ORACLE WMS DOMAIN OBJECTS - TypedDict definitions for domain objects
    # =========================================================================

    class DomainObjects:
        """DBT Oracle WMS domain object Pydantic model definitions."""

        # Domain objects using the configurations above


# Moved Pydantic model classes to module level to avoid F821 issues


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
    "DBTOracleWMSAnalysisConfiguration",
    "DBTOracleWMSCompilationConfiguration",
    "DBTOracleWMSDocumentationConfiguration",
    "DBTOracleWMSExecutionConfiguration",
    "DBTOracleWMSMaterialization",
    "DBTOracleWMSProjectConfiguration",
    "DBTOracleWMSRunStatus",
    "DBTOracleWMSSnapshotConfiguration",
    "DBTOracleWMSTestType",
    "FlextDbtOracleWmsTypes",
]
