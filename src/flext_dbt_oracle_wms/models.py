"""Domain models for DBT Oracle WMS workflows.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels
from flext_oracle_wms import FlextOracleWmsModels

from flext_dbt_oracle_wms._models.base import FlextDbtOracleWmsModelsBase
from flext_dbt_oracle_wms._models.connection import FlextDbtOracleWmsModelsConnection
from flext_dbt_oracle_wms._models.dbt import FlextDbtOracleWmsModelsDbt
from flext_dbt_oracle_wms._models.items import FlextDbtOracleWmsModelsItems
from flext_dbt_oracle_wms._models.workflow import FlextDbtOracleWmsModelsWorkflow


class FlextDbtOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for DBT Oracle WMS objects."""

    class DbtOracleWms(
        FlextDbtOracleWmsModelsBase,
        FlextDbtOracleWmsModelsItems,
        FlextDbtOracleWmsModelsDbt,
        FlextDbtOracleWmsModelsWorkflow,
        FlextDbtOracleWmsModelsConnection,
    ):
        """DBT Oracle WMS domain namespace."""


m = FlextDbtOracleWmsModels

__all__: list[str] = ["FlextDbtOracleWmsModels", "m"]
