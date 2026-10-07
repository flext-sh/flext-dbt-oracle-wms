"""Base type definitions for DBT Oracle WMS — MRO composition of parent type namespaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_typings/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import t
from flext_oracle_wms import t as _oracle_wms_t


class FlextDbtOracleWmsTypesBase(t, _oracle_wms_t):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    # No domain-specific types are actively used via t.DbtOracleWms.*
    # All structured data uses Pydantic models via FlextDbtOracleWmsModels (m).


__all__: list[str] = ["FlextDbtOracleWmsTypesBase"]
