"""Domain types for DBT Oracle WMS project."""

from __future__ import annotations

from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels


# Re-export from models facade
DBTOracleWMSProject = FlextDbtOracleWmsModels.DBTOracleWMSProject
DBTOracleWMSModel = FlextDbtOracleWmsModels.DBTOracleWMSModel
DBTOracleWMSSource = FlextDbtOracleWmsModels.DBTOracleWMSSource
DBTOracleWMSTest = FlextDbtOracleWmsModels.DBTOracleWMSTest
DBTOracleWMSMacro = FlextDbtOracleWmsModels.DBTOracleWMSMacro
DBTOracleWMSSnapshot = FlextDbtOracleWmsModels.DBTOracleWMSSnapshot
DBTOracleWMSAnalysis = FlextDbtOracleWmsModels.DBTOracleWMSAnalysis
DBTOracleWMSCompilation = FlextDbtOracleWmsModels.DBTOracleWMSCompilation
DBTOracleWMSExecution = FlextDbtOracleWmsModels.DBTOracleWMSExecution
DBTOracleWMSDocumentation = FlextDbtOracleWmsModels.DBTOracleWMSDocumentation


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
]
