"""Boundary protocol aliases composed into the protocols facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_protocols/contracts
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms._protocols.dbt_runner import (
    FlextDbtOracleWmsProtocolsDbtRunner,
)
from flext_dbt_oracle_wms._protocols.wms_client import (
    FlextDbtOracleWmsProtocolsWmsClient,
)


class FlextDbtOracleWmsProtocolsContracts:
    """Boundary protocol contracts for the consumed WMS and dbt surfaces."""

    type WmsClient = FlextDbtOracleWmsProtocolsWmsClient
    type DbtRunner = FlextDbtOracleWmsProtocolsDbtRunner


__all__: list[str] = ["FlextDbtOracleWmsProtocolsContracts"]
