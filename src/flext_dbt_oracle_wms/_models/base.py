"""Base domain models for DBT Oracle WMS — connection profiles and core types."""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m, u
from flext_oracle_wms import FlextOracleWmsModels


class FlextDbtOracleWmsModelsBase(m, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms:
        """DBT Oracle WMS domain namespace."""

        # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — typed connection_profile.
        class DbtConnectionProfile(m.ImmutableValueModel):
            """Typed dbt Oracle WMS connection profile (satisfies p.Meltano.DbtConnectionProfile)."""

            type: Annotated[str, u.Field(description="Dbt adapter type identifier")] = (
                "oracle_wms"
            )
            base_url: Annotated[str, u.Field(description="Oracle WMS base URL")]
            environment: Annotated[str, u.Field(description="Oracle WMS environment")]
            target: Annotated[str, u.Field(description="Dbt target profile")]
            threads: Annotated[int, u.Field(description="Dbt parallel threads")]
            project: Annotated[
                str, u.Field(description="Dbt project name owning this profile")
            ]


__all__: list[str] = ["FlextDbtOracleWmsModelsBase"]
