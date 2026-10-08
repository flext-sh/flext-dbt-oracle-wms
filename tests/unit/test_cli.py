"""Behavior contract for flext_dbt_oracle_wms CLI service — public API only.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_cli
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tests import tm

from flext_dbt_oracle_wms import (
    FlextDbtOracleWms,
    FlextDbtOracleWmsClient,
    FlextDbtOracleWmsSettings,
    m,
    r,
)
from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from tests import u

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import t


class TestsFlextDbtOracleWmsCli:
    """Behavior contract for FlextDbtOracleWmsCliService public commands."""

    @staticmethod
    def _build_public_facade(
        *,
        pipeline_should_fail: bool = False,
    ) -> t.Triple[
        FlextDbtOracleWms,
        u.DbtOracleWms.Tests.ScriptedWmsClient,
        u.DbtOracleWms.Tests.ScriptedDbtRunner,
    ]:
        settings = FlextDbtOracleWmsSettings.model_validate({
            "DbtOracleWms": {"oracle_wms_base_url": "https://wms.example.com"},
        })
        wms = u.DbtOracleWms.Tests.ScriptedWmsClient()
        runner = u.DbtOracleWms.Tests.ScriptedDbtRunner(
            r[m.Meltano.CommandExecutionResult].fail("dbt run failed")
            if pipeline_should_fail
            else None,
        )
        client = FlextDbtOracleWmsClient(
            settings,
            wms_client=wms,
            meltano_runner=runner,
        )
        return FlextDbtOracleWms(settings=settings, client=client), wms, runner

    def test_main_with_empty_args_returns_info_exit_code(self) -> None:
        """Test main with empty args returns info exit code."""
        facade, _, _ = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main([]), eq=0)

    def test_execute_command_discover_returns_success(self) -> None:
        """Test execute command discover returns success."""
        facade, _, _ = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("discover"), eq=0)

    def test_main_extract_with_entity_invokes_client(self) -> None:
        """Test main extract with entity invokes client."""
        facade, wms, _ = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main(["extract", "items"]), eq=0)
        tm.that(wms.extracted_entities, eq=("items",))

    def test_main_extract_without_entity_invokes_client(self) -> None:
        """Test main extract without entity invokes client."""
        facade, wms, _ = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main(["extract"]), eq=0)
        tm.that(len(wms.extracted_entities), eq=1)

    def test_extract_invalid_entity_fails_before_client_call(self) -> None:
        """Test extract invalid entity fails before client call."""
        facade, wms, _ = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.fail(service.handle_extract({"entity": 42}))
        tm.that(wms.extracted_entities, eq=())

    def test_execute_command_pipeline_returns_failure_on_error(self) -> None:
        """Test execute command pipeline returns failure on error."""
        facade, _, _ = self._build_public_facade(pipeline_should_fail=True)
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("pipeline"), eq=1)

    def test_execute_command_pipeline_runs_through_facade(self) -> None:
        """Test execute command pipeline runs through facade."""
        facade, _, runner = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("pipeline"), eq=0)
        tm.that(runner.calls, eq=1)

    def test_execute_command_unknown_returns_failure(self) -> None:
        """Test execute command unknown returns failure."""
        facade, _, _ = self._build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("unknown"), eq=1)

    @staticmethod
    def test_module_main_uses_public_cli_entrypoint() -> None:
        """Test module main uses public cli entrypoint."""
        tm.that(main(["info"]), eq=0)
