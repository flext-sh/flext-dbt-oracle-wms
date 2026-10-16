"""Public API facade for DBT Oracle WMS operations.

MRO facade composing the service mixins from ``services/`` (canonical FLEXT
structure per AGENTS.md §U15).

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_dbt_oracle_wms.services import FlextDbtOracleWmsWorkflow

# NOTE (multi-agent): mro-wgwh.4 — canonical api.py replaces the parallel
# simple_api branch (operator order: simple_api must not exist); behavior lives
# in services/* mixins composed by MRO.

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, p


class FlextDbtOracleWms(FlextDbtOracleWmsWorkflow):
    """Unified DBT Oracle WMS facade for extraction, modeling, and workflows."""

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: p.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize the public DBT Oracle WMS facade.

        Args:
            settings: Settings contract; the global settings singleton is
                used when omitted.
            client: Injected WMS client boundary; a real client is created
                lazily when omitted.
            service: Injected workflow service boundary; a default service
                is created lazily when omitted.

        """
        super().__init__(settings=settings, client=client, service=service)


dbt_oracle_wms: FlextDbtOracleWms = FlextDbtOracleWms.fetch_global()
"""Process-wide DBT Oracle WMS facade singleton resolved from the global container."""

__all__: list[str] = ["FlextDbtOracleWms", "dbt_oracle_wms"]
