"""FLEXT DBT Oracle WMS Types - Domain-specific DBT Oracle WMS type definitions.

This module provides DBT Oracle WMS-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# DBT ORACLE WMS-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle WMS operations
# =============================================================================


# DBT Oracle WMS domain TypeVars
class FlextDbtOracleWmsTypes(FlextTypes):
    """DBT Oracle WMS-specific type definitions extending FlextTypes.

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
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
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
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.JsonValue]]
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
            str, str | int | float | dict[str, FlextTypes.JsonValue]
        ]
        type LocationData = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type AllocationData = dict[str, str | int | bool | dict[str, object]]
        type OrderData = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type TaskData = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type ShipmentData = dict[str, str | list[str] | dict[str, object]]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle WMS
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle WMS transformation complex types."""

        type TransformationConfig = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type WmsTransformation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DataValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type MaterializationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type OutputFormat = dict[str, str | dict[str, object]]
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DIMENSIONAL MODELING TYPES - WMS dimensional model types
    # =========================================================================

    class DimensionalModeling:
        """WMS dimensional modeling complex types."""

        type DimensionModel = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type FactModel = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type BridgeModel = dict[str, str | list[str] | dict[str, object]]
        type StarSchema = dict[str, list[dict[str, FlextTypes.JsonValue]]]
        type ScdConfiguration = dict[str, str | bool | dict[str, object]]
        type GrainDefinition = dict[str, str | list[str]]

    # =========================================================================
    # WMS BUSINESS LOGIC TYPES - Warehouse management business rule types
    # =========================================================================

    class WmsBusinessLogic:
        """WMS business logic complex types."""

        type InventoryRules = dict[str, bool | str | float | dict[str, object]]
        type AllocationRules = dict[
            str, str | int | bool | dict[str, FlextTypes.JsonValue]
        ]
        type PickingRules = dict[str, str | list[str] | dict[str, object]]
        type ReceivingRules = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type ShippingRules = dict[str, str | int | dict[str, object]]
        type QualityRules = dict[str, bool | float | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle WMS
    # =========================================================================

    class DbtModel:
        """DBT Oracle WMS model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | dict[str, object]]
        type ModelDependency = dict[str, str | list[str] | dict[str, object]]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type ModelDocumentation = dict[str, str | dict[str, object]]
        type ModelMaterialization = dict[str, str | dict[str, object]]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle WMS
    # =========================================================================

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConnection = dict[str, object | dict[str, object]]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SourceFreshness = dict[str, str | int | dict[str, object]]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ORACLE WMS ADAPTER TYPES - Oracle WMS-specific adapter configuration
    # =========================================================================

    class OracleWmsAdapter:
        """Oracle WMS adapter complex types."""

        type AdapterConfiguration = dict[str, object | dict[str, object]]
        type ConnectionAdapter = dict[str, str | int | bool | dict[str, object]]
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SchemaAdapter = dict[str, str | list[str] | dict[str, object]]
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue]
        ]
        type WmsAdapter = dict[str, str | int | dict[str, object]]

    # =========================================================================
    # PERFORMANCE OPTIMIZATION TYPES - Oracle WMS performance optimization
    # =========================================================================

    class PerformanceOptimization:
        """Oracle WMS performance optimization complex types."""

        type PartitionStrategy = dict[str, str | list[str] | dict[str, object]]
        type IndexStrategy = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type MaterializationStrategy = dict[str, str | dict[str, object]]
        type CacheStrategy = dict[str, bool | int | dict[str, FlextTypes.JsonValue]]
        type ParallelProcessing = dict[str, int | bool | dict[str, object]]
        type OracleHints = dict[str, str | list[str]]

    # =========================================================================
    # DBT ORACLE WMS PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes):
        """DBT Oracle WMS-specific project types extending FlextTypes.

        Adds DBT Oracle WMS transformation-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT Oracle WMS domain owns Oracle WMS data transformation-specific types.
        """

        # DBT Oracle WMS-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes
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


# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle WMS TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtOracleWmsTypes",
]
