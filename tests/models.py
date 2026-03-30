"""Test models for flext-dbt-oracle-wms.

Provides FlextDbtOracleWmsTestModels, combining FlextTestsModels with
FlextDbtOracleWmsModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_oracle_wms import FlextDbtOracleWmsModels


class FlextDbtOracleWmsTestModels(FlextTestsModels, FlextDbtOracleWmsModels):
    """Test models combining FlextTestsModels with flext-dbt-oracle-wms models."""

    class Tests(FlextTestsModels.Tests):
        """Project-specific test fixtures namespace."""

        class DbtOracleWms:
            """DBT Oracle WMS-specific test fixtures."""


m = FlextDbtOracleWmsTestModels

__all__ = [
    "FlextDbtOracleWmsTestModels",
    "m",
]
