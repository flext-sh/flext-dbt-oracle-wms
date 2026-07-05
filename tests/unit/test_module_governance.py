"""Behavior contract for flext_dbt_oracle_wms public entrypoints."""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms

__all__: list[str] = ["TestsFlextDbtOracleWmsModuleGovernance"]


class TestsFlextDbtOracleWmsModuleGovernance:
    """Behavior contract for flext_dbt_oracle_wms package entrypoints."""

    @pytest.mark.parametrize(
        ("command", "expected_exit_code"),
        [
            ("info", 0),
            ("unknown", 1),
            ("", 1),
        ],
    )
    def test_execute_command_maps_command_to_exit_code(
        self,
        command: str,
        expected_exit_code: int,
    ) -> None:
        service = FlextDbtOracleWmsCliService()
        tm.that(service.execute_command(command), eq=expected_exit_code)

    def test_handle_info_returns_success_with_package_label(self) -> None:
        service = FlextDbtOracleWmsCliService()
        result = service.handle_info()
        tm.that(result.success, eq=True)
        tm.that(result.value, eq="FLEXT DBT Oracle WMS")

    @pytest.mark.parametrize(
        "argv",
        [
            [],
            ["info"],
        ],
    )
    def test_main_entrypoint_defaults_to_info_success(
        self,
        argv: list[str],
    ) -> None:
        tm.that(main(argv), eq=0)

    def test_module_main_matches_service_main(self) -> None:
        service = FlextDbtOracleWmsCliService()
        tm.that(main(["info"]), eq=service.main(["info"]))

    def test_public_facade_constructs_with_defaults(self) -> None:
        facade = FlextDbtOracleWms()
        tm.that(facade.settings.oracle_wms_environment, eq="development")
