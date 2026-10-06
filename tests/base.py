"""Service base for flext-dbt-oracle-wms tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_tests import FlextTestsServiceBase

from flext_dbt_oracle_wms import m
from tests.settings import TestsFlextDbtOracleWmsSettings


class TestsFlextDbtOracleWmsServiceBase(FlextTestsServiceBase):
    """DBT Oracle WMS test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type (canonical
    # pattern per flext-cli tests/base.py).
    @classmethod
    @override
    def runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtOracleWmsSettings)


s = TestsFlextDbtOracleWmsServiceBase

__all__: list[str] = ["TestsFlextDbtOracleWmsServiceBase", "s"]
