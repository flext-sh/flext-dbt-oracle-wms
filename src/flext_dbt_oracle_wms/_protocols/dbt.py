# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_protocols/dbt
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols


class FlextDbtOracleWmsProtocolsDbt:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtModel(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        name: str
        dbt_model_type: str
        schema_name: str
        table_name: str
        materialization: str
        sql_content: str
        description: str
        columns: Sequence[Mapping[str, str]]
        dependencies: Sequence[str]
        wms_entity_type: str
        oracle_source: str
        wms_business_rules: Sequence[str]


__all__: list[str] = [
    "FlextDbtOracleWmsProtocolsDbt",
]
