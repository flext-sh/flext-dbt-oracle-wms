"""Test constants for flext-dbt-oracle-wms tests.

Provides TestsFlextDbtOracleWmsConstants, extending FlextTestsConstants with
flext-dbt-oracle-wms-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import c as tests_c

from flext_dbt_oracle_wms import c


class TestsFlextDbtOracleWmsConstants(c, tests_c):
    """Test constants for flext-dbt-oracle-wms."""

    class Tests(tests_c.Tests):
        """Test-scoped constants facade."""


c = TestsFlextDbtOracleWmsConstants

__all__: list[str] = ["TestsFlextDbtOracleWmsConstants", "c"]
