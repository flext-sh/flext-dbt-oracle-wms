"""flext-dbt-oracle-wms config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/dbt_oracle_wms.yaml`` business-rule SSOT.
The ``_config.py`` facade validates the model-less YAML slice into these
classes and exposes the ready objects under ``config.DbtOracleWms``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FlextDbtOracleWmsConfigModels:
    """Namespace of typed flext-dbt-oracle-wms config models."""

    class Dbt(BaseModel):
        """DBT runtime defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        project_name: str = Field(description="DBT project name.")
        threads: int = Field(
            ge=1, description="Number of DBT threads for parallel execution."
        )
        target: str = Field(description="DBT target profile.")
        materialization: str = Field(description="Default DBT materialization.")

    class Defaults(BaseModel):
        """DBT model defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        model_type: str = Field(description="Default model type.")
        schema_name: str = Field(description="Default target schema name.")

    class OracleWms(BaseModel):
        """Oracle WMS integration defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        environment: str = Field(description="Oracle WMS environment.")
        base_url: str = Field(description="Base URL for Oracle WMS API.")

    class Runtime(BaseModel):
        """Runtime behavior defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        performance_recommendation_threshold: int = Field(
            ge=1, description="Threshold for performance recommendations."
        )

    class DbtOracleWms(BaseModel):
        """Root DBT Oracle WMS business-rule namespace."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        dbt: FlextDbtOracleWmsConfigModels.Dbt = Field(
            description="DBT runtime defaults."
        )
        defaults: FlextDbtOracleWmsConfigModels.Defaults = Field(
            description="DBT model defaults."
        )
        oracle_wms: FlextDbtOracleWmsConfigModels.OracleWms = Field(
            description="Oracle WMS integration defaults."
        )
        runtime: FlextDbtOracleWmsConfigModels.Runtime = Field(
            description="Runtime behavior defaults."
        )

    class Root(BaseModel):
        """Root flext-dbt-oracle-wms config validated from ``config/*.yaml``."""

        model_config = ConfigDict(frozen=True, extra="ignore")

        DbtOracleWms: FlextDbtOracleWmsConfigModels.DbtOracleWms = Field(
            description="DBT Oracle WMS business-rule config namespace."
        )


__all__: list[str] = ["FlextDbtOracleWmsConfigModels"]
