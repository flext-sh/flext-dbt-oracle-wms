"""Shared service foundation for flext-dbt-oracle-wms components.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoDbtServiceBase

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, c, m, p, t


class FlextDbtOracleWmsServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle-wms services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        m.Field(description="Canonical dbt project name for DBT Oracle WMS services"),
    ] = c.DbtOracleWms.Dbt.PROJECT_NAME

    settings_type: p.SettingsType | None = m.Field(
        default=FlextDbtOracleWmsSettings,
        exclude=True,
        description="Canonical settings owner for DBT Oracle WMS service runtimes.",
    )

    @property
    @override
    def settings(self) -> FlextDbtOracleWmsSettings:
        """The same validated project settings elected by this service runtime.

        Raises:
            TypeError: If a foreign settings owner was injected.

        """
        elected = super().settings
        if not isinstance(elected, FlextDbtOracleWmsSettings):
            msg = "DBT Oracle WMS runtime requires its declared settings owner"
            raise TypeError(msg)
        return elected

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
