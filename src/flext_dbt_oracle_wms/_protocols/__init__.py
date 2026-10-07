# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._protocols.base import FlextDbtOracleWmsProtocolsBase
    from flext_dbt_oracle_wms._protocols.contracts import (
        FlextDbtOracleWmsProtocolsContracts,
    )
    from flext_dbt_oracle_wms._protocols.dbt_runner import (
        FlextDbtOracleWmsProtocolsDbtRunner,
    )
    from flext_dbt_oracle_wms._protocols.wms_client import (
        FlextDbtOracleWmsProtocolsWmsClient,
    )


__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsProtocolsBase",
    "FlextDbtOracleWmsProtocolsContracts",
    "FlextDbtOracleWmsProtocolsDbtRunner",
    "FlextDbtOracleWmsProtocolsWmsClient",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleWmsProtocolsBase": ".base",
        "FlextDbtOracleWmsProtocolsContracts": ".contracts",
        "FlextDbtOracleWmsProtocolsDbtRunner": ".dbt_runner",
        "FlextDbtOracleWmsProtocolsWmsClient": ".wms_client",
    }),
    public_exports=__all__,
)
