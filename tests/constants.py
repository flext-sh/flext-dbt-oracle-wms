"""Test constants for flext-dbt-oracle-wms tests.

Provides TestsFlextDbtOracleWmsConstants, extending FlextTestsConstants with
flext-dbt-oracle-wms-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_dbt_oracle_wms import FlextDbtOracleWmsConstants


class TestsFlextDbtOracleWmsConstants(FlextDbtOracleWmsConstants, FlextTestsConstants):
    """Test constants for flext-dbt-oracle-wms."""

    class Tests(FlextTestsConstants.Tests):
        """Test-scoped constants facade."""


c = TestsFlextDbtOracleWmsConstants

__all__: list[str] = ["TestsFlextDbtOracleWmsConstants", "c"]
