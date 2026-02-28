"""FLEXT DBT Oracle WMS Domain Types - Centralized type exports from typings.py.

This module re-exports all domain types from the centralized typings.py module.
All type definitions have been moved to typings.py following FLEXT domain separation standards.

Copyright (c) 2025 FLEXT Contributors SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms.typings import (
    t,
)


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
    "DBTOracleWMSAnalysis",
    "DBTOracleWMSCompilation",
    "DBTOracleWMSDocumentation",
    "DBTOracleWMSExecution",
    "DBTOracleWMSMacro",
    "DBTOracleWMSModel",
    "DBTOracleWMSProject",
    "DBTOracleWMSSnapshot",
    "DBTOracleWMSSource",
    "DBTOracleWMSTest",
    "t",
]
