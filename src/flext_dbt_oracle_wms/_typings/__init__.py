# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms. Typings package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import defer_lazy_bases, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms._typings.base import FlextDbtOracleWmsTypesBase


__all__: tuple[str, ...] = ("FlextDbtOracleWmsTypesBase",)

install_lazy_exports(
    __name__,
    globals(),
    {"FlextDbtOracleWmsTypesBase": ".base"},
    public_exports=__all__,
    deferred_members={
        "FlextDbtOracleWmsTypesBase": (),
    },
)

defer_lazy_bases(
    __name__,
    {
        "FlextDbtOracleWmsTypesBase": (
            ("flext_meltano", "t"),
            ("flext_oracle_wms", "t"),
        ),
    },
)
