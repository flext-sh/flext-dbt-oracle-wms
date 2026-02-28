"""DBT-ready Pydantic models and transformation helpers."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t
from pydantic import BaseModel, ConfigDict, Field, ValidationError


class _RawItemRecord(BaseModel):
    """Validated raw Oracle WMS item payload."""

    model_config = ConfigDict(populate_by_name=True)

    item_id: str = Field(alias="itemId")
    item_number: str = Field(alias="itemNumber")
    item_description: str | None = Field(default=None, alias="itemDescription")


class FlextDbtOracleWmsItemDimension(BaseModel):
    """Item dimension payload for DBT."""

    item_id: str
    item_number: str
    item_description: str | None = None

    def to_dbt_dict(self) -> Mapping[str, t.GeneralValueType]:
        """Serialize item dimension to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsLocationDimension(BaseModel):
    """Location dimension payload for DBT."""

    location_id: str
    location_name: str
    facility_id: str

    def to_dbt_dict(self) -> Mapping[str, t.GeneralValueType]:
        """Serialize location dimension to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsInventoryFact(BaseModel):
    """Inventory fact payload for DBT."""

    item_id: str
    location_id: str
    facility_id: str
    quantity_on_hand: float = Field(default=0.0)

    def to_dbt_dict(self) -> Mapping[str, t.GeneralValueType]:
        """Serialize inventory fact to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsShipmentFact(BaseModel):
    """Shipment fact payload for DBT."""

    shipment_id: str
    order_id: str
    facility_id: str
    shipment_status: str = "CREATED"

    def to_dbt_dict(self) -> Mapping[str, t.GeneralValueType]:
        """Serialize shipment fact to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsTransformer:
    """Transformer converting raw entity data to DBT model payloads."""

    def transform_items(
        self,
        records: list[Mapping[str, t.GeneralValueType]],
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

    def transform_all_entities(
        self,
        entity_data: Mapping[str, list[Mapping[str, t.GeneralValueType]]],
    ) -> Mapping[str, list[t.GeneralValueType]]:
        """Transform supported entity sets into DBT payloads."""
        items = self.transform_items(entity_data.get("items", []))
        return {"items": [item.to_dbt_dict() for item in items]}

    def validate_business_rules(
        self,
        records: list[Mapping[str, t.GeneralValueType]],
    ) -> FlextResult[bool]:
        """Validate that at least one record is present."""
        if not records:
            return FlextResult[bool].fail("No records to validate")
        return FlextResult[bool].ok(True)


__all__ = [
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
]
