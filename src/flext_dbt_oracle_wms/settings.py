"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_core import FlextLogger, FlextSettings
from pydantic import Field

logger = FlextLogger(__name__)


class FlextDbtOracleWmsSettings(FlextSettings):
    """Runtime settings for DBT Oracle WMS transformations."""

    required_fields_per_entity: Annotated[
        dict[str, list[str]],
        Field(
            default_factory=dict,
            description="Required fields per WMS entity for validation",
        ),
    ]
    oracle_wms_environment: Annotated[
        str,
        Field(
            default="development",
            description="Oracle WMS environment (development/production)",
        ),
    ]
    oracle_wms_base_url: Annotated[
        str, Field(default="", description="Base URL for Oracle WMS API")
    ]


__all__ = ["FlextDbtOracleWmsSettings"]
