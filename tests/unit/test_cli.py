"""Behavior contract for flext_dbt_oracle_wms CLI service — public API only."""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

from flext_tests import tm

from flext_dbt_oracle_wms import r
from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.cli import FlextDbtOracleWmsCliService, main
from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
from tests.models import m
from tests.protocols import p
from tests.typings import t
from tests.utilities import u


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
    def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
        return r[t.StrSequence].ok(["items", "shipments"])

    @override
    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        _ = filters
        self.last_entity = entity_name
        if entity_name not in {"inventory", "items"}:
            return r[Sequence[t.ConfigurationMapping]].fail("unknown entity")
        return r[Sequence[t.ConfigurationMapping]].ok([{"entity": entity_name}])

    @override
    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.Dict]:
        _ = filters
        _ = model_names
        self.pipeline_called = True
        if self.pipeline_should_fail:
            return r[m.Dict].fail("boom")
        return r[m.Dict].ok(
            m.Dict.model_validate({
                "pipeline_status": "completed",
                "processed_entities": ",".join(entity_names or []),
                "total_records": 2,
            }),
        )


class _CliService(u.DbtOracleWms.Service):
    def __init__(self) -> None:
        self.settings = m.DbtOracleWms.FlextDbtOracleWmsSettings()
        self.logged_payload: m.Dict | None = None

    @override
    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: t.StrSequence | None = None,
        additional_data: t.ConfigValueMapping | None = None,
    ) -> m.Dict:
        _ = entity_names
        _ = additional_data
        return m.Dict.model_validate({
            "tracking_id": f"{workflow_name}:{workflow_type}",
        })

    @override
    def log_workflow_completion(
        self,
        tracking_info: t.ConfigurationMapping,
        result: p.Result[m.Dict],
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
        facade, client, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main(["extract", "items"]), eq=0)
        tm.that(client.last_entity, eq="items")

    def test_main_extract_without_entity_defaults_to_inventory(self) -> None:
        facade, client, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.main(["extract"]), eq=0)
        tm.that(client.last_entity, eq="inventory")

    def test_execute_command_pipeline_returns_failure_on_error(self) -> None:
        facade, _, _ = _build_public_facade(pipeline_should_fail=True)
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("pipeline"), eq=1)

    def test_execute_command_pipeline_runs_through_facade(self) -> None:
        facade, client, helper = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("pipeline"), eq=0)
        tm.that(client.pipeline_called, eq=True)
        assert helper.logged_payload is not None
        tm.that(helper.logged_payload["generate_models"], eq=False)
        tm.that(helper.logged_payload["run_transformations"], eq=True)

    def test_execute_command_unknown_returns_failure(self) -> None:
        facade, _, _ = _build_public_facade()
        service = FlextDbtOracleWmsCliService(service=facade)
        tm.that(service.execute_command("unknown"), eq=1)

    def test_module_main_uses_public_cli_entrypoint(self) -> None:
        tm.that(main(["info"]), eq=0)
