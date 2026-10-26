# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Dbt Oracle WMS Types — MRO composition of parent type namespaces.

No domain-specific types are actively used via t.DbtOracleWms.*.
All structured data uses Pydantic models via FlextDbtOracleWmsModels (m).

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import t as flext_meltano_t
from flext_oracle_wms import t as flext_oracle_wms_t

from flext_dbt_oracle_wms._typings import FlextDbtOracleWmsTypesBase


class FlextDbtOracleWmsTypes(flext_meltano_t, flext_oracle_wms_t):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    class DbtOracleWms(FlextDbtOracleWmsTypesBase, flext_oracle_wms_t.OracleWms):
        """DBT Oracle WMS type namespace composing the parent declarations."""


# Facade assignment - enables canonical t.* consumption for consumers
t = FlextDbtOracleWmsTypes
__all__: list[str] = ["FlextDbtOracleWmsTypes", "t"]
