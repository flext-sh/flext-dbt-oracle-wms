"""Constants used by the DBT Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_meltano import FlextMeltanoConstants

from flext_dbt_oracle_wms import t


class FlextDbtOracleWmsConstants(FlextMeltanoConstants):
    """Constants for DBT Oracle WMS with dual inheritance from Meltano and WMS domains."""

    class DbtOracleWms:
        """DBT Oracle WMS project-specific constants."""

        class Core:
            """Core package metadata constants."""

            NAME: Final[str] = "flext-dbt-oracle-wms"
            VERSION: Final[str] = "0.10.0-dev"

        class Dbt:
            """DBT constants and enum values."""

            PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"
            PROFILE: Final[str] = "flext_oracle_wms"
            SCHEMA_PREFIX: Final[str] = "wms"

            @unique
            class Materialization(StrEnum):
                """DBT materialization types."""

                TABLE = "table"
                VIEW = "view"
                INCREMENTAL = "incremental"

            @unique
            class TestType(StrEnum):
                """DBT test types."""

                UNIQUE = "unique"
                NOT_NULL = "not_null"
                RELATIONSHIPS = "relationships"

            MATERIALIZATIONS: Final[tuple[str, ...]] = tuple(
                member.value for member in Materialization.__members__.values()
            )
            TEST_TYPES: Final[tuple[str, ...]] = tuple(
                member.value for member in TestType.__members__.values()
            )

        class Entities:
            """Oracle WMS entity constants."""

            WMS_ENTITIES: Final[tuple[str, ...]] = (
                "inventory",
                "location",
                "allocation",
                "order",
                "item",
                "shipment",
                "receipt",
                "task",
                "wave",
            )

        class DbtOracleWmsProcessing:
            """Processing constants for DBT Oracle WMS workloads."""

            DEFAULT_BATCH_SIZE: Final[int] = FlextMeltanoConstants.DEFAULT_BATCH_SIZE
            INCREMENTAL_LOOKBACK_DAYS: Final[int] = 7
            DATA_QUALITY_THRESHOLD: Final[float] = 0.95
            HIGH_VOLUME_THRESHOLD: Final[int] = 100
            MEDIUM_VOLUME_THRESHOLD: Final[int] = 10
            HIGH_FREQUENCY_THRESHOLD: Final[int] = 1000

            @unique
            class ProcessingStatus(StrEnum):
                """Pipeline processing status values."""

                PENDING = "pending"
                PROCESSING = "processing"
                COMPLETED = "completed"
                FAILED = "failed"

            @unique
            class RunStatus(StrEnum):
                """DBT run status values."""

                SUCCESS = "success"
                ERROR = "error"
                SKIPPED = "skipped"
                RUNNING = "running"
                QUEUED = "queued"

            PROCESSING_STATUSES: Final[tuple[str, ...]] = tuple(
                member.value for member in ProcessingStatus.__members__.values()
            )

        class Configuration:
            """Default runtime configuration values."""

            DEFAULT_CONFIG: Final[dict[str, t.ContainerValue | None]] = {
                "project_name": "flext_dbt_oracle_wms",
                "profile": "flext_oracle_wms",
                "schema_prefix": "wms",
                "batch_size": 1000,
                "incremental_lookback_days": 7,
                "data_quality_threshold": 0.95,
            }

        @unique
        class DbtTargets(StrEnum):
            """Valid DBT target environments."""

            DEV = "dev"
            DEVELOPMENT = "development"
            STAGING = "staging"
            PROD = "prod"
            PRODUCTION = "production"
            TEST = "test"
            LOCAL = "local"

        @unique
        class OracleWmsEnvironments(StrEnum):
            """Valid Oracle WMS environments."""

            DEV = "dev"
            TEST = "test"
            STAGING = "staging"
            PROD = "prod"
            PRODUCTION = "production"

    @unique
    class ProjectType(StrEnum):
        """Project-type identifiers for dbt Oracle WMS packages."""

        LIBRARY = "library"
        APPLICATION = "application"
        SERVICE = "service"
        DBT_ORACLE_WMS = "dbt-oracle-wms"
        WMS_TRANSFORM = "wms-transform"
        WMS_ANALYTICS = "wms-analytics"
        WMS_DBT_MODELS = "wms-dbt-models"
        DBT_WMS_PROJECT = "dbt-wms-project"
        WMS_DIMENSIONAL = "wms-dimensional"
        WMS_WAREHOUSE = "wms-warehouse"
        WMS_ETL = "wms-etl"
        DBT_WMS_PIPELINE = "dbt-wms-pipeline"
        WMS_REPORTING = "wms-reporting"
        WMS_DBT = "wms-dbt"
        WMS_DATA_WAREHOUSE = "wms-data-warehouse"
        WMS_INVENTORY_ANALYTICS = "wms-inventory-analytics"
        WMS_ALLOCATION_ANALYTICS = "wms-allocation-analytics"
        WMS_OPERATIONAL_REPORTING = "wms-operational-reporting"
        WMS_PERFORMANCE_ANALYTICS = "wms-performance-analytics"
        WAREHOUSE_BI = "warehouse-bi"
        WMS_COMPLIANCE_REPORTING = "wms-compliance-reporting"


c = FlextDbtOracleWmsConstants

__all__ = ["FlextDbtOracleWmsConstants", "c"]
