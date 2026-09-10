"""DBT Oracle WMS constant enumerations."""

from __future__ import annotations

from enum import StrEnum, unique


@unique
class _Materialization(StrEnum):
    """DBT materialization types."""

    TABLE = "table"
    VIEW = "view"
    INCREMENTAL = "incremental"


class FlextDbtOracleWmsConstantsEnums:
    """DBT Oracle WMS enumerations composed into the constants facade."""

    class Dbt:
        """DBT enumeration namespace."""

        Materialization = _Materialization


__all__: list[str] = ["FlextDbtOracleWmsConstantsEnums"]
