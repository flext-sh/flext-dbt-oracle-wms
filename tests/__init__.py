# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_dbt_oracle_wms import (
        constants,
        models,
        protocols,
        test_basic,
        test_simple_api,
        typings,
        unit,
        utilities,
    )
    from flext_dbt_oracle_wms.constants import (
        FlextDbtOracleWmsTestConstants,
        FlextDbtOracleWmsTestConstants as c,
    )
    from flext_dbt_oracle_wms.models import (
        FlextDbtOracleWmsTestModels,
        FlextDbtOracleWmsTestModels as m,
    )
    from flext_dbt_oracle_wms.protocols import (
        FlextDbtOracleWmsTestProtocols,
        FlextDbtOracleWmsTestProtocols as p,
    )
    from flext_dbt_oracle_wms.typings import (
        FlextDbtOracleWmsTestTypes,
        FlextDbtOracleWmsTestTypes as t,
    )
    from flext_dbt_oracle_wms.unit import test_package_import
    from flext_dbt_oracle_wms.utilities import (
        FlextDbtOracleWmsTestUtilities,
        FlextDbtOracleWmsTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_dbt_oracle_wms.unit",),
    {
        "FlextDbtOracleWmsTestConstants": "flext_dbt_oracle_wms.constants",
        "FlextDbtOracleWmsTestModels": "flext_dbt_oracle_wms.models",
        "FlextDbtOracleWmsTestProtocols": "flext_dbt_oracle_wms.protocols",
        "FlextDbtOracleWmsTestTypes": "flext_dbt_oracle_wms.typings",
        "FlextDbtOracleWmsTestUtilities": "flext_dbt_oracle_wms.utilities",
        "c": ("flext_dbt_oracle_wms.constants", "FlextDbtOracleWmsTestConstants"),
        "constants": "flext_dbt_oracle_wms.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_dbt_oracle_wms.models", "FlextDbtOracleWmsTestModels"),
        "models": "flext_dbt_oracle_wms.models",
        "p": ("flext_dbt_oracle_wms.protocols", "FlextDbtOracleWmsTestProtocols"),
        "protocols": "flext_dbt_oracle_wms.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("flext_dbt_oracle_wms.typings", "FlextDbtOracleWmsTestTypes"),
        "test_basic": "flext_dbt_oracle_wms.test_basic",
        "test_simple_api": "flext_dbt_oracle_wms.test_simple_api",
        "typings": "flext_dbt_oracle_wms.typings",
        "u": ("flext_dbt_oracle_wms.utilities", "FlextDbtOracleWmsTestUtilities"),
        "unit": "flext_dbt_oracle_wms.unit",
        "utilities": "flext_dbt_oracle_wms.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
