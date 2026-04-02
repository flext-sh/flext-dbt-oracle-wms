"""Shared service foundation for flext-dbt-oracle-wms components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-oracle-wms domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextSettings
from flext_meltano import FlextMeltanoDbtServiceBase

from flext_dbt_oracle_wms import FlextDbtOracleWmsModels, t


class FlextDbtOracleWmsServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle-wms services.

    Inherits dbt execution infrastructure from FlextMeltanoDbtServiceBase.
    Adds typed settings for the dbt-oracle-wms domain.
    """

    dbt_project_name: t.NonEmptyStr = "dbt-oracle-wms"

    @property
    @override
    def settings(
        self,
    ) -> FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsSettings:
        """Return the typed dbt-oracle-wms settings namespace."""
        return FlextSettings.get_global().get_namespace(
            "dbt_oracle_wms",
            FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsSettings,
        )

    @override
    def get_connection_profile(self) -> t.ContainerMapping:
        """Return dbt connection profile for Oracle WMS."""
        s = self.settings
        return {
            "type": "oracle_wms",
            "environment": s.oracle_wms_environment,
            "base_url": s.oracle_wms_base_url,
            "dbt_target": s.dbt_target,
            "dbt_threads": s.dbt_threads,
            "project": self.dbt_project_name,
        }


__all__ = ["FlextDbtOracleWmsServiceBase"]
