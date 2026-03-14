"""Domain types for DBT Oracle WMS project."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated

from flext_core import t
from pydantic import BaseModel, Field


class DBTOracleWMSProject(BaseModel):
    """DBT project configuration."""

    name: Annotated[str, Field(default="flext_dbt_oracle_wms")]
    profile: Annotated[str, Field(default="flext_oracle_wms")]


class DBTOracleWMSModel(BaseModel):
    """DBT model definition."""

    name: Annotated[str, Field(default="")]
    materialization: Annotated[str, Field(default="view")]


class DBTOracleWMSSource(BaseModel):
    """DBT source definition."""

    name: Annotated[str, Field(default="")]
    source_schema: Annotated[
        Mapping[str, t.ContainerValue | None],
        Field(default_factory=dict),
    ]


class DBTOracleWMSTest(BaseModel):
    """DBT test definition."""

    name: Annotated[str, Field(default="")]
    severity: Annotated[str, Field(default="warn")]


class DBTOracleWMSMacro(BaseModel):
    """DBT macro definition."""

    name: Annotated[str, Field(default="")]


class DBTOracleWMSSnapshot(BaseModel):
    """DBT snapshot definition."""

    name: Annotated[str, Field(default="")]


class DBTOracleWMSAnalysis(BaseModel):
    """DBT analysis definition."""

    name: Annotated[str, Field(default="")]


class DBTOracleWMSCompilation(BaseModel):
    """DBT compilation definition."""

    name: Annotated[str, Field(default="")]


class DBTOracleWMSExecution(BaseModel):
    """DBT execution definition."""

    name: Annotated[str, Field(default="")]


class DBTOracleWMSDocumentation(BaseModel):
    """DBT documentation definition."""

    name: Annotated[str, Field(default="")]


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
