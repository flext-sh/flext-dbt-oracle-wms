"""Unit tests for the DBT Oracle WMS simple facade."""

from __future__ import annotations

from typing import override

from flext_dbt_oracle_wms import (
    FlextDbtOracleWms,
    FlextDbtOracleWmsClient,
)
from tests import m, r, t, u


class _SuccessfulConnectionClient(FlextDbtOracleWmsClient):
    def __init__(self) -> None:
        self.config = m.DbtOracleWms.FlextDbtOracleWmsSettings()

    @override
    def test_oracle_wms_connection(self) -> r[t.Dict]:
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "status": "connected",
                "base_url": "https://wms.example.com",
            }),
        )


class _WorkflowClient(FlextDbtOracleWmsClient):
    def __init__(self) -> None:
        self.config = m.DbtOracleWms.FlextDbtOracleWmsSettings()
        self.entity_names: t.StrSequence | None = None

    @override
    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
        model_names: t.StrSequence | None = None,
    ) -> r[t.Dict]:
        _ = filters
        _ = model_names
        self.entity_names = entity_names
        return r[t.Dict].ok(
            t.Dict.model_validate({
                "pipeline_status": "completed",
                "processed_entities": ",".join(entity_names or []),
                "total_records": 4,
            }),
        )


class _MonitoringService(u.DbtOracleWms.Service):
    def __init__(self) -> None:
        self.config = m.DbtOracleWms.FlextDbtOracleWmsSettings()
        self.logged_tracking_id = ""
        self.logged_success = False

    @override
    def log_workflow_completion(
        self,
        tracking_info: t.ConfigurationMapping,
        result: r[t.Dict],
    ) -> None:
        self.logged_tracking_id = str(tracking_info.get("tracking_id", ""))
        self.logged_success = result.is_success

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


def test_validate_wms_connection_uses_client_result() -> None:
    config = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    service = FlextDbtOracleWms(config=config)
    service._client = _SuccessfulConnectionClient()
    result = service.validate_wms_connection()
    assert result.is_success
    assert result.value is True


def test_run_oracle_wms_to_dbt_workflow_uses_real_pipeline_result() -> None:
    config = m.DbtOracleWms.FlextDbtOracleWmsSettings(
        oracle_wms_base_url="https://wms.example.com",
    )
    service = FlextDbtOracleWms(config=config)
    workflow_client = _WorkflowClient()
    monitoring_service = _MonitoringService()
    service._client = workflow_client
    service._monitoring_service = monitoring_service
    result = service.run_oracle_wms_to_dbt_workflow(
        inventory_items=["item-1"],
        generate_models=False,
        run_transformations=True,
    )
    assert result.is_success
    assert result.value["pipeline_status"] == "completed"
    assert result.value["processed_entities"] == "items"
    assert result.value["tracking_id"] == "oracle_wms_to_dbt:dbt_oracle_wms"
    assert workflow_client.entity_names == ["items"]
    assert monitoring_service.logged_tracking_id == "oracle_wms_to_dbt:dbt_oracle_wms"
    assert monitoring_service.logged_success is True
