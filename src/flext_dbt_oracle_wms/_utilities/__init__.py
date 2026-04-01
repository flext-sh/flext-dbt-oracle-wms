# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT Oracle WMS utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes

    from flext_dbt_oracle_wms._utilities.client import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtOracleWmsClient": "flext_dbt_oracle_wms._utilities.client",
    "client": "flext_dbt_oracle_wms._utilities.client",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
