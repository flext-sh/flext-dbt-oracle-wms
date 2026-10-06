"""Transformer for WMS entity data to DBT models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle_wms/_utilities/transformer
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import TYPE_CHECKING

from flext_core import r
from flext_dbt_oracle_wms import c, m, t

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class FlextDbtOracleWmsUtilitiesTransformer:
    """Transformer for WMS entity data to DBT models."""

    class Transformer:
        """WMS entity data transformer for DBT pipeline preparation."""

        def transform_all_entities(
            self,
            entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
        ) -> p.Result[m.DbtOracleWms.EntityTransformationSet]:
            """Transform WMSentities into a typed transformation set.

            Returns:
                The resulting ``p.Result[m.DbtOracleWms.EntityTransformationSet]``.
            """
            # NOTE (multi-agent, bead mro-wfc8.3): returns a typed model (no
            # item.model_dump() roundtrip; WmsItems are surfaced directly).
            return self.transform_items(entity_data.get("items", [])).map(
                lambda items: m.DbtOracleWms.EntityTransformationSet(
                    entity_names=("items",),
                    items=tuple(items),
                ),
            )

        @staticmethod
        def transform_items(
            records: t.SequenceOf[t.ConfigurationMapping],
        ) -> p.Result[Sequence[m.DbtOracleWms.WmsItem]]:
            """Transform item records to typed WmsItem models.

            Returns:
                The resulting ``p.Result[Sequence[m.DbtOracleWms.WmsItem]]``.
            """
            transformed: MutableSequence[m.DbtOracleWms.WmsItem] = []
            for index, record in enumerate(records):
                try:
                    item = m.DbtOracleWms.WmsItem.model_validate(record)
                except c.ValidationError as exc:
                    return r[Sequence[m.DbtOracleWms.WmsItem]].fail(
                        f"Invalid item record at index {index}: {exc}",
                    )
                transformed.append(item)
            return r[Sequence[m.DbtOracleWms.WmsItem]].ok(transformed)


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesTransformer"]
