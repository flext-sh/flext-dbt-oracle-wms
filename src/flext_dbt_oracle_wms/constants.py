"""Constants used by the DBT Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_meltano import FlextMeltanoConstants
from flext_oracle_wms import FlextOracleWmsConstants


class FlextDbtOracleWmsConstants(FlextMeltanoConstants, FlextOracleWmsConstants):
    """Constants for DBT Oracle WMS with dual inheritance from Meltano and WMS domains."""

    class DbtOracleWms:
        """DBT Oracle WMS project-specific constants."""

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

            MATERIALIZATIONS: Final[tuple[str, ...]] = tuple(
                member.value for member in Materialization.__members__.values()
            )


c = FlextDbtOracleWmsConstants

__all__ = ["FlextDbtOracleWmsConstants", "c"]
