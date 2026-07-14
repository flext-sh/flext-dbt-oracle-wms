# AUTO-GENERATED FILE — canonical lazy tests facade. Regenerate with: make gen
"""Test package facade exposing the project test aliases lazily."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from tests.base import (
        TestsFlextDbtOracleWmsServiceBase as TestsFlextDbtOracleWmsServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextDbtOracleWmsConstants as TestsFlextDbtOracleWmsConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextDbtOracleWmsModels as TestsFlextDbtOracleWmsModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextDbtOracleWmsProtocols as TestsFlextDbtOracleWmsProtocols,
        p as p,
    )
    from tests.typings import (
        TestsFlextDbtOracleWmsTypes as TestsFlextDbtOracleWmsTypes,
        t as t,
    )
    from tests.utilities import (
        TestsFlextDbtOracleWmsUtilities as TestsFlextDbtOracleWmsUtilities,
        u as u,
    )

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".constants": ("TestsFlextDbtOracleWmsConstants", "c"),
        ".typings": ("TestsFlextDbtOracleWmsTypes", "t"),
        ".protocols": ("TestsFlextDbtOracleWmsProtocols", "p"),
        ".models": ("TestsFlextDbtOracleWmsModels", "m"),
        ".utilities": ("TestsFlextDbtOracleWmsUtilities", "u"),
        ".base": ("TestsFlextDbtOracleWmsServiceBase", "s"),
    },
)

install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
