"""DBT-ready Pydantic models and transformation helpers."""

from __future__ import annotations

from flext_core import FlextResult, FlextTypes as t
from pydantic import BaseModel, Field


class FlextDbtOracleWmsItemDimension(BaseModel):
    """Item dimension payload for DBT."""

    item_id: str
    item_number: str
    item_description: str | None = None

    def to_dbt_dict(self) -> dict[str, t.GeneralValueType]:
        """Serialize item dimension to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsLocationDimension(BaseModel):
    """Location dimension payload for DBT."""

    location_id: str
    location_name: str
    facility_id: str

    def to_dbt_dict(self) -> dict[str, t.GeneralValueType]:
        """Serialize location dimension to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsInventoryFact(BaseModel):
    """Inventory fact payload for DBT."""

    item_id: str
    location_id: str
    facility_id: str
    quantity_on_hand: float = Field(default=0.0)

    def to_dbt_dict(self) -> dict[str, t.GeneralValueType]:
        """Serialize inventory fact to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsShipmentFact(BaseModel):
    """Shipment fact payload for DBT."""

    shipment_id: str
    order_id: str
    facility_id: str
    shipment_status: str = "CREATED"

    def to_dbt_dict(self) -> dict[str, t.GeneralValueType]:
        """Serialize shipment fact to DBT dictionary format."""
        return self.model_dump()


class FlextDbtOracleWmsTransformer:
    """Transformer converting raw entity data to DBT model payloads."""

    def transform_items(
        self,
        records: list[dict[str, t.GeneralValueType]],
    ) -> list[FlextDbtOracleWmsItemDimension]:
        """Transform records into item dimensions."""
        transformed: list[FlextDbtOracleWmsItemDimension] = []
        for record in records:
            item_id = record.get("itemId")
            item_number = record.get("itemNumber")
            if isinstance(item_id, str) and isinstance(item_number, str):
                transformed.append(
                    FlextDbtOracleWmsItemDimension(
                        item_id=item_id,
                        item_number=item_number,
                        item_description=record.get("itemDescription")
                        if isinstance(record.get("itemDescription"), str)
                        else None,
                    )
                )
        return transformed

    def transform_all_entities(
        self,
        entity_data: dict[str, list[dict[str, t.GeneralValueType]]],
    ) -> dict[str, list[t.GeneralValueType]]:
        """Transform supported entity sets into DBT payloads."""
        items = self.transform_items(entity_data.get("items", []))
        return {"items": [item.to_dbt_dict() for item in items]}

    def validate_business_rules(
        self,
        records: list[dict[str, t.GeneralValueType]],
    ) -> FlextResult[bool]:
        """Validate that at least one record is present."""
        if not records:
            return FlextResult[bool].fail("No records to validate")
        return FlextResult[bool].ok(True)


ItemDimension = FlextDbtOracleWmsItemDimension
LocationDimension = FlextDbtOracleWmsLocationDimension
InventoryFact = FlextDbtOracleWmsInventoryFact
ShipmentFact = FlextDbtOracleWmsShipmentFact
OracleWMSTransformer = FlextDbtOracleWmsTransformer

__all__ = [
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
    "InventoryFact",
    "ItemDimension",
    "LocationDimension",
    "OracleWMSTransformer",
    "ShipmentFact",
]
