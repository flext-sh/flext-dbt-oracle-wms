"""Constants used by the DBT Oracle WMS package."""

from __future__ import annotations

from flext_meltano import c
from flext_oracle_wms import FlextOracleWmsConstants

from ._constants.base import FlextDbtOracleWmsConstantsBase
from ._constants.enums import FlextDbtOracleWmsConstantsEnums


class FlextDbtOracleWmsConstants(c, FlextOracleWmsConstants):
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
