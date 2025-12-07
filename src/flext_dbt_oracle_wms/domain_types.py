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
    DBTOracleWMSAnalysisConfiguration,
    DBTOracleWMSAnalysisTimeout,
    DBTOracleWMSCompilationConfiguration,
    DBTOracleWMSCompilationTimeout,
    DBTOracleWMSDocumentationConfiguration,
    DBTOracleWMSDocumentationTimeout,
    DBTOracleWMSExecutionConfiguration,
    DBTOracleWMSExecutionTimeout,
    DBTOracleWMSMacroTimeout,
    DBTOracleWMSMaterialization,
    DBTOracleWMSModelTimeout,
    DBTOracleWMSProjectConfiguration,
    DBTOracleWMSProjectTimeout,
    DBTOracleWMSRunStatus,
    DBTOracleWMSSnapshotConfiguration,
    DBTOracleWMSSnapshotTimeout,
    DBTOracleWMSSourceTimeout,
    DBTOracleWMSTestTimeout,
    DBTOracleWMSTestType,
    EntityId,
    OracleWMSConnectionId,
    OracleWMSOperationId,
    OracleWMSQueryId,
    OracleWMSSchemaId,
    ProjectName,
    TimeoutSeconds,
    TimestampISO,
    UpdatedAt,
    Version,
    t,
)

# For backward compatibility, expose the TypedDict classes
# These are already imported from typings.py above


# Domain type classes with real inheritance
class DBTOracleWMSProject(t.DomainObjects.DBTOracleWMSProject):
    """DBTOracleWMSProject - real inheritance from DomainObjects.DBTOracleWMSProject."""


class DBTOracleWMSModel(t.DomainObjects.DBTOracleWMSModel):
    """DBTOracleWMSModel - real inheritance from DomainObjects.DBTOracleWMSModel."""


class DBTOracleWMSSource(t.DomainObjects.DBTOracleWMSSource):
    """DBTOracleWMSSource - real inheritance from DomainObjects.DBTOracleWMSSource."""


class DBTOracleWMSTest(t.DomainObjects.DBTOracleWMSTest):
    """DBTOracleWMSTest - real inheritance from DomainObjects.DBTOracleWMSTest."""


class DBTOracleWMSMacro(t.DomainObjects.DBTOracleWMSMacro):
    """DBTOracleWMSMacro - real inheritance from DomainObjects.DBTOracleWMSMacro."""


class DBTOracleWMSSnapshot(t.DomainObjects.DBTOracleWMSSnapshot):
    """DBTOracleWMSSnapshot - real inheritance from DomainObjects.DBTOracleWMSSnapshot."""


class DBTOracleWMSAnalysis(t.DomainObjects.DBTOracleWMSAnalysis):
    """DBTOracleWMSAnalysis - real inheritance from DomainObjects.DBTOracleWMSAnalysis."""


class DBTOracleWMSCompilation(
    t.DomainObjects.DBTOracleWMSCompilation,
):
    """DBTOracleWMSCompilation - real inheritance from DomainObjects.DBTOracleWMSCompilation."""


class DBTOracleWMSExecution(t.DomainObjects.DBTOracleWMSExecution):
    """DBTOracleWMSExecution - real inheritance from DomainObjects.DBTOracleWMSExecution."""


class DBTOracleWMSDocumentation(
    t.DomainObjects.DBTOracleWMSDocumentation,
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
    # Module-level aliases
    "EntityId",
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
    # Core types
    "t",
]
