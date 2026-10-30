"""Command-line handlers for DBT Oracle WMS package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/cli
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys
from collections.abc import Callable, Mapping, MutableMapping, Sequence
from typing import ClassVar

from flext_dbt_oracle_wms import FlextDbtOracleWms, p, r, t, u


class FlextDbtOracleWmsCliService:
    """CLI adapter that calls the public DBT Oracle WMS facade."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    _default_command: ClassVar[str] = "info"
    _default_entity: ClassVar[str] = "inventory"
    _service: FlextDbtOracleWms

    def __init__(self, service: FlextDbtOracleWms | None = None) -> None:
        """Initialize CLI service with the canonical DBT Oracle WMS facade.

        Args:
            service: Facade instance to dispatch commands through; a new
                default facade is created when omitted.

        """
        super().__init__()
        self._service = service if service is not None else FlextDbtOracleWms()

    def execute_command(
        self,
        command: str,
        args: Mapping[str, t.JsonValue | None] | None = None,
    ) -> int:
        """Execute a named CLI command and return an exit code.

        Args:
            command: Command name (``discover``, ``extract``,
                ``pipeline``, or ``info``).
            args: Optional command options, such as ``entity`` for the
                extract command.

        Returns:
            ``0`` when the command succeeds, ``1`` on unknown command or
            failure.

        """
        callables: Mapping[str, Callable[[], p.Result[str]]] = {
            "discover": self.handle_discover,
            "extract": lambda: self.handle_extract(args),
            "pipeline": self.handle_pipeline,
            "info": self.handle_info,
        }
        func = callables.get(command)
        if func is None:
            self.logger.error("Unknown command", command=command)
            return 1
        result = func()
        return 1 if result.failure else 0

    def main(self, argv: Sequence[str] | None = None) -> int:
        """Run the package CLI from argv-like input.

        Args:
            argv: Argument sequence to parse; defaults to
                ``sys.argv[1:]`` when omitted.

        Returns:
            ``0`` when the dispatched command succeeds, ``1`` otherwise.

        """
        command_args = list(argv) if argv is not None else sys.argv[1:]
        command = command_args[0] if command_args else self._default_command
        command_options: MutableMapping[str, t.JsonValue | None] = {}
        if command == "extract" and len(command_args) > 1:
            command_options["entity"] = command_args[1]
        return self.execute_command(command, command_options or None)

    def handle_discover(self) -> p.Result[str]:
        """Handle the discover command.

        Returns:
            Ok result with a completion message, or the discovery
            failure.

        """
        result = self._service.discover_oracle_wms_entities()
        if result.failure:
            return r[str].from_failure(result)
        return r[str].ok("Discovery completed successfully")

    def handle_extract(
        self,
        args: Mapping[str, t.JsonValue | None] | None = None,
    ) -> p.Result[str]:
        """Handle the extract command.

        Args:
            args: Optional command options; the ``entity`` key selects
                the WMS entity to extract.

        Returns:
            Ok result with a completion message, or the extraction or
            validation failure.

        """
        entity = self._default_entity
        if args is not None:
            entity_value = args.get("entity")
            if entity_value is not None:
                validated = u.validate_value(u.str_adapter(), entity_value)
                if validated.failure:
                    return r[str].from_failure(validated)
                stripped = validated.value.strip()
                if stripped:
                    entity = stripped
        result = self._service.extract_oracle_wms_data(entity, None)
        if result.failure:
            return r[str].from_failure(result)
        return r[str].ok("Extraction completed successfully")

    @staticmethod
    def handle_info() -> p.Result[str]:
        """Handle the package info command.

        Returns:
            Ok result carrying the package display name.

        """
        return r[str].ok("FLEXT DBT Oracle WMS")

    def handle_pipeline(self) -> p.Result[str]:
        """Handle the full pipeline command.

        Returns:
            Ok result with a completion message, or the pipeline
            failure.

        """
        result = self._service.run_oracle_wms_to_dbt_workflow(
            generate_models=False,
            run_transformations=True,
        )
        if result.failure:
            return r[str].from_failure(result)
        return r[str].ok("Pipeline completed successfully")


def main(argv: Sequence[str] | None = None) -> int:
    """Run the DBT Oracle WMS CLI entrypoint.

    Args:
        argv: Argument sequence to parse; defaults to ``sys.argv[1:]``
            when omitted.

    Returns:
        ``0`` when the dispatched command succeeds, ``1`` otherwise.

    """
    return FlextDbtOracleWmsCliService().main(argv)


__all__: list[str] = ["FlextDbtOracleWmsCliService", "main"]
