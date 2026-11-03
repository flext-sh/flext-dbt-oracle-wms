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
    class DbtModel(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> str:
            """DBT model name."""
            ...

        @property
        def dbt_model_type(self) -> str:
            """DBT model classification."""
            ...

        @property
        def schema_name(self) -> str:
            """Target schema name."""
            ...

        @property
        def table_name(self) -> str:
            """Target table name."""
            ...

        @property
        def materialization(self) -> str:
            """DBT materialization strategy."""
            ...

        @property
        def sql_content(self) -> str:
            """Model SQL body."""
            ...

        @property
        def description(self) -> str:
            """Human-readable model description."""
            ...

        @property
        def columns(self) -> Sequence[Mapping[str, str]]:
            """Column metadata payloads."""
            ...

        @property
        def dependencies(self) -> Sequence[str]:
            """Upstream model dependencies."""
            ...

        @property
        def wms_entity_type(self) -> str:
            """Oracle WMS entity represented by this model."""
            ...

        @property
        def oracle_source(self) -> str:
            """Oracle source for this model."""
            ...

        @property
        def wms_business_rules(self) -> Sequence[str]:
            """WMS-specific business rules attached to the model."""
            ...


__all__: list[str] = [
    "FlextDbtOracleWmsProtocolsDbt",
]
