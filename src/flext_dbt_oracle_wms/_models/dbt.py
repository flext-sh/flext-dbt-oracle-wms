"""DBT model metadata.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_models/dbt
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Annotated

from flext_meltano import m

from flext_dbt_oracle_wms import c


class FlextDbtOracleWmsModelsDbt(m):
    """DBT model metadata namespace."""

    class DbtModel(m.ArbitraryTypesModel):
        """WMS-specific DBT model metadata."""

        name: Annotated[str, m.Field(description="DBT model name")]
        dbt_model_type: Annotated[
            str,
            m.Field(description="DBT model classification"),
        ] = "staging"
        schema_name: Annotated[str, m.Field(description="Target schema name")] = (
            "wms_staging"
        )
        table_name: Annotated[str, m.Field(description="Target table name")]
        materialization: Annotated[
            str,
            m.Field(description="DBT materialization strategy"),
        ] = c.DbtOracleWms.Dbt.Materialization.VIEW.value
        sql_content: Annotated[str, m.Field(description="Model SQL body")]
        description: Annotated[
            str,
            m.Field(description="Human-readable model description"),
        ] = ""
        columns: Annotated[
            Sequence[Mapping[str, str]],
            m.Field(description="Column metadata payloads"),
        ] = m.Field(default_factory=tuple)
        dependencies: Annotated[
            Sequence[str],
            m.Field(description="Upstream model dependencies"),
        ] = m.Field(default_factory=tuple)
        wms_entity_type: Annotated[
            str,
            m.Field(description="Oracle WMS entity represented by this model"),
        ]
        oracle_source: Annotated[
            str,
            m.Field(description="Oracle source for this model"),
        ]
        wms_business_rules: Annotated[
            Sequence[str],
            m.Field(description="WMS-specific business rules attached to the model"),
        ] = m.Field(default_factory=tuple)


__all__: list[str] = ["FlextDbtOracleWmsModelsDbt"]
