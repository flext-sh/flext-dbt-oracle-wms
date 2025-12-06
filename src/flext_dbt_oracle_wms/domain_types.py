"""FLEXT DBT Oracle WMS Domain Types - Centralized type exports from typings.py.

This module re-exports all domain types from the centralized typings.py module.
All type definitions have been moved to typings.py following FLEXT domain separation standards.

Copyright (c) 2025 FLEXT Contributors SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# Import all types from the centralized typings.py module
# Re-export domain objects from typings.py
from flext_dbt_oracle_wms.typings import (
    CreatedAt,
    DBTOracleWMSAnalysisTimeout,
    DBTOracleWMSCompilationTimeout,
    DBTOracleWMSDocumentationTimeout,
    DBTOracleWMSExecutionTimeout,
    DBTOracleWMSMacroTimeout,
    DBTOracleWMSMaterialization,
    DBTOracleWMSModelTimeout,
    DBTOracleWMSProjectTimeout,
    DBTOracleWMSRunStatus,
    DBTOracleWMSSnapshotTimeout,
    DBTOracleWMSSourceTimeout,
    DBTOracleWMSTestTimeout,
    DBTOracleWMSTestType,
    EntityId,
    FlextDbtOracleWmsTypes,
    FlextDbtOracleWmsTypes as DomainObjects,
    OracleWMSConnectionId,
    OracleWMSOperationId,
    OracleWMSQueryId,
    OracleWMSSchemaId,
    ProjectName,
    TimeoutSeconds,
    TimestampISO,
    UpdatedAt,
    Version,
)

# For backward compatibility, expose the TypedDict classes
DBTOracleWMSProjectConfiguration = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSProjectConfiguration
)
DBTOracleWMSSnapshotConfiguration = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSSnapshotConfiguration
)
DBTOracleWMSAnalysisConfiguration = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSAnalysisConfiguration
)
DBTOracleWMSCompilationConfiguration = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSCompilationConfiguration
)
DBTOracleWMSExecutionConfiguration = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSExecutionConfiguration
)
DBTOracleWMSDocumentationConfiguration = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSDocumentationConfiguration
)


# Domain type classes with real inheritance
class DBTOracleWMSProject(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSProject):
    """DBTOracleWMSProject - real inheritance from DomainObjects.DBTOracleWMSProject."""


class DBTOracleWMSModel(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSModel):
    """DBTOracleWMSModel - real inheritance from DomainObjects.DBTOracleWMSModel."""


class DBTOracleWMSSource(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSSource):
    """DBTOracleWMSSource - real inheritance from DomainObjects.DBTOracleWMSSource."""


class DBTOracleWMSTest(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSTest):
    """DBTOracleWMSTest - real inheritance from DomainObjects.DBTOracleWMSTest."""


class DBTOracleWMSMacro(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSMacro):
    """DBTOracleWMSMacro - real inheritance from DomainObjects.DBTOracleWMSMacro."""


class DBTOracleWMSSnapshot(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSSnapshot):
    """DBTOracleWMSSnapshot - real inheritance from DomainObjects.DBTOracleWMSSnapshot."""


class DBTOracleWMSAnalysis(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSAnalysis):
    """DBTOracleWMSAnalysis - real inheritance from DomainObjects.DBTOracleWMSAnalysis."""


class DBTOracleWMSCompilation(
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSCompilation,
):
    """DBTOracleWMSCompilation - real inheritance from DomainObjects.DBTOracleWMSCompilation."""


class DBTOracleWMSExecution(FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSExecution):
    """DBTOracleWMSExecution - real inheritance from DomainObjects.DBTOracleWMSExecution."""


class DBTOracleWMSDocumentation(
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSDocumentation,
):
    """DBTOracleWMSDocumentation - real inheritance from DomainObjects.DBTOracleWMSDocumentation."""


# ==============================================================================
# EXPORTS - All types now centralized in typings.py
# ==============================================================================


__all__: list[str] = [
    "CreatedAt",
    # Domain objects
    "DBTOracleWMSAnalysis",
    "DBTOracleWMSAnalysisConfiguration",
    "DBTOracleWMSAnalysisTimeout",
    "DBTOracleWMSCompilation",
    "DBTOracleWMSCompilationConfiguration",
    "DBTOracleWMSCompilationTimeout",
    "DBTOracleWMSDocumentation",
    "DBTOracleWMSDocumentationConfiguration",
    "DBTOracleWMSDocumentationTimeout",
    "DBTOracleWMSExecution",
    "DBTOracleWMSExecutionConfiguration",
    "DBTOracleWMSExecutionTimeout",
    "DBTOracleWMSMacro",
    "DBTOracleWMSMacroTimeout",
    # Enums
    "DBTOracleWMSMaterialization",
    "DBTOracleWMSModel",
    "DBTOracleWMSModelTimeout",
    "DBTOracleWMSProject",
    "DBTOracleWMSProjectConfiguration",
    "DBTOracleWMSProjectTimeout",
    "DBTOracleWMSRunStatus",
    "DBTOracleWMSSnapshot",
    "DBTOracleWMSSnapshotConfiguration",
    "DBTOracleWMSSnapshotTimeout",
    "DBTOracleWMSSource",
    "DBTOracleWMSSourceTimeout",
    "DBTOracleWMSTest",
    "DBTOracleWMSTestTimeout",
    "DBTOracleWMSTestType",
    "DomainObjects",
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
]
