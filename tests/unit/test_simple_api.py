"""Unit tests for the DBT Oracle WMS simple facade."""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

from flext_dbt_oracle_wms import FlextDbtOracleWms, FlextDbtOracleWmsClient
from tests import m, r, t, u


class _SuccessfulConnectionClient(FlextDbtOracleWmsClient):
    def __init__(self, settings: m.DbtOracleWms.FlextDbtOracleWmsSettings) -> None:
        self.settings = settings

    @override
    def test_oracle_wms_connection(self) -> r[t.Dict]:
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "status": "connected",
                "base_url": "https://wms.example.com",
            }),
        )


class _WorkflowClient(FlextDbtOracleWmsClient):
    entity_names: t.StrSequence | None = None
    extracted_entity: str | None = None

    def __init__(self, settings: m.DbtOracleWms.FlextDbtOracleWmsSettings) -> None:
        self.settings = settings

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
        type(self).extracted_entity = entity_name
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
        type(self).entity_names = entity_names
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "pipeline_status": "completed",
                "processed_entities": ",".join(entity_names or []),
                "total_records": 4,
            }),
        )


class _Service(u.DbtOracleWms.Service):
    logged_tracking_id = ""
    logged_success = False

    def __init__(self) -> None:
        self.settings = m.DbtOracleWms.FlextDbtOracleWmsSettings()

    @override
    def generate_workflow_recommendations(
        self,
        entities: Sequence[t.ConfigurationMapping] | None = None,
    ) -> r[t.Dict]:
        total = len(entities or [])
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "total_entities": total,
                "recommendation": "",
                "dbt_threads": "4",
                "target": "dev",
            }),
        )

    @override
    def log_workflow_completion(
        self,
        tracking_info: t.ConfigurationMapping,
        result: r[t.Dict],
    ) -> None:
        type(self).logged_tracking_id = str(tracking_info.get("tracking_id", ""))
        type(self).logged_success = result.success

    @override
    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: t.StrSequence | None = None,
        additional_data: t.ConfigValueMapping | None = None,
    ) -> t.Dict:
        _ = entity_names
        _ = additional_data
        return t.Dict.model_validate({
            "tracking_id": f"{workflow_name}:{workflow_type}",
        })


def test_validate_wms_connection_uses_public_client_protocol() -> None:
    settings = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    service = FlextDbtOracleWms(
        settings=settings,
        client=_SuccessfulConnectionClient(settings),
    )
    result = service.validate_wms_connection()
    assert result.success
    assert result.value is True


def test_discover_oracle_wms_entities_uses_public_client_protocol() -> None:
    settings = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    service = FlextDbtOracleWms(settings=settings, client=_WorkflowClient(settings))
    result = service.discover_oracle_wms_entities()
    assert result.success
    assert result.value == ["items", "shipments"]


def test_extract_oracle_wms_data_uses_public_client_protocol() -> None:
    settings = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    _WorkflowClient.extracted_entity = None
    workflow_client = _WorkflowClient(settings)
    service = FlextDbtOracleWms(settings=settings, client=workflow_client)
    result = service.extract_oracle_wms_data("items")
    assert result.success
    assert _WorkflowClient.extracted_entity == "items"


def test_run_oracle_wms_to_dbt_workflow_uses_public_protocols() -> None:
    settings = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    _WorkflowClient.entity_names = None
    _Service.logged_tracking_id = ""
    _Service.logged_success = False
    workflow_client = _WorkflowClient(settings)
    service_helper = _Service()
    service = FlextDbtOracleWms(
        settings=settings,
        client=workflow_client,
        service=service_helper,
    )
    result = service.run_oracle_wms_to_dbt_workflow(
        inventory_items=["item-1"],
        generate_models=False,
        run_transformations=True,
    )
    assert result.success
    assert result.value["pipeline_status"] == "completed"
    assert result.value["processed_entities"] == "items"
    assert result.value["tracking_id"] == "oracle_wms_to_dbt:dbt_oracle_wms"
    assert _WorkflowClient.entity_names == ["items"]
    assert _Service.logged_tracking_id == "oracle_wms_to_dbt:dbt_oracle_wms"
    assert _Service.logged_success
