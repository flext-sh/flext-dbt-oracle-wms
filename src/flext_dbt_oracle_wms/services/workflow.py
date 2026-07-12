"""Workflow orchestration for the DBT Oracle WMS public facade."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from flext_core import r
from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings
from flext_dbt_oracle_wms.models import m
from flext_dbt_oracle_wms.services.models import FlextDbtOracleWmsModelsApi

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p
    from flext_dbt_oracle_wms.typings import t
    from flext_dbt_oracle_wms.utilities import u


class FlextDbtOracleWmsWorkflow(FlextDbtOracleWmsModelsApi):
    """Workflow execution and service lifecycle operations."""

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: u.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize workflow facade dependencies cooperatively."""
        super().__init__(settings=settings, client=client, service=service)

    def run_oracle_wms_to_dbt_workflow(
        self,
        inventory_items: t.StrSequence | None = None,
        shipments: t.StrSequence | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> p.Result[m.Dict]:
        """Run the real Oracle WMS-to-DBT workflow using domain-backed clients."""
        self.logger.info("Running Oracle WMS-to-DBT workflow")
        entity_names = self._resolve_entity_names(inventory_items, shipments)
        tracking_info = self.service.track_workflow_execution(
            workflow_name="oracle_wms_to_dbt",
            workflow_type="dbt_oracle_wms",
            entity_names=entity_names,
        )
        tracking_context: t.ConfigurationMapping = {
            "tracking_id": str(tracking_info.get("tracking_id", "")),
            "workflow_name": "oracle_wms_to_dbt",
            "workflow_type": "dbt_oracle_wms",
        }
        generated_models: str | None = None
        model_names: t.StrSequence | None = None
        if generate_models:
            model_generation_result = self.generate_dbt_models_from_wms(
                inventory_items,
                shipments,
            )
            if model_generation_result.failure:
                failure_result = r[m.Dict].fail(
                    model_generation_result.error or "DBT model generation failed",
                )
                self.service.log_workflow_completion(
                    tracking_context,
                    failure_result,
                )
                return failure_result
            generated_model_payload = dict(model_generation_result.value)
            model_names = [
                name
                for name in str(
                    generated_model_payload.get("model_names", ""),
                ).split(",")
                if name
            ]
            generated_models = str(generated_model_payload.get("model_names", ""))
        workflow_result = (
            self.client.run_full_oracle_wms_to_dbt_pipeline(
                entity_names=entity_names,
                model_names=model_names,
            )
            if run_transformations
            else self.extract_wms_metadata(
                inventory_items,
                shipments,
            )
        )
        if workflow_result.failure:
            failure_result = r[m.Dict].fail(
                workflow_result.error or "Oracle WMS workflow execution failed",
            )
            self.service.log_workflow_completion(
                tracking_context,
                failure_result,
            )
            return failure_result
        workflow_payload = dict(workflow_result.value)
        workflow_payload["generate_models"] = generate_models
        workflow_payload["run_transformations"] = run_transformations
        workflow_payload["tracking_id"] = str(tracking_info.get("tracking_id", ""))
        if generated_models is not None:
            workflow_payload["generated_models"] = generated_models
        success_result = r[m.Dict].ok(m.Dict.model_validate(workflow_payload))
        self.service.log_workflow_completion(
            tracking_context,
            success_result,
        )
        return success_result

    def validate_wms_connection(self) -> p.Result[bool]:
        """Validate the Oracle WMS connection using the real client health check."""
        self.logger.info("Validating Oracle WMS connection")
        connection_result = self.client.test_oracle_wms_connection()
        if connection_result.failure:
            return r[bool].fail(
                connection_result.error or "Oracle WMS connection validation failed",
            )
        return r[bool].ok(True)

    @override
    def execute(
        self,
    ) -> p.Result[FlextDbtOracleWmsSettings]:
        """Execute DBT Oracle WMS domain service logic."""
        self.logger.info("Executing DBT Oracle WMS service")
        return r[FlextDbtOracleWmsSettings].ok(self.settings)


__all__: list[str] = ["FlextDbtOracleWmsWorkflow"]
