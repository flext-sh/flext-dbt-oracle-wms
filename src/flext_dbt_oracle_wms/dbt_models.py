"""DBT Oracle WMS model definitions and transformers."""

from __future__ import annotations

from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels


# Re-export from models facade
FlextDbtOracleWmsItemDimension = FlextDbtOracleWmsModels.FlextDbtOracleWmsItemDimension
FlextDbtOracleWmsInventoryFact = FlextDbtOracleWmsModels.FlextDbtOracleWmsInventoryFact
FlextDbtOracleWmsLocationDimension = FlextDbtOracleWmsModels.FlextDbtOracleWmsLocationDimension
FlextDbtOracleWmsShipmentFact = FlextDbtOracleWmsModels.FlextDbtOracleWmsShipmentFact
FlextDbtOracleWmsTransformer = FlextDbtOracleWmsModels.FlextDbtOracleWmsTransformer


__all__ = [
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
]
