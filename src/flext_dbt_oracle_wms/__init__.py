# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT ORACLE WMS - Oracle WMS Data Transformations using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

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

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_dbt_oracle_wms import (
        _utilities,
        cli,
        client,
        constants,
        models,
        protocols,
        simple_api,
        typings,
        utilities,
    )
    from flext_dbt_oracle_wms._utilities import FlextDbtOracleWmsClient
    from flext_dbt_oracle_wms.cli import (
        FlextDbtOracleWmsCliService,
        discover,
        extract,
        info,
        logger,
        main,
        pipeline,
    )
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsConstants,
        FlextDbtOracleWmsConstants as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsModels,
        FlextDbtOracleWmsModels as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsProtocols,
        FlextDbtOracleWmsProtocols as p,
    )
    from flext_dbt_oracle_wms.simple_api import FlextDbtOracleWms
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTypes,
        FlextDbtOracleWmsTypes as t,
    )
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsUtilities,
        FlextDbtOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
    ("flext_dbt_oracle_wms._utilities",),
    {
        "FlextDbtOracleWms": "flext_dbt_oracle_wms.simple_api",
        "FlextDbtOracleWmsCliService": "flext_dbt_oracle_wms.cli",
        "FlextDbtOracleWmsConstants": "flext_dbt_oracle_wms.constants",
        "FlextDbtOracleWmsModels": "flext_dbt_oracle_wms.models",
        "FlextDbtOracleWmsProtocols": "flext_dbt_oracle_wms.protocols",
        "FlextDbtOracleWmsTypes": "flext_dbt_oracle_wms.typings",
        "FlextDbtOracleWmsUtilities": "flext_dbt_oracle_wms.utilities",
        "_utilities": "flext_dbt_oracle_wms._utilities",
        "c": ("flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsConstants"),
        "cli": "flext_dbt_oracle_wms.cli",
        "client": "flext_dbt_oracle_wms.client",
        "constants": "flext_dbt_oracle_wms.constants",
        "d": "flext_meltano",
        "discover": "flext_dbt_oracle_wms.cli",
        "e": "flext_meltano",
        "extract": "flext_dbt_oracle_wms.cli",
        "h": "flext_meltano",
        "info": "flext_dbt_oracle_wms.cli",
        "logger": "flext_dbt_oracle_wms.cli",
        "m": ("flext_dbt_oracle_wms.models", "FlextDbtOracleWmsModels"),
        "main": "flext_dbt_oracle_wms.cli",
        "models": "flext_dbt_oracle_wms.models",
        "p": ("flext_dbt_oracle_wms.protocols", "FlextDbtOracleWmsProtocols"),
        "pipeline": "flext_dbt_oracle_wms.cli",
        "protocols": "flext_dbt_oracle_wms.protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "simple_api": "flext_dbt_oracle_wms.simple_api",
        "t": ("flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTypes"),
        "typings": "flext_dbt_oracle_wms.typings",
        "u": ("flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsUtilities"),
        "utilities": "flext_dbt_oracle_wms.utilities",
        "x": "flext_meltano",
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
