# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_protocols/items
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols


class FlextDbtOracleWmsProtocolsItems:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class WmsItem(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def item_id(self) -> str:
            """Unique item identifier."""
            ...

        @property
        def item_number(self) -> str:
            """Item number code."""
            ...

        @property
        def item_description(self) -> str:
            """Description of the item."""
            ...


__all__: list[str] = [
    "FlextDbtOracleWmsProtocolsItems",
]
