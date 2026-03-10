"""Domain types for DBT Oracle WMS project."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import t
from pydantic import BaseModel, Field


class DBTOracleWMSProject(BaseModel):
    """DBT project configuration."""

    name: str = Field(default="flext_dbt_oracle_wms")
    profile: str = Field(default="flext_oracle_wms")


class DBTOracleWMSModel(BaseModel):
    """DBT model definition."""

    name: str = Field(default="")
    materialization: str = Field(default="view")


class DBTOracleWMSSource(BaseModel):
    """DBT source definition."""

    name: str = Field(default="")
    source_schema: Mapping[str, t.ContainerValue] = Field(default_factory=dict)


class DBTOracleWMSTest(BaseModel):
    """DBT test definition."""

    name: str = Field(default="")
    severity: str = Field(default="warn")


class DBTOracleWMSMacro(BaseModel):
    """DBT macro definition."""

    name: str = Field(default="")


class DBTOracleWMSSnapshot(BaseModel):
    """DBT snapshot definition."""

    name: str = Field(default="")


class DBTOracleWMSAnalysis(BaseModel):
    """DBT analysis definition."""

    name: str = Field(default="")


class DBTOracleWMSCompilation(BaseModel):
    """DBT compilation definition."""

    name: str = Field(default="")


class DBTOracleWMSExecution(BaseModel):
    """DBT execution definition."""

    name: str = Field(default="")


class DBTOracleWMSDocumentation(BaseModel):
    """DBT documentation definition."""

    name: str = Field(default="")


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
