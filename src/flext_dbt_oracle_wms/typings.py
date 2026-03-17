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

from collections.abc import Mapping
from datetime import datetime
from typing import Annotated

from flext_core import t
from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

from flext_dbt_oracle_wms import c

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

        type ProjectConfiguration = dict[
            str,
            t.ContainerValue | None | Mapping[str, t.ContainerValue | None],
        ]
        type ModelConfiguration = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type SourceConfiguration = dict[
            str,
            str | list[Mapping[str, t.ContainerValue | None]],
        ]
        type ProfileConfiguration = dict[str, t.ContainerValue | None]
        type MacroConfiguration = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type TestConfiguration = dict[str, str | bool | list[str]]

    class OracleWmsConnection:
        """Oracle WMS connection complex types."""

        type ConnectionConfig = dict[
            str,
            str | int | bool | Mapping[str, t.ContainerValue | None],
        ]
        type DatabaseConnection = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type PoolingConfig = dict[
            str,
            int | bool | Mapping[str, t.ContainerValue | None],
        ]
        type SecurityConfig = dict[
            str,
            bool | str | Mapping[str, t.ContainerValue | None],
        ]
        type SessionConfig = dict[
            str,
            str | int | Mapping[str, t.ContainerValue | None],
        ]
        type TimeoutConfig = dict[str, int | float]

    class WmsData:
        """Oracle WMS data complex types."""

        type InventoryData = dict[
            str,
            str | int | float | Mapping[str, t.ContainerValue | None],
        ]
        type LocationData = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type AllocationData = dict[
            str,
            str | int | bool | Mapping[str, t.ContainerValue | None],
        ]
        type OrderData = dict[
            str,
            str | list[Mapping[str, t.ContainerValue | None]],
        ]
        type TaskData = dict[
            str,
            str | int | Mapping[str, t.ContainerValue | None],
        ]
        type ShipmentData = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]

    class DbtTransformation:
        """DBT Oracle WMS transformation complex types."""

        type TransformationConfig = dict[
            str,
            t.ContainerValue | None | Mapping[str, t.ContainerValue | None],
        ]
        type WmsTransformation = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type DataValidation = dict[
            str,
            bool | str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type MaterializationConfig = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type OutputFormat = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type ProcessingStep = dict[
            str,
            str | int | Mapping[str, t.ContainerValue | None],
        ]

    class DimensionalModeling:
        """WMS dimensional modeling complex types."""

        type DimensionModel = dict[
            str,
            str | list[Mapping[str, t.ContainerValue | None]],
        ]
        type FactModel = dict[str, str | Mapping[str, t.ContainerValue | None]]
        type BridgeModel = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type StarSchema = dict[str, list[dict[str, t.ContainerValue | None]]]
        type ScdConfiguration = dict[
            str,
            str | bool | Mapping[str, t.ContainerValue | None],
        ]
        type GrainDefinition = dict[str, str | list[str]]

    class WmsBusinessLogic:
        """WMS business logic complex types."""

        type InventoryRules = dict[
            str,
            bool | str | float | Mapping[str, t.ContainerValue | None],
        ]
        type AllocationRules = dict[
            str,
            str | int | bool | Mapping[str, t.ContainerValue | None],
        ]
        type PickingRules = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type ReceivingRules = dict[
            str,
            bool | str | Mapping[str, t.ContainerValue | None],
        ]
        type ShippingRules = dict[
            str,
            str | int | Mapping[str, t.ContainerValue | None],
        ]
        type QualityRules = dict[
            str,
            bool | float | Mapping[str, t.ContainerValue | None],
        ]

    class DbtModel:
        """DBT Oracle WMS model complex types."""

        type ModelDefinition = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type ModelExecution = dict[
            str,
            str | bool | int | Mapping[str, t.ContainerValue | None],
        ]
        type ModelDependency = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type ModelTest = dict[
            str,
            str | bool | Mapping[str, t.ContainerValue | None],
        ]
        type ModelDocumentation = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type ModelMaterialization = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type SourceConnection = dict[
            str,
            t.ContainerValue | None | Mapping[str, t.ContainerValue | None],
        ]
        type SourceTable = dict[
            str,
            str | list[Mapping[str, t.ContainerValue | None]],
        ]
        type SourceFreshness = dict[
            str,
            str | int | Mapping[str, t.ContainerValue | None],
        ]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]

    class OracleWmsAdapter:
        """Oracle WMS adapter complex types."""

        type AdapterConfiguration = dict[
            str,
            t.ContainerValue | None | Mapping[str, t.ContainerValue | None],
        ]
        type ConnectionAdapter = dict[
            str,
            str | int | bool | Mapping[str, t.ContainerValue | None],
        ]
        type QueryAdapter = dict[str, str | Mapping[str, t.ContainerValue | None]]
        type SchemaAdapter = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type TransactionAdapter = dict[
            str,
            bool | str | Mapping[str, t.ContainerValue | None],
        ]
        type WmsAdapter = dict[
            str,
            str | int | Mapping[str, t.ContainerValue | None],
        ]

    class PerformanceOptimization:
        """Oracle WMS performance optimization complex types."""

        type PartitionStrategy = dict[
            str,
            str | list[str] | Mapping[str, t.ContainerValue | None],
        ]
        type IndexStrategy = dict[
            str,
            str | bool | Mapping[str, t.ContainerValue | None],
        ]
        type MaterializationStrategy = dict[
            str,
            str | Mapping[str, t.ContainerValue | None],
        ]
        type CacheStrategy = dict[
            str,
            bool | int | Mapping[str, t.ContainerValue | None],
        ]
        type ParallelProcessing = dict[
            str,
            int | bool | Mapping[str, t.ContainerValue | None],
        ]
        type OracleHints = dict[str, str | list[str]]

    class Project:
        """DBT Oracle WMS-specific project types.

        Adds DBT Oracle WMS transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle WMS domain owns Oracle WMS data transformation-specific types.
        """

        type ProjectType = c.ProjectType
        type DbtOracleWmsProjectConfig = dict[str, t.ContainerValue | None]
        type WmsTransformConfig = dict[str, str | int | bool | list[str]]
        type WmsAnalyticsConfig = dict[
            str,
            bool | str | Mapping[str, t.ContainerValue | None],
        ]
        type DbtWmsPipelineConfig = dict[str, t.ContainerValue | None]

    class DomainObjects:
        """DBT Oracle WMS domain object Pydantic model definitions."""


type DBTOracleWMSAnalysisConfiguration = dict[str, t.ContainerValue | None]
type DBTOracleWMSCompilationConfiguration = dict[str, t.ContainerValue | None]
type DBTOracleWMSDocumentationConfiguration = dict[str, t.ContainerValue | None]
type DBTOracleWMSExecutionConfiguration = dict[str, t.ContainerValue | None]
type DBTOracleWMSProjectConfiguration = dict[str, t.ContainerValue | None]
type DBTOracleWMSSnapshotConfiguration = dict[str, t.ContainerValue | None]
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
