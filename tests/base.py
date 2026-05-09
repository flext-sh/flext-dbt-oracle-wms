"""Service base for flext-dbt-oracle-wms tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_dbt_oracle_wms import m
from tests.settings import TestsFlextDbtOracleWmsSettings


class TestsFlextDbtOracleWmsServiceBase(tests_s):
    """DBT Oracle WMS test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextDbtOracleWmsSettings:
        """Return the typed DBT Oracle WMS+Tests settings singleton."""
        return TestsFlextDbtOracleWmsSettings.fetch_global()

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtOracleWmsSettings)


s = TestsFlextDbtOracleWmsServiceBase

__all__: list[str] = ["TestsFlextDbtOracleWmsServiceBase", "s"]
