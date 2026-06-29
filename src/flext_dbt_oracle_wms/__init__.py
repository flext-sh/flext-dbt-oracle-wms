# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
from flext_dbt_oracle_wms.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_dbt_oracle_wms.cli import (
        FlextDbtOracleWmsCliService as FlextDbtOracleWmsCliService,
        main as main,
    )
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants as FlextDbtOracleWmsConstants,
        c as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels as FlextDbtOracleWmsModels,
        m as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsProtocols as FlextDbtOracleWmsProtocols,
        p as p,
    )
    from flext_dbt_oracle_wms.settings import (
        FlextDbtOracleWmsSettings as FlextDbtOracleWmsSettings,
    )
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes as FlextDbtOracleWmsTypes,
        t as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities as FlextDbtOracleWmsUtilities,
        u as u,
    )
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
_LAZY_IMPORTS = build_lazy_import_map(
    {
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
        "flext_meltano": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
    "FlextDbtOracleWmsCliService",
    "FlextDbtOracleWmsConstants",
    "FlextDbtOracleWmsModels",
    "FlextDbtOracleWmsProtocols",
    "FlextDbtOracleWmsSettings",
    "FlextDbtOracleWmsTypes",
    "FlextDbtOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
