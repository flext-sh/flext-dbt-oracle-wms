"""Command-line handlers for DBT Oracle WMS package."""

from __future__ import annotations

import sys
from collections.abc import Mapping

from flext_core import FlextLogger, FlextResult, t
from pydantic import TypeAdapter, ValidationError

from .client import FlextDbtOracleWmsClient

logger = FlextLogger(__name__)
_STRING_ADAPTER = TypeAdapter(str)


class FlextDbtOracleWmsCliService:
    """CLI adapter that calls typed client operations."""

    def __init__(self) -> None:
        """Initialize CLI service with a DBT Oracle WMS client."""
        super().__init__()
        self._client = FlextDbtOracleWmsClient()

    def handle_discover(
        self,
        _args: Mapping[str, t.ContainerValue] | None = None,
    ) -> FlextResult[str]:
        """Handle discover command."""
        result = self._client.discover_oracle_wms_entities()
        if result.is_failure:
            return FlextResult[str].fail(result.error or "Discover failed")
        return FlextResult[str].ok("Discovery completed successfully")

    def handle_extract(
        self,
        args: Mapping[str, t.ContainerValue] | None = None,
    ) -> FlextResult[str]:
        """Handle extract command."""
        entity = "inventory"
        if args is not None:
            entity_value = args.get("entity")
            try:
                validated_entity = _STRING_ADAPTER.validate_python(entity_value).strip()
            except ValidationError:
                validated_entity = ""
            if validated_entity:
                entity = validated_entity
        result = self._client.extract_oracle_wms_data(entity, None)
        if result.is_failure:
            return FlextResult[str].fail(result.error or "Extract failed")
        return FlextResult[str].ok("Extraction completed successfully")

    def handle_pipeline(
        self,
        _args: Mapping[str, t.ContainerValue] | None = None,
    ) -> FlextResult[str]:
        """Handle full pipeline command."""
        result = self._client.run_full_oracle_wms_to_dbt_pipeline()
        if result.is_failure:
            return FlextResult[str].fail(result.error or "Pipeline failed")
        return FlextResult[str].ok("Pipeline completed successfully")

    def handle_info(
        self,
        _args: Mapping[str, t.ContainerValue] | None = None,
    ) -> FlextResult[str]:
        """Handle package info command."""
        return FlextResult[str].ok("FLEXT DBT Oracle WMS")


def discover() -> None:
    """Execute discover command and exit with status code."""
    result = FlextDbtOracleWmsCliService().handle_discover()
    if result.is_failure:
        sys.exit(1)


def extract() -> None:
    """Execute extract command and exit with status code."""
    result = FlextDbtOracleWmsCliService().handle_extract()
    if result.is_failure:
        sys.exit(1)


def pipeline() -> None:
    """Execute pipeline command and exit with status code."""
    result = FlextDbtOracleWmsCliService().handle_pipeline()
    if result.is_failure:
        sys.exit(1)


def info() -> None:
    """Execute info command and exit with status code."""
    result = FlextDbtOracleWmsCliService().handle_info()
    if result.is_failure:
        sys.exit(1)


def main() -> None:
    """Main package CLI entrypoint."""
    command = sys.argv[1] if len(sys.argv) > 1 else "info"
    if command == "discover":
        discover()
    elif command == "extract":
        extract()
    elif command == "pipeline":
        pipeline()
    elif command == "info":
        info()
    else:
        logger.error("Unknown command", extra={"command": command})
        sys.exit(1)


if __name__ == "__main__":
    main()
