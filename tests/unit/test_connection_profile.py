"""Behavior contract for the dbt Oracle WMS connection profile."""

from __future__ import annotations

from flext_meltano import p

from flext_dbt_oracle_wms import FlextDbtOracleWmsServiceBase, m


class TestsFlextDbtOracleWmsConnectionProfile:
    """Public contract of the typed dbt Oracle WMS connection profile."""

    def test_connection_profile_returns_typed_oracle_wms_wire_shape(self) -> None:
        """connection_profile returns the typed dbt Oracle WMS wire shape."""
        profile = FlextDbtOracleWmsServiceBase().connection_profile

        assert isinstance(profile, m.DbtOracleWms.DbtConnectionProfile)
        assert isinstance(profile, p.Meltano.DbtConnectionProfile)
        assert profile.model_dump() == {
            "type": "oracle_wms",
            "base_url": profile.base_url,
            "environment": profile.environment,
            "target": profile.target,
            "threads": profile.threads,
            "project": profile.project,
        }
