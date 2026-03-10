"""DBT-ready Pydantic models and transformation helpers."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t
from pydantic import ValidationError


class FlextDbtOracleWmsTransformer:
    """Transformer converting raw entity data to DBT model payloads."""

    def transform_all_entities(
        self, entity_data: Mapping[str, list[Mapping[str, t.ContainerValue]]]
    ) -> Mapping[str, list[t.ContainerValue]]:
        """Transform supported entity sets into DBT payloads."""
        items = self.transform_items(entity_data.get("items", []))
        return {"items": [item.to_dbt_dict() for item in items]}

    def transform_items(
        self, records: list[Mapping[str, t.ContainerValue]]
    ) -> list[FlextDbtOracleWmsItemDimension]:
        """Transform records into item dimensions."""
        transformed: list[FlextDbtOracleWmsItemDimension] = []
        for record in records:
            try:
                raw_record = _RawItemRecord.model_validate(record)
            except ValidationError:
                continue
            transformed.append(
                FlextDbtOracleWmsItemDimension(
                    item_id=raw_record.item_id,
                    item_number=raw_record.item_number,
                    item_description=raw_record.item_description,
                )
            )
        return transformed

    def validate_business_rules(
        self, records: list[Mapping[str, t.ContainerValue]]
    ) -> FlextResult[bool]:
        """Validate that at least one record is present."""
        if not records:
            return FlextResult[bool].fail("No records to validate")
        return FlextResult[bool].ok(True)


__all__ = [
    "FlextDbtOracleWmsInventoryFact",  # noqa: F822
    "FlextDbtOracleWmsItemDimension",  # noqa: F822
    "FlextDbtOracleWmsLocationDimension",  # noqa: F822
    "FlextDbtOracleWmsShipmentFact",  # noqa: F822
    "FlextDbtOracleWmsTransformer",
]
