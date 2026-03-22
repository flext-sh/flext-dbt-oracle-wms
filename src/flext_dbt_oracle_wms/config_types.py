"""Configuration models for DBT Oracle WMS package."""

from __future__ import annotations

from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels

# Re-export from models facade
DBTOracleWMSConfiguration = FlextDbtOracleWmsModels.DBTOracleWMSConfiguration
DBTOracleWMSModelConfiguration = FlextDbtOracleWmsModels.DBTOracleWMSModelConfiguration
DBTOracleWMSSourceConfiguration = (
    FlextDbtOracleWmsModels.DBTOracleWMSSourceConfiguration
)
DBTOracleWMSTestConfiguration = FlextDbtOracleWmsModels.DBTOracleWMSTestConfiguration
DBTOracleWMSMacroConfiguration = FlextDbtOracleWmsModels.DBTOracleWMSMacroConfiguration
DBTOracleWMSProfileConfiguration = (
    FlextDbtOracleWmsModels.DBTOracleWMSProfileConfiguration
)
FlextDBTOracleWMSSettings = FlextDbtOracleWmsModels.FlextDBTOracleWMSSettings


__all__ = [
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTestConfiguration",
    "FlextDBTOracleWMSSettings",
]
