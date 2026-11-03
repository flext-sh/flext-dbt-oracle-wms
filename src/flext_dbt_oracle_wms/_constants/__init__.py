# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._constants.base import FlextDbtOracleWmsConstantsBase


__all__: tuple[str, ...] = ("FlextDbtOracleWmsConstantsBase",)

install_lazy_exports(
    __name__,
    globals(),
    {"FlextDbtOracleWmsConstantsBase": ".base"},
    public_exports=__all__,
)
