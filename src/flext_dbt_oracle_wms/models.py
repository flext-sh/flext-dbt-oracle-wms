"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoModels
from flext_oracle_wms.wms_models import FlextOracleWmsModels
from pydantic import Field

from .constants import FlextDbtOracleWmsConstants


class FlextDbtOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtModel(FlextMeltanoModels.ArbitraryTypesModel):
        """Single DBT model metadata payload."""

        name: str
        dbt_model_type: str
        wms_entity_type: str
        schema_name: str
        table_name: str
        columns: list[dict[str, object]] = Field(default=[])
        materialization: str
        sql_content: str
        description: str
        oracle_source: str
        dependencies: list[str] = Field(default_factory=list)
        wms_business_rules: list[str] = Field(default_factory=list)

        def validate_business_rules(self) -> FlextResult[bool]:
            """Validate essential DBT model constraints."""
            if not self.name:
                return FlextResult[bool].fail("Model name cannot be empty")
            if (
                self.materialization
                not in FlextDbtOracleWmsConstants.DbtOracleWms.Dbt.MATERIALIZATIONS
            ):
                return FlextResult[bool].fail("Invalid materialization")
            return FlextResult[bool].ok(True)

    class ModelGenerator:
        """Generator for lightweight DBT model objects."""

        def __init__(self, config: Mapping[str, t.GeneralValueType]) -> None:
            """Store generation config for later model creation."""
            super().__init__()
            self.config = config

        def generate_wms_staging_models(
            self,
            oracle_sources: list[str],
        ) -> FlextResult[list[FlextDbtOracleWmsModels.DbtModel]]:
            """Create one staging model per source name."""
            models = [
                FlextDbtOracleWmsModels.DbtModel.model_validate({
                    "name": f"stg_wms_{source}",
                    "dbt_model_type": "staging",
                    "wms_entity_type": source,
                    "schema_name": "wms_staging",
                    "table_name": f"stg_{source}",
                    "materialization": FlextDbtOracleWmsConstants.DbtOracleWms.Dbt.Materialization.VIEW.value,
                    "sql_content": f"select * from {{{{ source('oracle_wms', '{source}') }}}}",  # nosec B608
                    "description": f"Staging model for {source}",
                    "oracle_source": source,
                })
                for source in oracle_sources
            ]
            return FlextResult[list[FlextDbtOracleWmsModels.DbtModel]].ok(models)

    @classmethod
    def create_generator(
        cls,
        config: Mapping[str, t.GeneralValueType],
    ) -> FlextDbtOracleWmsModels.ModelGenerator:
        """Create a model generator with explicit configuration."""
        return cls.ModelGenerator(config)


m = FlextDbtOracleWmsModels

__all__ = ["FlextDbtOracleWmsModels", "m"]
