"""Constants used by the DBT Oracle WMS package."""

from __future__ import annotations

from typing import Final

from flext_meltano import c
from flext_oracle_wms import FlextOracleWmsConstants

from ._constants.base import FlextDbtOracleWmsConstantsBase
from ._constants.enums import DbtMaterialization


class FlextDbtOracleWmsConstants(c, FlextOracleWmsConstants):
    """Constants for DBT Oracle WMS with dual inheritance from Meltano and WMS domains."""

    class DbtOracleWms(FlextDbtOracleWmsConstantsBase, FlextOracleWmsConstants):
        """DBT Oracle WMS project-specific constants."""

        class Dbt:
            """DBT constants and enum values."""

            PROJECT_NAME: Final[str] = "flext_dbt_oracle_wms"
            Materialization = DbtMaterialization


c = FlextDbtOracleWmsConstants

__all__: list[str] = ["FlextDbtOracleWmsConstants", "c"]
