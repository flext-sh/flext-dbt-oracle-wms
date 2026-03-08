"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import TypeAdapter

_STRING_ADAPTER = TypeAdapter(str)
__all__ = ["FlextDbtOracleWmsSettings"]
