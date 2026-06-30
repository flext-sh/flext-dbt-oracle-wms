# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_DBT_ORACLE_WMS_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._utilities": ("_utilities",),
        ".base": (
            "FlextDbtOracleWmsServiceBase",
            "s",
        ),
        ".cli": (
            "FlextDbtOracleWmsCliService",
            "main",
        ),
        ".constants": (
            "FlextDbtOracleWmsConstants",
            "c",
        ),
        ".models": (
            "FlextDbtOracleWmsModels",
            "m",
        ),
        ".protocols": (
            "FlextDbtOracleWmsProtocols",
            "p",
        ),
        ".settings": ("FlextDbtOracleWmsSettings",),
        ".typings": (
            "FlextDbtOracleWmsTypes",
            "t",
        ),
        ".utilities": (
            "FlextDbtOracleWmsUtilities",
            "u",
        ),
    },
)

__all__: list[str] = ["FLEXT_DBT_ORACLE_WMS_LAZY_IMPORTS_PART_01"]
