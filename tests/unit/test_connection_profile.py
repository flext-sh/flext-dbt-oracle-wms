"""Behavior contract for the dbt Oracle WMS connection profile."""

from __future__ import annotations

from flext_dbt_oracle_wms import FlextDbtOracleWmsServiceBase, m
from flext_meltano import p


def test_connection_profile_returns_typed_oracle_wms_wire_shape() -> None:
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
