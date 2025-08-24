"""Compatibility facade: re-export dbt_models via models.py.

Standardizes imports to use flext_dbt_oracle_wms.models across the codebase.
"""

from __future__ import annotations

from .dbt_models import *
