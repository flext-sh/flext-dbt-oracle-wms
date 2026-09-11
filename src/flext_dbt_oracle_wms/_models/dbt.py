"""DBT model metadata."""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m, u

from flext_dbt_oracle_wms import c, t


class FlextDbtOracleWmsModelsDbt(m):
    """DBT model metadata namespace."""

    class DbtOracleWms:
        """DBT Oracle WMS dbt namespace."""

        class DbtModel(m.ArbitraryTypesModel):
            """WMS-specific DBT model metadata."""

            name: Annotated[str, u.Field(description="DBT model name")]
            dbt_model_type: Annotated[
                str, u.Field(description="DBT model classification")
            ] = "staging"
            schema_name: Annotated[str, u.Field(description="Target schema name")] = (
                "wms_staging"
            )
            table_name: Annotated[str, u.Field(description="Target table name")]
            materialization: Annotated[
                str, u.Field(description="DBT materialization strategy")
            ] = c.DbtOracleWms.Dbt.Materialization.VIEW.value
            sql_content: Annotated[str, u.Field(description="Model SQL body")]
            description: Annotated[
                str, u.Field(description="Human-readable model description")
            ] = ""
            columns: Annotated[
                t.SequenceOf[t.StrMapping],
                u.Field(description="Column metadata payloads"),
            ] = u.Field(default_factory=tuple)
            dependencies: Annotated[
                t.StrSequence, u.Field(description="Upstream model dependencies")
            ] = u.Field(default_factory=tuple)
            wms_entity_type: Annotated[
                str, u.Field(description="Oracle WMS entity represented by this model")
            ]
            oracle_source: Annotated[
                str, u.Field(description="Oracle source for this model")
            ]
            wms_business_rules: Annotated[
                t.StrSequence,
                u.Field(
                    description="WMS-specific business rules attached to the model"
                ),
            ] = u.Field(default_factory=tuple)


__all__: list[str] = ["FlextDbtOracleWmsModelsDbt"]
