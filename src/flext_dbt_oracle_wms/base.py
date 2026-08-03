"""Shared service foundation for flext-dbt-oracle-wms components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

# NOTE (multi-agent): mro-rn88 — import `settings` singleton for strict `from <pkg> import settings` access.
from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, c, m, settings, t
from flext_meltano import FlextMeltanoDbtServiceBase, p, u


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
    def connection_profile(self) -> p.Meltano.DbtConnectionProfile:
        """Dbt connection profile for Oracle WMS-backed workflows."""
        # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — typed connection_profile.
        wms = settings.DbtOracleWms
        return m.DbtOracleWms.DbtConnectionProfile(
            base_url=wms.oracle_wms_base_url,
            environment=wms.oracle_wms_environment,
            target=wms.dbt_target,
            threads=wms.dbt_threads,
            project=self.dbt_project_name,
        )


s = FlextDbtOracleWmsServiceBase

__all__: list[str] = ["FlextDbtOracleWmsServiceBase", "s"]
