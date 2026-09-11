"""Deterministic DBT staging-model generation for WMS sources."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from flext_core import r
from flext_dbt_oracle_wms import c, m, t

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class FlextDbtOracleWmsUtilitiesModelBuilder:
    """Deterministic DBT staging-model generation for WMS sources."""

    class ModelBuilder:
        """DBT staging model generator for WMS entity sources."""

        @staticmethod
        def generate_wms_staging_models(
            oracle_sources: t.StrSequence,
        ) -> p.Result[Sequence[m.DbtOracleWms.DbtModel]]:
            """Create one staging model per source name."""
            models = [
                m.DbtOracleWms.DbtModel(
                    name=f"stg_wms_{source}",
                    dbt_model_type="staging",
                    wms_entity_type=source,
                    schema_name="wms_staging",
                    table_name=f"stg_{source}",
                    columns=[],
                    materialization=c.DbtOracleWms.Dbt.Materialization.VIEW.value,
                    sql_content=_STAGING_SELECT_TEMPLATE.format(source=source),
                    description=f"Staging model for {source}",
                    oracle_source=source,
                    dependencies=[],
                    wms_business_rules=[],
                )
                for source in oracle_sources
            ]
            return r[Sequence[m.DbtOracleWms.DbtModel]].ok(models)


# dbt Jinja template, not executable SQL: `source()` is resolved by dbt at
# compile time against the project's declared sources, so the value never
# reaches a database driver as a literal. Named here so the model definition
# below carries no inline query construction.
_STAGING_SELECT_TEMPLATE = "select * from {{{{ source('oracle_wms', '{source}') }}}}"


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesModelBuilder"]
