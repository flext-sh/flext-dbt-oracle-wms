"""Connection and pipeline result models."""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m, u

from flext_dbt_oracle_wms import t


class FlextDbtOracleWmsModelsConnection(m):
    """Connection status and pipeline result models."""

    class ConnectionStatus(m.ImmutableValueModel):
        """Typed Oracle WMS connection status."""

        status: Annotated[str, u.Field(description="Connection status")]
        environment: Annotated[str, u.Field(description="Environment name")]
        base_url: Annotated[str, u.Field(description="Oracle WMS base URL")]
        status_code: Annotated[int, u.Field(description="HTTP status code")]

    class PipelineResult(m.ImmutableValueModel):
        """Typed full pipeline result."""

        processed_entities: Annotated[
            t.StrSequence, u.Field(description="Entities processed by the pipeline")
        ]
        total_records: Annotated[int, u.Field(description="Total records processed")]
        transformation_status: Annotated[
            str, u.Field(description="Transformation status")
        ]
        pipeline_status: Annotated[str, u.Field(description="Overall pipeline status")]


__all__: list[str] = ["FlextDbtOracleWmsModelsConnection"]
