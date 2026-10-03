"""Behavior contract for the FlextDbtOracleWms API facade — public API only."""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_dbt_oracle_wms import (
    FlextDbtOracleWms,
    FlextDbtOracleWmsClient,
    FlextDbtOracleWmsSettings,
    m,
    r,
    t,
)
from tests import u


class TestsFlextDbtOracleWmsApi:
    """Behavior contract for FlextDbtOracleWms public methods."""

    _BASE_URL = "https://wms.example.com"
    _TRACKING_ID = "oracle_wms_to_dbt:dbt_oracle_wms"

    def _settings(self) -> FlextDbtOracleWmsSettings:
        return FlextDbtOracleWmsSettings(oracle_wms_base_url=self._BASE_URL)

    def _facade(
        self,
        *,
        wms: u.DbtOracleWms.Tests.ScriptedWmsClient | None = None,
        runner: u.DbtOracleWms.Tests.ScriptedDbtRunner | None = None,
    ) -> FlextDbtOracleWms:
        settings = self._settings()
        client = FlextDbtOracleWmsClient(
            settings,
            wms_client=(
                wms if wms is not None else u.DbtOracleWms.Tests.ScriptedWmsClient()
            ),
            meltano_runner=(
                runner
                if runner is not None
                else u.DbtOracleWms.Tests.ScriptedDbtRunner()
            ),
        )
        return FlextDbtOracleWms(settings=settings, client=client)

    def test_validate_wms_connection_succeeds_when_client_reports_healthy(self) -> None:
        facade = self._facade()

        result = facade.validate_wms_connection()

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=True)

    def test_validate_wms_connection_propagates_client_connection_failure(self) -> None:
        wms = u.DbtOracleWms.Tests.ScriptedWmsClient(
            health=r[m.Api.HttpResponse].fail("Oracle WMS endpoint unreachable")
        )
        facade = self._facade(wms=wms)

        result = facade.validate_wms_connection()

        tm.fail(result, has="unreachable")

    def test_discover_entities_returns_the_client_entity_list(self) -> None:
        wms = u.DbtOracleWms.Tests.ScriptedWmsClient(
            entities=r[t.StrSequence].ok(["items", "shipments"])
        )
        facade = self._facade(wms=wms)

        result = facade.discover_oracle_wms_entities()

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=["items", "shipments"])

    def test_discover_entities_propagates_client_discovery_failure(self) -> None:
        wms = u.DbtOracleWms.Tests.ScriptedWmsClient(
            entities=r[t.StrSequence].fail("entity catalog unavailable")
        )
        facade = self._facade(wms=wms)

        result = facade.discover_oracle_wms_entities()

        tm.fail(result, has="catalog")

    @pytest.mark.parametrize("entity_name", ["items", "shipments"])
    def test_extract_returns_records_for_the_requested_entity(
        self, entity_name: str
    ) -> None:
        wms = u.DbtOracleWms.Tests.ScriptedWmsClient()
        facade = self._facade(wms=wms)

        result = facade.extract_oracle_wms_data(entity_name)

        tm.that(result.success, eq=True)
        tm.that(result.value, eq=[{"entity": entity_name}])
        tm.that(wms.extracted_entities, eq=(entity_name,))

    def test_run_workflow_with_transformations_returns_pipeline_summary(self) -> None:
        facade = self._facade()

        result = facade.run_oracle_wms_to_dbt_workflow(
            inventory_items=["item-1"], generate_models=False, run_transformations=True
        )

        tm.that(result.success, eq=True)
        tm.that(result.value.workflow_status, eq="completed")
        tm.that(result.value.entity_names, eq=("items",))
        tm.that(result.value.tracking_id, eq=self._TRACKING_ID)

    def test_run_workflow_default_path_extracts_metadata(self) -> None:
        wms = u.DbtOracleWms.Tests.ScriptedWmsClient(
            records_by_entity={
                "items": ({"item_id": "item-1"},),
                "shipments": ({"shipment_id": "shp-1"},),
            }
        )
        facade = self._facade(wms=wms)

        result = facade.run_oracle_wms_to_dbt_workflow(
            inventory_items=["item-1"], generate_models=False, run_transformations=False
        )

        tm.that(result.success, eq=True)
        tm.that(result.value.workflow_status, eq="metadata_extracted")
        tm.that(result.value.tracking_id, eq=self._TRACKING_ID)

    def test_run_workflow_propagates_pipeline_failure(self) -> None:
        runner = u.DbtOracleWms.Tests.ScriptedDbtRunner(
            r[m.Meltano.CommandExecutionResult].fail("pipeline transformation aborted")
        )
        facade = self._facade(runner=runner)

        result = facade.run_oracle_wms_to_dbt_workflow(
            inventory_items=["item-1"], generate_models=False, run_transformations=True
        )

        tm.fail(result, has="aborted")
        tm.that(runner.calls, eq=1)
