"""Configuration models for DBT Oracle WMS package."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .settings import FlextDbtOracleWmsSettings


class DBTOracleWMSConfiguration(BaseModel):
    project_name: str = Field(default="flext_dbt_oracle_wms")
    profile: str = Field(default="flext_oracle_wms")


class DBTOracleWMSModelConfiguration(DBTOracleWMSConfiguration):
    materialization: str = Field(default="view")


class DBTOracleWMSSourceConfiguration(DBTOracleWMSConfiguration):
    source_name: str = Field(default="oracle_wms")


class DBTOracleWMSTestConfiguration(DBTOracleWMSConfiguration):
    severity: str = Field(default="warn")


class DBTOracleWMSMacroConfiguration(DBTOracleWMSConfiguration):
    macro_namespace: str = Field(default="wms")


class DBTOracleWMSProfileConfiguration(DBTOracleWMSConfiguration):
    target: str = Field(default="dev")


class FlextDBTOracleWMSSettings(FlextDbtOracleWmsSettings):
    pass


__all__ = [
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTestConfiguration",
    "FlextDBTOracleWMSSettings",
]
