"""Behavior contract for the FlextDbtOracleWms API facade — public API only."""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

import pytest
from flext_tests import tm

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, r
from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.api import FlextDbtOracleWms
from tests import m, p, t, u


class _FakeWmsClient(FlextDbtOracleWmsClient):
    """Pure input->output fake at the Oracle WMS client boundary.

    Carries no capture state: forwarding is proven only through the values
    that flow back to the facade caller.
    """

    _connection: p.Result[m.DbtOracleWms.ConnectionStatus]
    _entities: p.Result[t.StrSequence]
    _records_by_entity: dict[str, Sequence[t.ConfigurationMapping]]
    _pipeline: p.Result[m.DbtOracleWms.PipelineResult]

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings,
        *,
        connection: p.Result[m.DbtOracleWms.ConnectionStatus] | None = None,
        entities: p.Result[t.StrSequence] | None = None,
        records_by_entity: dict[str, Sequence[t.ConfigurationMapping]] | None = None,
        pipeline: p.Result[m.DbtOracleWms.PipelineResult] | None = None,
    ) -> None:
        self._connection = (
            connection
            if connection is not None
            else r[m.DbtOracleWms.ConnectionStatus].ok(
                m.DbtOracleWms.ConnectionStatus(
                    status="connected",
                    environment="development",
                    base_url="",
                    status_code=200,
                ),
            )
        )
        self._entities = (
            entities
            if entities is not None
            else r[t.StrSequence].ok(["items", "shipments"])
        )
        self._records_by_entity = records_by_entity or {}
        self._pipeline = (
            pipeline
            if pipeline is not None
            else r[m.DbtOracleWms.PipelineResult].ok(
                m.DbtOracleWms.PipelineResult(
                    processed_entities=(),
                    total_records=0,
                    transformation_status="success",
                    pipeline_status="completed",
                ),
            )
        )

    @override
    def test_oracle_wms_connection(self) -> p.Result[m.DbtOracleWms.ConnectionStatus]:
        return self._connection

    @override
    def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
        return self._entities

    @override
    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        _ = filters
        records = self._records_by_entity.get(entity_name, [{"entity": entity_name}])
        return r[Sequence[t.ConfigurationMapping]].ok(records)

    @override
    def run_full_oracle_wms_to_dbt_pipeline(
        self,
        entity_names: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.DbtOracleWms.PipelineResult]:
        _ = filters
        _ = model_names
        if self._pipeline.failure:
            return self._pipeline
        return r[m.DbtOracleWms.PipelineResult].ok(
            self._pipeline.value.model_copy(
                update={"processed_entities": tuple(entity_names or ())},
            ),
        )


class _FakeWmsService(u.DbtOracleWms.Service):
    """Deterministic workflow-service fake with no interaction-capture state."""

    def __init__(self, tracking_id: str = "trk-fixed") -> None:
        FlextDbtOracleWmsSettings()
        self._tracking_id = tracking_id

    @override
    def generate_workflow_recommendations(
        self,
        entities: t.SequenceOf[t.ConfigurationMapping] | None = None,
    ) -> p.Result[m.DbtOracleWms.WorkflowRecommendation]:
        return r[m.DbtOracleWms.WorkflowRecommendation].ok(
            m.DbtOracleWms.WorkflowRecommendation(
                total_entities=len(entities or []),
                recommendation="",
                dbt_threads="4",
                target="dev",
            ),
        )

    @override
    def log_workflow_completion(
        self,
        tracking_info: m.DbtOracleWms.WorkflowTracking,
        result: p.Result[m.DbtOracleWms.WorkflowResult],
    ) -> None:
        _ = tracking_info
        _ = result

    @override
    def track_workflow_execution(
        self,
        workflow_name: str,
        workflow_type: str,
        entity_names: t.StrSequence | None = None,
        additional_data: t.ConfigValueMapping | None = None,
    ) -> m.DbtOracleWms.WorkflowTracking:
        _ = workflow_name
        _ = workflow_type
        _ = entity_names
        _ = additional_data
        return m.DbtOracleWms.WorkflowTracking(
            workflow_name="oracle_wms_to_dbt",
            workflow_type="dbt_oracle_wms",
            tracking_id=self._tracking_id,
            entity_names=(),
            status="running",
        )


