"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_dbt_oracle_wms.constants import c
from flext_dbt_oracle_wms.typings import t
from flext_meltano import m, u
from flext_oracle_wms import FlextOracleWmsModels


class FlextDbtOracleWmsModels(m, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms:
        """DBT Oracle WMS domain namespace."""

        # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — typed connection_profile.
        class DbtConnectionProfile(m.ImmutableValueModel):
            """Typed dbt Oracle WMS connection profile (satisfies p.Meltano.DbtConnectionProfile)."""

            type: Annotated[str, u.Field(description="Dbt adapter type identifier")] = (
                "oracle_wms"
            )
            base_url: Annotated[str, u.Field(description="Oracle WMS base URL")]
            environment: Annotated[str, u.Field(description="Oracle WMS environment")]
            target: Annotated[str, u.Field(description="Dbt target profile")]
            threads: Annotated[int, u.Field(description="Dbt parallel threads")]
            project: Annotated[
                str, u.Field(description="Dbt project name owning this profile")
            ]

        class RawItemRecord(m.ImmutableValueModel):
            """Raw item record from Oracle WMS."""

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")

            item_id: Annotated[
                str,
                u.Field(default="", description="Unique item identifier"),
            ]
            item_number: Annotated[
                str,
                u.Field(default="", description="Item number code"),
            ]
            item_description: Annotated[
                str,
                u.Field(default="", description="Description of the item"),
            ]

        class FlextDbtOracleWmsItemDimension(m.ImmutableValueModel):
            """Item dimension model for WMS analytics."""

            item_id: Annotated[
                str,
                u.Field(default="", description="Unique item identifier"),
            ]
            item_number: Annotated[
                str,
                u.Field(default="", description="Item number code"),
            ]
            item_description: Annotated[
                str,
                u.Field(default="", description="Description of the item"),
            ]

            # NOTE (multi-agent, bead mro-wfc8): to_dbt_dict() removed — model_dump()
            # emits the identical DBT-compatible mapping (fields are 1:1); dict helpers
            # do not belong on models (flext-law §2a).

        # NOTE (multi-agent, bead mro-wfc8): FlextDbtOracleWmsTransformer moved to
        # u.DbtOracleWms.Transformer (behavior belongs in utilities, not among models; §2a).

        class DbtModel(m.ArbitraryTypesModel):
            """WMS-specific DBT model metadata."""

            name: Annotated[str, u.Field(description="DBT model name")]
            dbt_model_type: Annotated[
                str,
                u.Field(description="DBT model classification"),
            ] = "staging"
            schema_name: Annotated[
                str,
                u.Field(description="Target schema name"),
            ] = "wms_staging"
            table_name: Annotated[str, u.Field(description="Target table name")]
            materialization: Annotated[
                str,
                u.Field(description="DBT materialization strategy"),
            ] = c.DbtOracleWms.Dbt.Materialization.VIEW.value
            sql_content: Annotated[str, u.Field(description="Model SQL body")]
            description: Annotated[
                str,
                u.Field(description="Human-readable model description"),
            ] = ""
            columns: Annotated[
                t.SequenceOf[t.StrMapping],
                u.Field(description="Column metadata payloads"),
            ] = u.Field(default_factory=tuple)
            dependencies: Annotated[
                t.StrSequence,
                u.Field(description="Upstream model dependencies"),
            ] = u.Field(default_factory=tuple)
            wms_entity_type: Annotated[
                str,
                u.Field(description="Oracle WMS entity represented by this model"),
            ]
            oracle_source: Annotated[
                str,
                u.Field(description="Oracle source for this model"),
            ]
            wms_business_rules: Annotated[
                t.StrSequence,
                u.Field(
                    description="WMS-specific business rules attached to the model",
                ),
            ] = u.Field(default_factory=tuple)

        # NOTE (multi-agent, bead mro-wfc8): ModelGenerator moved to
        # u.DbtOracleWms.ModelBuilder.generate_wms_staging_models (behavior belongs in
        # utilities, not among models; §2a). The unused settings parameter was dropped.

    # NOTE (multi-agent, bead mro-wfc8): create_generator removed with ModelGenerator —
    # callers use u.DbtOracleWms.ModelBuilder.generate_wms_staging_models directly (§2a).


m = FlextDbtOracleWmsModels

__all__: list[str] = ["FlextDbtOracleWmsModels", "m"]
