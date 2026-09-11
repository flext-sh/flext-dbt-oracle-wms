"""FlextDbtOracleWmsConfig — frozen config singleton for flext-dbt-oracle-wms (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``DbtOracleWms:`` key and
are exposed through the open ``config.DbtOracleWms`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.DbtOracleWms.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoConfig, m


class FlextDbtOracleWmsConfig(FlextMeltanoConfig):
    """DbtOracleWms config auto-loaded model-less from ``config/*.yaml``."""

    class DbtOracleWms(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

        model_config = m.ConfigDict(extra="allow", frozen=True)


config: FlextDbtOracleWmsConfig = FlextDbtOracleWmsConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_oracle_wms import config``."""

__all__: list[str] = ["FlextDbtOracleWmsConfig", "config"]
