"""FlextDbtOracleWmsSettings — namespaced under ``settings.DbtOracleWms``.

Universal fields via MRO; project fields in the ``DbtOracleWms`` group with
simple scalar types (env-settable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextDbtOracleWmsSettings(FlextMeltanoSettings):
    """Runtime configuration for dbt Oracle WMS; fields under ``settings.DbtOracleWms.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _DbtOracleWms(BaseModel):
        """Namespaced dbt Oracle WMS settings."""

        required_fields_per_entity: Annotated[
            dict[str, tuple[str, ...]],
            Field(
                default_factory=dict,
                description="Required fields per WMS entity (typed mapping)",
            ),
        ]
        oracle_wms_environment: Annotated[
            str,
            Field(
                default="development",
                description="Oracle WMS environment (development/production)",
            ),
        ]
        oracle_wms_base_url: Annotated[
            str,
            Field(default="", description="Base URL for Oracle WMS API"),
        ]
        dbt_threads: Annotated[
            int,
            Field(
                default=4, description="Number of DBT threads for parallel execution"
            ),
        ]
        dbt_target: Annotated[
            str,
            Field(default="dev", description="DBT target profile (dev/prod)"),
        ]

    if TYPE_CHECKING:
        DbtOracleWms: _DbtOracleWms
    else:
        DbtOracleWms: _DbtOracleWms = Field(
            default_factory=_DbtOracleWms,
            description="Namespaced dbt Oracle WMS settings.",
        )


settings: FlextDbtOracleWmsSettings = FlextDbtOracleWmsSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_oracle_wms import settings``."""

__all__: list[str] = ["FlextDbtOracleWmsSettings", "settings"]
