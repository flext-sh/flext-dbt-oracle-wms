"""Test utilities for flext-dbt-oracle-wms.

Provides TestsFlextDbtOracleWmsUtilities, combining TestsFlextUtilities with
FlextDbtOracleWmsUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from flext_tests import FlextTestsUtilities

from flext_dbt_oracle_wms import FlextDbtOracleWmsUtilities, m, r, t

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class TestsFlextDbtOracleWmsUtilities(FlextTestsUtilities, FlextDbtOracleWmsUtilities):
    """Test utilities combining FlextTestsUtilities with flext-dbt-oracle-wms utilities."""

    class DbtOracleWms(FlextDbtOracleWmsUtilities.DbtOracleWms):
        """DbtOracleWms test utilities namespace."""

        class Tests:
            """Internal tests declarations."""

            class ScriptedWmsClient:
                """Deterministic Oracle WMS boundary fake returning canned typed results.

                Implements the p.DbtOracleWms.WmsClient boundary protocol with no
                I/O: every method reports a canned typed result and the extract
                boundary captures the requested entity names for observable
                forwarding assertions.
                """

                def __init__(
                    self,
                    *,
                    entities: p.Result[t.StrSequence] | None = None,
                    records_by_entity: (
                        t.MappingKV[str, t.SequenceOf[t.StrMapping]] | None
                    ) = None,
                    health: p.Result[m.Api.HttpResponse] | None = None,
                ) -> None:
                    """Initialize canned boundary results and capture state."""
                    self.started: bool = False
                    self.extracted_entities: t.SequenceOf[str] = ()
                    self._entities = (
                        entities
                        if entities is not None
                        else r[t.StrSequence].ok(("items", "shipments"))
                    )
                    self._records_by_entity: t.MappingKV[
                        str, t.SequenceOf[t.StrMapping]
                    ] = records_by_entity or {}
                    self._health = (
                        health
                        if health is not None
                        else r[m.Api.HttpResponse].ok(
                            m.Api.HttpResponse(status_code=200)
                        )
                    )

                def start(self) -> p.Result[bool]:
                    """Mark the boundary started and report success."""
                    self.started = True
                    return r[bool].ok(True)

                def discover_entities(self) -> p.Result[t.StrSequence]:
                    """Report the canned entity catalog."""
                    return self._entities

                def get_entity_data(
                    self,
                    entity_name: str,
                    limit: int | None = None,
                    filters: t.ConfigurationMapping | None = None,
                ) -> p.Result[t.SequenceOf[t.StrMapping]]:
                    """Report canned records for the requested entity and capture it."""
                    _ = limit
                    _ = filters
                    self.extracted_entities = (*self.extracted_entities, entity_name)
                    records = self._records_by_entity.get(
                        entity_name, ({"entity": entity_name},)
                    )
                    return r[t.SequenceOf[t.StrMapping]].ok(records)

                def health_check(self) -> p.Result[m.Api.HttpResponse]:
                    """Report the canned health response."""
                    return self._health

            class ScriptedDbtRunner:
                """Deterministic dbt runner boundary fake with call capture.

                Implements the p.DbtOracleWms.DbtRunner boundary protocol: the
                canned typed command result is reported verbatim and every
                invocation is counted for observable forwarding assertions.
                """

                def __init__(
                    self,
                    result: p.Result[m.Meltano.CommandExecutionResult] | None = None,
                ) -> None:
                    """Initialize the canned command result and call counter."""
                    self.calls: int = 0
                    self._result = (
                        result
                        if result is not None
                        else r[m.Meltano.CommandExecutionResult].ok(
                            m.Meltano.CommandExecutionResult(
                                command=("dbt", "run"),
                                success=True,
                                exit_code=0,
                                output="",
                                error="",
                                execution_time=0.0,
                            )
                        )
                    )

                def run_dbt_transformation(
                    self,
                    models: t.StrSequence | None = None,
                    project_dir: Path | None = None,
                ) -> p.Result[m.Meltano.CommandExecutionResult]:
                    """Count the call and report the canned command result."""
                    _ = models
                    _ = project_dir
                    self.calls += 1
                    return self._result


u = TestsFlextDbtOracleWmsUtilities

__all__: list[str] = ["TestsFlextDbtOracleWmsUtilities", "u"]
