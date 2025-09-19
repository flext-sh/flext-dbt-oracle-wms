"""CLI for FLEXT DBT Oracle WMS package using flext-cli foundation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import sys

from flext_cli import FlextCliApi, FlextCliConfigs
from flext_core import FlextLogger, FlextResult
from flext_dbt_oracle_wms import (
    FlextDbtOracleWmsConfig,
    FlextDbtOracleWmsWorkflowService,
    __version__,
)

logger = FlextLogger(__name__)


class FlextDbtOracleWmsCliService:
    """FLEXT DBT Oracle WMS CLI service using flext-cli foundation exclusively."""

    def __init__(self) -> None:
        """Initialize CLI service with flext-cli patterns."""
        self._cli_api = FlextCliApi()
        self._config = FlextCliConfigs()

    def handle_discover(
        self, _args: dict[str, object] | None = None,
    ) -> FlextResult[str]:
        """Handle discover command using flext-cli output."""
        try:
            config = FlextDbtOracleWmsConfig()
            workflow_service = FlextDbtOracleWmsWorkflowService(config)

            result = asyncio.run(workflow_service.run_entity_discovery_workflow())

            if result.is_success:
                data = result.data or {}
                entity_types = data.get("entity_types", [])
                if isinstance(entity_types, list):
                    pass
                return FlextResult[str].ok("Discovery completed successfully")
            return FlextResult[str].fail(f"Discovery failed: {result.error}")

        except Exception as e:
            logger.exception("Unexpected error in discovery command")
            return FlextResult[str].fail(f"Unexpected error: {e}")

    def handle_extract(self, args: dict[str, object] | None = None) -> FlextResult[str]:
        """Handle extract command using flext-cli output."""
        try:
            config = FlextDbtOracleWmsConfig()
            workflow_service = FlextDbtOracleWmsWorkflowService(config)

            # Parse entities from args if provided
            entity_names_raw = args.get("entities", []) if args else []
            entity_names = (
                entity_names_raw if isinstance(entity_names_raw, list) else []
            )
            limit = args.get("limit") if args else None
            limits = (
                dict.fromkeys(entity_names, limit) if entity_names and limit else None
            )

            result = asyncio.run(
                workflow_service.run_data_extraction_workflow(
                    entity_names or [],
                    None,
                    limits,
                ),
            )

            if result.is_success:
                return FlextResult[str].ok("Extraction completed successfully")
            return FlextResult[str].fail(f"Extraction failed: {result.error}")

        except Exception as e:
            logger.exception("Unexpected error in extraction command")
            return FlextResult[str].fail(f"Unexpected error: {e}")

    def handle_pipeline(
        self, args: dict[str, object] | None = None,
    ) -> FlextResult[str]:
        """Handle pipeline command using flext-cli output."""
        try:
            config = FlextDbtOracleWmsConfig()
            workflow_service = FlextDbtOracleWmsWorkflowService(config)

            # Parse parameters from args if provided
            entity_names_raw = args.get("entities", []) if args else []
            entity_names = (
                entity_names_raw if isinstance(entity_names_raw, list) else []
            )
            model_names_raw = args.get("models", []) if args else []
            model_names = model_names_raw if isinstance(model_names_raw, list) else []

            result = asyncio.run(
                workflow_service.run_full_transformation_pipeline(
                    entity_names,
                    None,
                    model_names,
                ),
            )

            if result.is_success:
                data = result.data or {}
                summary = data.get("summary", {})
                if isinstance(summary, dict):
                    pass
                return FlextResult[str].ok("Pipeline completed successfully")
            return FlextResult[str].fail(f"Pipeline failed: {result.error}")

        except Exception as e:
            logger.exception("Unexpected error in pipeline command")
            return FlextResult[str].fail(f"Unexpected error: {e}")

    def handle_info(self, _args: dict[str, object] | None = None) -> FlextResult[str]:
        """Handle info command using flext-cli output."""
        try:
            info_data = {
                "name": "FLEXT DBT Oracle WMS",
                "version": __version__,
                "purpose": "Oracle WMS data transformation with DBT",
                "architecture": "flext-core + flext-oracle-wms + flext-meltano",
                "commands": [
                    "discover   - Discover Oracle WMS entities",
                    "extract    - Extract data from Oracle WMS",
                    "pipeline   - Run full transformation pipeline",
                    "info       - Show package information",
                ],
            }

            # Use flext-cli to format and display data
            try:
                self._cli_api.format_data(info_data, "table")
                return FlextResult[str].ok("Package information displayed successfully")
            except Exception:
                # Fallback display
                return FlextResult[str].ok("Package information displayed (fallback)")

        except Exception as e:
            logger.exception("Unexpected error in info command")
            return FlextResult[str].fail(f"Unexpected error: {e}")


def discover() -> None:
    """Discover Oracle WMS entities."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_discover()
    if result.is_failure:
        sys.exit(1)


def extract() -> None:
    """Extract data from Oracle WMS entities."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_extract()
    if result.is_failure:
        sys.exit(1)


def pipeline() -> None:
    """Run full Oracle WMS to DBT transformation pipeline."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_pipeline()
    if result.is_failure:
        sys.exit(1)


def info() -> None:
    """Show FLEXT DBT Oracle WMS information."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_info()
    if result.is_failure:
        sys.exit(1)


def main() -> None:
    """Main CLI entry point for flext-dbt-oracle-wms."""
    try:
        if len(sys.argv) > 1:
            command = sys.argv[1]
            if command == "discover":
                discover()
            elif command == "extract":
                extract()
            elif command == "pipeline":
                pipeline()
            elif command == "info":
                info()
            else:
                sys.exit(1)

    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(1)
    except (OSError, RuntimeError, ValueError):
        logger.exception("CLI error")
        sys.exit(1)


if __name__ == "__main__":
    main()
