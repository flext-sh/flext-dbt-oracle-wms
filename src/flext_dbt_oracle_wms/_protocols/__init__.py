# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import defer_lazy_bases, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._protocols.base import FlextDbtOracleWmsProtocolsBase
    from flext_dbt_oracle_wms._protocols.connection import (
        FlextDbtOracleWmsProtocolsConnection,
    )
    from flext_dbt_oracle_wms._protocols.contracts import (
        FlextDbtOracleWmsProtocolsContracts,
    )
    from flext_dbt_oracle_wms._protocols.dbt import FlextDbtOracleWmsProtocolsDbt
    from flext_dbt_oracle_wms._protocols.dbt_runner import (
        FlextDbtOracleWmsProtocolsDbtRunner,
    )
    from flext_dbt_oracle_wms._protocols.items import FlextDbtOracleWmsProtocolsItems
    from flext_dbt_oracle_wms._protocols.wms_client import (
        FlextDbtOracleWmsProtocolsWmsClient,
    )
    from flext_dbt_oracle_wms._protocols.workflow import (
        FlextDbtOracleWmsProtocolsWorkflow,
    )


__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsProtocolsBase",
    "FlextDbtOracleWmsProtocolsConnection",
    "FlextDbtOracleWmsProtocolsContracts",
    "FlextDbtOracleWmsProtocolsDbt",
    "FlextDbtOracleWmsProtocolsDbtRunner",
    "FlextDbtOracleWmsProtocolsItems",
    "FlextDbtOracleWmsProtocolsWmsClient",
    "FlextDbtOracleWmsProtocolsWorkflow",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextDbtOracleWmsProtocolsBase": ".base",
        "FlextDbtOracleWmsProtocolsConnection": ".connection",
        "FlextDbtOracleWmsProtocolsContracts": ".contracts",
        "FlextDbtOracleWmsProtocolsDbt": ".dbt",
        "FlextDbtOracleWmsProtocolsDbtRunner": ".dbt_runner",
        "FlextDbtOracleWmsProtocolsItems": ".items",
        "FlextDbtOracleWmsProtocolsWmsClient": ".wms_client",
        "FlextDbtOracleWmsProtocolsWorkflow": ".workflow",
    },
    public_exports=__all__,
    deferred_members={
        "FlextDbtOracleWmsProtocolsBase": (
            "DbtOracleWms",
            "DbtConnectionProfile",
        ),
        "FlextDbtOracleWmsProtocolsConnection": (
            "ConnectionStatus",
            "PipelineResult",
        ),
        "FlextDbtOracleWmsProtocolsContracts": (),
        "FlextDbtOracleWmsProtocolsDbt": ("DbtModel",),
        "FlextDbtOracleWmsProtocolsDbtRunner": ("DbtRunner",),
        "FlextDbtOracleWmsProtocolsItems": ("WmsItem",),
        "FlextDbtOracleWmsProtocolsWmsClient": ("WmsClient",),
        "FlextDbtOracleWmsProtocolsWorkflow": (
            "EntityTransformationSet",
            "TransformationResult",
            "WorkflowTracking",
            "WorkflowRecommendation",
            "WmsMetadataResult",
            "DbtModelGenerationResult",
            "WorkflowResult",
            "DbtExecutionResult",
        ),
    },
)

defer_lazy_bases(
    __name__,
    {
        "FlextDbtOracleWmsProtocolsContracts": (
            (".", "FlextDbtOracleWmsProtocolsDbtRunner"),
            (".", "FlextDbtOracleWmsProtocolsWmsClient"),
        ),
    },
)
