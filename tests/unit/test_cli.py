"""Unit tests for the DBT Oracle WMS CLI service."""

from __future__ import annotations

from collections.abc import Sequence

import pytest

import flext_dbt_oracle_wms.cli as cli_module
from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from tests import r, t


class _StubDbtOracleWms:
    last_entity: str | None = None
    pipeline_should_fail = False
    pipeline_generate_models = False
    pipeline_run_transformations = False

    def discover_oracle_wms_entities(self) -> r[t.StrSequence]:
        return r[t.StrSequence].ok(["items", "shipments"])

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> r[Sequence[t.ConfigurationMapping]]:
        _ = filters
        type(self).last_entity = entity_name
        if entity_name not in {"inventory", "items"}:
            return r[Sequence[t.ConfigurationMapping]].fail("unknown entity")
        return r[Sequence[t.ConfigurationMapping]].ok([
            {"entity": entity_name},
        ])

    def run_oracle_wms_to_dbt_workflow(
        self,
        inventory_items: t.StrSequence | None = None,
        shipments: t.StrSequence | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> r[t.Dict]:
        _ = inventory_items
        _ = shipments
        type(self).pipeline_generate_models = generate_models
        type(self).pipeline_run_transformations = run_transformations
        if type(self).pipeline_should_fail:
            return r[t.Dict].fail("boom")
        return r[t.Dict].ok(t.Dict.model_validate({"status": "ok"}))


def _install_stub_service(monkeypatch: pytest.MonkeyPatch) -> type[_StubDbtOracleWms]:
    _StubDbtOracleWms.last_entity = None
    _StubDbtOracleWms.pipeline_should_fail = False
    _StubDbtOracleWms.pipeline_generate_models = False
    _StubDbtOracleWms.pipeline_run_transformations = False
    monkeypatch.setattr(cli_module, "FlextDbtOracleWms", _StubDbtOracleWms)
    return _StubDbtOracleWms


def test_cli_main_defaults_to_info(monkeypatch: pytest.MonkeyPatch) -> None:
    _install_stub_service(monkeypatch)
    service = FlextDbtOracleWmsCliService()
    assert service.main([]) == 0


def test_cli_executes_discover_command(monkeypatch: pytest.MonkeyPatch) -> None:
    _install_stub_service(monkeypatch)
    service = FlextDbtOracleWmsCliService()
    assert service.execute_command("discover") == 0


def test_cli_executes_extract_command_through_public_facade(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stub_service = _install_stub_service(monkeypatch)
    service = FlextDbtOracleWmsCliService()
    assert service.main(["extract", "items"]) == 0
    assert stub_service.last_entity == "items"


def test_cli_uses_default_extract_entity(monkeypatch: pytest.MonkeyPatch) -> None:
    stub_service = _install_stub_service(monkeypatch)
    service = FlextDbtOracleWmsCliService()
    assert service.main(["extract"]) == 0
    assert stub_service.last_entity == "inventory"


def test_cli_returns_failure_for_pipeline_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stub_service = _install_stub_service(monkeypatch)
    stub_service.pipeline_should_fail = True
    service = FlextDbtOracleWmsCliService()
    assert service.execute_command("pipeline") == 1


def test_cli_runs_pipeline_through_public_facade(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stub_service = _install_stub_service(monkeypatch)
    service = FlextDbtOracleWmsCliService()
    assert service.execute_command("pipeline") == 0
    assert stub_service.pipeline_generate_models is False
    assert stub_service.pipeline_run_transformations is True


def test_cli_returns_failure_for_unknown_command(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_stub_service(monkeypatch)
    service = FlextDbtOracleWmsCliService()
    assert service.execute_command("unknown") == 1


def test_module_main_uses_public_cli_entrypoint(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_stub_service(monkeypatch)
    monkeypatch.setattr("sys.argv", ["flext-dbt-oracle-wms", "info"])
    assert main() == 0
