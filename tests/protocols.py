"""Test protocol definitions for flext-dbt-oracle-wms.

Provides FlextDbtOracleWmsTestProtocols, combining FlextTestsProtocols with
FlextDbtOracleWmsProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols


class FlextDbtOracleWmsTestProtocols(FlextTestsProtocols, FlextDbtOracleWmsProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtOracleWmsProtocols."""

    class DbtOracleWms(FlextDbtOracleWmsProtocols.DbtOracleWms):
        """DbtOracleWms domain protocols extending project protocols."""

        class Tests:
            """DbtOracleWms-specific test protocols."""


p = FlextDbtOracleWmsTestProtocols
__all__ = ["FlextDbtOracleWmsTestProtocols", "p"]
