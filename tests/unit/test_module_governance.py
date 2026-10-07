"""Behavior contract for flext_dbt_oracle_wms public entrypoints.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_module_governance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_dbt_oracle_wms.api import FlextDbtOracleWms
from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main


class TestsFlextDbtOracleWmsModuleGovernance:
    """Behavior contract for flext_dbt_oracle_wms package entrypoints."""

    @staticmethod
    @pytest.mark.parametrize(
        ("command", "expected_exit_code"),
        [("info", 0), ("unknown", 1), ("", 1)],
    )
    def test_execute_command_maps_command_to_exit_code(
        command: str,
        expected_exit_code: int,
    ) -> None:
        """Test execute command maps command to exit code."""
        service = FlextDbtOracleWmsCliService()
        tm.that(service.execute_command(command), eq=expected_exit_code)

    @staticmethod
    def test_handle_info_returns_success_with_package_label() -> None:
        """Test handle info returns success with package label."""
        service = FlextDbtOracleWmsCliService()
        result = service.handle_info()
        tm.that(result.success, eq=True)
        tm.that(result.value, eq="FLEXT DBT Oracle WMS")

    @staticmethod
    @pytest.mark.parametrize("argv", [[], ["info"]])
    def test_main_entrypoint_defaults_to_info_success(argv: list[str]) -> None:
        """Test main entrypoint defaults to info success."""
        tm.that(main(argv), eq=0)

    @staticmethod
    def test_module_main_matches_service_main() -> None:
        """Test module main matches service main."""
        service = FlextDbtOracleWmsCliService()
        tm.that(main(["info"]), eq=service.main(["info"]))

    @staticmethod
    def test_public_facade_constructs_with_defaults() -> None:
        """Test public facade constructs with defaults."""
        facade = FlextDbtOracleWms()
        # NOTE (multi-agent): mro-rn88 — project fields live under the DbtOracleWms namespace.
        tm.that(facade.settings.DbtOracleWms.oracle_wms_environment, eq="development")
