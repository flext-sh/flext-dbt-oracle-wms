"""Test protocol definitions for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsProtocols, combining p with
FlextDbtOracleWmsProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols


class TestsFlextDbtOracleWmsProtocols(p):
    """Test protocols combining p and FlextDbtOracleWmsProtocols.

    Provides access to:
    - p.Tests.Docker.* (from p)
    - p.Tests.Factory.* (from p)
    - p.DbtOracleWms.* (from FlextDbtOracleWmsProtocols)
    """

    class DbtOracleWms(FlextDbtOracleWmsProtocols):
        """DbtOracleWms domain protocols extending project protocols."""

        class Tests:
            """DbtOracleWms-specific test protocols."""


p = TestsFlextDbtOracleWmsProtocols
__all__ = ["TestsFlextDbtOracleWmsProtocols", "p"]
