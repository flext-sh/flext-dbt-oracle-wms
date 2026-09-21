"""Base utility helpers for DBT Oracle WMS operations."""

from __future__ import annotations

from flext_meltano import u
from flext_oracle_wms import u as _oracle_wms_u


class FlextDbtOracleWmsUtilitiesBase(u, _oracle_wms_u):
    """Namespace with utility helpers for extraction and modeling."""


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesBase"]
