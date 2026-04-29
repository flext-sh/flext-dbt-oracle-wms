"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from collections.abc import (
    Mapping,
    MutableSequence,
    Sequence,
)
from typing import Annotated, ClassVar

from flext_core import FlextSettings, p, r, u
from flext_dbt_oracle_wms.constants import c
from flext_dbt_oracle_wms.typings import t
from flext_meltano import m
from flext_oracle_wms import FlextOracleWmsModels


class FlextDbtOracleWmsModels(m, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms:
        """DBT Oracle WMS domain namespace."""

        class RawItemRecord(m.Value):
            """Raw item record from Oracle WMS."""

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")

            item_id: Annotated[
                str, u.Field(default="", description="Unique item identifier")
            ]
            item_number: Annotated[
                str, u.Field(default="", description="Item number code")
            ]
            item_description: Annotated[
                str, u.Field(default="", description="Description of the item")
            ]

        class FlextDbtOracleWmsItemDimension(m.Value):
            """Item dimension model for WMS analytics."""

            item_id: Annotated[
                str, u.Field(default="", description="Unique item identifier")
            ]
            item_number: Annotated[
                str, u.Field(default="", description="Item number code")
            ]
            item_description: Annotated[
                str, u.Field(default="", description="Description of the item")
            ]

            def to_dbt_dict(self) -> t.ConfigurationMapping:
                """Convert item dimension to DBT-compatible dictionary."""
                return {
                    "item_id": self.item_id,
                    "item_number": self.item_number,
                    "item_description": self.item_description,
                }

        class FlextDbtOracleWmsTransformer:
            """Transformer for WMS entity data to DBT models."""

            def transform_all_entities(
                self,
                entity_data: Mapping[str, Sequence[t.ConfigurationMapping]],
            ) -> Mapping[str, Sequence[t.ConfigurationMapping]]:
                """Transform all WMS entities to DBT-compatible format."""
                items: Sequence[
                    FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsItemDimension
                ] = self.transform_items(entity_data.get("items", []))
                return {"items": [item.to_dbt_dict() for item in items]}

            def transform_items(
                self,
                records: Sequence[t.ConfigurationMapping],
            ) -> Sequence[
                FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsItemDimension
            ]:
                """Transform item records to item dimension models."""
                transformed: MutableSequence[
                    FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsItemDimension
                ] = []
                for record in records:
                    try:
                        raw_record = FlextDbtOracleWmsModels.DbtOracleWms.RawItemRecord.model_validate(
                            record,
                        )
                    except c.ValidationError:
                        continue
                    transformed.append(
                        FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsItemDimension(
                            item_id=raw_record.item_id,
                            item_number=raw_record.item_number,
                            item_description=raw_record.item_description,
                        )
                    )
                return transformed

            def validate_business_rules(
                self,
                records: Sequence[t.ConfigurationMapping],
            ) -> p.Result[bool]:
                """Validate business rules for WMS records."""
                if not records:
                    return r[bool].fail("No records to validate")
                return r[bool].ok(True)

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
                Sequence[t.StrMapping],
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
                    description="WMS-specific business rules attached to the model"
                ),
            ] = u.Field(default_factory=tuple)

        class ModelGenerator:
            """Generator for lightweight DBT model objects."""

            def __init__(self, settings: t.StrMapping | None = None) -> None:
                """Store optional generation-time configuration."""
                super().__init__()
                self.settings = settings or {}

            def generate_wms_staging_models(
                self,
                oracle_sources: t.StrSequence,
            ) -> p.Result[Sequence[FlextDbtOracleWmsModels.DbtOracleWms.DbtModel]]:
                """Create one staging model per source name."""
                models = [
                    FlextDbtOracleWmsModels.DbtOracleWms.DbtModel(
                        name=f"stg_wms_{source}",
                        dbt_model_type="staging",
                        wms_entity_type=source,
                        schema_name="wms_staging",
                        table_name=f"stg_{source}",
                        columns=[],
                        materialization=c.DbtOracleWms.Dbt.Materialization.VIEW.value,
                        sql_content=f"select * from {{{{ source('oracle_wms', '{source}') }}}}",  # nosec B608
                        description=f"Staging model for {source}",
                        oracle_source=source,
                        dependencies=[],
                        wms_business_rules=[],
                    )
                    for source in oracle_sources
                ]
                return r[Sequence[FlextDbtOracleWmsModels.DbtOracleWms.DbtModel]].ok(
                    models
                )

        class FlextDbtOracleWmsSettings(FlextSettings):
            """Runtime settings for DBT Oracle WMS transformations."""

            required_fields_per_entity: Annotated[
                Mapping[str, t.StrSequence],
                u.Field(description="Required fields per WMS entity for validation"),
            ] = u.Field(default_factory=dict)
            oracle_wms_environment: Annotated[
                str,
                u.Field(
                    default="development",
                    description="Oracle WMS environment (development/production)",
                ),
            ]
            oracle_wms_base_url: Annotated[
                str,
                u.Field(default="", description="Base URL for Oracle WMS API"),
            ]
            dbt_threads: Annotated[
                int,
                u.Field(
                    default=4,
                    description="Number of DBT threads for parallel execution",
                ),
            ]
            dbt_target: Annotated[
                str,
                u.Field(default="dev", description="DBT target profile (dev/prod)"),
            ]

    @classmethod
    def create_generator(
        cls,
        settings: t.StrMapping | None = None,
    ) -> FlextDbtOracleWmsModels.DbtOracleWms.ModelGenerator:
        """Create a model generator with explicit configuration."""
        return cls.DbtOracleWms.ModelGenerator(settings=settings)


m = FlextDbtOracleWmsModels

__all__: list[str] = ["FlextDbtOracleWmsModels", "m"]
