"""FlextDbtOracleWmsSettings - Configuration for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, ClassVar

from flext_core import FlextSettings, m, t, u


@FlextSettings.auto_register("dbt-oracle-wms")
class FlextDbtOracleWmsSettings(FlextSettings):
    """Runtime configuration for dbt Oracle WMS."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_", extra="ignore"
    )

    required_fields_per_entity: Annotated[
        Mapping[str, t.StrSequence],
        u.Field(description="Required fields per WMS entity for validation"),
    ] = u.Field(default_factory=dict)
    oracle_wms_environment: Annotated[
        str,
        u.Field(
            default="development",
            description="Oracle WMS environment (development/production)",
        ),
    ]
    oracle_wms_base_url: Annotated[
        str,
        u.Field(default="", description="Base URL for Oracle WMS API"),
    ]
    dbt_threads: Annotated[
        int,
        u.Field(
            default=4,
            description="Number of DBT threads for parallel execution",
        ),
    ]
    dbt_target: Annotated[
        str,
        u.Field(default="dev", description="DBT target profile (dev/prod)"),
    ]


__all__: list[str] = ["FlextDbtOracleWmsSettings"]
