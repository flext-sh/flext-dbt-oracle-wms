"""FlextDbtOracleWmsConfig frozen config singleton for flext-dbt-oracle-wms.

Reference: ADR-005 §7. Business rules live in ``config/*.yaml`` under the
``DbtOracleWms:`` key, validated once into the typed ``config.DbtOracleWms``
namespace. Access is ``config.DbtOracleWms.<field>``.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m


class FlextDbtOracleWmsConfig(FlextMeltanoConfig):
    """DbtOracleWms config auto-loaded from ``config/*.yaml`` and validated.

    MRO carries ``FlextSettings`` FIRST (ENFORCE-042); unlike never-instantiated
    namespace holders, this class IS instantiated by ``fetch_global``, so the
    instance-inert holder contract does not apply and pydantic settings
    construction machinery stays intact.
    """

    class Identity(m.FrozenModel):
        """Project identity metadata from ``config/dbt-oracle-wms.yaml``."""

        name: str = m.Field(min_length=1, description="Configured project name.")
        version: str = m.Field(
            min_length=1, description="Configured project version."
        )

    DbtOracleWms: Annotated[
        Identity,
        m.Field(description="Project identity from ``config/dbt-oracle-wms.yaml``."),
    ]


config: FlextDbtOracleWmsConfig = FlextDbtOracleWmsConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_oracle_wms``
import ``config``."""

__all__: list[str] = ["FlextDbtOracleWmsConfig", "config"]
