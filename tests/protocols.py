"""Test protocol definitions for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsProtocols, combining FlextTestsProtocols with
FlextDbtOracleWmsProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms.protocols import FlextDbtOracleWmsProtocols
from flext_tests import FlextTestsProtocols


class TestsFlextDbtOracleWmsProtocols(FlextTestsProtocols, FlextDbtOracleWmsProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtOracleWmsProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.DbtOracleWms.* (from FlextDbtOracleWmsProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with DbtOracleWms-specific protocols.
        """

        class DbtOracleWms:
            """DbtOracleWms-specific test protocols."""


# Runtime aliases
p = TestsFlextDbtOracleWmsProtocols
p = TestsFlextDbtOracleWmsProtocols

__all__ = ["TestsFlextDbtOracleWmsProtocols", "p"]
