"""FLEXT DBT Oracle WMS Types - Domain-specific DBT Oracle WMS type definitions.

This module provides DBT Oracle WMS-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# DBT ORACLE WMS-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle WMS operations
# =============================================================================


# DBT Oracle WMS domain TypeVars
class FlextDbtOracleWmsTypes(FlextCore.Types):
    """DBT Oracle WMS-specific type definitions extending FlextCore.Types.

    Domain-specific type system for DBT Oracle WMS data transformation operations.
    Contains ONLY complex DBT Oracle WMS-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types for Oracle WMS
    # =========================================================================

    class DbtProject:
        """DBT Oracle WMS project complex types."""

        type ProjectConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type ModelConfiguration = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SourceConfiguration = dict[str, str | list[FlextCore.Types.Dict]]
        type ProfileConfiguration = dict[str, FlextCore.Types.ConfigValue]
        type MacroConfiguration = dict[str, str | FlextCore.Types.Dict]
        type TestConfiguration = dict[str, str | bool | FlextCore.Types.StringList]

    # =========================================================================
    # ORACLE WMS CONNECTION TYPES - Oracle WMS database connection configuration
    # =========================================================================

    class OracleWmsConnection:
        """Oracle WMS connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | FlextCore.Types.Dict]
        type DatabaseConnection = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type PoolingConfig = dict[str, int | bool | FlextCore.Types.Dict]
        type SecurityConfig = dict[
            str, bool | str | dict[str, FlextCore.Types.ConfigValue]
        ]
        type SessionConfig = dict[str, str | int | FlextCore.Types.Dict]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # WMS DATA TYPES - Oracle WMS warehouse management data types
    # =========================================================================

    class WmsData:
        """Oracle WMS data complex types."""

        type InventoryData = dict[
            str, str | int | float | dict[str, FlextCore.Types.JsonValue]
        ]
        type LocationData = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type AllocationData = dict[str, str | int | bool | FlextCore.Types.Dict]
        type OrderData = dict[str, str | list[dict[str, FlextCore.Types.JsonValue]]]
        type TaskData = dict[str, str | int | dict[str, FlextCore.Types.JsonValue]]
        type ShipmentData = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle WMS
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle WMS transformation complex types."""

        type TransformationConfig = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type WmsTransformation = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type DataValidation = dict[
            str, bool | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type MaterializationConfig = dict[
            str, str | dict[str, FlextCore.Types.JsonValue]
        ]
        type OutputFormat = dict[str, str | FlextCore.Types.Dict]
        type ProcessingStep = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # DIMENSIONAL MODELING TYPES - WMS dimensional model types
    # =========================================================================

    class DimensionalModeling:
        """WMS dimensional modeling complex types."""

        type DimensionModel = dict[
            str, str | list[dict[str, FlextCore.Types.JsonValue]]
        ]
        type FactModel = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type BridgeModel = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type StarSchema = dict[str, list[dict[str, FlextCore.Types.JsonValue]]]
        type ScdConfiguration = dict[str, str | bool | FlextCore.Types.Dict]
        type GrainDefinition = dict[str, str | FlextCore.Types.StringList]

    # =========================================================================
    # WMS BUSINESS LOGIC TYPES - Warehouse management business rule types
    # =========================================================================

    class WmsBusinessLogic:
        """WMS business logic complex types."""

        type InventoryRules = dict[str, bool | str | float | FlextCore.Types.Dict]
        type AllocationRules = dict[
            str, str | int | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type PickingRules = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type ReceivingRules = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type ShippingRules = dict[str, str | int | FlextCore.Types.Dict]
        type QualityRules = dict[
            str, bool | float | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle WMS
    # =========================================================================

    class DbtModel:
        """DBT Oracle WMS model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | FlextCore.Types.Dict]
        type ModelDependency = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type ModelTest = dict[str, str | bool | dict[str, FlextCore.Types.JsonValue]]
        type ModelDocumentation = dict[str, str | FlextCore.Types.Dict]
        type ModelMaterialization = dict[
            str, str | dict[str, FlextCore.Types.ConfigValue]
        ]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle WMS
    # =========================================================================

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SourceConnection = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type SourceTable = dict[str, str | list[dict[str, FlextCore.Types.JsonValue]]]
        type SourceFreshness = dict[str, str | int | FlextCore.Types.Dict]
        type SourceTest = dict[str, str | bool | FlextCore.Types.StringList]
        type SourceSchema = dict[str, str | dict[str, FlextCore.Types.JsonValue]]

    # =========================================================================
    # ORACLE WMS ADAPTER TYPES - Oracle WMS-specific adapter configuration
    # =========================================================================

    class OracleWmsAdapter:
        """Oracle WMS adapter complex types."""

        type AdapterConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type ConnectionAdapter = dict[str, str | int | bool | FlextCore.Types.Dict]
        type QueryAdapter = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SchemaAdapter = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type WmsAdapter = dict[str, str | int | FlextCore.Types.Dict]

    # =========================================================================
    # PERFORMANCE OPTIMIZATION TYPES - Oracle WMS performance optimization
    # =========================================================================

    class PerformanceOptimization:
        """Oracle WMS performance optimization complex types."""

        type PartitionStrategy = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type IndexStrategy = dict[
            str, str | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type MaterializationStrategy = dict[str, str | FlextCore.Types.Dict]
        type CacheStrategy = dict[
            str, bool | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type ParallelProcessing = dict[str, int | bool | FlextCore.Types.Dict]
        type OracleHints = dict[str, str | FlextCore.Types.StringList]

    # =========================================================================
    # DBT ORACLE WMS PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """DBT Oracle WMS-specific project types extending FlextCore.Types.Project.

        Adds DBT Oracle WMS transformation-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        DBT Oracle WMS domain owns Oracle WMS data transformation-specific types.
        """

        # DBT Oracle WMS-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
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
        type DbtOracleWmsProjectConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type WmsTransformConfig = dict[
            str, str | int | bool | FlextCore.Types.StringList
        ]
        type WmsAnalyticsConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type DbtWmsPipelineConfig = dict[str, FlextCore.Types.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle WMS TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextDbtOracleWmsTypes",
]
