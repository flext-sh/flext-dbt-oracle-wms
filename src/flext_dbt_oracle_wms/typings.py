"""FLEXT Dbt Oracle WMS Types — MRO composition of parent type namespaces.

No domain-specific types are actively used via t.DbtOracleWms.*.
All structured data uses Pydantic models via FlextDbtOracleWmsModels (m).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes


class FlextDbtOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """MRO facade composing Meltano + OracleWms type namespaces."""


# Facade assignment - enables canonical t.* consumption for consumers
t = FlextDbtOracleWmsTypes

__all__ = [
    "FlextDbtOracleWmsTypes",
    "t",
]
