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

DBTOracleWMSProject = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSProject
DBTOracleWMSModel = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSModel
DBTOracleWMSSource = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSSource
DBTOracleWMSTest = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSTest
DBTOracleWMSMacro = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSMacro
DBTOracleWMSSnapshot = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSSnapshot
DBTOracleWMSAnalysis = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSAnalysis
DBTOracleWMSCompilation = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSCompilation
DBTOracleWMSExecution = FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSExecution
DBTOracleWMSDocumentation = (
    FlextDbtOracleWmsTypes.DomainObjects.DBTOracleWMSDocumentation
)

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
