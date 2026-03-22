"""Test type definitions for flext-dbt-oracle-wms.

Provides FlextDbtOracleWmsTestTypes, combining FlextTestsTypes with
FlextDbtOracleWmsTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_oracle_wms import FlextDbtOracleWmsTypes


class FlextDbtOracleWmsTestTypes(FlextTestsTypes, FlextDbtOracleWmsTypes):
    """Test types combining FlextTestsTypes with flext-dbt-oracle-wms types."""


t = FlextDbtOracleWmsTestTypes
__all__ = ["FlextDbtOracleWmsTestTypes", "t"]
