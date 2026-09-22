"""Test models for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsModels, combining TestsFlextModels with
FlextDbtOracleWmsModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import m as tests_m

from flext_dbt_oracle_wms import m


class TestsFlextDbtOracleWmsModels(tests_m, m):
    """Test models combining FlextTestsModels with flext-dbt-oracle-wms models."""

    class DbtOracleWms(m.DbtOracleWms):
        """DbtOracleWms test models namespace."""

        class Tests:
            """Test-specific models."""

    class Tests(tests_m.Tests):
        """Test-scoped models facade."""


m = TestsFlextDbtOracleWmsModels

__all__: list[str] = ["TestsFlextDbtOracleWmsModels", "m"]
