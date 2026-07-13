"""DBT model generation and execution monitoring for the public facade."""

from __future__ import annotations

import shlex
from typing import TYPE_CHECKING

from flext_core import r
from flext_dbt_oracle_wms import m, u
from flext_dbt_oracle_wms.services.metadata import FlextDbtOracleWmsMetadata

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p, t
    from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings


class FlextDbtOracleWmsModelsApi(FlextDbtOracleWmsMetadata):
    """DBT model generation and DBT command monitoring operations."""

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: u.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize DBT model facade dependencies cooperatively."""
        super().__init__(settings=settings, client=client, service=service)

    def generate_dbt_models_from_wms(
        self,
        inventory_items: t.StrSequence | None = None,
        shipments: t.StrSequence | None = None,
        output_dir: str | None = None,
    ) -> p.Result[m.DbtOracleWms.DbtModelGenerationResult]:
        """Generate DBT model metadata from real entity selections."""
        self.logger.info("Generating DBT models from Oracle WMS")
        entity_names = self._resolve_entity_names(inventory_items, shipments)
        if entity_names is None:
            discovery_result = self.client.discover_oracle_wms_entities()
            if discovery_result.failure:
                return r[m.DbtOracleWms.DbtModelGenerationResult].fail(
                    discovery_result.error or "Oracle WMS entity discovery failed",
                )
            entity_names = discovery_result.value
        generated_models_result = (
            u.DbtOracleWms.ModelBuilder.generate_wms_staging_models(
                entity_names,
            )
        )
        if generated_models_result.failure:
            return r[m.DbtOracleWms.DbtModelGenerationResult].fail(
                generated_models_result.error or "DBT model generation failed",
            )
        recommendations_result = self.service.generate_workflow_recommendations(
            [{"entity_name": entity_name} for entity_name in entity_names],
        )
        if recommendations_result.failure:
            return r[m.DbtOracleWms.DbtModelGenerationResult].fail(
                recommendations_result.error
                or "Workflow recommendation generation failed",
            )
        generated_models = generated_models_result.value
        return r[m.DbtOracleWms.DbtModelGenerationResult].ok(
            m.DbtOracleWms.DbtModelGenerationResult(
                model_names=tuple(model.name for model in generated_models),
                models_generated=len(generated_models),
                output_dir=output_dir or "",
                recommendation=recommendations_result.value.recommendation,
                status="models_generated",
            ),
        )

    def monitor_dbt_execution(
        self,
        command: str,
        timeout_seconds: int = 300,
    ) -> p.Result[m.DbtOracleWms.DbtExecutionResult]:
        """Run and monitor a real DBT transformation through flext-meltano."""
        self.logger.info("Monitoring DBT execution: %s", command)
        command_parts = shlex.split(command)
        if not command_parts:
            return r[m.DbtOracleWms.DbtExecutionResult].fail(
                "DBT command cannot be empty"
            )
        if command_parts[0] != "dbt":
            return r[m.DbtOracleWms.DbtExecutionResult].fail(
                "DBT monitoring requires a command beginning with 'dbt'",
            )
        dbt_subcommand = command_parts[1] if len(command_parts) > 1 else "run"
        if dbt_subcommand not in {"run", "build"}:
            return r[m.DbtOracleWms.DbtExecutionResult].fail(
                "DBT monitoring is implemented only for dbt run/build",
            )
        model_names: t.MutableSequenceOf[str] = []
        if "--models" in command_parts:
            models_index = command_parts.index("--models")
            model_names = command_parts[models_index + 1 :]
        if "-m" in command_parts:
            models_index = command_parts.index("-m")
            model_names = command_parts[models_index + 1 :]
        execution_result = self.client.transform_with_dbt(
            entity_data={},
            model_names=model_names or None,
        )
        if execution_result.failure:
            return r[m.DbtOracleWms.DbtExecutionResult].fail(
                execution_result.error or "DBT transformation monitoring failed",
            )
        command_result = execution_result.value
        return r[m.DbtOracleWms.DbtExecutionResult].ok(
            m.DbtOracleWms.DbtExecutionResult(
                command=command,
                dbt_subcommand=dbt_subcommand,
                requested_timeout_seconds=timeout_seconds,
                transformation=m.DbtOracleWms.TransformationResult(
                    transformed_tables=tuple(command_result.command),
                    requested_models=tuple(model_names),
                    command_result=command_result,
                ),
            ),
        )


__all__: list[str] = ["FlextDbtOracleWmsModelsApi"]
