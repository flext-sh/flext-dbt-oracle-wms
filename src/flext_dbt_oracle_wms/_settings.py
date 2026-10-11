"""FlextDbtOracleWmsSettings — namespaced under ``settings.DbtOracleWms``.

Universal fields via MRO; project fields in the ``DbtOracleWms`` group with
simple scalar types (env-settable).

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_meltano import FlextMeltanoSettings, m, t


class FlextDbtOracleWmsSettings(FlextMeltanoSettings):
    """Runtime configuration for dbt Oracle WMS.

    Fields live under ``settings.DbtOracleWms.*``.
    """

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _DbtOracleWms(m.BaseModel):
        """Namespaced dbt Oracle WMS settings."""

        required_fields_per_entity: Annotated[
            t.MappingKV[str, t.StrSequence],
            m.Field(
                description="Required fields per WMS entity (typed mapping)",
            ),
        ] = m.Field(default_factory=dict)
        oracle_wms_environment: Annotated[
            str,
            m.Field(
                description="Oracle WMS environment (development/production)",
            ),
        ] = "development"
        oracle_wms_base_url: Annotated[
            str, m.Field(description="Base URL for Oracle WMS API")
        ] = ""
        dbt_threads: Annotated[
            int,
            m.Field(
                description="Number of DBT threads for parallel execution",
            ),
        ] = 4
        dbt_target: Annotated[
            str, m.Field(description="DBT target profile (dev/prod)")
        ] = "dev"

    if TYPE_CHECKING:
        DbtOracleWms: _DbtOracleWms
    else:
        DbtOracleWms: _DbtOracleWms = m.Field(
            default_factory=_DbtOracleWms,
            description="Namespaced dbt Oracle WMS settings.",
        )


settings: FlextDbtOracleWmsSettings = FlextDbtOracleWmsSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_oracle_wms``
import ``settings``."""

__all__: list[str] = ["FlextDbtOracleWmsSettings", "settings"]
