"""Base constants for DBT Oracle WMS — project metadata and DBT constants."""

from __future__ import annotations

from typing import Final


class FlextDbtOracleWmsConstantsBase:
    """Base DBT Oracle WMS constants: metadata and DBT constants."""

    class Dbt:
        """DBT constants and enum values."""

        PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"

        class Materialization:
            """DBT materialization types."""

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"


__all__: list[str] = ["FlextDbtOracleWmsConstantsBase"]
