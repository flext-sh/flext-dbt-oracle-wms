"""DBT Oracle WMS model definitions and transformers."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import r, t
from pydantic import BaseModel, ConfigDict, Field, ValidationError


class _RawItemRecord(BaseModel):
    model_config = ConfigDict(extra="ignore")

    item_id: str = Field(default="")
    item_number: str = Field(default="")
    item_description: str = Field(default="")


class FlextDbtOracleWmsItemDimension(BaseModel):
    """Item dimension model for WMS analytics."""

    item_id: str = Field(default="")
    item_number: str = Field(default="")
    item_description: str = Field(default="")

    def to_dbt_dict(self) -> Mapping[str, t.ContainerValue]:
        """Convert item dimension to DBT-compatible dictionary."""
        return {
            "item_id": self.item_id,
            "item_number": self.item_number,
            "item_description": self.item_description,
        }


class FlextDbtOracleWmsInventoryFact(BaseModel):
    """Inventory fact table model."""

    record: Mapping[str, t.ContainerValue] = Field(default_factory=dict)


class FlextDbtOracleWmsLocationDimension(BaseModel):
    """Location dimension model for warehouse analytics."""

    record: Mapping[str, t.ContainerValue] = Field(default_factory=dict)


class FlextDbtOracleWmsShipmentFact(BaseModel):
    """Shipment fact table model."""

    record: Mapping[str, t.ContainerValue] = Field(default_factory=dict)


class FlextDbtOracleWmsTransformer:
    """Transformer for WMS entity data to DBT models."""

    def transform_all_entities(
        self, entity_data: Mapping[str, list[Mapping[str, t.ContainerValue]]]
    ) -> Mapping[str, list[t.ContainerValue]]:
        """Transform all WMS entities to DBT-compatible format."""
        items: list[FlextDbtOracleWmsItemDimension] = self.transform_items(
            entity_data.get("items", [])
        )
        return {"items": [item.to_dbt_dict() for item in items]}

    def transform_items(
        self, records: list[Mapping[str, t.ContainerValue]]
    ) -> list[FlextDbtOracleWmsItemDimension]:
        """Transform item records to item dimension models."""
        transformed: list[FlextDbtOracleWmsItemDimension] = []
        for record in records:
            try:
                raw_record: _RawItemRecord = _RawItemRecord.model_validate(record)
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
    ) -> r[bool]:
        """Validate business rules for WMS records."""
        if not records:
            return r[bool].fail("No records to validate")
        return r[bool].ok(True)


__all__ = [
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
]
