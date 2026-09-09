"""Utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from flext_meltano import u
from flext_oracle_wms import FlextOracleWmsUtilities

from ._utilities.base import FlextDbtOracleWmsUtilitiesBase
from ._utilities.model_builder import FlextDbtOracleWmsUtilitiesModelBuilder
from ._utilities.service import FlextDbtOracleWmsUtilitiesService
from ._utilities.transformer import FlextDbtOracleWmsUtilitiesTransformer


class FlextDbtOracleWmsUtilities(u, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms(
        FlextDbtOracleWmsUtilitiesBase,
        FlextDbtOracleWmsUtilitiesService,
        FlextDbtOracleWmsUtilitiesTransformer,
        FlextDbtOracleWmsUtilitiesModelBuilder,
    ):
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""


u = FlextDbtOracleWmsUtilities

__all__: list[str] = ["FlextDbtOracleWmsUtilities", "u"]
