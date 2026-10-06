# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._models.base import FlextDbtOracleWmsModelsBase
    from flext_dbt_oracle_wms._models.connection import (
        FlextDbtOracleWmsModelsConnection,
    )
    from flext_dbt_oracle_wms._models.dbt import FlextDbtOracleWmsModelsDbt
    from flext_dbt_oracle_wms._models.items import FlextDbtOracleWmsModelsItems
    from flext_dbt_oracle_wms._models.workflow import FlextDbtOracleWmsModelsWorkflow


__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsModelsBase",
    "FlextDbtOracleWmsModelsConnection",
    "FlextDbtOracleWmsModelsDbt",
    "FlextDbtOracleWmsModelsItems",
    "FlextDbtOracleWmsModelsWorkflow",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleWmsModelsBase": ".base",
        "FlextDbtOracleWmsModelsConnection": ".connection",
        "FlextDbtOracleWmsModelsDbt": ".dbt",
        "FlextDbtOracleWmsModelsItems": ".items",
        "FlextDbtOracleWmsModelsWorkflow": ".workflow",
    }),
    public_exports=__all__,
)
