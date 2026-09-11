"""Test type definitions for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsTypes, combining TestsFlextTypes with
FlextDbtOracleWmsTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_oracle_wms.typings import FlextDbtOracleWmsTypes


class TestsFlextDbtOracleWmsTypes(FlextTestsTypes, FlextDbtOracleWmsTypes):
    """Test types combining FlextTestsTypes with flext-dbt-oracle-wms types."""


t = TestsFlextDbtOracleWmsTypes

__all__: list[str] = ["TestsFlextDbtOracleWmsTypes", "t"]
