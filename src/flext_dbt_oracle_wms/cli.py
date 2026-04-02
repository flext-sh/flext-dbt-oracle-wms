"""Command-line handlers for DBT Oracle WMS package."""

from __future__ import annotations

import sys
from collections.abc import Mapping

from pydantic import ValidationError

from flext_core import FlextLogger, r
from flext_dbt_oracle_wms import t

from .client import FlextDbtOracleWmsClient

logger = FlextLogger(__name__)


class FlextDbtOracleWmsCliService:
    """CLI adapter that calls typed client operations."""

    def __init__(self) -> None:
        """Initialize CLI service with a DBT Oracle WMS client."""
        super().__init__()
        self._client = FlextDbtOracleWmsClient()

    def handle_discover(
        self,
        _args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> r[str]:
        """Handle discover command."""
        result = self._client.discover_oracle_wms_entities()
        if result.is_failure:
            return r[str].fail(result.error or "Discover failed")
        return r[str].ok("Discovery completed successfully")

    def handle_extract(
        self,
        args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> r[str]:
        """Handle extract command."""
        entity = "inventory"
        if args is not None:
            entity_value = args.get("entity")
            try:
                validated_entity = t.TEXT_VALUE_ADAPTER.validate_python(
                    entity_value,
                ).strip()
            except ValidationError:
                validated_entity = ""
            if validated_entity:
                entity = validated_entity
        result = self._client.extract_oracle_wms_data(entity, None)
        if result.is_failure:
            return r[str].fail(result.error or "Extract failed")
        return r[str].ok("Extraction completed successfully")

    def handle_info(
        self,
        _args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> r[str]:
        """Handle package info command."""
        return r[str].ok("FLEXT DBT Oracle WMS")

    def handle_pipeline(
        self,
        _args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> r[str]:
        """Handle full pipeline command."""
        result = self._client.run_full_oracle_wms_to_dbt_pipeline()
        if result.is_failure:
            return r[str].fail(result.error or "Pipeline failed")
        return r[str].ok("Pipeline completed successfully")


def discover() -> int:
    """Execute discover command and return status code."""
    result = FlextDbtOracleWmsCliService().handle_discover()
    return 1 if result.is_failure else 0


def extract() -> int:
    """Execute extract command and return status code."""
    result = FlextDbtOracleWmsCliService().handle_extract()
    return 1 if result.is_failure else 0


def pipeline() -> int:
    """Execute pipeline command and return status code."""
    result = FlextDbtOracleWmsCliService().handle_pipeline()
    return 1 if result.is_failure else 0


def info() -> int:
    """Execute info command and return status code."""
    result = FlextDbtOracleWmsCliService().handle_info()
    return 1 if result.is_failure else 0


def main() -> int:
    """Main package CLI entrypoint."""
    command = sys.argv[1] if len(sys.argv) > 1 else "info"
    if command == "discover":
        return discover()
    if command == "extract":
        return extract()
    if command == "pipeline":
        return pipeline()
    if command == "info":
        return info()
    logger.error("Unknown command", command=command)
    return 1


if __name__ == "__main__":
    sys.exit(main())
