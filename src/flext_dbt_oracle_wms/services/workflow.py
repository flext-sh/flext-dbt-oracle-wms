"""Workflow orchestration for the DBT Oracle WMS public facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/services/workflow
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, override

from flext_dbt_oracle_wms import m, r, t, u
from flext_dbt_oracle_wms.services import FlextDbtOracleWmsGeneration

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class FlextDbtOracleWmsWorkflow(FlextDbtOracleWmsGeneration):
    """Workflow execution and service lifecycle operations."""

    def __init__(
        self,
        settings: p.Settings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: p.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize workflow facade dependencies cooperatively.

        Args:
            settings: Settings contract forwarded to the base runtime.
            client: Injected WMS client boundary; created lazily when
                omitted.
            service: Injected workflow service boundary; created lazily
                when omitted.

        """
        super().__init__(settings=settings, client=client, service=service)

    def run_oracle_wms_to_dbt_workflow(
        self,
        inventory_items: Sequence[str] | None = None,
        shipments: Sequence[str] | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> p.Result[m.DbtOracleWms.WorkflowResult]:
        """Run the real Oracle WMS-to-DBT workflow using domain-backed clients.

        Args:
            inventory_items: Inventory item identifiers selecting the
                items entity; discovery is used when neither selection
                is given.
            shipments: Shipment identifiers selecting the shipments
                entity.
            generate_models: Whether to generate DBT models first.
            run_transformations: Whether to run the full transformation
                pipeline instead of only extracting metadata.

        Returns:
            Result wrapping the workflow summary, or a failure from any
            workflow stage.

        """
        self.logger.info("Running Oracle WMS-to-DBT workflow")
        entity_names = self._resolve_entity_names(inventory_items, shipments)
        tracking_info = self.service.track_workflow_execution(
            workflow_name="oracle_wms_to_dbt",
            workflow_type="dbt_oracle_wms",
            entity_names=entity_names,
        )
        generated_models: Sequence[str] = ()
        model_names: Sequence[str] | None = None
        if generate_models:
            model_generation_result = self.generate_dbt_models_from_wms(
                inventory_items,
                shipments,
            )
            if model_generation_result.failure:
                return self._log_and_return(
                    tracking_info,
                    r[m.DbtOracleWms.WorkflowResult].from_failure(
                        model_generation_result,
                    ),
                )
            generated_models = model_generation_result.value.model_names
            model_names = generated_models or None
        # Each branch's result type is statically known, so each builds its own
        # WorkflowResult directly — no runtime isinstance type-switch (flext-law §4).
        if run_transformations:
            workflow_result = self.client.run_full_oracle_wms_to_dbt_pipeline(
                entity_names=entity_names,
                model_names=model_names,
            ).map(
                lambda pipeline: m.DbtOracleWms.WorkflowResult(
                    tracking_id=tracking_info.tracking_id,
                    generate_models=generate_models,
                    run_transformations=True,
                    generated_models=generated_models,
                    entity_names=tuple(pipeline.processed_entities),
                    total_records=pipeline.total_records,
                    transformation_status=pipeline.transformation_status,
                    workflow_status=pipeline.pipeline_status,
                ),
            )
        else:
            workflow_result = self.extract_wms_metadata(inventory_items, shipments).map(
                lambda metadata: m.DbtOracleWms.WorkflowResult(
                    tracking_id=tracking_info.tracking_id,
                    generate_models=generate_models,
                    run_transformations=False,
                    generated_models=generated_models,
                    entity_names=tuple(metadata.available_entities),
                    total_records=metadata.inventory_count + metadata.shipment_count,
                    transformation_status=metadata.status,
                    workflow_status=metadata.status,
                ),
            )
        return self._log_and_return(tracking_info, workflow_result)

    def _log_and_return(
        self,
        tracking_info: m.DbtOracleWms.WorkflowTracking,
        result: p.Result[m.DbtOracleWms.WorkflowResult],
    ) -> p.Result[m.DbtOracleWms.WorkflowResult]:
        """Log workflow completion and pass the result through unchanged.

        Args:
            tracking_info: Tracking payload identifying the workflow.
            result: Workflow result to log and return.

        Returns:
            The given result, unchanged.

        """
        self.service.log_workflow_completion(tracking_info, result)
        return result

    def validate_wms_connection(self) -> p.Result[bool]:
        """Validate the Oracle WMS connection using the real client health check.

        Returns:
            Ok result with ``True`` when the connection check succeeds,
            or the connection failure.

        """
        self.logger.info("Validating Oracle WMS connection")
        connection_result = self.client.test_oracle_wms_connection()
        if connection_result.failure:
            return r[bool].from_failure(connection_result)
        return r[bool].ok(value=True)

    @override
    def execute(self) -> p.Result[t.JsonMapping]:
        """Return runtime settings through the inherited JSON service contract.

        Domain generation and workflow operations retain their dedicated typed
        results; this lifecycle operation serializes the injected settings only.

        Returns:
            Result wrapping the serialized runtime settings payload.

        """
        self.logger.info("Executing DBT Oracle WMS service")
        return r[t.JsonMapping].ok(
            u.json_mapping_adapter().validate_python(
                self.settings.model_dump(mode="json")
            )
        )


__all__: list[str] = ["FlextDbtOracleWmsWorkflow"]
