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
            datetime, "Timestamp of when entity was last updated"
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

        type ProjectConfiguration = dict[
            str,
            FlextMeltanoTypes.load_python_module.ContainerValue
            | None
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ModelConfiguration = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SourceConfiguration = dict[
            str,
            str
            | list[
                Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None]
            ],
        ]
        type ProfileConfiguration = dict[
            str, FlextMeltanoTypes.load_python_module.ContainerValue | None
        ]
        type MacroConfiguration = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type TestConfiguration = dict[str, str | bool | list[str]]

        type ConnectionConfig = dict[
            str,
            str
            | int
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type DatabaseConnection = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type PoolingConfig = dict[
            str,
            int
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SecurityConfig = dict[
            str,
            bool
            | str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SessionConfig = dict[
            str,
            str
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type TimeoutConfig = dict[str, int | float]

        type InventoryData = dict[
            str,
            str
            | int
            | float
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type LocationData = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type AllocationData = dict[
            str,
            str
            | int
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type OrderData = dict[
            str,
            str
            | list[
                Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None]
            ],
        ]
        type TaskData = dict[
            str,
            str
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ShipmentData = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]

        type TransformationConfig = dict[
            str,
            FlextMeltanoTypes.load_python_module.ContainerValue
            | None
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type WmsTransformation = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type DataValidation = dict[
            str,
            bool
            | str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type MaterializationConfig = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type OutputFormat = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ProcessingStep = dict[
            str,
            str
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]

        type DimensionModel = dict[
            str,
            str
            | list[
                Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None]
            ],
        ]
        type FactModel = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type BridgeModel = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type StarSchema = dict[
            str,
            list[dict[str, FlextMeltanoTypes.load_python_module.ContainerValue | None]],
        ]
        type ScdConfiguration = dict[
            str,
            str
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type GrainDefinition = dict[str, str | list[str]]

        type InventoryRules = dict[
            str,
            bool
            | str
            | float
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type AllocationRules = dict[
            str,
            str
            | int
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type PickingRules = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ReceivingRules = dict[
            str,
            bool
            | str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ShippingRules = dict[
            str,
            str
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type QualityRules = dict[
            str,
            bool
            | float
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]

        type ModelDefinition = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ModelExecution = dict[
            str,
            str
            | bool
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ModelDependency = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ModelTest = dict[
            str,
            str
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ModelDocumentation = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ModelMaterialization = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]

    class DbtSource:
        """DBT Oracle WMS source complex types."""

        type SourceDefinition = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SourceConnection = dict[
            str,
            FlextMeltanoTypes.load_python_module.ContainerValue
            | None
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SourceTable = dict[
            str,
            str
            | list[
                Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None]
            ],
        ]
        type SourceFreshness = dict[
            str,
            str
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]

        type AdapterConfiguration = dict[
            str,
            FlextMeltanoTypes.load_python_module.ContainerValue
            | None
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ConnectionAdapter = dict[
            str,
            str
            | int
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type QueryAdapter = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type SchemaAdapter = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type TransactionAdapter = dict[
            str,
            bool
            | str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type WmsAdapter = dict[
            str,
            str
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]

        type PartitionStrategy = dict[
            str,
            str
            | list[str]
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type IndexStrategy = dict[
            str,
            str
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type MaterializationStrategy = dict[
            str,
            str
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type CacheStrategy = dict[
            str,
            bool
            | int
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type ParallelProcessing = dict[
            str,
            int
            | bool
            | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
        ]
        type OracleHints = dict[str, str | list[str]]

    type ProjectType = c.ProjectType
    type DbtOracleWmsProjectConfig = dict[
        str, FlextMeltanoTypes.load_python_module.ContainerValue | None
    ]
    type WmsTransformConfig = dict[str, str | int | bool | list[str]]
    type WmsAnalyticsConfig = dict[
        str,
        bool
        | str
        | Mapping[str, FlextMeltanoTypes.load_python_module.ContainerValue | None],
    ]
    type DbtWmsPipelineConfig = dict[
        str, FlextMeltanoTypes.load_python_module.ContainerValue | None
    ]


# Facade assignment - enables t.TypeAlias syntax for consumers
t = FlextDbtOracleWmsTypes

__all__ = [
    "FlextDbtOracleWmsTypes",
    "t",
]
