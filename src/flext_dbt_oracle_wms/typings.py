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

from collections.abc import Mapping, Sequence
from datetime import datetime
from typing import Annotated

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

from flext_dbt_oracle_wms import c


class FlextDbtOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """DBT Oracle WMS-specific type definitions extending t.

    Domain-specific type system for DBT Oracle WMS data transformation operations.
    Contains ONLY complex DBT Oracle WMS-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class DbtOracleWms:
        """Oracle WMS specific ID type aliases."""

        type OracleWMSOperationId = str
        type OracleWMSConnectionId = str
        type OracleWMSSchemaId = str
        type OracleWMSQueryId = str

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

        type ProjectConfiguration = Mapping[
            str,
            FlextOracleWmsTypes.ContainerValue
            | None
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ModelConfiguration = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type SourceConfiguration = Mapping[
            str,
            str | Sequence[Mapping[str, FlextOracleWmsTypes.ContainerValue | None]],
        ]
        type ProfileConfiguration = Mapping[
            str,
            FlextOracleWmsTypes.ContainerValue | None,
        ]
        type MacroConfiguration = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type TestConfiguration = Mapping[
            str,
            str | bool | FlextOracleWmsTypes.StrSequence,
        ]

        type ConnectionConfig = Mapping[
            str,
            FlextOracleWmsTypes.Scalar
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type DatabaseConnection = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type PoolingConfig = Mapping[
            str,
            int | bool | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type SecurityConfig = Mapping[
            str,
            bool | str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type SessionConfig = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type TimeoutConfig = Mapping[str, int | float]

        type InventoryData = Mapping[
            str,
            str | int | float | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type LocationData = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type AllocationData = Mapping[
            str,
            FlextOracleWmsTypes.Scalar
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type OrderData = Mapping[
            str,
            str | Sequence[Mapping[str, FlextOracleWmsTypes.ContainerValue | None]],
        ]
        type TaskData = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ShipmentData = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]

        type TransformationConfig = Mapping[
            str,
            FlextOracleWmsTypes.ContainerValue
            | None
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type WmsTransformation = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type DataValidation = Mapping[
            str,
            bool
            | str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type MaterializationConfig = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type OutputFormat = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ProcessingStep = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]

        type DimensionModel = Mapping[
            str,
            str | Sequence[Mapping[str, FlextOracleWmsTypes.ContainerValue | None]],
        ]
        type FactModel = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type BridgeModel = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type StarSchema = Mapping[
            str,
            Sequence[Mapping[str, FlextOracleWmsTypes.ContainerValue | None]],
        ]
        type ScdConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type GrainDefinition = Mapping[str, str | FlextOracleWmsTypes.StrSequence]

        type InventoryRules = Mapping[
            str,
            bool
            | str
            | float
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type AllocationRules = Mapping[
            str,
            FlextOracleWmsTypes.Scalar
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type PickingRules = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ReceivingRules = Mapping[
            str,
            bool | str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ShippingRules = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type QualityRules = Mapping[
            str,
            bool | float | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]

        type ModelDefinition = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ModelExecution = Mapping[
            str,
            str | bool | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ModelDependency = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ModelTest = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ModelDocumentation = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type ModelMaterialization = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]

        class DbtSource:
            """DBT Oracle WMS source complex types."""

            type SourceDefinition = Mapping[
                str,
                str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type SourceConnection = Mapping[
                str,
                FlextOracleWmsTypes.ContainerValue
                | None
                | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type SourceTable = Mapping[
                str,
                str | Sequence[Mapping[str, FlextOracleWmsTypes.ContainerValue | None]],
            ]
            type SourceFreshness = Mapping[
                str,
                str | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type SourceTest = Mapping[str, str | bool | FlextOracleWmsTypes.StrSequence]
            type SourceSchema = Mapping[
                str,
                str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]

            type AdapterConfiguration = Mapping[
                str,
                FlextOracleWmsTypes.ContainerValue
                | None
                | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type ConnectionAdapter = Mapping[
                str,
                FlextOracleWmsTypes.Scalar
                | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type QueryAdapter = Mapping[
                str,
                str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type SchemaAdapter = Mapping[
                str,
                str
                | FlextOracleWmsTypes.StrSequence
                | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type TransactionAdapter = Mapping[
                str,
                bool | str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type WmsAdapter = Mapping[
                str,
                str | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]

            type PartitionStrategy = Mapping[
                str,
                str
                | FlextOracleWmsTypes.StrSequence
                | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type IndexStrategy = Mapping[
                str,
                str | bool | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type MaterializationStrategy = Mapping[
                str,
                str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type CacheStrategy = Mapping[
                str,
                bool | int | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type ParallelProcessing = Mapping[
                str,
                int | bool | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
            ]
            type OracleHints = Mapping[str, str | FlextOracleWmsTypes.StrSequence]

        type ProjectType = c.DbtOracleWms.ProjectType
        type DbtOracleWmsProjectConfig = Mapping[
            str,
            FlextOracleWmsTypes.ContainerValue | None,
        ]
        type WmsTransformConfig = Mapping[
            str,
            FlextOracleWmsTypes.Scalar | FlextOracleWmsTypes.StrSequence,
        ]
        type WmsAnalyticsConfig = Mapping[
            str,
            bool | str | Mapping[str, FlextOracleWmsTypes.ContainerValue | None],
        ]
        type DbtWmsPipelineConfig = Mapping[
            str, FlextOracleWmsTypes.ContainerValue | None
        ]


# Facade assignment - enables t.TypeAlias syntax for consumers
t = FlextDbtOracleWmsTypes

__all__ = [
    "FlextDbtOracleWmsTypes",
    "t",
]
