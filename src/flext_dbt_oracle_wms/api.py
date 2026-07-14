"""Public API facade for DBT Oracle WMS operations.

MRO facade composing the service mixins from ``services/`` (canonical FLEXT
structure per AGENTS.md §U15).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle_wms import p, u
from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings

# NOTE (multi-agent): mro-wgwh.4 — canonical api.py replaces the parallel
# simple_api branch (operator order: simple_api must not exist); behavior lives
# in services/* mixins composed by MRO.
from flext_dbt_oracle_wms.services.workflow import FlextDbtOracleWmsWorkflow


class FlextDbtOracleWms(FlextDbtOracleWmsWorkflow):
    """Unified DBT Oracle WMS facade for extraction, modeling, and workflow execution."""

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: u.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize the public DBT Oracle WMS facade."""
        super().__init__(settings=settings, client=client, service=service)


dbt_oracle_wms = FlextDbtOracleWms

__all__: list[str] = ["FlextDbtOracleWms", "dbt_oracle_wms"]
