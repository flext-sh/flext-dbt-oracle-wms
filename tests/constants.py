"""Test constants for flext-dbt-oracle-wms tests.

Provides FlextDbtOracleWmsTestConstants, extending FlextTestsConstants with
flext-dbt-oracle-wms-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants


class FlextDbtOracleWmsTestConstants(FlextTestsConstants):
    """Test constants for flext-dbt-oracle-wms."""


c = FlextDbtOracleWmsTestConstants
__all__ = ["FlextDbtOracleWmsTestConstants", "c"]
