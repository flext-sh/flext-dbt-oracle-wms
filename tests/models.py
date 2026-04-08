"""Test models for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsModels, combining TestsFlextModels with
FlextDbtOracleWmsModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_oracle_wms import FlextDbtOracleWmsModels


class TestsFlextDbtOracleWmsModels(FlextTestsModels, FlextDbtOracleWmsModels):
    """Test models combining FlextTestsModels with flext-dbt-oracle-wms models."""

    class DbtOracleWms(FlextDbtOracleWmsModels.DbtOracleWms):
        """DbtOracleWms test models namespace."""

        class Tests:
            """Test-specific models."""


m = TestsFlextDbtOracleWmsModels

__all__ = [
    "TestsFlextDbtOracleWmsModels",
    "m",
]
