"""Test type definitions for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsTypes, combining TestsFlextTypes with
FlextDbtOracleWmsTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import t as tests_t

from flext_dbt_oracle_wms import t


class TestsFlextDbtOracleWmsTypes(tests_t, t):
    """Test types combining FlextTestsTypes with flext-dbt-oracle-wms types."""

    class Tests(tests_t.Tests):
        """Test-scoped type aliases facade."""


t = TestsFlextDbtOracleWmsTypes

__all__: list[str] = ["TestsFlextDbtOracleWmsTypes", "t"]
