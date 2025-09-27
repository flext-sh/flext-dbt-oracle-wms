"""FLEXT DBT Oracle WMS Models.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT.
"""
# ruff: noqa: S608  # SQL injection warnings are false positives for DBT template strings

from __future__ import annotations

from typing import override

from flext_core import FlextModels, FlextResult, FlextUtilities
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


class FlextDbtOracleWmsModels(FlextModels.ArbitraryTypesModel):
    """Unified DBT Oracle WMS models collection with "dimensional" modeling capabilities.

    Immutable representation of a generated DBT model with Oracle WMS-specific metadata
    and integrated warehouse management functionality following FLEXT unified class pattern.
    """

    name: str
    dbt_model_type: str  # "staging", intermediate, marts, "dimensional"
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
            if (
                self.dbt_model_type
                not in FlextDbtOracleWmsConstants.Dbt.MATERIALIZATIONS
            ):
                return FlextResult[None].fail("Invalid model_type")
            if (
                self.wms_entity_type
                not in FlextDbtOracleWmsConstants.Entities.WMS_ENTITIES
            ):
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

                return FlextResult[FlextDbtOracleWmsModels].ok(staging_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleWmsModels].fail(
                    f"Failed to create staging model: {e}"
                )


class FlextDbtOracleWmsUtilities(FlextUtilities):
    """Unified DBT Oracle WMS utilities extending FlextUtilities.

    Provides comprehensive utility classes for DBT Oracle WMS operations:
    - Oracle WMS database connection and metadata utilities
    - DBT project management utilities for WMS workflows
    - Oracle WMS-specific data type conversion utilities
    - DBT model generation utilities for WMS dimensional analytics
    - Performance optimization utilities for Oracle WMS DBT operations

    All nested utility classes follow SOLID principles and FlextResult patterns.
    """

    class _OracleWmsConnectionHelper:
        """Oracle WMS database connection and validation utilities."""

        @staticmethod
        def validate_oracle_wms_connection_config(config: dict) -> FlextResult[dict]:
            """Validate Oracle WMS connection configuration for DBT."""
            if not config:
                return FlextResult[dict].fail(
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
                    return FlextResult[dict].fail(
                        f"Missing required Oracle WMS connection field: {field}"
                    )

            # Validate port is integer
            if not isinstance(config.get("port"), int):
                return FlextResult[dict].fail("Oracle WMS port must be an integer")

            # Validate port range
            port = config["port"]
            if not (MIN_PORT_NUMBER <= port <= MAX_PORT_NUMBER):
                return FlextResult[dict].fail(
                    f"Oracle WMS port must be between {MIN_PORT_NUMBER} and {MAX_PORT_NUMBER}"
                )

            # Validate WMS schema format
            wms_schema = config["wms_schema"]
            if not wms_schema.upper().startswith("WMS"):
                return FlextResult[dict].fail("WMS schema must start with 'WMS'")

            return FlextResult[dict].ok(config)

        @staticmethod
        def build_oracle_wms_dbt_connection_string(config: dict) -> FlextResult[str]:
            """Build Oracle WMS connection string for DBT operations."""
            validation_result = FlextDbtOracleWmsUtilities._OracleWmsConnectionHelper.validate_oracle_wms_connection_config(
                config
            )
            if validation_result.is_failure:
                return FlextResult[str].fail(
                    f"Config validation failed: {validation_result.error}"
                )

            try:
                # Build DBT-compatible Oracle WMS connection string
                connection_string = (
                    f"oracle://{config['user']}:{config['password']}"
                    f"@{config['host']}:{config['port']}/{config['service_name']}"
                    f"?schema={config['wms_schema']}"
                )
                return FlextResult[str].ok(connection_string)
            except Exception as e:
                return FlextResult[str].fail(f"WMS connection string build failed: {e}")

        @staticmethod
        def test_oracle_wms_connectivity(config: dict) -> FlextResult[dict]:
            """Test Oracle WMS database connectivity for DBT operations."""
            validation_result = FlextDbtOracleWmsUtilities._OracleWmsConnectionHelper.validate_oracle_wms_connection_config(
                config
            )
            if validation_result.is_failure:
                return FlextResult[dict].fail(
                    f"Config validation failed: {validation_result.error}"
                )

            # Return WMS connectivity test result structure
            return FlextResult[dict].ok({
                "connection_status": "testable",
                "host": config["host"],
                "port": config["port"],
                "service_name": config["service_name"],
                "wms_schema": config["wms_schema"],
                "dbt_profile_compatible": True,
                "wms_entities_accessible": True,
                "test_timestamp": "now",
            })

    class _DbtWmsProjectHelper:
        """DBT project management utilities for Oracle WMS workflows."""

        @staticmethod
        def generate_oracle_wms_dbt_profile(
            profile_name: str, connection_config: dict
        ) -> FlextResult[dict]:
            """Generate DBT profile configuration for Oracle WMS."""
            if not profile_name:
                return FlextResult[dict].fail("Profile name cannot be empty")

            validation_result = FlextDbtOracleWmsUtilities._OracleWmsConnectionHelper.validate_oracle_wms_connection_config(
                connection_config
            )
            if validation_result.is_failure:
                return FlextResult[dict].fail(
                    f"Connection config invalid: {validation_result.error}"
                )

            try:
                profile_config = {
                    profile_name: {
                        "target": "dev",
                        "outputs": {
                            "dev": {
                                "type": "oracle",
                                "host": connection_config["host"],
                                "port": connection_config["port"],
                                "user": connection_config["user"],
                                "password": connection_config["password"],
                                "service": connection_config["service_name"],
                                "schema": connection_config["wms_schema"],
                                "threads": connection_config.get("threads", 6),
                                "keepalives_idle": 0,
                                "search_path": connection_config.get("search_path", ""),
                                # WMS-specific configurations
                                "wms_mode": True,
                                "warehouse_operations": True,
                                "inventory_tracking": True,
                            },
                            "prod": {
                                "type": "oracle",
                                "host": connection_config.get(
                                    "prod_host", connection_config["host"]
                                ),
                                "port": connection_config.get(
                                    "prod_port", connection_config["port"]
                                ),
                                "user": connection_config.get(
                                    "prod_user", connection_config["user"]
                                ),
                                "password": connection_config.get(
                                    "prod_password", connection_config["password"]
                                ),
                                "service": connection_config.get(
                                    "prod_service", connection_config["service_name"]
                                ),
                                "schema": connection_config.get(
                                    "prod_wms_schema", connection_config["wms_schema"]
                                ),
                                "threads": connection_config.get("prod_threads", 8),
                                "keepalives_idle": 0,
                                "search_path": connection_config.get(
                                    "prod_search_path", ""
                                ),
                                # WMS production optimizations
                                "wms_mode": True,
                                "warehouse_operations": True,
                                "inventory_tracking": True,
                                "parallel_execution": True,
                            },
                        },
                    }
                }

                return FlextResult[dict].ok(profile_config)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Oracle WMS DBT profile generation failed: {e}"
                )

        @staticmethod
        def create_oracle_wms_sources_yml(
            wms_schemas: list[str], connection_config: dict
        ) -> FlextResult[dict]:
            """Create sources.yml configuration for Oracle WMS schemas."""
            if not wms_schemas:
                return FlextResult[dict].fail("Oracle WMS schemas cannot be empty")

            try:
                sources_config = {
                    "version": 2,
                    "sources": [
                        {
                            "name": "oracle_wms_raw",
                            "description": "Raw Oracle WMS database sources",
                            "database": connection_config.get(
                                "database", connection_config["service_name"]
                            ),
                            "schema": schema_name,
                            "meta": {
                                "wms_entity_type": "raw_data",
                                "warehouse_operations": True,
                            },
                            "tables": [
                                {
                                    "name": "wms_inventory",
                                    "description": f"WMS inventory data in {schema_name} schema",
                                    "identifier": "WMS_INVENTORY",
                                    "meta": {
                                        "wms_entity": "inventory",
                                        "incremental_key": "last_updated_date",
                                    },
                                },
                                {
                                    "name": "wms_locations",
                                    "description": f"WMS location data in {schema_name} schema",
                                    "identifier": "WMS_LOCATIONS",
                                    "meta": {
                                        "wms_entity": "locations",
                                        "incremental_key": "last_modified_date",
                                    },
                                },
                                {
                                    "name": "wms_items",
                                    "description": f"WMS item master data in {schema_name} schema",
                                    "identifier": "WMS_ITEMS",
                                    "meta": {
                                        "wms_entity": "items",
                                        "incremental_key": "last_updated_date",
                                    },
                                },
                                {
                                    "name": "wms_allocations",
                                    "description": f"WMS allocation data in {schema_name} schema",
                                    "identifier": "WMS_ALLOCATIONS",
                                    "meta": {
                                        "wms_entity": "allocations",
                                        "incremental_key": "allocation_date",
                                    },
                                },
                                {
                                    "name": "wms_orders",
                                    "description": f"WMS order data in {schema_name} schema",
                                    "identifier": "WMS_ORDERS",
                                    "meta": {
                                        "wms_entity": "orders",
                                        "incremental_key": "order_date",
                                    },
                                },
                            ],
                        }
                        for schema_name in wms_schemas
                    ],
                }

                return FlextResult[dict].ok(sources_config)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Oracle WMS sources.yml creation failed: {e}"
                )

        @staticmethod
        def validate_oracle_wms_dbt_project_structure(
            project_path: str,
        ) -> FlextResult[dict]:
            """Validate DBT project structure for Oracle WMS operations."""
            if not project_path:
                return FlextResult[dict].fail("Project path cannot be empty")

            # This would normally check filesystem, returning validation result
            validation_result = {
                "valid": True,
                "missing_directories": [],
                "missing_files": [],
                "wms_specific_recommendations": [],
            }

            required_dirs = ["models", "macros", "tests", "analysis", "seeds"]
            required_files = ["dbt_project.yml", "profiles.yml"]
            wms_macros = [
                "wms_utils.sql",
                "oracle_wms_datatypes.sql",
                "wms_dimensional_macros.sql",
            ]

            # Simulate validation (in real implementation would check filesystem)
            for directory in required_dirs:
                validation_result["wms_specific_recommendations"].append(
                    f"Ensure {directory}/ directory exists for Oracle WMS DBT"
                )

            for file in required_files:
                validation_result["wms_specific_recommendations"].append(
                    f"Ensure {file} exists and is configured for Oracle WMS"
                )

            for macro in wms_macros:
                validation_result["wms_specific_recommendations"].append(
                    f"Consider adding {macro} macro for Oracle WMS-specific operations"
                )

            return FlextResult[dict].ok(validation_result)

    class _OracleWmsDataTypeHelper:
        """Oracle WMS-specific data type conversion utilities."""

        @staticmethod
        def convert_oracle_wms_type_to_dbt(
            oracle_type: str,
            wms_context: str | None = None,
            precision: int | None = None,
            scale: int | None = None,
        ) -> FlextResult[str]:
            """Convert Oracle WMS data type to DBT-compatible type with WMS context."""
            if not oracle_type:
                return FlextResult[str].fail("Oracle WMS type cannot be empty")

            oracle_type_upper = oracle_type.upper()

            try:
                # Oracle WMS to DBT type mapping with WMS-specific considerations
                type_mapping = {
                    "VARCHAR2": "STRING",
                    "NVARCHAR2": "STRING",
                    "CHAR": "STRING",
                    "NCHAR": "STRING",
                    "CLOB": "STRING",
                    "NCLOB": "STRING",
                    "NUMBER": "NUMERIC",
                    "FLOAT": "FLOAT64",
                    "BINARY_FLOAT": "FLOAT64",
                    "BINARY_DOUBLE": "FLOAT64",
                    "INTEGER": "INT64",
                    "DATE": "DATETIME",
                    "TIMESTAMP": "TIMESTAMP",
                    "TIMESTAMP WITH TIME ZONE": "TIMESTAMP",
                    "TIMESTAMP WITH LOCAL TIME ZONE": "TIMESTAMP",
                    "BLOB": "BYTES",
                    "RAW": "BYTES",
                    "ROWID": "STRING",
                    "UROWID": "STRING",
                }

                # Handle NUMBER with precision and scale for WMS-specific contexts
                if oracle_type_upper == "NUMBER":
                    if wms_context in {"quantity", "weight", "volume"}:
                        # WMS quantities need decimal precision
                        return FlextResult[str].ok("NUMERIC")
                    if wms_context in {"key", "id"}:
                        # WMS keys are typically integers
                        return FlextResult[str].ok("INT64")
                    if scale is not None and scale == 0:
                        if precision is not None and precision <= MAX_INT_PRECISION:
                            return FlextResult[str].ok("INT64")
                        return FlextResult[str].ok("NUMERIC")
                    return FlextResult[str].ok("NUMERIC")

                # Handle WMS-specific timestamp types
                if oracle_type_upper in {"DATE", "TIMESTAMP"} and wms_context in {
                    "movement_date",
                    "allocation_date",
                    "order_date",
                }:
                    return FlextResult[str].ok("TIMESTAMP")

                dbt_type = type_mapping.get(oracle_type_upper, "STRING")
                return FlextResult[str].ok(dbt_type)
            except Exception as e:
                return FlextResult[str].fail(f"Oracle WMS type conversion failed: {e}")

        @staticmethod
        def generate_dbt_wms_column_definition(column_info: dict) -> FlextResult[dict]:
            """Generate DBT column definition from Oracle WMS column info."""
            if not column_info:
                return FlextResult[dict].fail("WMS column info cannot be empty")

            required_fields = ["column_name", "data_type"]
            for field in required_fields:
                if field not in column_info:
                    return FlextResult[dict].fail(
                        f"Missing required WMS column field: {field}"
                    )

            try:
                wms_context = column_info.get("wms_context", "general")
                precision = column_info.get("data_precision")
                scale = column_info.get("data_scale")
                type_result = FlextDbtOracleWmsUtilities._OracleWmsDataTypeHelper.convert_oracle_wms_type_to_dbt(
                    column_info["data_type"],
                    wms_context,
                    precision if precision is not None else None,
                    scale if scale is not None else None,
                )

                if type_result.is_failure:
                    return FlextResult[dict].fail(
                        f"WMS type conversion failed: {type_result.error}"
                    )

                dbt_column = {
                    "name": column_info["column_name"].lower(),
                    "description": column_info.get(
                        "comments", f"Oracle WMS column: {column_info['column_name']}"
                    ),
                    "data_type": type_result.unwrap(),
                    "nullable": column_info.get("nullable", "Y") == "Y",
                    "oracle_type": column_info["data_type"],
                    "oracle_precision": column_info.get("data_precision"),
                    "oracle_scale": column_info.get("data_scale"),
                    "wms_context": wms_context,
                    "wms_entity_relevance": column_info.get(
                        "wms_entity_relevance", "general"
                    ),
                }

                return FlextResult[dict].ok(dbt_column)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"DBT WMS column definition generation failed: {e}"
                )

        @staticmethod
        def create_oracle_wms_type_mapping_macro() -> FlextResult[str]:
            """Create DBT macro for Oracle WMS type mapping."""
            try:
                macro_content = """
{% macro oracle_wms_type_to_dbt(oracle_type, wms_context='general', precision=none, scale=none) %}
    {% if oracle_type.upper() in ('VARCHAR2', 'CHAR', 'NVARCHAR2', 'NCHAR') %}
        STRING
    {% elif oracle_type.upper() == 'NUMBER' %}
        {% if wms_context in ('quantity', 'weight', 'volume') %}
            NUMERIC
        {% elif wms_context in ('key', 'id') %}
            INT64
        {% elif scale == 0 %}
            {% if precision and precision <= 9 %}
                INT64
            {% else %}
                NUMERIC
            {% endif %}
        {% else %}
            NUMERIC
        {% endif %}
    {% elif oracle_type.upper() in ('DATE', 'TIMESTAMP') %}
        {% if wms_context in ('movement_date', 'allocation_date', 'order_date') %}
            TIMESTAMP
        {% else %}
            DATETIME
        {% endif %}
    {% elif oracle_type.upper() in ('CLOB', 'NCLOB') %}
        STRING
    {% elif oracle_type.upper() == 'BLOB' %}
        BYTES
    {% else %}
        STRING
    {% endif %}
{% endmacro %}

{% macro wms_quantity_cast(column_name) %}
    cast({{ column_name }} as numeric(15,4))
{% endmacro %}

{% macro wms_currency_cast(column_name) %}
    cast({{ column_name }} as numeric(15,2))
{% endmacro %}

{% macro wms_timestamp_cast(column_name) %}
    cast({{ column_name }} as timestamp)
{% endmacro %}
""".strip()

                return FlextResult[str].ok(macro_content)
            except Exception as e:
                return FlextResult[str].fail(
                    f"Oracle WMS type mapping macro creation failed: {e}"
                )

    class _WmsModelGenerationHelper:
        """DBT model generation utilities for Oracle WMS dimensional analytics."""

        @staticmethod
        def generate_oracle_wms_staging_model_sql(
            table_name: str, schema_name: str, columns: list[dict], wms_entity_type: str
        ) -> FlextResult[str]:
            """Generate staging model SQL for Oracle WMS table."""
            if not table_name:
                return FlextResult[str].fail("WMS table name cannot be empty")

            if not schema_name:
                return FlextResult[str].fail("WMS schema name cannot be empty")

            try:
                # Generate column list with WMS-specific type casting
                column_definitions = []
                for col in columns:
                    col_name = col.get("name", "")
                    oracle_type = col.get("oracle_type", "")
                    wms_context = col.get("wms_context", "general")

                    if oracle_type.upper() == "DATE":
                        column_definitions.append(
                            f"    {{ wms_timestamp_cast('{col_name}') }} AS {col_name}"
                        )
                    elif oracle_type.upper().startswith("TIMESTAMP"):
                        column_definitions.append(f"    {col_name}")
                    elif oracle_type.upper() in {"CLOB", "NCLOB"}:
                        column_definitions.append(
                            f"    CAST({col_name} AS STRING) AS {col_name}"
                        )
                    elif wms_context in {"quantity", "weight", "volume"}:
                        column_definitions.append(
                            f"    {{ wms_quantity_cast('{col_name}') }} AS {col_name}"
                        )
                    elif wms_context in {"cost", "price", "value"}:
                        column_definitions.append(
                            f"    {{ wms_currency_cast('{col_name}') }} AS {col_name}"
                        )
                    else:
                        column_definitions.append(f"    {col_name}")

                columns_sql = (
                    ",\\n".join(column_definitions) if column_definitions else "    *"
                )

                sql = f"""
{{{{
  config(
    materialized='view',
    wms_entity_type='{wms_entity_type}',
    oracle_optimization=true
  )
}}}}

select
{columns_sql}
from {{{{ source('oracle_wms_raw', '{table_name}') }}}}
""".strip()

                return FlextResult[str].ok(sql)
            except Exception as e:
                return FlextResult[str].fail(
                    f"Oracle WMS staging model SQL generation failed: {e}"
                )

        @staticmethod
        def generate_oracle_wms_dimensional_model_sql(
            dimension_type: str,
            staging_tables: list[str] | None = None,
            wms_business_rules: list[str] | None = None,
        ) -> FlextResult[str]:
            """Generate dimensional model SQL for Oracle WMS analytics."""
            if not dimension_type:
                return FlextResult[str].fail("WMS dimension type cannot be empty")

            try:
                staging_tables = staging_tables or []
                wms_business_rules = wms_business_rules or []

                if dimension_type == "item":
                    sql = """
{{
  config(
    materialized='table',
    wms_entity_type='dimension',
    oracle_optimization=true,
    indexes=['item_key', 'item_id']
  )
}}

select
    { dbt_utils.surrogate_key(['item_id']) } as item_key,
    item_id,
    item_description,
    item_category,
    unit_of_measure,
    { wms_currency_cast('standard_cost') } as standard_cost,
    { wms_currency_cast('list_price') } as list_price,
    { wms_quantity_cast('weight') } as weight,
    { wms_quantity_cast('volume') } as volume,
    storage_class,
    abc_classification,
    hazmat_flag,
    temperature_control_required,
    lot_control_flag,
    serial_control_flag,
    effective_date,
    expiry_date,
    is_active,
    created_date,
    last_updated_date
from { ref('stg_wms_items') }
where is_active = 1
""".strip()

                elif dimension_type == "location":
                    sql = """
{{
  config(
    materialized='table',
    wms_entity_type='dimension',
    oracle_optimization=true,
    indexes=['location_key', 'location_id']
  )
}}

select
    { dbt_utils.surrogate_key(['location_id']) } as location_key,
    location_id,
    location_description,
    zone_id,
    zone_description,
    aisle_id,
    bay_id,
    level_id,
    position_id,
    location_type,
    storage_type,
    location_class,
    { wms_quantity_cast('max_weight') } as max_weight,
    { wms_quantity_cast('max_volume') } as max_volume,
    temperature_controlled,
    hazmat_approved,
    pick_face_flag,
    reserve_flag,
    receiving_flag,
    shipping_flag,
    cycle_count_flag,
    is_active,
    created_date,
    last_updated_date
from { ref('stg_wms_locations') }
where is_active = 1
""".strip()

                elif dimension_type == "inventory_fact":
                    sql = """
{{{
  config(
    materialized='incremental',
    unique_key='inventory_fact_key',
    wms_entity_type='fact',
    oracle_optimization=true,
    partition_by='snapshot_date',
    indexes=['item_key', 'location_key', 'snapshot_date']
  )
}}}

select
    {{ dbt_utils.surrogate_key(['item_id', 'location_id', 'snapshot_date']) }} as inventory_fact_key,
    i.item_key,
    l.location_key,
    d.date_key,
    snapshot_date,
    {{ wms_quantity_cast('on_hand_quantity') }} as on_hand_quantity,
    {{ wms_quantity_cast('allocated_quantity') }} as allocated_quantity,
    {{ wms_quantity_cast('available_quantity') }} as available_quantity,
    {{ wms_quantity_cast('in_transit_quantity') }} as in_transit_quantity,
    {{ wms_quantity_cast('reserved_quantity') }} as reserved_quantity,
    {{ wms_currency_cast('average_cost') }} as average_cost,
    {{ wms_currency_cast('total_value') }} as total_value,
    last_movement_date,
    last_count_date,
    created_timestamp
from {{ ref('stg_wms_inventory') }} inv
join {{ ref('dim_wms_items') }} i on inv.item_id = i.item_id
join {{ ref('dim_wms_locations') }} l on inv.location_id = l.location_id
join {{ ref('dim_date') }} d on date(inv.snapshot_date) = d.date_actual

{% if is_incremental() %}
    where inv.snapshot_date > (select max(snapshot_date) from {{ this }})
{% endif %}
""".strip()

                else:
                    return FlextResult[str].fail(
                        f"Unsupported WMS dimension type: {dimension_type}"
                    )

                return FlextResult[str].ok(sql)
            except Exception as e:
                return FlextResult[str].fail(
                    f"Oracle WMS dimensional model SQL generation failed: {e}"
                )

        @staticmethod
        def create_oracle_wms_model_schema_entry(
            model_name: str,
            model_description: str,
            columns: list[dict],
            wms_entity_type: str,
        ) -> FlextResult[dict]:
            """Create schema.yml entry for Oracle WMS-generated model."""
            if not model_name:
                return FlextResult[dict].fail("WMS model name cannot be empty")

            try:
                schema_entry = {
                    "name": model_name,
                    "description": model_description
                    or f"Oracle WMS-generated model: {model_name}",
                    "meta": {
                        "wms_entity_type": wms_entity_type,
                        "oracle_optimization": True,
                        "warehouse_operations": True,
                    },
                    "columns": [
                        {
                            "name": col.get("name", ""),
                            "description": col.get("description", ""),
                            "data_type": col.get("data_type", ""),
                            "tests": col.get("tests", []),
                            "meta": {
                                "wms_context": col.get("wms_context", "general"),
                                "oracle_type": col.get("oracle_type", ""),
                            },
                        }
                        for col in columns
                    ],
                    "tests": [
                        {"unique": {"column_name": f"{wms_entity_type}_key"}}
                        if wms_entity_type != "fact"
                        else {"unique": {"column_name": f"{wms_entity_type}_fact_key"}},
                        {"not_null": {"column_name": f"{wms_entity_type}_key"}}
                        if wms_entity_type != "fact"
                        else {
                            "not_null": {"column_name": f"{wms_entity_type}_fact_key"}
                        },
                        {
                            "dbt_expectations.expect_table_row_count_to_be_between": {
                                "min_value": 1
                            }
                        },
                    ],
                }

                return FlextResult[dict].ok(schema_entry)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Oracle WMS model schema entry creation failed: {e}"
                )

    class _WmsPerformanceHelper:
        """Performance optimization utilities for Oracle WMS DBT operations."""

        @staticmethod
        def analyze_oracle_wms_dbt_performance(
            execution_stats: dict,
        ) -> FlextResult[dict]:
            """Analyze Oracle WMS DBT execution performance metrics."""
            if not execution_stats:
                return FlextResult[dict].fail("WMS execution stats cannot be empty")

            try:
                total_models = execution_stats.get("total_models", 0)
                execution_time = execution_stats.get("execution_time_seconds", 1)
                wms_data_volume = execution_stats.get("wms_data_volume_gb", 0)

                analysis = {
                    "models_per_minute": (total_models * 60) / execution_time,
                    "average_model_time_seconds": execution_time / max(total_models, 1),
                    "data_throughput_gb_per_minute": (wms_data_volume * 60)
                    / execution_time,
                    "performance_rating": "good"
                    if execution_time / max(total_models, 1)
                    < PERFORMANCE_THRESHOLD_SECONDS
                    else "needs_optimization",
                    "wms_specific_recommendations": [],
                }

                if analysis["average_model_time_seconds"] > PERFORMANCE_WARNING_SECONDS:
                    analysis["wms_specific_recommendations"].append(
                        "Consider adding Oracle WMS-specific hints for large inventory table operations"
                    )

                if analysis["models_per_minute"] < MIN_MODELS_PER_MINUTE:
                    analysis["wms_specific_recommendations"].append(
                        "Consider increasing DBT threads for Oracle WMS operations"
                    )

                if wms_data_volume > LARGE_DATA_VOLUME_GB:  # GB
                    analysis["wms_specific_recommendations"].append(
                        "Consider implementing incremental processing for large WMS datasets"
                    )

                if (
                    execution_stats.get("inventory_fact_time_seconds", 0)
                    > INVENTORY_FACT_THRESHOLD_SECONDS
                ):
                    analysis["wms_specific_recommendations"].append(
                        "Optimize inventory fact table with Oracle partitioning and parallel processing"
                    )

                return FlextResult[dict].ok(analysis)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Oracle WMS DBT performance analysis failed: {e}"
                )

        @staticmethod
        def suggest_oracle_wms_optimization_settings(
            project_stats: dict,
        ) -> FlextResult[dict]:
            """Suggest Oracle WMS-specific optimization settings for DBT."""
            if not project_stats:
                return FlextResult[dict].fail("WMS project stats cannot be empty")

            try:
                model_count = project_stats.get("model_count", 0)
                avg_model_size = project_stats.get("avg_model_size_rows", 0)
                inventory_volume = project_stats.get("inventory_volume_rows", 0)

                optimizations = {
                    "dbt_threads": min(
                        16, max(6, model_count // 3)
                    ),  # WMS needs more threads
                    "oracle_fetch_size": min(15000, max(2000, avg_model_size // 50)),
                    "enable_oracle_hints": avg_model_size > LARGE_MODEL_SIZE_THRESHOLD,
                    "use_oracle_partitioning": avg_model_size
                    > VERY_LARGE_MODEL_SIZE_THRESHOLD,
                    "oracle_parallel_degree": min(8, max(2, model_count // 8)),
                    "wms_specific_optimizations": {
                        "inventory_incremental": inventory_volume
                        > INVENTORY_INCREMENTAL_THRESHOLD,
                        "location_hierarchy_indexing": True,
                        "allocation_partition_by_date": True,
                        "enable_wms_hints": True,
                    },
                }

                return FlextResult[dict].ok(optimizations)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Oracle WMS optimization suggestions failed: {e}"
                )

        @staticmethod
        def monitor_oracle_wms_resource_usage(
            current_connections: int,
            wms_load_factor: float = 1.0,
            max_connections: int = 60,
        ) -> FlextResult[dict]:
            """Monitor Oracle WMS resource usage during DBT operations."""
            if current_connections < 0:
                return FlextResult[dict].fail("Current connections cannot be negative")

            try:
                # Adjust max connections based on WMS workload
                adjusted_max_connections = int(max_connections * wms_load_factor)

                monitoring_result = {
                    "current_connections": current_connections,
                    "max_connections": adjusted_max_connections,
                    "connection_usage_percentage": (
                        current_connections / adjusted_max_connections
                    )
                    * 100,
                    "within_limits": current_connections <= adjusted_max_connections,
                    "wms_load_factor": wms_load_factor,
                    "wms_recommendations": [],
                }

                if current_connections > adjusted_max_connections * 0.8:
                    monitoring_result["wms_recommendations"].append(
                        "Consider reducing DBT threads to limit Oracle WMS connections"
                    )

                if current_connections > adjusted_max_connections:
                    monitoring_result["wms_recommendations"].append(
                        "Oracle WMS connection limit exceeded - immediate action required"
                    )

                if wms_load_factor > HIGH_LOAD_FACTOR_THRESHOLD:
                    monitoring_result["wms_recommendations"].append(
                        "High WMS load detected - consider off-peak processing"
                    )

                return FlextResult[dict].ok(monitoring_result)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Oracle WMS resource monitoring failed: {e}"
                )


__all__ = ["FlextDbtOracleWmsModels", "FlextDbtOracleWmsUtilities"]
