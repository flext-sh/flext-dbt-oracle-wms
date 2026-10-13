"""Boundary protocol contracts composed into the protocols facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms._protocols import (
    FlextDbtOracleWmsProtocolsDbtRunner,
    FlextDbtOracleWmsProtocolsWmsClient,
)


class FlextDbtOracleWmsProtocolsContracts(
    FlextDbtOracleWmsProtocolsDbtRunner,
    FlextDbtOracleWmsProtocolsWmsClient,
):
    """Boundary protocol contracts for the consumed WMS and dbt surfaces."""


__all__: list[str] = ["FlextDbtOracleWmsProtocolsContracts"]
