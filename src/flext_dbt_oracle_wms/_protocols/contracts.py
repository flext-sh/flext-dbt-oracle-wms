"""Boundary protocol aliases composed into the protocols facade."""

from __future__ import annotations

from .dbt_runner import FlextDbtOracleWmsProtocolsDbtRunner
from .wms_client import FlextDbtOracleWmsProtocolsWmsClient


class FlextDbtOracleWmsProtocolsContracts:
    """Boundary protocol contracts for the consumed WMS and dbt surfaces."""

    type WmsClient = FlextDbtOracleWmsProtocolsWmsClient
    type DbtRunner = FlextDbtOracleWmsProtocolsDbtRunner


__all__: list[str] = ["FlextDbtOracleWmsProtocolsContracts"]
