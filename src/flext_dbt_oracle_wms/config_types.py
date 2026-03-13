"""Configuration models for DBT Oracle WMS package."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field

from .settings import FlextDbtOracleWmsSettings


class DBTOracleWMSConfiguration(BaseModel):
    """Base configuration for DBT Oracle WMS project."""

    project_name: Annotated[str, Field(default="flext_dbt_oracle_wms")]
    profile: Annotated[str, Field(default="flext_oracle_wms")]


class DBTOracleWMSModelConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT model materialization."""

    materialization: Annotated[str, Field(default="view")]


class DBTOracleWMSSourceConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT source definitions."""

    source_name: Annotated[str, Field(default="oracle_wms")]


class DBTOracleWMSTestConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT test execution."""

    severity: Annotated[str, Field(default="warn")]


class DBTOracleWMSMacroConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT macro namespace."""

    macro_namespace: Annotated[str, Field(default="wms")]


class DBTOracleWMSProfileConfiguration(DBTOracleWMSConfiguration):
    """Configuration for DBT profile and target."""

    target: Annotated[str, Field(default="dev")]


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
