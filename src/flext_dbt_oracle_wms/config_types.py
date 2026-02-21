"""Configuration models for DBT Oracle WMS package."""

from __future__ import annotations

from typing import Literal

from flext_core import FlextSettings, t
from pydantic import BaseModel, ConfigDict, Field


class FlextDBTOracleWMSSettings(FlextSettings):
    """Minimal settings model for DBT Oracle WMS configuration."""

    project_name: str = Field(default="flext-dbt-oracle-wms")
    version: str = Field(default="0.10.0-dev")
    profile: str = Field(default="flext_oracle_wms")
    wms_entities: list[str] = Field(default_factory=lambda: ["inventory", "location"])


class DBTOracleWMSConfiguration(BaseModel):
    """Top-level DBT Oracle WMS configuration payload."""

    model_config = ConfigDict(frozen=False, extra="forbid")
    project_name: str
    version: str
    profile: str


class DBTOracleWMSModelConfiguration(BaseModel):
    """DBT model configuration payload."""

    model_config = ConfigDict(frozen=False, extra="forbid")
    materialized: Literal["table", "view", "incremental"]
    schema_name: str = Field(alias="schema")
    tags: list[str]


class DBTOracleWMSSourceConfiguration(BaseModel):
    """DBT source configuration payload."""

    model_config = ConfigDict(frozen=False, extra="forbid")
    name: str
    schema_name: str = Field(alias="schema")
    tables: list[dict[str, t.GeneralValueType]]


class DBTOracleWMSTestConfiguration(BaseModel):
    """DBT test configuration payload."""

    model_config = ConfigDict(frozen=False, extra="forbid")
    store_failures: bool
    schema_name: str = Field(alias="schema")


class DBTOracleWMSMacroConfiguration(BaseModel):
    """DBT macro configuration payload."""

    model_config = ConfigDict(frozen=False, extra="forbid")
    name: str
    description: str
    arguments: list[str]


class DBTOracleWMSProfileConfiguration(BaseModel):
    """DBT profile configuration payload."""

    model_config = ConfigDict(frozen=False, extra="forbid")
    target: str
    outputs: dict[str, t.GeneralValueType]


__all__ = [
    "DBTOracleWMSConfiguration",
    "DBTOracleWMSMacroConfiguration",
    "DBTOracleWMSModelConfiguration",
    "DBTOracleWMSProfileConfiguration",
    "DBTOracleWMSSourceConfiguration",
    "DBTOracleWMSTestConfiguration",
    "FlextDBTOracleWMSSettings",
]
