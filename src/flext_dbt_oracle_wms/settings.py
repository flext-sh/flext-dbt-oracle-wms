"""FlextDbtOracleWmsSettings - Configuration for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextSettings
from flext_dbt_oracle_wms import m


@FlextSettings.auto_register("dbt-oracle-wms")
class FlextDbtOracleWmsSettings(FlextSettings):
    """Runtime configuration for dbt Oracle WMS."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_", extra="ignore"
    )


__all__: list[str] = ["FlextDbtOracleWmsSettings"]
