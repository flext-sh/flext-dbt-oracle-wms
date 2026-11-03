# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_protocols/connection
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols


class FlextDbtOracleWmsProtocolsConnection:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class ConnectionStatus(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def status(self) -> str:
            """Connection status."""
            ...

        @property
        def environment(self) -> str:
            """Environment name."""
            ...

        @property
        def base_url(self) -> str:
            """Oracle WMS base URL."""
            ...

        @property
        def status_code(self) -> int:
            """HTTP status code."""
            ...

    @runtime_checkable
    class PipelineResult(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def processed_entities(self) -> Sequence[str]:
            """Entities processed by the pipeline."""
            ...

        @property
        def total_records(self) -> int:
            """Total records processed."""
            ...

        @property
        def transformation_status(self) -> str:
            """Transformation status."""
            ...

        @property
        def pipeline_status(self) -> str:
            """Overall pipeline status."""
            ...


__all__: list[str] = [
    "FlextDbtOracleWmsProtocolsConnection",
]
