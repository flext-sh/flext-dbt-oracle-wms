"""Connection and pipeline result models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_models/connection
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated

from flext_meltano import m


class FlextDbtOracleWmsModelsConnection(m):
    """Connection status and pipeline result models."""

    class ConnectionStatus(m.ImmutableValueModel):
        """Typed Oracle WMS connection status."""

        status: Annotated[str, m.Field(description="Connection status")]
        environment: Annotated[str, m.Field(description="Environment name")]
        base_url: Annotated[str, m.Field(description="Oracle WMS base URL")]
        status_code: Annotated[int, m.Field(description="HTTP status code")]

    class PipelineResult(m.ImmutableValueModel):
        """Typed full pipeline result."""

        processed_entities: Annotated[
            Sequence[str],
            m.Field(description="Entities processed by the pipeline"),
        ]
        total_records: Annotated[int, m.Field(description="Total records processed")]
        transformation_status: Annotated[
            str,
            m.Field(description="Transformation status"),
        ]
        pipeline_status: Annotated[str, m.Field(description="Overall pipeline status")]


__all__: list[str] = ["FlextDbtOracleWmsModelsConnection"]
