"""FLEXT DBT ORACLE WMS API - Unified facade for DBT Oracle WMS operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Unified facade for FLEXT DBT Oracle WMS operations with complete FLEXT integration.
"""

from __future__ import annotations

from flext_core import FlextCore

from flext_dbt_oracle_wms.client import FlextDbtOracleWmsClient
from flext_dbt_oracle_wms.config import FlextDbtOracleWmsConfig
from flext_dbt_oracle_wms.services import (
    FlextDbtOracleWmsMonitoringService,
    FlextDbtOracleWmsWorkflowService,
)


class FlextDbtOracleWms(FlextCore.Service[FlextDbtOracleWmsConfig]):
    """Unified DBT Oracle WMS facade with complete FLEXT ecosystem integration.

    This is the single unified class for the flext-dbt-oracle-wms domain providing
    access to all DBT Oracle WMS domain functionality with centralized patterns.

    **UNIFIED CLASS PATTERN**: One class per module with nested helpers only.
    **CENTRALIZED APPROACH**: All operations follow centralized patterns:
    - FlextDbtOracleWms.* for DBT Oracle WMS-specific operations
    - Centralized validation through FlextDbtOracleWmsWorkflowService
    - No wrappers, aliases, or fallbacks
    - Direct use of flext-core centralized services

    **FLEXT INTEGRATION**: Complete integration with flext-core patterns:
    - FlextCore.Container for dependency injection
    - FlextCore.Context for operation context
    - FlextCore.Logger for structured logging
    - FlextCore.Result for railway-oriented error handling

    **PYTHON 3.13+ COMPATIBILITY**: Uses modern patterns and latest type features.
    """

    def __init__(self, config: FlextDbtOracleWmsConfig | None = None) -> None:
        """Initialize the unified DBT Oracle WMS service."""
        super().__init__()
        self._config = config or FlextDbtOracleWmsConfig()
        self._client: FlextDbtOracleWmsClient | None = None
        self._workflow_service: FlextDbtOracleWmsWorkflowService | None = None
        self._monitoring_service: FlextDbtOracleWmsMonitoringService | None = None

        # Complete FLEXT ecosystem integration
        self._container = FlextCore.Container.get_global().clear()().get_or_create()
        self._context = FlextCore.Context()
        self.logger = FlextCore.Logger(__name__)

    @classmethod
    def create(cls) -> FlextDbtOracleWms:
        """Create a new FlextDbtOracleWms instance (factory method)."""
        return cls()

    @property
    def client(self) -> FlextDbtOracleWmsClient:
        """Get the DBT Oracle WMS client instance."""
        if self._client is None:
            self._client = FlextDbtOracleWmsClient(self._config)
        return self._client

    @property
    def workflow_service(self) -> FlextDbtOracleWmsWorkflowService:
        """Get the workflow service instance."""
        if self._workflow_service is None:
            self._workflow_service = FlextDbtOracleWmsWorkflowService(self._config)
        return self._workflow_service

    @property
    def monitoring_service(self) -> FlextDbtOracleWmsMonitoringService:
        """Get the monitoring service instance."""
        if self._monitoring_service is None:
            self._monitoring_service = FlextDbtOracleWmsMonitoringService(self._config)
        return self._monitoring_service

    @property
    def config(self) -> FlextDbtOracleWmsConfig:
        """Get the current configuration."""
        return self._config

    # =============================================================================
    # MAIN WORKFLOW OPERATIONS - Enhanced with FlextCore.Result error handling
    # =============================================================================

    def run_oracle_wms_to_dbt_workflow(
        self,
        inventory_items: FlextCore.Types.StringList | None = None,
        shipments: FlextCore.Types.StringList | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Run complete Oracle WMS-to-DBT workflow.

        Args:
            inventory_items: List of inventory items to process
            shipments: List of shipments to process
            generate_models: Whether to generate DBT models
            run_transformations: Whether to run transformations

        Returns:
            FlextCore.Result containing workflow results

        """
        try:
            self.logger.info("Running Oracle WMS-to-DBT workflow")
            return self.workflow_service.run_oracle_wms_to_dbt_workflow(
                inventory_items=inventory_items,
                shipments=shipments,
                generate_models=generate_models,
                run_transformations=run_transformations,
            )
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Workflow execution failed: {e}"
            )

    def generate_dbt_models_from_wms(
        self,
        inventory_items: FlextCore.Types.StringList | None = None,
        shipments: FlextCore.Types.StringList | None = None,
        output_dir: str | None = None,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Generate DBT models from Oracle WMS data.

        Args:
            inventory_items: List of inventory items to process
            shipments: List of shipments to process
            output_dir: Output directory for generated models

        Returns:
            FlextCore.Result containing model generation results

        """
        try:
            self.logger.info("Generating DBT models from Oracle WMS")
            return self.workflow_service.generate_dbt_models_from_wms(
                inventory_items=inventory_items,
                shipments=shipments,
                output_dir=output_dir,
            )
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Model generation failed: {e}"
            )

    def extract_wms_metadata(
        self,
        inventory_items: FlextCore.Types.StringList | None = None,
        shipments: FlextCore.Types.StringList | None = None,
        include_inventory_details: bool = True,
        include_shipment_tracking: bool = True,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Extract Oracle WMS metadata.

        Args:
            inventory_items: List of inventory items to process
            shipments: List of shipments to process
            include_inventory_details: Whether to include inventory details
            include_shipment_tracking: Whether to include shipment tracking

        Returns:
            FlextCore.Result containing metadata extraction results

        """
        try:
            self.logger.info("Extracting Oracle WMS metadata")
            return self.workflow_service.extract_wms_metadata(
                inventory_items=inventory_items,
                shipments=shipments,
                include_inventory_details=include_inventory_details,
                include_shipment_tracking=include_shipment_tracking,
            )
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Metadata extraction failed: {e}"
            )

    def monitor_dbt_execution(
        self,
        command: str,
        timeout_seconds: int = 300,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Monitor DBT command execution with metrics.

        Args:
            command: DBT command to execute
            timeout_seconds: Timeout for command execution

        Returns:
            FlextCore.Result containing monitoring results

        """
        try:
            self.logger.info(f"Monitoring DBT execution: {command}")
            return self.monitoring_service.monitor_dbt_execution(
                command=command,
                timeout_seconds=timeout_seconds,
            )
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Monitoring failed: {e}"
            )

    def validate_wms_connection(self) -> FlextCore.Result[bool]:
        """Validate Oracle WMS connection.

        Returns:
            FlextCore.Result containing connection validation result

        """
        try:
            self.logger.info("Validating Oracle WMS connection")
            return self.client.validate_connection()
        except Exception as e:
            return FlextCore.Result[bool].fail(f"Connection validation failed: {e}")

    def get_wms_inventory_info(
        self,
        item_id: str,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Get detailed information about WMS inventory item.

        Args:
            item_id: Inventory item identifier

        Returns:
            FlextCore.Result containing inventory item information

        """
        try:
            self.logger.info(f"Getting WMS inventory info: {item_id}")
            return self.client.get_inventory_info(item_id=item_id)
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Inventory info retrieval failed: {e}"
            )

    def get_wms_shipment_info(
        self,
        shipment_id: str,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Get detailed information about WMS shipment.

        Args:
            shipment_id: Shipment identifier

        Returns:
            FlextCore.Result containing shipment information

        """
        try:
            self.logger.info(f"Getting WMS shipment info: {shipment_id}")
            return self.client.get_shipment_info(shipment_id=shipment_id)
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Shipment info retrieval failed: {e}"
            )


# Alias for backward compatibility
FlextDbtOracleWmsAPI = FlextDbtOracleWms

__all__ = [
    "FlextDbtOracleWms",
    "FlextDbtOracleWmsAPI",
]
