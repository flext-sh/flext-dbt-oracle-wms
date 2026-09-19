"""Protocols for DBT Oracle WMS integration points.

Composes the family-part protocols from ``_protocols/`` (base, ``wms_client``,
``dbt_runner``) into the public ``DbtOracleWms`` namespace rather than
re-declaring them inline, eliminating duplication of the contract defined in
``_protocols/base.py``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import p
from flext_oracle_wms import FlextOracleWmsProtocols as oracle_wms_p

from ._protocols.base import FlextDbtOracleWmsProtocolsBase
from ._protocols.dbt_runner import FlextDbtOracleWmsDbtRunner
from ._protocols.wms_client import FlextDbtOracleWmsProtocolsWmsClient


class FlextDbtOracleWmsProtocols(p, oracle_wms_p):
    """Namespace for DBT Oracle WMS protocol contracts.

    Extends :class:`FlextDbtOracleWmsProtocolsBase` (source of truth for
    ``Client`` and ``Service``), composes the Oracle WMS parent contracts, and
    exposes the boundary protocols ``WmsClient`` and ``DbtRunner`` from their
    dedicated family-part modules.
    """

    class DbtOracleWms(
        FlextDbtOracleWmsProtocolsBase.DbtOracleWms,
        oracle_wms_p.OracleWms,
    ):
        """DBT Oracle WMS protocol namespace."""

        WmsClient = FlextDbtOracleWmsProtocolsWmsClient.WmsClient
        DbtRunner = FlextDbtOracleWmsDbtRunner


p = FlextDbtOracleWmsProtocols

__all__: list[str] = ["FlextDbtOracleWmsProtocols", "p"]
