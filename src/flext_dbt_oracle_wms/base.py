"""Shared service foundation for flext-dbt-oracle-wms components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, c, m, t
from flext_meltano import FlextMeltanoDbtServiceBase, u


class FlextDbtOracleWmsServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle-wms services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT Oracle WMS services"),
    ] = c.DbtOracleWms.Dbt.PROJECT_NAME

    @classmethod
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT Oracle WMS services."""
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtOracleWmsSettings)

    @property
    @override
    def settings(self) -> FlextDbtOracleWmsSettings:
        """The typed dbt-oracle-wms settings namespace."""
        return FlextDbtOracleWmsSettings.fetch_global()

    @property
    @override
    def connection_profile(self) -> t.JsonMapping:
        """Dbt connection profile for Oracle WMS-backed workflows."""
        active_settings = self.settings
        return {
            "type": "oracle_wms",
            "base_url": active_settings.oracle_wms_base_url,
            "environment": active_settings.oracle_wms_environment,
            "target": active_settings.dbt_target,
            "threads": active_settings.dbt_threads,
            "project": self.dbt_project_name,
        }


s = FlextDbtOracleWmsServiceBase

__all__: list[str] = ["FlextDbtOracleWmsServiceBase", "s"]
