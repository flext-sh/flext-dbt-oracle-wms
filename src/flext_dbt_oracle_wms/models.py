"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from collections.abc import Mapping, MutableSequence, Sequence
from typing import Annotated, ClassVar

from flext_core import FlextSettings, r
from flext_meltano import FlextMeltanoModels
from flext_oracle_wms.models import FlextOracleWmsModels
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from flext_dbt_oracle_wms import c, t


class FlextDbtOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms:
        """DBT Oracle WMS domain namespace -- m.DbtOracleWms.*."""

        # Domain types from domain_types.py
        class DBTOracleWMSProject(BaseModel):
            """DBT project configuration."""

            name: Annotated[str, Field(default="flext_dbt_oracle_wms")]
            profile: Annotated[str, Field(default="flext_oracle_wms")]

        class DBTOracleWMSModel(BaseModel):
            """DBT model definition."""

            name: Annotated[str, Field(default="")]
            materialization: Annotated[str, Field(default="view")]

        class DBTOracleWMSSource(BaseModel):
            """DBT source definition."""

            name: Annotated[str, Field(default="")]
            source_schema: Annotated[Mapping[str, t.ContainerValue | None]] = Field(
                default_factory=dict
            )

        class DBTOracleWMSTest(BaseModel):
            """DBT test definition."""

            name: Annotated[str, Field(default="")]
            severity: Annotated[str, Field(default="warn")]

        class DBTOracleWMSMacro(BaseModel):
            """DBT macro definition."""

            name: Annotated[str, Field(default="")]

        class DBTOracleWMSSnapshot(BaseModel):
            """DBT snapshot definition."""

            name: Annotated[str, Field(default="")]

        class DBTOracleWMSAnalysis(BaseModel):
            """DBT analysis definition."""

            name: Annotated[str, Field(default="")]

        class DBTOracleWMSCompilation(BaseModel):
            """DBT compilation definition."""

            name: Annotated[str, Field(default="")]

        class DBTOracleWMSExecution(BaseModel):
            """DBT execution definition."""

            name: Annotated[str, Field(default="")]

        class DBTOracleWMSDocumentation(BaseModel):
            """DBT documentation definition."""

            name: Annotated[str, Field(default="")]

        # Configuration types from config_types.py
        class DBTOracleWMSConfiguration(BaseModel):
            """Base configuration for DBT Oracle WMS project."""

            project_name: Annotated[str, Field(default="flext_dbt_oracle_wms")]
            profile: Annotated[str, Field(default="flext_oracle_wms")]

        class DBTOracleWMSModelConfiguration(DBTOracleWMSConfiguration):
            """Configuration for DBT model materialization."""

            materialization: Annotated[str, Field(default="view")]

        class DBTOracleWMSSourceConfiguration(DBTOracleWMSConfiguration):
            """Configuration for DBT source definitions."""

            source_name: Annotated[str, Field(default="oracle_wms")]

        class DBTOracleWMSTestConfiguration(DBTOracleWMSConfiguration):
            """Configuration for DBT test execution."""

            severity: Annotated[str, Field(default="warn")]

        class DBTOracleWMSMacroConfiguration(DBTOracleWMSConfiguration):
            """Configuration for DBT macro namespace."""

            macro_namespace: Annotated[str, Field(default="wms")]

        class DBTOracleWMSProfileConfiguration(DBTOracleWMSConfiguration):
            """Configuration for DBT profile and target."""

            target: Annotated[str, Field(default="dev")]

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

        class FlextDbtOracleWmsInventoryFact(BaseModel):
            """Inventory fact table model."""

            record: t.ConfigurationMapping = Field(default_factory=dict)

        class FlextDbtOracleWmsLocationDimension(BaseModel):
            """Location dimension model for warehouse analytics."""

            record: t.ConfigurationMapping = Field(default_factory=dict)

        class FlextDbtOracleWmsShipmentFact(BaseModel):
            """Shipment fact table model."""

            record: t.ConfigurationMapping = Field(default_factory=dict)

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

        class DbtModel(FlextMeltanoModels.ArbitraryTypesModel):
            """Single DBT model metadata payload."""

            name: str
            dbt_model_type: str
            wms_entity_type: str
            schema_name: str
            table_name: str
            columns: Sequence[t.ConfigurationMapping] = Field(default_factory=list)
            materialization: str
            sql_content: str
            description: str
            oracle_source: str
            dependencies: t.StrSequence = Field(default_factory=list)
            wms_business_rules: t.StrSequence = Field(default_factory=list)

            def validate_business_rules(self) -> r[bool]:
                """Validate essential DBT model constraints."""
                if not self.name:
                    return r[bool].fail("Model name cannot be empty")
                if self.materialization not in c.DbtOracleWms.Dbt.MATERIALIZATIONS:
                    return r[bool].fail("Invalid materialization")
                return r[bool].ok(True)

        class ModelGenerator:
            """Generator for lightweight DBT model objects."""

            def __init__(self, config: t.ConfigurationMapping) -> None:
                """Store generation config for later model creation."""
                super().__init__()
                self.config = config

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

        class FlextDBTOracleWMSSettings(FlextDbtOracleWmsSettings):
            """Settings for FLEXT DBT Oracle WMS integration."""

    @classmethod
    def create_generator(
        cls,
        config: t.ConfigurationMapping,
    ) -> FlextDbtOracleWmsModels.DbtOracleWms.ModelGenerator:
        """Create a model generator with explicit configuration."""
        return cls.DbtOracleWms.ModelGenerator(config)


__all__ = ["FlextDbtOracleWmsModels", "m"]

m = FlextDbtOracleWmsModels
