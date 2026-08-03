"""Test utilities for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsUtilities, combining TestsFlextUtilities with
FlextDbtOracleWmsUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms import FlextDbtOracleWmsUtilities
from flext_tests import FlextTestsUtilities


class TestsFlextDbtOracleWmsUtilities(FlextTestsUtilities, FlextDbtOracleWmsUtilities):
    """Test utilities combining FlextTestsUtilities with flext-dbt-oracle-wms utilities."""

    class DbtOracleWms(FlextDbtOracleWmsUtilities.DbtOracleWms):
        """DbtOracleWms test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = TestsFlextDbtOracleWmsUtilities

__all__: list[str] = ["TestsFlextDbtOracleWmsUtilities", "u"]
