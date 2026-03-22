"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextLogger

from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels

logger = FlextLogger(__name__)


# Re-export from models facade
FlextDbtOracleWmsSettings = FlextDbtOracleWmsModels.FlextDbtOracleWmsSettings


__all__ = ["FlextDbtOracleWmsSettings"]
