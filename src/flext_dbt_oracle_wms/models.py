"""FLEXT DBT Oracle WMS Models.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextModels, FlextResult


class FlextDbtOracleWmsModels(FlextModels.Entity):
    """Unified DBT Oracle WMS models collection with dimensional modeling capabilities.

    Immutable representation of a generated DBT model with Oracle WMS-specific metadata
    and integrated warehouse management functionality following FLEXT unified class pattern.
    """

    name: str
    dbt_model_type: str  # staging, intermediate, marts, dimensional
    wms_entity_type: str  # inventory, location, allocation, order, item
    schema_name: str
    table_name: str
    columns: list[dict[str, object]]
    materialization: str
    sql_content: str
    description: str
    oracle_source: str
    dependencies: list[str]
    wms_business_rules: list[str]

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate DBT Oracle WMS model business rules."""
        try:
            if not self.name.strip():
                return FlextResult[None].fail("Model name cannot be empty")
            if self.dbt_model_type not in {
                "staging",
                "intermediate",
                "marts",
                "dimensional",
            }:
                return FlextResult[None].fail("Invalid model_type")
            if self.wms_entity_type not in {
                "inventory",
                "location",
                "allocation",
                "order",
                "item",
                "task",
                "dimension",
                "fact",
            }:
                return FlextResult[None].fail("Invalid WMS entity type")
            if not self.schema_name.strip() or not self.table_name.strip():
                return FlextResult[None].fail("Schema and table names cannot be empty")
            if not self.sql_content.strip():
                return FlextResult[None].fail("SQL content cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Business rule validation failed: {e}")

    def get_file_path(self) -> str:
        """Get the file path for this DBT Oracle WMS model."""
        return f"models/{self.dbt_model_type}/{self.name}.sql"

    def get_schema_file_path(self) -> str:
        """Get the schema file path for this DBT Oracle WMS model."""
        return f"models/{self.dbt_model_type}/schema.yml"

    def to_sql_file(self) -> FlextResult[str]:
        """Convert model to SQL file content with Oracle WMS optimizations."""
        try:
            config_block = f"""
{{{{
  config(
    materialized='{self.materialization}',
    schema='{self.schema_name}',
    alias='{self.table_name}',
    oracle_optimizations=True,
    wms_entity_type='{self.wms_entity_type}'
  )
}}}}"""
            content = f"{config_block}\n\n{self.sql_content}"
            return FlextResult[str].ok(content)
        except Exception as e:
            return FlextResult[str].fail(f"SQL file generation failed: {e}")

    def to_schema_entry(self) -> FlextResult[dict[str, object]]:
        """Convert model to schema.yml entry with WMS metadata."""
        try:
            schema_entry: dict[str, object] = {
                "name": self.name,
                "description": self.description,
                "meta": {
                    "wms_entity_type": self.wms_entity_type,
                    "oracle_source": self.oracle_source,
                    "wms_business_rules": self.wms_business_rules,
                },
                "columns": [
                    {
                        "name": col["name"],
                        "description": col.get("description", ""),
                        "data_type": col.get("data_type", ""),
                        "wms_context": col.get("wms_context", ""),
                    }
                    for col in self.columns
                ],
            }
            return FlextResult[dict["str", "object"]].ok(schema_entry)
        except Exception as e:
            return FlextResult[dict["str", "object"]].fail(
                f"Schema entry generation failed: {e}"
            )

    @classmethod
    def create_generator(
        cls,
        config: dict[str, object],
    ) -> FlextDbtOracleWmsModels._ModelGenerator:
        """Create a WMS model generator instance."""
        return cls._ModelGenerator(config)

    class _ModelGenerator:
        """Internal model generator class for DBT Oracle WMS models."""

        @override
        def __init__(
            self,
            config: dict[str, object],
        ) -> None:
            """Initialize the Oracle WMS model generator."""
            self.config = config

        def generate_wms_dimensional_models(
            self, wms_entities: list[str]
        ) -> FlextResult[list[FlextDbtOracleWmsModels]]:
            """Generate dimensional models from Oracle WMS entities."""
            dimensional_models: list[FlextDbtOracleWmsModels] = []

            for wms_entity in wms_entities:
                # Generate dimension model
                dim_result = self._create_dimension_model(wms_entity)
                if dim_result.is_success:
                    dimensional_models.append(dim_result.unwrap())

                # Generate fact model if applicable
                if wms_entity in {"inventory", "allocation", "order"}:
                    fact_result = self._create_fact_model(wms_entity)
                    if fact_result.is_success:
                        dimensional_models.append(fact_result.unwrap())

            return FlextResult[list[FlextDbtOracleWmsModels]].ok(dimensional_models)

        def generate_wms_staging_models(
            self, oracle_sources: list[str]
        ) -> FlextResult[list[FlextDbtOracleWmsModels]]:
            """Generate staging models from Oracle WMS sources."""
            staging_models: list[FlextDbtOracleWmsModels] = []

            for oracle_source in oracle_sources:
                model_result = self._create_staging_model(oracle_source)
                if model_result.is_success:
                    staging_models.append(model_result.unwrap())

            return FlextResult[list[FlextDbtOracleWmsModels]].ok(staging_models)

        def _create_dimension_model(
            self, wms_entity: str
        ) -> FlextResult[FlextDbtOracleWmsModels]:
            """Create a dimension model for WMS entity."""
            try:
                sql_content = f"""
select
    {wms_entity}_key,
    {wms_entity}_id,
    {wms_entity}_name,
    description,
    status,
    created_date,
    modified_date,
    is_active
from {{{{ ref('stg_wms_{wms_entity}') }}}}
"""

                dimension_model = FlextDbtOracleWmsModels(
                    name=f"dim_wms_{wms_entity}",
                    dbt_model_type=dimensional,
                    wms_entity_type=wms_entity,
                    schema_name=wms_mart,
                    table_name=f"dim_{wms_entity}",
                    columns=[
                        {
                            "name": f"{wms_entity}_key",
                            "description": f"Surrogate key for {wms_entity}",
                            "data_type": "NUMBER",
                            "wms_context": "primary_key",
                        },
                        {
                            "name": f"{wms_entity}_id",
                            "description": f"Natural key for {wms_entity}",
                            "data_type": VARCHAR2(50),
                            "wms_context": "natural_key",
                        },
                        {
                            "name": f"{wms_entity}_name",
                            "description": f"Name of {wms_entity}",
                            "data_type": VARCHAR2(255),
                            "wms_context": "descriptive",
                        },
                        {
                            "name": "description",
                            "description": f"Description of {wms_entity}",
                            "data_type": VARCHAR2(1000),
                            "wms_context": "descriptive",
                        },
                        {
                            "name": "status",
                            "description": "Status",
                            "data_type": VARCHAR2(20),
                            "wms_context": "business_rule",
                        },
                        {
                            "name": "is_active",
                            "description": "Active flag",
                            "data_type": NUMBER(1),
                            "wms_context": "business_rule",
                        },
                    ],
                    materialization=table,
                    sql_content=sql_content.strip(),
                    description=f"Dimension table for WMS {wms_entity} entities",
                    oracle_source=f"WMS.{wms_entity.upper()}",
                    dependencies=[f"stg_wms_{wms_entity}"],
                    wms_business_rules=[
                        f"{wms_entity}_id must be unique",
                        "status must be valid WMS status",
                    ],
                    domain_events=[],
                )

                return FlextResult[FlextDbtOracleWmsModels].ok(dimension_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleWmsModels].fail(
                    f"Failed to create dimension model: {e}"
                )

        def _create_fact_model(
            self, wms_entity: str
        ) -> FlextResult[FlextDbtOracleWmsModels]:
            """Create a fact model for WMS entity."""
            try:
                sql_content = f"""
select
    {wms_entity}_fact_key,
    {wms_entity}_key,
    location_key,
    item_key,
    date_key,
    quantity,
    unit_cost,
    total_value,
    transaction_date,
    created_timestamp
from {{{{ ref('int_wms_{wms_entity}') }}}}
"""

                fact_model = FlextDbtOracleWmsModels(
                    name=f"fact_wms_{wms_entity}",
                    dbt_model_type=dimensional,
                    wms_entity_type=fact,
                    schema_name=wms_mart,
                    table_name=f"fact_{wms_entity}",
                    columns=[
                        {
                            "name": f"{wms_entity}_fact_key",
                            "description": f"Surrogate key for {wms_entity} fact",
                            "data_type": "NUMBER",
                            "wms_context": "primary_key",
                        },
                        {
                            "name": f"{wms_entity}_key",
                            "description": f"Foreign key to dim_{wms_entity}",
                            "data_type": "NUMBER",
                            "wms_context": "foreign_key",
                        },
                        {
                            "name": "location_key",
                            "description": "Foreign key to dim_location",
                            "data_type": "NUMBER",
                            "wms_context": "foreign_key",
                        },
                        {
                            "name": "item_key",
                            "description": "Foreign key to dim_item",
                            "data_type": "NUMBER",
                            "wms_context": "foreign_key",
                        },
                        {
                            "name": "date_key",
                            "description": "Foreign key to dim_date",
                            "data_type": "NUMBER",
                            "wms_context": "foreign_key",
                        },
                        {
                            "name": "quantity",
                            "description": "Quantity measure",
                            "data_type": NUMBER(15, 4),
                            "wms_context": "measure",
                        },
                        {
                            "name": "unit_cost",
                            "description": "Unit cost measure",
                            "data_type": NUMBER(15, 4),
                            "wms_context": "measure",
                        },
                        {
                            "name": "total_value",
                            "description": "Total value measure",
                            "data_type": NUMBER(15, 2),
                            "wms_context": "measure",
                        },
                    ],
                    materialization=incremental,
                    sql_content=sql_content.strip(),
                    description=f"Fact table for WMS {wms_entity} transactions",
                    oracle_source=f"WMS.{wms_entity.upper()}_TRANSACTIONS",
                    dependencies=[
                        f"int_wms_{wms_entity}",
                        "dim_location",
                        "dim_item",
                        "dim_date",
                    ],
                    wms_business_rules=[
                        "quantity >= 0",
                        "unit_cost >= 0",
                        "total_value = quantity * unit_cost",
                    ],
                    domain_events=[],
                )

                return FlextResult[FlextDbtOracleWmsModels].ok(fact_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleWmsModels].fail(
                    f"Failed to create fact model: {e}"
                )

        def _create_staging_model(
            self, oracle_source: str
        ) -> FlextResult[FlextDbtOracleWmsModels]:
            """Create a staging model from Oracle WMS source."""
            try:
                sql_content = f"""
select *
from {{{{ source('oracle_wms', '{oracle_source.lower()}') }}}}
"""

                staging_model = FlextDbtOracleWmsModels(
                    name=f"stg_wms_{oracle_source.lower()}",
                    dbt_model_type=staging,
                    wms_entity_type=oracle_source.lower(),
                    schema_name=wms_staging,
                    table_name=f"stg_{oracle_source.lower()}",
                    columns=[],
                    materialization=view,
                    sql_content=sql_content.strip(),
                    description=f"Staging model for Oracle WMS {oracle_source}",
                    oracle_source=f"WMS.{oracle_source.upper()}",
                    dependencies=[],
                    wms_business_rules=[],
                    domain_events=[],
                )

                return FlextResult[FlextDbtOracleWmsModels].ok(staging_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleWmsModels].fail(
                    f"Failed to create staging model: {e}"
                )


__all__ = ["FlextDbtOracleWmsModels"]
