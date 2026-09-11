"""WMS item record models."""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_meltano import m, u

from flext_dbt_oracle_wms import t


class FlextDbtOracleWmsModelsItems(m):
    """WMS item models."""

    # NOTE (multi-agent, bead mro-wfc8.3): WmsItem collapses the former identical
    # RawItemRecord + FlextDbtOracleWmsItemDimension (same 3 fields). extra=ignore keeps
    # ingestion tolerant of extra WMS record keys; model_dump() emits the DBT mapping.
    class WmsItem(m.ImmutableValueModel):
        """WMS item record / dimension (single typed model)."""

        model_config: ClassVar[t.ConfigDict] = m.ConfigDict(extra="ignore")

        item_id: Annotated[
            str, u.Field(default="", description="Unique item identifier")
        ]
        item_number: Annotated[
            str, u.Field(default="", description="Item number code")
        ]
        item_description: Annotated[
            str, u.Field(default="", description="Description of the item")
        ]


__all__: list[str] = ["FlextDbtOracleWmsModelsItems"]
