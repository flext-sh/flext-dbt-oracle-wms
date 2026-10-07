"""Base constants for DBT Oracle WMS — project metadata and DBT constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_constants/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextDbtOracleWmsConstantsBase:
    """Base DBT Oracle WMS constants: metadata and DBT constants."""

    class Dbt:
        """DBT constants and enum values."""

        PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"


__all__: list[str] = ["FlextDbtOracleWmsConstantsBase"]
