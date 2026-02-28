"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities


class FlextDbtOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms:
        """Oracle WMS extraction helpers."""

        @staticmethod
        def extract_wms_inventory_data(
            extraction_config: Mapping[str, t.GeneralValueType],
        ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
            """Return basic extraction metadata for inventory loads."""
            return FlextResult[dict[str, t.GeneralValueType]].ok({
                "extraction_config": extraction_config,
                "inventory_records": [],
            })

    class WmsDimensionalModeling:
        """DBT SQL generation helpers for dimensional models."""

        @staticmethod
        def generate_wms_inventory_dimension(
            inventory_config: Mapping[str, t.GeneralValueType],
        ) -> FlextResult[str]:
            """Generate SQL for inventory dimension model."""
            _ = inventory_config
            return FlextResult[str].ok("select * from {{ ref('stg_wms_inventory') }}")


__all__ = ["FlextDbtOracleWmsUtilities", "u"]


u = FlextDbtOracleWmsUtilities
