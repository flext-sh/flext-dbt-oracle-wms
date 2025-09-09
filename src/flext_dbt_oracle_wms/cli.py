"""CLI for FLEXT DBT Oracle WMS package using flext-cli foundation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import sys

from flext_core import FlextResult, FlextLogger
from flext_cli import FlextCliApi, FlextCliConfig

from flext_dbt_oracle_wms import (
    FlextDbtOracleWmsConfig,
    __version__,
    create_oracle_wms_workflow_service,
)

logger = FlextLogger(__name__)


class FlextDbtOracleWmsCliService:
    """FLEXT DBT Oracle WMS CLI service using flext-cli foundation exclusively."""
    
    def __init__(self) -> None:
        """Initialize CLI service with flext-cli patterns."""
        self._cli_api = FlextCliApi()
        self._config = FlextCliConfig()
        
    def handle_discover(self, args: dict = None) -> FlextResult[str]:
        """Handle discover command using flext-cli output."""
        try:
            config = FlextDbtOracleWmsConfig()
            workflow_service = create_oracle_wms_workflow_service(config)

            print("Discovering Oracle WMS entities...")
            result = asyncio.run(workflow_service.run_entity_discovery_workflow())

            if result.is_success:
                data = result.data or {}
                print("✅ Discovery completed successfully!")
                print(f"📊 Discovered {data.get('discovered_entities', 0)} entities")
                entity_types = data.get("entity_types", [])
                if isinstance(entity_types, list):
                    print(f"🏷️  Entity types: {', '.join(entity_types)}")
                else:
                    print(f"🏷️  Entity types: {entity_types}")
                return FlextResult[str].ok("Discovery completed successfully")
            else:
                print(f"❌ Discovery failed: {result.error}")
                return FlextResult[str].fail(f"Discovery failed: {result.error}")

        except Exception as e:
            logger.exception("Unexpected error in discovery command")
            print(f"❌ Unexpected error: {e}")
            return FlextResult[str].fail(f"Unexpected error: {e}")

    def handle_extract(self, args: dict = None) -> FlextResult[str]:
        """Handle extract command using flext-cli output."""
        try:
            config = FlextDbtOracleWmsConfig()
            workflow_service = create_oracle_wms_workflow_service(config)
            
            # Parse entities from args if provided
            entity_names = args.get('entities', []) if args else []
            limit = args.get('limit') if args else None
            limits = dict.fromkeys(entity_names, limit) if entity_names and limit else None

            print(f"Extracting Oracle WMS data: {entity_names or 'all discovered'}")
            result = asyncio.run(
                workflow_service.run_data_extraction_workflow(
                    entity_names or [],
                    None,
                    limits,
                ),
            )

            if result.is_success:
                data = result.data or {}
                print("✅ Extraction completed successfully!")
                print(f"📊 Total records: {data.get('total_records', 0)}")
                return FlextResult[str].ok("Extraction completed successfully")
            else:
                print(f"❌ Extraction failed: {result.error}")
                return FlextResult[str].fail(f"Extraction failed: {result.error}")

        except Exception as e:
            logger.exception("Unexpected error in extraction command")
            print(f"❌ Unexpected error: {e}")
            return FlextResult[str].fail(f"Unexpected error: {e}")

    def handle_pipeline(self, args: dict = None) -> FlextResult[str]:
        """Handle pipeline command using flext-cli output."""
        try:
            config = FlextDbtOracleWmsConfig()
            workflow_service = create_oracle_wms_workflow_service(config)
            
            # Parse parameters from args if provided
            entity_names = args.get('entities', []) if args else []
            model_names = args.get('models', []) if args else []

            print("🚀 Starting full Oracle WMS to DBT pipeline...")
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
                    print("✅ Pipeline completed successfully!")
                    print(f"📊 Processed: {summary.get('entities_processed', 0)} entities")
                else:
                    print("✅ Pipeline completed successfully!")
                    print(f"📊 Summary: {summary}")
                return FlextResult[str].ok("Pipeline completed successfully")
            else:
                print(f"❌ Pipeline failed: {result.error}")
                return FlextResult[str].fail(f"Pipeline failed: {result.error}")

        except Exception as e:
            logger.exception("Unexpected error in pipeline command")
            print(f"❌ Unexpected error: {e}")
            return FlextResult[str].fail(f"Unexpected error: {e}")

    def handle_info(self, args: dict = None) -> FlextResult[str]:
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
                    "info       - Show package information"
                ]
            }
            
            # Use flext-cli to format and display data
            try:
                formatted_data = self._cli_api.format_data(info_data)
                print("🏢 FLEXT DBT Oracle WMS")
                print(f"📦 Version: {__version__}")
                print("🎯 Purpose: Oracle WMS data transformation with DBT")
                print("🔧 Architecture: flext-core + flext-oracle-wms + flext-meltano")
                print("")
                print("Available commands:")
                print("  discover   - Discover Oracle WMS entities")
                print("  extract    - Extract data from Oracle WMS")
                print("  pipeline   - Run full transformation pipeline")
                print("  info       - Show package information")
                print("")
                print("Use --help with any command for more details")
                return FlextResult[str].ok("Package information displayed successfully")
            except Exception:
                # Fallback display
                print("🏢 FLEXT DBT Oracle WMS")
                print(f"📦 Version: {__version__}")
                print("🎯 Purpose: Oracle WMS data transformation with DBT")
                print("🔧 Architecture: flext-core + flext-oracle-wms + flext-meltano")
                return FlextResult[str].ok("Package information displayed (fallback)")

        except Exception as e:
            logger.exception("Unexpected error in info command")
            print(f"❌ Unexpected error: {e}")
            return FlextResult[str].fail(f"Unexpected error: {e}")


def discover() -> None:
    """Discover Oracle WMS entities."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_discover()
    if result.is_failure:
        print(f"Error: {result.error}")
        sys.exit(1)


def extract() -> None:
    """Extract data from Oracle WMS entities."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_extract()
    if result.is_failure:
        print(f"Error: {result.error}")
        sys.exit(1)


def pipeline() -> None:
    """Run full Oracle WMS to DBT transformation pipeline."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_pipeline()
    if result.is_failure:
        print(f"Error: {result.error}")
        sys.exit(1)


def info() -> None:
    """Show FLEXT DBT Oracle WMS information."""
    cli_service = FlextDbtOracleWmsCliService()
    result = cli_service.handle_info()
    if result.is_failure:
        print(f"Error: {result.error}")
        sys.exit(1)


def main() -> None:
    """Main CLI entry point for flext-dbt-oracle-wms."""
    try:
        # Simple command dispatching without Click
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
                print("Available commands: discover, extract, pipeline, info")
                sys.exit(1)
        else:
            print("FLEXT DBT Oracle WMS - Oracle WMS data transformation with DBT")
            print("Available commands: discover, extract, pipeline, info")
        
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(1)
    except (OSError, RuntimeError, ValueError) as e:
        logger.error(f"CLI error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
