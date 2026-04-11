"""Unit tests for the DBT Oracle WMS CLI service."""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

from flext_dbt_oracle_wms import (
    FlextDbtOracleWms,
    FlextDbtOracleWmsClient,
    FlextDbtOracleWmsCliService,
    main,
)
from tests import m, r, t, u


class _CliClient(FlextDbtOracleWmsClient):
    def __init__(
        self,
        settings: m.DbtOracleWms.FlextDbtOracleWmsSettings,
        *,
        pipeline_should_fail: bool = False,
    ) -> None:
        self.settings = settings
        self.last_entity: str | None = None
        self.pipeline_should_fail = pipeline_should_fail
        self.pipeline_called = False

    @override
    def discover_oracle_wms_entities(self) -> r[t.StrSequence]:
        return r[t.StrSequence].ok(["items", "shipments"])

    @override
    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> r[Sequence[t.ConfigurationMapping]]:
        _ = filters
        self.last_entity = entity_name
        if entity_name not in {"inventory", "items"}:
            return r[Sequence[t.ConfigurationMapping]].fail("unknown entity")
        return r[Sequence[t.ConfigurationMapping]].ok([
            {"entity": entity_name},
        ])

    @override
    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
        model_names: t.StrSequence | None = None,
    ) -> r[t.Dict]:
        _ = filters
        _ = model_names
        self.pipeline_called = True
        if self.pipeline_should_fail:
            return r[t.Dict].fail("boom")
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "pipeline_status": "completed",
                "processed_entities": ",".join(entity_names or []),
                "total_records": 2,
            }),
        )


class _CliService(u.DbtOracleWms.Service):
    def __init__(self) -> None:
        self.settings = m.DbtOracleWms.FlextDbtOracleWmsSettings()
        self.logged_payload: t.Dict | None = None

    @override
    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: t.StrSequence | None = None,
        additional_data: t.SettingsValueMapping | None = None,
    ) -> t.Dict:
        _ = entity_names
        _ = additional_data
        return t.Dict.model_validate({
            "tracking_id": f"{workflow_name}:{workflow_type}",
        })

    @override
    def log_workflow_completion(
        self,
        tracking_info: t.ConfigurationMapping,
        result: r[t.Dict],
    ) -> None:
        _ = tracking_info
        self.logged_payload = result.value if result.success else None


def _build_public_facade(
    *,
    pipeline_should_fail: bool = False,
) -> t.Triple[FlextDbtOracleWms, _CliClient, _CliService]:
    settings = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    client = _CliClient(settings, pipeline_should_fail=pipeline_should_fail)
    helper = _CliService()
    return (
        FlextDbtOracleWms(settings=settings, client=client, service=helper),
        client,
        helper,
    )


def test_cli_main_defaults_to_info() -> None:
    facade, _, _ = _build_public_facade()
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.main([]) == 0


def test_cli_executes_discover_command() -> None:
    facade, _, _ = _build_public_facade()
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.execute_command("discover") == 0


def test_cli_executes_extract_command_through_public_facade() -> None:
    facade, client, _ = _build_public_facade()
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.main(["extract", "items"]) == 0
    assert client.last_entity == "items"


def testuses_default_extract_entity() -> None:
    facade, client, _ = _build_public_facade()
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.main(["extract"]) == 0
    assert client.last_entity == "inventory"


def test_cli_returns_failure_for_pipeline_errors() -> None:
    facade, _, _ = _build_public_facade(pipeline_should_fail=True)
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.execute_command("pipeline") == 1


def test_cli_runs_pipeline_through_public_facade() -> None:
    facade, client, helper = _build_public_facade()
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.execute_command("pipeline") == 0
    assert client.pipeline_called is True
    assert helper.logged_payload is not None
    assert helper.logged_payload["generate_models"] is False
    assert helper.logged_payload["run_transformations"] is True


def test_cli_returns_failure_for_unknown_command() -> None:
    facade, _, _ = _build_public_facade()
    service = FlextDbtOracleWmsCliService(service=facade)
    assert service.execute_command("unknown") == 1


def test_module_main_uses_public_cli_entrypoint() -> None:
    assert main(["info"]) == 0
