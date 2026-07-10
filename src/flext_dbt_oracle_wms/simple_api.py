"""FLEXT DBT ORACLE WMS API - Unified facade for DBT Oracle WMS operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Unified facade for FLEXT DBT Oracle WMS operations with complete FLEXT integration.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_dbt_oracle_wms._simple_api_workflow import FlextDbtOracleWmsWorkflow

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p
    from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings
    from flext_dbt_oracle_wms.utilities import u


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


__all__: list[str] = ["FlextDbtOracleWms"]
