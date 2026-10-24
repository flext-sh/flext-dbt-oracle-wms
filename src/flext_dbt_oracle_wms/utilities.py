# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utility helpers for DBT Oracle WMS operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from flext_dbt_oracle_wms._utilities import (
    FlextDbtOracleWmsUtilitiesBase,
    FlextDbtOracleWmsUtilitiesModelBuilder,
    FlextDbtOracleWmsUtilitiesService,
    FlextDbtOracleWmsUtilitiesTransformer,
)


class FlextDbtOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace with utility helpers for extraction and modeling."""

    class DbtOracleWms(
        FlextDbtOracleWmsUtilitiesBase,
        FlextDbtOracleWmsUtilitiesModelBuilder,
        FlextDbtOracleWmsUtilitiesService,
        FlextDbtOracleWmsUtilitiesTransformer,
    ):
        """Oracle WMS extraction and service helpers — u.DbtOracleWms.*."""


u = FlextDbtOracleWmsUtilities

__all__: list[str] = ["FlextDbtOracleWmsUtilities", "u"]
