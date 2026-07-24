"""Workflow orchestration for the DBT Oracle WMS public facade."""

from __future__ import annotations

from typing import override

from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, p, r, settings, t, u
from flext_dbt_oracle_wms.services.models import FlextDbtOracleWmsModelsApi


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
    ) -> p.Result[p.DbtOracleWms.WorkflowResult]:
        """Run the real Oracle WMS-to-DBT workflow using domain-backed clients."""
        self.logger.info("Running Oracle WMS-to-DBT workflow")
        entity_names = self._resolve_entity_names(inventory_items, shipments)
        tracking_info = self.service.track_workflow_execution(
            workflow_name="oracle_wms_to_dbt",
            workflow_type="dbt_oracle_wms",
            entity_names=entity_names,
        )
        generated_models: t.StrSequence = ()
        model_names: t.StrSequence | None = None
        if generate_models:
            model_generation_result = self.generate_dbt_models_from_wms(
                inventory_items, shipments
            )
            if model_generation_result.failure:
                return self._log_and_return(
                    tracking_info,
                    r[p.DbtOracleWms.WorkflowResult].fail(
                        model_generation_result.error or "DBT model generation failed"
                    ),
                )
            generated_models = model_generation_result.value.model_names
            model_names = generated_models or None
        # Each branch's result type is statically known, so each builds its own
        # WorkflowResult directly — no runtime isinstance type-switch (flext-law §4).
        if run_transformations:
            workflow_result = self.client.run_full_oracle_wms_to_dbt_pipeline(
                entity_names=entity_names, model_names=model_names
            ).map(
                lambda pipeline: p.DbtOracleWms.WorkflowResult(
                    tracking_id=tracking_info.tracking_id,
                    generate_models=generate_models,
                    run_transformations=True,
                    generated_models=generated_models,
                    entity_names=tuple(pipeline.processed_entities),
                    total_records=pipeline.total_records,
                    transformation_status=pipeline.transformation_status,
                    workflow_status=pipeline.pipeline_status,
                )
            )
        else:
            workflow_result = self.extract_wms_metadata(inventory_items, shipments).map(
                lambda metadata: p.DbtOracleWms.WorkflowResult(
                    tracking_id=tracking_info.tracking_id,
                    generate_models=generate_models,
                    run_transformations=False,
                    generated_models=generated_models,
                    entity_names=tuple(metadata.available_entities),
                    total_records=metadata.inventory_count + metadata.shipment_count,
                    transformation_status=metadata.status,
                    workflow_status=metadata.status,
                )
            )
        return self._log_and_return(tracking_info, workflow_result)

    def _log_and_return(
        self,
        tracking_info: p.DbtOracleWms.WorkflowTracking,
        result: p.Result[p.DbtOracleWms.WorkflowResult],
    ) -> p.Result[p.DbtOracleWms.WorkflowResult]:
        """Log workflow completion and pass the result through unchanged."""
        self.service.log_workflow_completion(tracking_info, result)
        return result

    def validate_wms_connection(self) -> p.Result[bool]:
        """Validate the Oracle WMS connection using the real client health check."""
        self.logger.info("Validating Oracle WMS connection")
        connection_result = self.client.test_oracle_wms_connection()
        if connection_result.failure:
            return r[bool].fail(
                connection_result.error or "Oracle WMS connection validation failed"
            )
        return r[bool].ok(True)

    @override
    def execute(self) -> p.Result[FlextDbtOracleWmsSettings]:
        """Execute DBT Oracle WMS domain service logic."""
        self.logger.info("Executing DBT Oracle WMS service")
        return r[FlextDbtOracleWmsSettings].ok(settings)


__all__: list[str] = ["FlextDbtOracleWmsWorkflow"]
