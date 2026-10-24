"""Behavior contract for the dbt Oracle WMS connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_connection_profile
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms import FlextDbtOracleWmsServiceBase, FlextDbtOracleWmsSettings
from tests import m, p, tm


class TestsFlextDbtOracleWmsConnectionProfile:
    """Public contract of the typed dbt Oracle WMS connection profile."""

    @staticmethod
    def test_connection_profile_uses_injected_runtime_settings() -> None:
        """The dbt runner receives the same configuration as the domain workflow."""
        settings = FlextDbtOracleWmsSettings.model_validate({
            "DbtOracleWms": {
                "oracle_wms_base_url": "https://wms.example.com",
                "oracle_wms_environment": "profile-environment",
                "dbt_target": "profile-target",
                "dbt_threads": 7,
            },
        })
        service = FlextDbtOracleWmsServiceBase(settings=settings)

        profile = service.connection_profile
        payload = profile.model_dump(mode="json")

        tm.that(service.settings is settings)
        tm.that(payload["base_url"], eq=settings.DbtOracleWms.oracle_wms_base_url)
        tm.that(payload["environment"], eq=settings.DbtOracleWms.oracle_wms_environment)
        tm.that(payload["target"], eq=settings.DbtOracleWms.dbt_target)
        tm.that(payload["threads"], eq=settings.DbtOracleWms.dbt_threads)
        tm.that(profile.project, eq=service.dbt_project_name)

    @staticmethod
    def test_connection_profile_returns_typed_oracle_wms_wire_shape() -> None:
        """connection_profile returns the typed dbt Oracle WMS wire shape."""
        service = FlextDbtOracleWmsServiceBase()
        profile = service.connection_profile
        settings = service.settings

        tm.that(profile, is_=m.DbtOracleWms.DbtConnectionProfile)
        tm.that(profile, is_=p.Meltano.DbtConnectionProfile)
        tm.that(
            profile.model_dump(mode="json"),
            eq={
                "type": "oracle_wms",
                "base_url": settings.DbtOracleWms.oracle_wms_base_url,
                "environment": settings.DbtOracleWms.oracle_wms_environment,
                "target": settings.DbtOracleWms.dbt_target,
                "threads": settings.DbtOracleWms.dbt_threads,
                "project": service.dbt_project_name,
            },
        )
