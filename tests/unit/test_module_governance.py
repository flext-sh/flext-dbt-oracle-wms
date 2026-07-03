"""Behavior contract for flext_dbt_oracle_wms public entrypoints."""

from __future__ import annotations

from flext_tests import tm

from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms


class TestsFlextDbtOracleWmsModuleGovernance:
    """Behavior contract for flext_dbt_oracle_wms package exports."""

    def test_public_entrypoints_are_importable_and_callable(self) -> None:
        tm.that(FlextDbtOracleWms.__name__, eq="FlextDbtOracleWms")
        tm.that(callable(main), eq=True)
        tm.that(FlextDbtOracleWmsCliService.__name__, eq="FlextDbtOracleWmsCliService")
