"""Base utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from flext_meltano import u
from flext_oracle_wms import FlextOracleWmsUtilities


class FlextDbtOracleWmsUtilitiesBase(u, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms:
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""

        PERFORMANCE_RECOMMENDATION_THRESHOLD: int = 20


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesBase"]