class TestsFlextDbtOracleWmsApi:
    """Behavior contract for FlextDbtOracleWms public methods."""

    _BASE_URL = "https://wms.example.com"

    def _settings(self) -> FlextDbtOracleWmsSettings:
        return FlextDbtOracleWmsSettings(oracle_wms_base_url=self._BASE_URL)

    def _facade(
        self,
        *,
        client: _FakeWmsClient | None = None,
        service: _FakeWmsService | None = None,
    ) -> FlextDbtOracleWms:
        settings = self._settings()
        return FlextDbtOracleWms(
            settings=settings,
            client=client if client is not None else _FakeWmsClient(settings),
            service=service,
        )

    def test_validate_wms_connection_succeeds_when_client_reports_healthy(self) -> None:
        facade = self._facade()

        result = facade.validate_wms_connection()

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=True)

    def test_validate_wms_connection_propagates_client_connection_failure(self) -> None:
        settings = self._settings()
        client = _FakeWmsClient(
            settings,
            connection=r[m.DbtOracleWms.ConnectionStatus].fail(
                "Oracle WMS endpoint unreachable"
            ),
        )
        facade = self._facade(client=client)

        result = facade.validate_wms_connection()

        tm.fail(result, has="unreachable")

    def test_discover_entities_returns_the_client_entity_list(self) -> None:
        settings = self._settings()
        client = _FakeWmsClient(
            settings,
            entities=r[t.StrSequence].ok(["items", "shipments"]),
        )
        facade = self._facade(client=client)

        result = facade.discover_oracle_wms_entities()

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=["items", "shipments"])

    def test_discover_entities_propagates_client_discovery_failure(self) -> None:
        settings = self._settings()
        client = _FakeWmsClient(
            settings,
            entities=r[t.StrSequence].fail("entity catalog unavailable"),
        )
        facade = self._facade(client=client)

        result = facade.discover_oracle_wms_entities()

        tm.fail(result, has="catalog")

    @pytest.mark.parametrize("entity_name", ["items", "shipments"])
    def test_extract_returns_records_for_the_requested_entity(
        self,
        entity_name: str,
    ) -> None:
        facade = self._facade()

        result = facade.extract_oracle_wms_data(entity_name)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=[{"entity": entity_name}])

    def test_run_workflow_with_transformations_returns_pipeline_summary(self) -> None:
        settings = self._settings()
        client = _FakeWmsClient(
            settings,
            pipeline=r[m.DbtOracleWms.PipelineResult].ok(
                m.DbtOracleWms.PipelineResult(
                    processed_entities=(),
                    total_records=4,
                    transformation_status="success",
                    pipeline_status="completed",
                ),
            ),
        )
        facade = self._facade(client=client, service=_FakeWmsService("trk-77"))

        result = facade.run_oracle_wms_to_dbt_workflow(
            inventory_items=["item-1"],
            generate_models=False,
            run_transformations=True,
        )

        tm.that(result.success, eq=True)
        tm.that(result.value.workflow_status, eq="completed")
        tm.that(result.value.entity_names, eq=("items",))
        tm.that(result.value.tracking_id, eq="trk-77")

    def test_run_workflow_default_path_extracts_metadata(self) -> None:
        settings = self._settings()
        client = _FakeWmsClient(
            settings,
            records_by_entity={
                "items": [{"item_id": "item-1"}],
                "shipments": [{"shipment_id": "shp-1"}],
            },
        )
        facade = self._facade(client=client, service=_FakeWmsService("trk-42"))

        result = facade.run_oracle_wms_to_dbt_workflow(
            inventory_items=["item-1"],
            generate_models=False,
            run_transformations=False,
        )

        tm.that(result.success, eq=True)
        tm.that(result.value.workflow_status, eq="metadata_extracted")
        tm.that(result.value.tracking_id, eq="trk-42")

    def test_run_workflow_propagates_pipeline_failure(self) -> None:
        settings = self._settings()
        client = _FakeWmsClient(
            settings,
            pipeline=r[m.DbtOracleWms.PipelineResult].fail(
                "pipeline transformation aborted"
            ),
        )
        facade = self._facade(client=client, service=_FakeWmsService())

        result = facade.run_oracle_wms_to_dbt_workflow(
            inventory_items=["item-1"],
            generate_models=False,
            run_transformations=True,
        )

        tm.fail(result, has="aborted")
