"""FLEXT Dbt Oracle WMS Types — MRO composition of parent type namespaces.

No domain-specific types are actively used via t.DbtOracleWms.*.
All structured data uses Pydantic models via FlextDbtOracleWmsModels (m).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import t
from flext_oracle_wms import t as oracle_wms_t

from ._typings.base import FlextDbtOracleWmsTypesBase


class FlextDbtOracleWmsTypes(t):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    class DbtOracleWms(FlextDbtOracleWmsTypesBase, oracle_wms_t.OracleWms):
        """DBT Oracle WMS type namespace composing the parent declarations."""


# Facade assignment - enables canonical t.* consumption for consumers
t = FlextDbtOracleWmsTypes

__all__: list[str] = ["FlextDbtOracleWmsTypes", "t"]
