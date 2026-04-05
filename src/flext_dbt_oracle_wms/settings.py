"""FlextDbtOracleWmsSettings - Configuration for flext-dbt-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings


@FlextSettings.auto_register("dbt-oracle-wms")
class FlextDbtOracleWmsSettings(FlextSettings):
    """Runtime configuration for dbt Oracle WMS."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_",
        extra="ignore",
    )


__all__ = ["FlextDbtOracleWmsSettings"]
