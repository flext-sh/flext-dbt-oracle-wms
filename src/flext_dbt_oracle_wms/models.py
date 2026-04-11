"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from collections.abc import Mapping, MutableSequence, Sequence
from typing import Annotated, ClassVar, override

from flext_dbt_oracle import FlextDbtOracleModels
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from flext_core import FlextSettings, r
from flext_dbt_oracle_wms import c, t
from flext_oracle_wms import FlextOracleWmsModels


class FlextDbtOracleWmsModels(FlextDbtOracleModels, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms:
        """DBT Oracle WMS domain namespace -- m.DbtOracleWms.*."""

        # Models from dbt_models.py
        class RawItemRecord(BaseModel):
            """Raw item record from Oracle WMS."""

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

            item_id: Annotated[str, Field(default="")]
            item_number: Annotated[str, Field(default="")]
            item_description: Annotated[str, Field(default="")]

        class FlextDbtOracleWmsItemDimension(BaseModel):
            """Item dimension model for WMS analytics."""

            item_id: Annotated[str, Field(default="")]
            item_number: Annotated[str, Field(default="")]
            item_description: Annotated[str, Field(default="")]

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
                    except ValidationError:
                        continue
                    transformed.append(
                        FlextDbtOracleWmsModels.DbtOracleWms.FlextDbtOracleWmsItemDimension(
                            item_id=raw_record.item_id,
                            item_number=raw_record.item_number,
                            item_description=raw_record.item_description,
                        ),
                    )
                return transformed

            def validate_business_rules(
                self,
                records: Sequence[t.ConfigurationMapping],
            ) -> r[bool]:
                """Validate business rules for WMS records."""
                if not records:
                    return r[bool].fail("No records to validate")
                return r[bool].ok(True)

        class DbtModel(FlextDbtOracleModels.DbtOracle.Model):
            """WMS-specific DBT model metadata layered on the canonical DBT model."""

            wms_entity_type: Annotated[
                str,
                Field(description="Oracle WMS entity represented by this model"),
            ]
            oracle_source: Annotated[
                str,
                Field(description="Oracle WMS source name for this model"),
            ]
            wms_business_rules: Annotated[
                t.StrSequence,
                Field(description="WMS-specific business rules attached to the model"),
            ] = Field(default_factory=list)

        class ModelGenerator(FlextDbtOracleModels.DbtOracle.ModelGenerator):
            """Generator for lightweight DBT model objects."""

            def generate_wms_staging_models(
                self,
                oracle_sources: t.StrSequence,
            ) -> r[Sequence[FlextDbtOracleWmsModels.DbtOracleWms.DbtModel]]:
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
                Field(
                    description="Required fields per WMS entity for validation",
                ),
            ] = Field(default_factory=dict)
            oracle_wms_environment: Annotated[
                str,
                Field(
                    default="development",
                    description="Oracle WMS environment (development/production)",
                ),
            ]
            oracle_wms_base_url: Annotated[
                str,
                Field(default="", description="Base URL for Oracle WMS API"),
            ]
            dbt_threads: Annotated[
                int,
                Field(
                    default=4,
                    description="Number of DBT threads for parallel execution",
                ),
            ]
            dbt_target: Annotated[
                str,
                Field(default="dev", description="DBT target profile (dev/prod)"),
            ]

    @classmethod
    @override
    def create_generator(
        cls,
        settings: t.StrMapping | None = None,
    ) -> FlextDbtOracleWmsModels.DbtOracleWms.ModelGenerator:
        """Create a model generator with explicit configuration."""
        return cls.DbtOracleWms.ModelGenerator(settings)


__all__ = ["FlextDbtOracleWmsModels", "m"]

m = FlextDbtOracleWmsModels
