"""Test protocol definitions for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsProtocols, combining TestsFlextProtocols with
FlextDbtOracleWmsProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p as tests_p

from flext_dbt_oracle_wms import p


class TestsFlextDbtOracleWmsProtocols(tests_p, p):
    """Test protocols combining TestsFlextProtocols and FlextDbtOracleWmsProtocols."""

    class DbtOracleWms(p.DbtOracleWms):
        """DbtOracleWms domain protocols extending project protocols."""

        class Tests:
            """DbtOracleWms-specific test protocols."""

    class Tests(tests_p.Tests):
        """Test-scoped protocol contracts facade."""


p = TestsFlextDbtOracleWmsProtocols

__all__: list[str] = ["TestsFlextDbtOracleWmsProtocols", "p"]
