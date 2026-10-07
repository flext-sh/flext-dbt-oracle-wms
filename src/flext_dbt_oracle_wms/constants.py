"""Constants used by the DBT Oracle WMS package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/constants
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants
from flext_oracle_wms import FlextOracleWmsConstants

from flext_dbt_oracle_wms._constants.base import FlextDbtOracleWmsConstantsBase
from flext_dbt_oracle_wms._constants.enums import FlextDbtOracleWmsConstantsEnums


class FlextDbtOracleWmsConstants(FlextMeltanoConstants, FlextOracleWmsConstants):
    """Constants for DBT Oracle WMS with dual inheritance from Meltano and WMS domains."""

    class DbtOracleWms(FlextDbtOracleWmsConstantsEnums, FlextDbtOracleWmsConstantsBase):
        """DBT Oracle WMS project-specific constants."""

        class Dbt(
            FlextDbtOracleWmsConstantsEnums.Dbt,
            FlextDbtOracleWmsConstantsBase.Dbt,
        ):
            """Merged DBT constants combining enum values and base project metadata."""


c = FlextDbtOracleWmsConstants

__all__: list[str] = ["FlextDbtOracleWmsConstants", "c"]
