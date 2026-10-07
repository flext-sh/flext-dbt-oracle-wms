# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._constants.base import FlextDbtOracleWmsConstantsBase
    from flext_dbt_oracle_wms._constants.enums import FlextDbtOracleWmsConstantsEnums


__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsConstantsBase",
    "FlextDbtOracleWmsConstantsEnums",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleWmsConstantsBase": ".base",
        "FlextDbtOracleWmsConstantsEnums": ".enums",
    }),
    public_exports=__all__,
)
