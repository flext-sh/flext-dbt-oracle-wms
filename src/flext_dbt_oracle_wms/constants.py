"""Constants used by the DBT Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_meltano import c
from flext_oracle_wms import FlextOracleWmsConstants


class FlextDbtOracleWmsConstants(c, FlextOracleWmsConstants):
    """Constants for DBT Oracle WMS with dual inheritance from Meltano and WMS domains."""

    class DbtOracleWms:
        """DBT Oracle WMS project-specific constants."""

        class Dbt:
            """DBT constants and enum values."""

            PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"

            @unique
            class Materialization(StrEnum):
                """DBT materialization types."""

                TABLE = "table"
                VIEW = "view"
                INCREMENTAL = "incremental"


c = FlextDbtOracleWmsConstants

__all__: list[str] = ["FlextDbtOracleWmsConstants", "c"]
