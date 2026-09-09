"""Behavior contract for flext_dbt_oracle_wms CLI service — public API only."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tests import tm

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, m, r
from flext_dbt_oracle_wms.api import FlextDbtOracleWms
from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from flext_dbt_oracle_wms.utilities import FlextDbtOracleWmsClient
from tests import u

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import t


def _build_public_facade(
    *, pipeline_should_fail: bool = False
) -> t.Triple[
    FlextDbtOracleWms,
    u.DbtOracleWms.Tests.ScriptedWmsClient,
    u.DbtOracleWms.Tests.ScriptedDbtRunner,
]:
    settings = FlextDbtOracleWmsSettings(oracle_wms_base_url="https://wms.example.com")
    wms = u.DbtOracleWms.Tests.ScriptedWmsClient()
    runner = u.DbtOracleWms.Tests.ScriptedDbtRunner(
        r[m.Meltano.CommandExecutionResult].fail("dbt run failed")
        if pipeline_should_fail
        else None
    )
    client = FlextDbtOracleWmsClient(settings, wms_client=wms, meltano_runner=runner)
    return FlextDbtOracleWms(settings=settings, client=client), wms, runner


class TestsFlextDbtOracleWmsCli:
    """Behavior contract for FlextDbtOracleWmsCliService public commands."""

    def test_main_with_empty_args_returns_info_exit_code(self) -> None:
        facade, _, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main([]), eq=0)

    def test_execute_command_discover_returns_success(self) -> None:
        facade, _, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("discover"), eq=0)

    def test_main_extract_with_entity_invokes_client(self) -> None:
        facade, wms, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main(["extract", "items"]), eq=0)
        tm.that(wms.extracted_entities, eq=("items",))

    def test_main_extract_without_entity_defaults_to_inventory(self) -> None:
        facade, wms, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main(["extract"]), eq=0)
        tm.that(wms.extracted_entities, eq=("inventory",))

    def test_execute_command_pipeline_returns_failure_on_error(self) -> None:
        facade, _, _ = _build_public_facade(pipeline_should_fail=True)
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("pipeline"), eq=1)

    def test_execute_command_pipeline_runs_through_facade(self) -> None:
        facade, _, runner = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("pipeline"), eq=0)
        tm.that(runner.calls, eq=1)

    def test_execute_command_unknown_returns_failure(self) -> None:
        facade, _, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("unknown"), eq=1)

    def test_module_main_uses_public_cli_entrypoint(self) -> None:
        tm.that(main(["info"]), eq=0)
