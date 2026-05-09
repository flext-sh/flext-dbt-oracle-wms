"""FLEXT DBT ORACLE WMS API - Unified facade for DBT Oracle WMS operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Unified facade for FLEXT DBT Oracle WMS operations with complete FLEXT integration.
"""

from __future__ import annotations

import shlex
from collections.abc import (
    Sequence,
)
from typing import override

from flext_core import r, s
from flext_dbt_oracle_wms import p
from flext_dbt_oracle_wms._utilities.client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.models import m
from flext_dbt_oracle_wms.settings import FlextDbtOracleWmsSettings
from flext_dbt_oracle_wms.typings import t
from flext_dbt_oracle_wms.utilities import u


class FlextDbtOracleWms(
    s[FlextDbtOracleWmsSettings],
):
    """Unified DBT Oracle WMS facade for extraction, modeling, and workflow execution."""

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: u.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize the unified DBT Oracle WMS service."""
        super().__init__(
            settings_type=None,
            settings_overrides=None,
            initial_context=None,
        )
        self._wms_config: FlextDbtOracleWmsSettings = (
            settings
            if settings is not None
            else FlextDbtOracleWmsSettings.fetch_global()
        )
        self._client: p.DbtOracleWms.Client | None = client
        self._service = service

    @property
    def client(self) -> p.DbtOracleWms.Client:
        """Get the DBT Oracle WMS client instance."""
        if self._client is None:
            self._client = FlextDbtOracleWmsClient(self._wms_config)
        return self._client

    @property
    @override
    def settings(self) -> FlextDbtOracleWmsSettings:
        """Get the current configuration."""
        return self._wms_config

    @property
    def service(self) -> u.DbtOracleWms.Service:
        """Get the workflow service instance."""
        if self._service is None:
            self._service = u.DbtOracleWms.Service()
        return self._service

    def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
        """Discover Oracle WMS entities through the public domain facade."""
        discovered: p.Result[t.StrSequence] = self.client.discover_oracle_wms_entities()
        return discovered

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        """Extract Oracle WMS entity records through the public domain facade."""
        extracted: p.Result[Sequence[t.ConfigurationMapping]] = (
            self.client.extract_oracle_wms_data(entity_name, filters)
        )
        return extracted

    @staticmethod
    def _resolve_entity_names(
        inventory_items: t.StrSequence | None,
        shipments: t.StrSequence | None,
    ) -> t.StrSequence | None:
        entity_names: t.MutableSequenceOf[str] = []
        if inventory_items is not None:
            entity_names.append("items")
        if shipments is not None:
            entity_names.append("shipments")
        return entity_names or None

    def _extract_entity_records(
        self,
        entity_name: str,
        requested_identifiers: t.StrSequence | None,
        identifier_fields: t.StrSequence,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        extract_result = self.client.extract_oracle_wms_data(entity_name)
        if extract_result.failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                extract_result.error or f"Failed to extract {entity_name}",
            )
        if requested_identifiers is None:
            return r[Sequence[t.ConfigurationMapping]].ok(extract_result.value)
        requested_values = {
            identifier.strip()
            for identifier in requested_identifiers
            if identifier.strip()
        }
        filtered_records = [
            record
            for record in extract_result.value
            if any(
                str(record.get(field, "")).strip() in requested_values
                for field in identifier_fields
            )
        ]
        if not filtered_records:
            return r[Sequence[t.ConfigurationMapping]].fail(
                f"No {entity_name} records matched the requested identifiers",
            )
        return r[Sequence[t.ConfigurationMapping]].ok(filtered_records)

    def extract_wms_metadata(
        self,
        inventory_items: t.StrSequence | None = None,
        shipments: t.StrSequence | None = None,
        *,
        include_inventory_details: bool = True,
        include_shipment_tracking: bool = True,
    ) -> p.Result[m.Dict]:
        """Extract Oracle WMS metadata from the real domain client."""
        self.logger.info("Extracting Oracle WMS metadata")
        available_entities_result = self.client.discover_oracle_wms_entities()
        if available_entities_result.failure:
            return r[m.Dict].fail(
                available_entities_result.error or "Oracle WMS entity discovery failed",
            )
        inventory_records: t.SequenceOf[t.ConfigurationMapping] = []
        shipment_records: t.SequenceOf[t.ConfigurationMapping] = []
        if include_inventory_details:
            inventory_result = self._extract_entity_records(
                "items",
                inventory_items,
                ("item_id", "item_number", "id", "sku"),
            )
            if inventory_result.failure:
                return r[m.Dict].fail(
                    inventory_result.error or "Inventory metadata extraction failed",
                )
            inventory_records = inventory_result.value
        if include_shipment_tracking:
            shipment_result = self._extract_entity_records(
                "shipments",
                shipments,
                ("shipment_id", "tracking_number", "id"),
            )
            if shipment_result.failure:
                return r[m.Dict].fail(
                    shipment_result.error or "Shipment metadata extraction failed",
                )
            shipment_records = shipment_result.value
        return r[m.Dict].ok(
            m.Dict.model_validate({
                "status": "metadata_extracted",
                "available_entities": ",".join(available_entities_result.value),
                "inventory_count": len(inventory_records),
                "shipment_count": len(shipment_records),
                "include_inventory_details": include_inventory_details,
                "include_shipment_tracking": include_shipment_tracking,
            }),
        )

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
            "dbt_target": self.settings.dbt_target,
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

    def fetch_wms_inventory_info(self, item_id: str) -> p.Result[m.Dict]:
        """Get inventory item data from the Oracle WMS domain client."""
        self.logger.info("Getting WMS inventory info: %s", item_id)
        inventory_result = self._extract_entity_records(
            "items",
            [item_id],
            ("item_id", "item_number", "id", "sku"),
        )
        if inventory_result.failure:
            return r[m.Dict].fail(
                inventory_result.error or "Inventory info retrieval failed",
            )
        return r[m.Dict].ok(m.Dict.model_validate(inventory_result.value[0]))

    def fetch_wms_shipment_info(self, shipment_id: str) -> p.Result[m.Dict]:
        """Get shipment data from the Oracle WMS domain client."""
        self.logger.info("Getting WMS shipment info: %s", shipment_id)
        shipment_result = self._extract_entity_records(
            "shipments",
            [shipment_id],
            ("shipment_id", "tracking_number", "id"),
        )
        if shipment_result.failure:
            return r[m.Dict].fail(
                shipment_result.error or "Shipment info retrieval failed",
            )
        return r[m.Dict].ok(m.Dict.model_validate(shipment_result.value[0]))

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
                "DBT monitoring requires a command beginning with 'dbt'"
            )
        dbt_subcommand = command_parts[1] if len(command_parts) > 1 else "run"
        if dbt_subcommand not in {"run", "build"}:
            return r[m.Dict].fail(
                "DBT monitoring is implemented only for dbt run/build"
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


__all__: list[str] = ["FlextDbtOracleWms"]
