"""DBT Oracle WMS constant enumerations."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final


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

        # dbt Jinja template, not executable SQL: `source()` is resolved by dbt at
        # compile time against the project's declared sources, so the value never
        # reaches a database driver as a literal.
        STAGING_SELECT_TEMPLATE: Final[str] = (
            "select * from {{{{ source('oracle_wms', '{source}') }}}}"
        )


__all__: list[str] = ["FlextDbtOracleWmsConstantsEnums"]
