"""DBT Oracle WMS constants: project metadata, materializations and templates.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_constants/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final


class FlextDbtOracleWmsConstantsBase:
    """Base DBT Oracle WMS constants composed into the constants facade."""

    class Dbt:
        """DBT project metadata, materializations and model templates."""

        PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"

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


__all__: list[str] = ["FlextDbtOracleWmsConstantsBase"]
