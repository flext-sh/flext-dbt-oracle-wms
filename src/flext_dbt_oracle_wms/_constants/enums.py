"""DBT Oracle WMS constant enumerations."""

from __future__ import annotations

from enum import StrEnum, unique

from .base import FlextDbtOracleWmsConstantsBase


@unique
class DbtMaterialization(StrEnum):
    """DBT materialization types."""

    TABLE = FlextDbtOracleWmsConstantsBase.Dbt.Materialization.TABLE
    VIEW = FlextDbtOracleWmsConstantsBase.Dbt.Materialization.VIEW
    INCREMENTAL = FlextDbtOracleWmsConstantsBase.Dbt.Materialization.INCREMENTAL


__all__: list[str] = ["DbtMaterialization"]
