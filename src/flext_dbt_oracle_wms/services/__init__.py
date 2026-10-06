# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms.services.base import FlextDbtOracleWmsBase
    from flext_dbt_oracle_wms.services.client import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms.services.generation import FlextDbtOracleWmsGeneration
    from flext_dbt_oracle_wms.services.metadata import FlextDbtOracleWmsMetadata
    from flext_dbt_oracle_wms.services.workflow import FlextDbtOracleWmsWorkflow


__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsBase",
    "FlextDbtOracleWmsClient",
    "FlextDbtOracleWmsGeneration",
    "FlextDbtOracleWmsMetadata",
    "FlextDbtOracleWmsWorkflow",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleWmsBase": ".base",
        "FlextDbtOracleWmsClient": ".client",
        "FlextDbtOracleWmsGeneration": ".generation",
        "FlextDbtOracleWmsMetadata": ".metadata",
        "FlextDbtOracleWmsWorkflow": ".workflow",
    }),
    public_exports=__all__,
)
