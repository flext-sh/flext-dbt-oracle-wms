"""Test protocol definitions for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsProtocols, combining TestsFlextProtocols with
FlextDbtOracleWmsProtocols for test-specific protocol definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from tests import FlextDbtOracleWmsProtocols


class TestsFlextDbtOracleWmsProtocols(FlextTestsProtocols, FlextDbtOracleWmsProtocols):
    """Test protocols combining TestsFlextProtocols and FlextDbtOracleWmsProtocols."""

    class Tests(FlextTestsProtocols.Tests):
        """DbtOracleWms-specific test protocols."""


p = TestsFlextDbtOracleWmsProtocols

__all__: list[str] = ["TestsFlextDbtOracleWmsProtocols", "p"]
