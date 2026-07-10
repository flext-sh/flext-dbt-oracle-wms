"""DBT model generation and execution monitoring for the public facade."""

from __future__ import annotations

import shlex
from typing import TYPE_CHECKING

from flext_core import r
from flext_dbt_oracle_wms._simple_api_metadata import FlextDbtOracleWmsMetadata
from flext_dbt_oracle_wms.models import m

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p
    from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.typings import t
    from flext_dbt_oracle_wms.utilities import u


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
    ) -> p.Result[m.Dict]:
        """Generate DBT model metadata from real entity selections."""
        self.logger.info("Generating DBT models from Oracle WMS")
        entity_names = self._resolve_entity_names(inventory_items, shipments)
        if entity_names is None:
            discovery_result = self.client.discover_oracle_wms_entities()
            if discovery_result.failure:
                return r[m.Dict].fail(
                    discovery_result.error or "Oracle WMS entity discovery failed",
                )
            entity_names = discovery_result.value
        generator = m.create_generator({
            "dbt_target": settings.DbtOracleWms.dbt_target,
            "output_dir": output_dir or "",
        })
        generated_models_result = generator.generate_wms_staging_models(entity_names)
        if generated_models_result.failure:
            return r[m.Dict].fail(
                generated_models_result.error or "DBT model generation failed",
            )
        recommendations_result = self.service.generate_workflow_recommendations(
            [{"entity_name": entity_name} for entity_name in entity_names],
        )
        if recommendations_result.failure:
            return r[m.Dict].fail(
                recommendations_result.error
                or "Workflow recommendation generation failed",
            )
        generated_models = generated_models_result.value
        return r[m.Dict].ok(
            m.Dict.model_validate({
                "status": "models_generated",
                "model_count": len(generated_models),
                "model_names": ",".join(model.name for model in generated_models),
                "output_dir": output_dir or "",
                "recommendation": str(
                    recommendations_result.value.get("recommendation", ""),
                ),
            }),
        )

    def monitor_dbt_execution(
        self,
        command: str,
        timeout_seconds: int = 300,
    ) -> p.Result[m.Dict]:
        """Run and monitor a real DBT transformation through flext-meltano."""
        self.logger.info("Monitoring DBT execution: %s", command)
        command_parts = shlex.split(command)
        if not command_parts:
            return r[m.Dict].fail("DBT command cannot be empty")
        if command_parts[0] != "dbt":
            return r[m.Dict].fail(
                "DBT monitoring requires a command beginning with 'dbt'",
            )
        dbt_subcommand = command_parts[1] if len(command_parts) > 1 else "run"
        if dbt_subcommand not in {"run", "build"}:
            return r[m.Dict].fail(
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
            return r[m.Dict].fail(
                execution_result.error or "DBT transformation monitoring failed",
            )
        execution_payload = dict(execution_result.value)
        execution_payload["command"] = command
        execution_payload["dbt_subcommand"] = dbt_subcommand
        execution_payload["requested_timeout_seconds"] = timeout_seconds
        return r[m.Dict].ok(
            m.Dict.model_validate(execution_payload),
        )


__all__: list[str] = ["FlextDbtOracleWmsModelsApi"]
