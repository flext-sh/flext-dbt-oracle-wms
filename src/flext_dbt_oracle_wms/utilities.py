"""Utility helpers for DBT Oracle WMS operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from flext_dbt_oracle_wms._utilities.base import FlextDbtOracleWmsUtilitiesBase
from flext_dbt_oracle_wms._utilities.model_builder import (
    FlextDbtOracleWmsUtilitiesModelBuilder,
)
from flext_dbt_oracle_wms._utilities.service import FlextDbtOracleWmsUtilitiesService
from flext_dbt_oracle_wms._utilities.transformer import (
    FlextDbtOracleWmsUtilitiesTransformer,
)


class FlextDbtOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
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
