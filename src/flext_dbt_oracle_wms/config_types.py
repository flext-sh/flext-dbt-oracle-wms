"""Configuration models for DBT Oracle WMS package."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .settings import FlextDbtOracleWmsSettings


class DBTOracleWMSConfiguration(BaseModel):
    """Base configuration for DBT Oracle WMS project."""

    project_name: str = Field(default="flext_dbt_oracle_wms")
    profile: str = Field(default="flext_oracle_wms")


class DBTOracleWMSModelConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT model materialization."""

    materialization: str = Field(default="view")


class DBTOracleWMSSourceConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT source definitions."""

    source_name: str = Field(default="oracle_wms")


class DBTOracleWMSTestConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT test execution."""

    severity: str = Field(default="warn")


class DBTOracleWMSMacroConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT macro namespace."""

    macro_namespace: str = Field(default="wms")


class DBTOracleWMSProfileConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT profile and target."""

    target: str = Field(default="dev")


class FlextDBTOracleWMSSettings(FlextDbtOracleWmsSettings):
    """Settings for FLEXT DBT Oracle WMS integration."""

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
