# AUTO-GENERATED FILE — Regenerate with: make gen
"""Services package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle_wms.services.base import (
        FlextDbtOracleWmsBase as FlextDbtOracleWmsBase,
    )
    from flext_dbt_oracle_wms.services.metadata import (
        FlextDbtOracleWmsMetadata as FlextDbtOracleWmsMetadata,
    )
    from flext_dbt_oracle_wms.services.models import (
        FlextDbtOracleWmsModelsApi as FlextDbtOracleWmsModelsApi,
    )
    from flext_dbt_oracle_wms.services.workflow import (
        FlextDbtOracleWmsWorkflow as FlextDbtOracleWmsWorkflow,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".base": ("FlextDbtOracleWmsBase",),
        ".metadata": ("FlextDbtOracleWmsMetadata",),
        ".models": ("FlextDbtOracleWmsModelsApi",),
        ".workflow": ("FlextDbtOracleWmsWorkflow",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
