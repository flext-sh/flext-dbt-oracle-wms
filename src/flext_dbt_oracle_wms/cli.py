"""Command-line handlers for DBT Oracle WMS package."""

from __future__ import annotations

import sys
from collections.abc import Mapping
from typing import ClassVar

from flext_core import r
from flext_dbt_oracle_wms import FlextDbtOracleWms, c, p, t, u


class FlextDbtOracleWmsCliService:
    """CLI adapter that calls the public DBT Oracle WMS facade."""

    _logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    _default_command: ClassVar[str] = "info"
    _default_entity: ClassVar[str] = "inventory"
    _service: FlextDbtOracleWms

    def __init__(self, service: FlextDbtOracleWms | None = None) -> None:
        """Initialize CLI service with the canonical DBT Oracle WMS facade."""
        super().__init__()
        self._service = service if service is not None else FlextDbtOracleWms()

    def execute_command(
        self,
        command: str,
        args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> int:
        """Execute a named CLI command and return an exit code."""
        handlers = {
            "discover": self.handle_discover,
            "extract": self.handle_extract,
            "pipeline": self.handle_pipeline,
            "info": self.handle_info,
        }
        handler = handlers.get(command)
        if handler is None:
            self._logger.error("Unknown command", command=command)
            return 1
        result = handler(args)
        return 1 if result.failure else 0

    def main(self, argv: t.StrSequence | None = None) -> int:
        """Run the package CLI from argv-like input."""
        command_args = list(argv) if argv is not None else sys.argv[1:]
        command = command_args[0] if command_args else self._default_command
        command_options: t.MutableMappingKV[str, t.ContainerValue | None] = {}
        if command == "extract" and len(command_args) > 1:
            command_options["entity"] = command_args[1]
        return self.execute_command(command, command_options or None)

    def handle_discover(
        self,
        _args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> r[str]:
        """Handle discover command."""
        result = self._service.discover_oracle_wms_entities()
        if result.failure:
            return r[str].fail(result.error or "Discover failed")
        return r[str].ok("Discovery completed successfully")

    def handle_extract(
        self,
        args: Mapping[str, t.ContainerValue | None] | None = None,
    ) -> r[str]:
        """Handle extract command."""
        entity = self._default_entity
        if args is not None:
            entity_value = args.get("entity")
            try:
                validated_entity = t.TEXT_VALUE_ADAPTER.validate_python(
                    entity_value,
                ).strip()
            except c.ValidationError:
                validated_entity = ""
            if validated_entity:
                entity = validated_entity
        result = self._service.extract_oracle_wms_data(entity, None)
        if result.failure:
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
        result = self._service.run_oracle_wms_to_dbt_workflow(
            generate_models=False,
            run_transformations=True,
        )
        if result.failure:
            return r[str].fail(result.error or "Pipeline failed")
        return r[str].ok("Pipeline completed successfully")


def main(argv: t.StrSequence | None = None) -> int:
    """Run the DBT Oracle WMS CLI entrypoint."""
    return FlextDbtOracleWmsCliService().main(argv)


__all__: list[str] = ["FlextDbtOracleWmsCliService", "main"]
