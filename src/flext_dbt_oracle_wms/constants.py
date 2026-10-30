# AUTO-GENERATED FILE — Regenerate with: make gen
"""Constants used by the DBT Oracle WMS package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/constants
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import c as flext_meltano_c
from flext_oracle_wms import c as flext_oracle_wms_c

from flext_dbt_oracle_wms._constants import (
    FlextDbtOracleWmsConstantsBase,
    FlextDbtOracleWmsConstantsEnums,
)


class FlextDbtOracleWmsConstants(flext_meltano_c, flext_oracle_wms_c):
    """Constants for DBT Oracle WMS with dual Meltano and WMS domain inheritance."""

    class DbtOracleWms(FlextDbtOracleWmsConstantsBase, FlextDbtOracleWmsConstantsEnums):
        """DBT Oracle WMS project-specific constants."""

        class Dbt(
            FlextDbtOracleWmsConstantsEnums.Dbt,
            FlextDbtOracleWmsConstantsBase.Dbt,
        ):
            """Merged DBT constants combining enum values and base project metadata."""


c = FlextDbtOracleWmsConstants
__all__: list[str] = ["FlextDbtOracleWmsConstants", "c"]
