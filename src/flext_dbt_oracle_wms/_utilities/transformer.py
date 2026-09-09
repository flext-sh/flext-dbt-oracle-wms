"""Transformer for WMS entity data to DBT models."""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import TYPE_CHECKING

from flext_meltano import u

from flext_core import r
from flext_dbt_oracle_wms import c, m, t

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import p


class FlextDbtOracleWmsUtilitiesTransformer(u.DbtOracleWms.Transformer):
    """Transformer for WMS entity data to DBT models."""

    def transform_all_entities(
        self,
        entity_data: t.MappingKV[str, t.SequenceOf[t.ConfigurationMapping]],
    ) -> p.Result[m.DbtOracleWms.EntityTransformationSet]:
        """Transform WMS entities into a typed transformation set."""
        # NOTE (multi-agent, bead mro-wfc8.3): returns a typed model (no
        # item.model_dump() roundtrip; WmsItems are surfaced directly).
        return self.transform_items(entity_data.get("items", [])).map(
            lambda items: m.DbtOracleWms.EntityTransformationSet(
                entity_names=("items",), items=tuple(items)
            )
        )

    def transform_items(
        self, records: t.SequenceOf[t.ConfigurationMapping]
    ) -> p.Result[Sequence[m.DbtOracleWms.WmsItem]]:
        """Transform item records to typed WmsItem models."""
        transformed: MutableSequence[m.DbtOracleWms.WmsItem] = []
        for index, record in enumerate(records):
            try:
                item = m.DbtOracleWms.WmsItem.model_validate(record)
            except c.ValidationError as exc:
                return r[Sequence[m.DbtOracleWms.WmsItem]].fail(
                    f"Invalid item record at index {index}: {exc}"
                )
            transformed.append(item)
        return r[Sequence[m.DbtOracleWms.WmsItem]].ok(transformed)

    def validate_business_rules(
        self, records: t.SequenceOf[t.ConfigurationMapping]
    ) -> p.Result[bool]:
        """Validate business rules for WMS records."""
        if not records:
            return r[bool].fail("No records to validate")
        return r[bool].ok(True)


__all__: list[str] = ["FlextDbtOracleWmsUtilitiesTransformer"]
