"""Shared service foundation for flext-dbt-oracle-wms components.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoDbtServiceBase

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, c, m, p, t, u


class FlextDbtOracleWmsServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle-wms services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT Oracle WMS services"),
    ] = c.DbtOracleWms.Dbt.PROJECT_NAME

    settings_type: t.SettingsClass | None = u.Field(
        default=FlextDbtOracleWmsSettings,
        exclude=True,
        description="Settings class for DBT Oracle WMS services.",
    )

    @classmethod
    def runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT Oracle WMS services."""
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtOracleWmsSettings)

    @property
    @override
    def settings(self) -> FlextDbtOracleWmsSettings:
        """The project's runtime settings without replacement of injected values.

        Raises:
            TypeError: If the runtime settings are not FlextDbtOracleWmsSettings.

        """
        runtime_settings = super().settings
        if not isinstance(runtime_settings, FlextDbtOracleWmsSettings):
            msg = "DBT Oracle WMS services require FlextDbtOracleWmsSettings"
            raise TypeError(msg)
        return runtime_settings

    @property
    @override
    def connection_profile(self) -> p.Meltano.DbtConnectionProfile:
        """Dbt connection profile for Oracle WMS-backed workflows."""
        wms = self.settings.DbtOracleWms
        return m.DbtOracleWms.DbtConnectionProfile(
            base_url=wms.oracle_wms_base_url,
            environment=wms.oracle_wms_environment,
            target=wms.dbt_target,
            threads=wms.dbt_threads,
            project=self.dbt_project_name,
        )


s = FlextDbtOracleWmsServiceBase

__all__: list[str] = ["FlextDbtOracleWmsServiceBase", "s"]
