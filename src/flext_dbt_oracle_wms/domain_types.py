from __future__ import annotations

from collections.abc import Mapping

from flext_core import t
from pydantic import BaseModel, Field


class DBTOracleWMSProject(BaseModel):
    name: str = Field(default="flext_dbt_oracle_wms")
    profile: str = Field(default="flext_oracle_wms")


class DBTOracleWMSModel(BaseModel):
    name: str = Field(default="")
    materialization: str = Field(default="view")


class DBTOracleWMSSource(BaseModel):
    name: str = Field(default="")
    source_schema: Mapping[str, t.ContainerValue] = Field(default_factory=dict)


class DBTOracleWMSTest(BaseModel):
    name: str = Field(default="")
    severity: str = Field(default="warn")


class DBTOracleWMSMacro(BaseModel):
    name: str = Field(default="")


class DBTOracleWMSSnapshot(BaseModel):
    name: str = Field(default="")


class DBTOracleWMSAnalysis(BaseModel):
    name: str = Field(default="")


class DBTOracleWMSCompilation(BaseModel):
    name: str = Field(default="")


class DBTOracleWMSExecution(BaseModel):
    name: str = Field(default="")


class DBTOracleWMSDocumentation(BaseModel):
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
