"""FLEXT DBT Oracle WMS Models.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT.
"""

# SQL injection warnings are false positives for DBT template strings
from __future__ import annotations

from typing import override

from flext_core import FlextCore

from flext_dbt_oracle_wms.constants import FlextDbtOracleWmsConstants

# Constants for magic values
MAX_PORT_NUMBER = 65535
MIN_PORT_NUMBER = 1
MAX_INT_PRECISION = 9
PERFORMANCE_THRESHOLD_SECONDS = 45
PERFORMANCE_WARNING_SECONDS = 90
MIN_MODELS_PER_MINUTE = 3
LARGE_DATA_VOLUME_GB = 10
INVENTORY_FACT_THRESHOLD_SECONDS = 120
LARGE_MODEL_SIZE_THRESHOLD = 50000
VERY_LARGE_MODEL_SIZE_THRESHOLD = 500000
INVENTORY_INCREMENTAL_THRESHOLD = 1000000
HIGH_LOAD_FACTOR_THRESHOLD = 1.5


class FlextDbtOracleWmsModels(FlextCore.Models.ArbitraryTypesModel):
    """Unified DBT Oracle WMS models collection with "dimensional" modeling capabilities.

    Immutable representation of a generated DBT model with Oracle WMS-specific metadata
    and integrated warehouse management functionality following FLEXT unified class pattern.
    """

    name: str
    dbt_model_type: str  # "staging", intermediate, marts, "dimensional"
    wms_entity_type: str  # inventory, location, allocation, order, item
    schema_name: str
    table_name: str
    columns: list[FlextCore.Types.Dict]
    materialization: str
    sql_content: str
    description: str
    oracle_source: str
    dependencies: FlextCore.Types.StringList
    wms_business_rules: FlextCore.Types.StringList

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate DBT Oracle WMS model business rules."""
        try:
            if not self.name.strip():
                return FlextCore.Result[None].fail("Model name cannot be empty")
            if (
                self.dbt_model_type
                not in FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS
            ):
                return FlextCore.Result[None].fail("Invalid model_type")
            if (
                self.wms_entity_type
                not in FlextDbtOracleWmsConstants.Entities.WMS_ENTITIES
            ):
                return FlextCore.Result[None].fail("Invalid WMS entity type")
            if not self.schema_name.strip() or not self.table_name.strip():
                return FlextCore.Result[None].fail(
                    "Schema and table names cannot be empty"
                )
            if not self.sql_content.strip():
                return FlextCore.Result[None].fail("SQL content cannot be empty")
            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Business rule validation failed: {e}")

    def get_file_path(self) -> str:
        """Get the file path for this DBT Oracle WMS model."""
        return f"models/{self.dbt_model_type}/{self.name}.sql"

    def get_schema_file_path(self) -> str:
        """Get the schema file path for this DBT Oracle WMS model."""
        return f"models/{self.dbt_model_type}/schema.yml"

    def to_sql_file(self) -> FlextCore.Result[str]:
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
            return FlextCore.Result[str].ok(content)
        except Exception as e:
            return FlextCore.Result[str].fail(f"SQL file generation failed: {e}")

    def to_schema_entry(self) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Convert model to schema.yml entry with WMS metadata."""
        try:
            schema_entry: FlextCore.Types.Dict = {
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
            return FlextCore.Result[dict["str", "object"]].ok(schema_entry)
        except Exception as e:
            return FlextCore.Result[dict["str", "object"]].fail(
                f"Schema entry generation failed: {e}"
            )

    @classmethod
    def create_generator(
        cls,
        config: FlextCore.Types.Dict,
    ) -> FlextDbtOracleWmsModels.ModelGenerator:
        """Create a WMS model generator instance."""
        return cls.ModelGenerator(config)

    class ModelGenerator:
        """Internal model generator class for DBT Oracle WMS models."""

        @override
        def __init__(
            self,
            config: FlextCore.Types.Dict,
        ) -> None:
            """Initialize the Oracle WMS model generator."""
            self.config = config

        def generate_wms_dimensional_models(
            self, wms_entities: FlextCore.Types.StringList
        ) -> FlextCore.Result[list[FlextDbtOracleWmsModels]]:
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

            return FlextCore.Result[list[FlextDbtOracleWmsModels]].ok(
                dimensional_models
            )

        def generate_wms_staging_models(
            self, oracle_sources: FlextCore.Types.StringList
        ) -> FlextCore.Result[list[FlextDbtOracleWmsModels]]:
            """Generate staging models from Oracle WMS sources."""
            staging_models: list[FlextDbtOracleWmsModels] = []

            for oracle_source in oracle_sources:
                model_result = self._create_staging_model(oracle_source)
                if model_result.is_success:
                    staging_models.append(model_result.unwrap())

            return FlextCore.Result[list[FlextDbtOracleWmsModels]].ok(staging_models)

        def _create_dimension_model(
            self, wms_entity: str
        ) -> FlextCore.Result[FlextDbtOracleWmsModels]:
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
                    dbt_model_type=FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS[
                        1
                    ],  # "view"
                    wms_entity_type=wms_entity,
                    schema_name="wms_mart",
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
                            "data_type": "VARCHAR2(50)",
                            "wms_context": "natural_key",
                        },
                        {
                            "name": f"{wms_entity}_name",
                            "description": f"Name of {wms_entity}",
                            "data_type": "VARCHAR2(255)",
                            "wms_context": "descriptive",
                        },
                        {
                            "name": "description",
                            "description": f"Description of {wms_entity}",
                            "data_type": "VARCHAR2(1000)",
                            "wms_context": "descriptive",
                        },
                        {
                            "name": "status",
                            "description": "Status",
                            "data_type": "VARCHAR2(20)",
                            "wms_context": "business_rule",
                        },
                        {
                            "name": "is_active",
                            "description": "Active flag",
                            "data_type": "NUMBER(1)",
                            "wms_context": "business_rule",
                        },
                    ],
                    materialization=FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS[
                        0
                    ],  # "table"
                    sql_content=sql_content.strip(),
                    description=f"Dimension table for WMS {wms_entity} entities",
                    oracle_source=f"WMS.{wms_entity.upper()}",
                    dependencies=[f"stg_wms_{wms_entity}"],
                    wms_business_rules=[
                        f"{wms_entity}_id must be unique",
                        "status must be valid WMS status",
                    ],
                )

                return FlextCore.Result[FlextDbtOracleWmsModels].ok(dimension_model)

            except Exception as e:
                return FlextCore.Result[FlextDbtOracleWmsModels].fail(
                    f"Failed to create dimension model: {e}"
                )

        def _create_fact_model(
            self, wms_entity: str
        ) -> FlextCore.Result[FlextDbtOracleWmsModels]:
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
                    dbt_model_type=FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS[
                        1
                    ],  # "view"
                    wms_entity_type="fact",
                    schema_name="wms_mart",
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
                            "data_type": "NUMBER(15, 4)",
                            "wms_context": "measure",
                        },
                        {
                            "name": "unit_cost",
                            "description": "Unit cost measure",
                            "data_type": "NUMBER(15, 4)",
                            "wms_context": "measure",
                        },
                        {
                            "name": "total_value",
                            "description": "Total value measure",
                            "data_type": "NUMBER(15, 2)",
                            "wms_context": "measure",
                        },
                    ],
                    materialization=FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS[
                        2
                    ],  # "incremental"
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
                )

                return FlextCore.Result[FlextDbtOracleWmsModels].ok(fact_model)

            except Exception as e:
                return FlextCore.Result[FlextDbtOracleWmsModels].fail(
                    f"Failed to create fact model: {e}"
                )

        def _create_staging_model(
            self, oracle_source: str
        ) -> FlextCore.Result[FlextDbtOracleWmsModels]:
            """Create a staging model from Oracle WMS source."""
            try:
                sql_content = f"""
select *
from {{{{ source('oracle_wms', '{oracle_source.lower()}') }}}}
"""

                staging_model = FlextDbtOracleWmsModels(
                    name=f"stg_wms_{oracle_source.lower()}",
                    dbt_model_type=FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS[
                        1
                    ],  # "view"
                    wms_entity_type=oracle_source.lower(),
                    schema_name="wms_staging",
                    table_name=f"stg_{oracle_source.lower()}",
                    columns=[],
                    materialization=FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS[
                        1
                    ],  # "view"
                    sql_content=sql_content.strip(),
                    description=f"Staging model for Oracle WMS {oracle_source}",
                    oracle_source=f"WMS.{oracle_source.upper()}",
                    dependencies=[],
                    wms_business_rules=[],
                )

                return FlextCore.Result[FlextDbtOracleWmsModels].ok(staging_model)

            except Exception as e:
                return FlextCore.Result[FlextDbtOracleWmsModels].fail(
                    f"Failed to create staging model: {e}"
                )

    class Utilities(FlextCore.Utilities):
        """Unified DBT Oracle WMS utilities extending FlextCore.Utilities.

        Provides comprehensive utility classes for DBT Oracle WMS operations:
        - Oracle WMS database connection and metadata utilities
        - DBT project management utilities for WMS workflows
        - Oracle WMS-specific data type conversion utilities
        - DBT model generation utilities for WMS dimensional analytics
        - Performance optimization utilities for Oracle WMS DBT operations

        All nested utility classes follow SOLID principles and FlextCore.Result patterns.
        """

        class _OracleWmsConnectionHelper:
            """Oracle WMS database connection and validation utilities."""

            @staticmethod
            def validate_oracle_wms_connection_config(
                config: dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate Oracle WMS connection configuration for DBT."""
                if not config:
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "Oracle WMS connection config cannot be empty"
                    )

                required_fields = [
                    "host",
                    "port",
                    "user",
                    "password",
                    "service_name",
                    "wms_schema",
                ]

                for field in required_fields:
                    if field not in config:
                        return FlextCore.Result[FlextCore.Types.Dict].fail(
                            f"Missing required Oracle WMS connection field: {field}"
                        )

                # Validate port is integer
                if not isinstance(config.get("port"), int):
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "Oracle WMS port must be an integer"
                    )

                # Validate port range
                port = config["port"]
                if not (MIN_PORT_NUMBER <= port <= MAX_PORT_NUMBER):
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        f"Oracle WMS port must be between {MIN_PORT_NUMBER} and {MAX_PORT_NUMBER}"
                    )

                # Validate WMS schema format
                wms_schema = config["wms_schema"]
                if not wms_schema.upper().startswith("WMS"):
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "WMS schema must start with 'WMS'"
                    )

                return FlextCore.Result[FlextCore.Types.Dict].ok(config)


__all__ = ["FlextDbtOracleWmsModels"]
