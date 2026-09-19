"""DBT Oracle WMS constant enumerations."""

from __future__ import annotations

from enum import StrEnum, unique


class FlextDbtOracleWmsConstantsEnums:
    """DBT Oracle WMS enumerations composed into the constants facade."""

    class Dbt:
        """DBT enumeration namespace."""

        @unique
        class Materialization(StrEnum):
            """DBT materialization types."""

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"


__all__: list[str] = ["FlextDbtOracleWmsConstantsEnums"]
