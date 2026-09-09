"""Domain models for DBT Oracle WMS workflows."""

from __future__ import annotations

from flext_meltano import m
from flext_oracle_wms import FlextOracleWmsModels

from ._models.base import FlextDbtOracleWmsModelsBase
from ._models.connection import FlextDbtOracleWmsModelsConnection
from ._models.dbt import FlextDbtOracleWmsModelsDbt
from ._models.items import FlextDbtOracleWmsModelsItems
from ._models.workflow import FlextDbtOracleWmsModelsWorkflow


class FlextDbtOracleWmsModels(m, FlextOracleWmsModels):
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
