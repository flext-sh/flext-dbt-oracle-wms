"""FlextDbtOracleWmsSettings - Configuration for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextDbtOracleWmsSettings(FlextMeltanoSettings):
    """Runtime configuration for dbt Oracle WMS."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_",
        extra="ignore",
    )

    required_fields_per_entity: Annotated[
        dict[str, list[str]],
        Field(description="Required fields per WMS entity for validation"),
    ] = Field(default_factory=dict)
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
            default=4,
            description="Number of DBT threads for parallel execution",
        ),
    ]
    dbt_target: Annotated[
        str,
        Field(default="dev", description="DBT target profile (dev/prod)"),
    ]



settings: FlextDbtOracleWmsSettings = FlextDbtOracleWmsSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_oracle_wms import settings``."""

__all__: list[str] = ["FlextDbtOracleWmsSettings", "settings"]
