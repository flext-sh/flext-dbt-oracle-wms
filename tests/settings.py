"""Runtime settings for flext-dbt-oracle-wms tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/settings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings


class TestsFlextDbtOracleWmsSettings(FlextDbtOracleWmsSettings, FlextTestsSettings):
    """DBT Oracle WMS settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtOracleWmsSettings"]
