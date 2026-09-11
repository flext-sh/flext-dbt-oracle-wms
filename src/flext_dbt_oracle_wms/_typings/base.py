"""Base type definitions for DBT Oracle WMS — MRO composition of parent type namespaces."""

from __future__ import annotations

from flext_meltano import t
from flext_oracle_wms import FlextOracleWmsTypes


class FlextDbtOracleWmsTypesBase(t, FlextOracleWmsTypes):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    # No domain-specific types are actively used via t.DbtOracleWms.*
    # All structured data uses Pydantic models via FlextDbtOracleWmsModels (m).


__all__: list[str] = ["FlextDbtOracleWmsTypesBase"]
