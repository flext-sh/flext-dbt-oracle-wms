# AUTO-GENERATED FILE — Regenerate with: make gen
"""Domain models for DBT Oracle WMS workflows.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m as flext_meltano_m
from flext_oracle_wms import m as flext_oracle_wms_m

from flext_dbt_oracle_wms._models import (
    FlextDbtOracleWmsModelsBase,
    FlextDbtOracleWmsModelsConnection,
    FlextDbtOracleWmsModelsDbt,
    FlextDbtOracleWmsModelsItems,
    FlextDbtOracleWmsModelsWorkflow,
)


class FlextDbtOracleWmsModels(flext_meltano_m, flext_oracle_wms_m):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms(
        FlextDbtOracleWmsModelsBase,
        FlextDbtOracleWmsModelsConnection,
        FlextDbtOracleWmsModelsDbt,
        FlextDbtOracleWmsModelsItems,
        FlextDbtOracleWmsModelsWorkflow,
    ):
        """DBT Oracle WMS domain namespace."""


m = FlextDbtOracleWmsModels
__all__: list[str] = ["FlextDbtOracleWmsModels", "m"]
