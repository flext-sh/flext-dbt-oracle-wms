"""Test utilities for flext-dbt-oracle-wms.

Provides FlextDbtOracleWmsTestUtilities, combining FlextTestsUtilities with
FlextDbtOracleWmsUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_dbt_oracle_wms import FlextDbtOracleWmsUtilities


class FlextDbtOracleWmsTestUtilities(FlextTestsUtilities, FlextDbtOracleWmsUtilities):
    """Test utilities combining FlextTestsUtilities with flext-dbt-oracle-wms utilities."""

    class DbtOracleWms(FlextDbtOracleWmsUtilities.DbtOracleWms):
        """DbtOracleWms test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = FlextDbtOracleWmsTestUtilities
__all__ = ["FlextDbtOracleWmsTestUtilities", "u"]
