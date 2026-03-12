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

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

from flext_dbt_oracle_wms.constants import c

DBTOracleWMSMaterialization = c.DbtOracleWms.Dbt.Materialization
DBTOracleWMSTestType = c.DbtOracleWms.Dbt.TestType


class FlextDbtOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """DBT Oracle WMS-specific type definitions extending t.

    Domain-specific type system for DBT Oracle WMS data transformation operations.
    Contains ONLY complex DBT Oracle WMS-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class Base:
        """Foundational type aliases for DBT Oracle WMS domain."""

        type EntityId = str
        type ProjectName = str
        type TimeoutSeconds = int
        type TimestampISO = str
        type Version = str
        type CreatedAt = Annotated[datetime, "Timestamp of when entity was created"]
        type UpdatedAt = Annotated[
            datetime, "Timestamp of when entity was last updated"
        ]

    class DbtOracleWms:
        """Oracle WMS specific ID type aliases."""

        type OracleWMSOperationId = str
        type OracleWMSConnectionId = str
        type OracleWMSSchemaId = str
        type OracleWMSQueryId = str

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

    class DbtProject:
        """DBT Oracle WMS project complex types."""

        type ProjectConfiguration = dict[str, object | Mapping[str, object]]
        type ModelConfiguration = dict[str, str | Mapping[str, object]]
        type SourceConfiguration = dict[str, str | list[Mapping[str, object]]]
        type ProfileConfiguration = dict[str, object]
        type MacroConfiguration = dict[str, str | Mapping[str, object]]
        type TestConfiguration = dict[str, str | bool | list[str]]

    class OracleWmsConnection:
        """Oracle WMS connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | Mapping[str, object]]
        type DatabaseConnection = dict[str, str | Mapping[str, object]]
        type PoolingConfig = dict[str, int | bool | Mapping[str, object]]
        type SecurityConfig = dict[str, bool | str | Mapping[str, object]]
        type SessionConfig = dict[str, str | int | Mapping[str, object]]
        type TimeoutConfig = dict[str, int | float]

    class WmsData:
        """Oracle WMS data complex types."""

        type InventoryData = dict[str, str | int | float | Mapping[str, object]]
        type LocationData = dict[str, str | list[str] | Mapping[str, object]]
        type AllocationData = dict[str, str | int | bool | Mapping[str, object]]
        type OrderData = dict[str, str | list[Mapping[str, object]]]
        type TaskData = dict[str, str | int | Mapping[str, object]]
        type ShipmentData = dict[str, str | list[str] | Mapping[str, object]]

    class DbtTransformation:
        """DBT Oracle WMS transformation complex types."""

        type TransformationConfig = dict[str, object | Mapping[str, object]]
        type WmsTransformation = dict[str, str | Mapping[str, object]]
        type DataValidation = dict[str, bool | str | list[str] | Mapping[str, object]]
        type MaterializationConfig = dict[str, str | Mapping[str, object]]
        type OutputFormat = dict[str, str | Mapping[str, object]]
        type ProcessingStep = dict[str, str | int | Mapping[str, object]]

    class DimensionalModeling:
        """WMS dimensional modeling complex types."""

        type DimensionModel = dict[str, str | list[Mapping[str, object]]]
        type FactModel = dict[str, str | Mapping[str, object]]
        type BridgeModel = dict[str, str | list[str] | Mapping[str, object]]
        type StarSchema = dict[str, list[dict[str, object]]]
        type ScdConfiguration = dict[str, str | bool | Mapping[str, object]]
        type GrainDefinition = dict[str, str | list[str]]

    class WmsBusinessLogic:
        """WMS business logic complex types."""

        type InventoryRules = dict[str, bool | str | float | Mapping[str, object]]
        type AllocationRules = dict[str, str | int | bool | Mapping[str, object]]
        type PickingRules = dict[str, str | list[str] | Mapping[str, object]]
        type ReceivingRules = dict[str, bool | str | Mapping[str, object]]
        type ShippingRules = dict[str, str | int | Mapping[str, object]]
        type QualityRules = dict[str, bool | float | Mapping[str, object]]

    class DbtModel:
        """DBT Oracle WMS model complex types."""

        type ModelDefinition = dict[str, str | Mapping[str, object]]
        type ModelExecution = dict[str, str | bool | int | Mapping[str, object]]
        type ModelDependency = dict[str, str | list[str] | Mapping[str, object]]
        type ModelTest = dict[str, str | bool | Mapping[str, object]]
        type ModelDocumentation = dict[str, str | Mapping[str, object]]
        type ModelMaterialization = dict[str, str | Mapping[str, object]]

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[str, str | Mapping[str, object]]
        type SourceConnection = dict[str, object | Mapping[str, object]]
        type SourceTable = dict[str, str | list[Mapping[str, object]]]
        type SourceFreshness = dict[str, str | int | Mapping[str, object]]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[str, str | Mapping[str, object]]

    class OracleWmsAdapter:
        """Oracle WMS adapter complex types."""

        type AdapterConfiguration = dict[str, object | Mapping[str, object]]
        type ConnectionAdapter = dict[str, str | int | bool | Mapping[str, object]]
        type QueryAdapter = dict[str, str | Mapping[str, object]]
        type SchemaAdapter = dict[str, str | list[str] | Mapping[str, object]]
        type TransactionAdapter = dict[str, bool | str | Mapping[str, object]]
        type WmsAdapter = dict[str, str | int | Mapping[str, object]]

    class PerformanceOptimization:
        """Oracle WMS performance optimization complex types."""

        type PartitionStrategy = dict[str, str | list[str] | Mapping[str, object]]
        type IndexStrategy = dict[str, str | bool | Mapping[str, object]]
        type MaterializationStrategy = dict[str, str | Mapping[str, object]]
        type CacheStrategy = dict[str, bool | int | Mapping[str, object]]
        type ParallelProcessing = dict[str, int | bool | Mapping[str, object]]
        type OracleHints = dict[str, str | list[str]]

    class Project:
        """DBT Oracle WMS-specific project types.

        Adds DBT Oracle WMS transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle WMS domain owns Oracle WMS data transformation-specific types.
        """

        type ProjectType = Literal[
            "library",
            "application",
            "service",
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
        type DbtOracleWmsProjectConfig = dict[str, object]
        type WmsTransformConfig = dict[str, str | int | bool | list[str]]
        type WmsAnalyticsConfig = dict[str, bool | str | Mapping[str, object]]
        type DbtWmsPipelineConfig = dict[str, object]

    class DomainObjects:
        """DBT Oracle WMS domain object Pydantic model definitions."""


type DBTOracleWMSAnalysisConfiguration = dict[str, object]
type DBTOracleWMSCompilationConfiguration = dict[str, object]
type DBTOracleWMSDocumentationConfiguration = dict[str, object]
type DBTOracleWMSExecutionConfiguration = dict[str, object]
type DBTOracleWMSProjectConfiguration = dict[str, object]
type DBTOracleWMSSnapshotConfiguration = dict[str, object]
DBTOracleWMSRunStatus = c.DbtOracleWms.DbtOracleWmsProcessing.RunStatus


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
