"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_oracle_wms import FlextOracleWmsEntity

from flext import FlextLogger, FlextResult, FlextSettings

logger = FlextLogger(__name__)


# === Internal helpers for safe type conversion ===
def _get_str(value: object, default: str | None = None) -> str | None:
    if value is None:
        return default
    if isinstance(value, str):
        return value
    try:
        return str(value)
    except Exception:
        return default


def _get_float(value: object, default: float | None = None) -> float | None:
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return default
    return default


def _get_bool(value: object, *, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "1", "yes", "y"}:
            return True
        if lowered in {"false", "0", "no", "n"}:
            return False
    return default


class FlextDbtOracleWmsItemDimension(FlextSettings):
    """Item dimension model for DBT Oracle WMS transformations.

    Represents an item dimension table structure optimized for analytics.

    Returns:
    str | None: Description of return value.

    """

    item_id: str
    item_number: str
    item_description: str | None = None
    item_category: str | None = None
    unit_of_measure: str | None = None
    unit_cost: float | None = None
    weight: float | None = None
    volume: float | None = None
    is_active: bool = True
    created_date: str | None = None
    modified_date: str | None = None

    @classmethod
    def from_oracle_wms_record(
        cls,
        record: dict[str, object],
    ) -> FlextDbtOracleWmsItemDimension:
        """Create item dimension from Oracle WMS record."""
        return cls(
            item_id=_get_str(record.get("itemId"), "") or "",
            item_number=_get_str(record.get("itemNumber"), "") or "",
            item_description=_get_str(record.get("itemDescription")),
            item_category=_get_str(record.get("itemCategory")),
            unit_of_measure=_get_str(record.get("unitOfMeasure")),
            unit_cost=_get_float(record.get("unitCost")),
            weight=_get_float(record.get("weight")),
            volume=_get_float(record.get("volume")),
            is_active=_get_bool(record.get("isActive"), default=True),
            created_date=_get_str(record.get("createdDate")),
            modified_date=_get_str(record.get("modifiedDate")),
        )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate item dimension business rules."""
        if not self.item_id or not self.item_number:
            return FlextResult[None].fail("Item ID and item number are required")

        if self.unit_cost is not None and self.unit_cost < 0:
            return FlextResult[None].fail("Unit cost cannot be negative")

        if self.weight is not None and self.weight < 0:
            return FlextResult[None].fail("Weight cannot be negative")

        return FlextResult[None].ok(None)

    def to_dbt_dict(self: object) -> dict[str, object]:
        """Convert to dictionary suitable for DBT processing."""
        return {
            "item_id": self.item_id,
            "item_number": self.item_number,
            "item_description": self.item_description,
            "item_category": self.item_category,
            "unit_of_measure": self.unit_of_measure,
            "unit_cost": self.unit_cost,
            "weight": self.weight,
            "volume": self.volume,
            "is_active": self.is_active,
            "created_date": self.created_date,
            "modified_date": self.modified_date,
        }


class FlextDbtOracleWmsLocationDimension(FlextSettings):
    """Location dimension model for DBT Oracle WMS transformations.

    Represents a location dimension table structure optimized for analytics.
    """

    location_id: str
    location_name: str
    facility_id: str
    zone: str | None = None
    aisle: str | None = None
    bay: str | None = None
    level: str | None = None
    position: str | None = None
    location_type: str | None = None
    capacity: float | None = None
    is_pickable: bool = True
    is_active: bool = True
    created_date: str | None = None
    modified_date: str | None = None

    @classmethod
    def from_oracle_wms_record(
        cls,
        record: dict[str, object],
    ) -> FlextDbtOracleWmsLocationDimension:
        """Create location dimension from Oracle WMS record."""
        return cls(
            location_id=_get_str(record.get("locationId"), "") or "",
            location_name=_get_str(record.get("locationName"), "") or "",
            facility_id=_get_str(record.get("facilityId"), "") or "",
            zone=_get_str(record.get("zone")),
            aisle=_get_str(record.get("aisle")),
            bay=_get_str(record.get("bay")),
            level=_get_str(record.get("level")),
            position=_get_str(record.get("position")),
            location_type=_get_str(record.get("locationType")),
            capacity=_get_float(record.get("capacity")),
            is_pickable=_get_bool(record.get("isPickable"), default=True),
            is_active=_get_bool(record.get("isActive"), default=True),
            created_date=_get_str(record.get("createdDate")),
            modified_date=_get_str(record.get("modifiedDate")),
        )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate location dimension business rules."""
        if not self.location_id or not self.location_name or not self.facility_id:
            return FlextResult[None].fail(
                "Location ID, name, and facility ID are required",
            )

        if self.capacity is not None and self.capacity < 0:
            return FlextResult[None].fail("Capacity cannot be negative")

        return FlextResult[None].ok(None)

    def to_dbt_dict(self: object) -> dict[str, object]:
        """Convert to dictionary suitable for DBT processing."""
        return {
            "location_id": self.location_id,
            "location_name": self.location_name,
            "facility_id": self.facility_id,
            "zone": self.zone,
            "aisle": self.aisle,
            "bay": self.bay,
            "level": self.level,
            "position": self.position,
            "location_type": self.location_type,
            "capacity": self.capacity,
            "is_pickable": self.is_pickable,
            "is_active": self.is_active,
            "created_date": self.created_date,
            "modified_date": self.modified_date,
        }


class FlextDbtOracleWmsInventoryFact(FlextSettings):
    """Inventory fact model for DBT Oracle WMS transformations.

    Represents inventory levels as fact table optimized for analytics.
    """

    item_id: str
    location_id: str
    facility_id: str
    quantity_on_hand: float
    quantity_available: float | None = None
    quantity_reserved: float | None = None
    quantity_allocated: float | None = None
    last_counted_date: str | None = None
    last_movement_date: str | None = None
    cost_per_unit: float | None = None
    total_value: float | None = None

    @classmethod
    def from_oracle_wms_record(
        cls,
        record: dict[str, object],
    ) -> FlextDbtOracleWmsInventoryFact:
        """Create inventory fact from Oracle WMS record."""
        quantity_on_hand = _get_float(record.get("quantityOnHand"), 0.0) or 0.0
        cost_per_unit = _get_float(record.get("costPerUnit"))

        total_value = None
        if cost_per_unit is not None and quantity_on_hand:
            total_value = quantity_on_hand * cost_per_unit

        return cls(
            item_id=_get_str(record.get("itemId"), "") or "",
            location_id=_get_str(record.get("locationId"), "") or "",
            facility_id=_get_str(record.get("facilityId"), "") or "",
            quantity_on_hand=quantity_on_hand,
            quantity_available=_get_float(record.get("quantityAvailable")),
            quantity_reserved=_get_float(record.get("quantityReserved")),
            quantity_allocated=_get_float(record.get("quantityAllocated")),
            last_counted_date=_get_str(record.get("lastCountedDate")),
            last_movement_date=_get_str(record.get("lastMovementDate")),
            cost_per_unit=cost_per_unit,
            total_value=total_value,
        )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate inventory fact business rules."""
        if not self.item_id or not self.location_id or not self.facility_id:
            return FlextResult[None].fail(
                "Item ID, location ID, and facility ID are required",
            )

        if self.quantity_on_hand < 0:
            return FlextResult[None].fail("Quantity on hand cannot be negative")

        if self.quantity_available is not None and self.quantity_available < 0:
            return FlextResult[None].fail("Quantity available cannot be negative")

        return FlextResult[None].ok(None)

    def to_dbt_dict(self: object) -> dict[str, object]:
        """Convert to dictionary suitable for DBT processing."""
        return {
            "item_id": self.item_id,
            "location_id": self.location_id,
            "facility_id": self.facility_id,
            "quantity_on_hand": self.quantity_on_hand,
            "quantity_available": self.quantity_available,
            "quantity_reserved": self.quantity_reserved,
            "quantity_allocated": self.quantity_allocated,
            "last_counted_date": self.last_counted_date,
            "last_movement_date": self.last_movement_date,
            "cost_per_unit": self.cost_per_unit,
            "total_value": self.total_value,
        }


class FlextDbtOracleWmsShipmentFact(FlextSettings):
    """Shipment fact model for DBT Oracle WMS transformations.

    Represents shipments as fact table optimized for analytics.
    """

    shipment_id: str
    order_id: str
    facility_id: str
    carrier: str | None = None
    tracking_number: str | None = None
    shipment_status: str
    planned_ship_date: str | None = None
    actual_ship_date: str | None = None
    planned_delivery_date: str | None = None
    actual_delivery_date: str | None = None
    total_weight: float | None = None
    total_value: float | None = None
    freight_cost: float | None = None

    @classmethod
    def from_oracle_wms_record(
        cls,
        record: dict[str, object],
    ) -> FlextDbtOracleWmsShipmentFact:
        """Create shipment fact from Oracle WMS record."""
        return cls(
            shipment_id=_get_str(record.get("shipmentId"), "") or "",
            order_id=_get_str(record.get("orderId"), "") or "",
            facility_id=_get_str(record.get("facilityId"), "") or "",
            carrier=_get_str(record.get("carrier")),
            tracking_number=_get_str(record.get("trackingNumber")),
            shipment_status=_get_str(record.get("shipmentStatus"), "CREATED")
            or "CREATED",
            planned_ship_date=_get_str(record.get("plannedShipDate")),
            actual_ship_date=_get_str(record.get("actualShipDate")),
            planned_delivery_date=_get_str(record.get("plannedDeliveryDate")),
            actual_delivery_date=_get_str(record.get("actualDeliveryDate")),
            total_weight=_get_float(record.get("totalWeight")),
            total_value=_get_float(record.get("totalValue")),
            freight_cost=_get_float(record.get("freightCost")),
        )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate shipment fact business rules."""
        if not self.shipment_id or not self.order_id or not self.facility_id:
            return FlextResult[None].fail(
                "Shipment ID, order ID, and facility ID are required",
            )

        valid_statuses = [
            "CREATED",
            "PICKED",
            "PACKED",
            "SHIPPED",
            "DELIVERED",
            "CANCELLED",
        ]
        if self.shipment_status not in valid_statuses:
            return FlextResult[None].fail(
                f"Invalid shipment status: {self.shipment_status}",
            )

        if self.total_weight is not None and self.total_weight < 0:
            return FlextResult[None].fail("Total weight cannot be negative")

        if self.freight_cost is not None and self.freight_cost < 0:
            return FlextResult[None].fail("Freight cost cannot be negative")

        return FlextResult[None].ok(None)

    def to_dbt_dict(self: object) -> dict[str, object]:
        """Convert to dictionary suitable for DBT processing."""
        return {
            "shipment_id": self.shipment_id,
            "order_id": self.order_id,
            "facility_id": self.facility_id,
            "carrier": self.carrier,
            "tracking_number": self.tracking_number,
            "shipment_status": self.shipment_status,
            "planned_ship_date": self.planned_ship_date,
            "actual_ship_date": self.actual_ship_date,
            "planned_delivery_date": self.planned_delivery_date,
            "actual_delivery_date": self.actual_delivery_date,
            "total_weight": self.total_weight,
            "total_value": self.total_value,
            "freight_cost": self.freight_cost,
        }


class FlextDbtOracleWmsTransformer:
    """Oracle WMS data transformer for DBT operations.

    Transforms Oracle WMS records into DBT-compatible data models.
    """

    @override
    def __init__(self: object) -> None:
        """Initialize Oracle WMS transformer."""
        logger.info("Initialized Oracle WMS DBT transformer")

    def transform_items(
        self,
        records: list[dict[str, object]],
    ) -> list[FlextDbtOracleWmsItemDimension]:
        """Transform Oracle WMS records to item dimensions.

        Args:
        records: List of Oracle WMS item records

        Returns:
        List of item dimension models

        """
        logger.info(
            "Transforming %d Oracle WMS records to item dimensions",
            len(records),
        )

        item_dims = []
        for record in records:
            try:
                item_dim = FlextDbtOracleWmsItemDimension.from_oracle_wms_record(record)

                # Validate business rules
                validation_result: FlextResult[object] = (
                    item_dim.validate_business_rules()
                )
                if validation_result.is_success:
                    item_dims.append(item_dim)
                else:
                    logger.warning(
                        "Item dimension validation failed for %s: %s",
                        record.get("itemId", "unknown"),
                        validation_result.error,
                    )

            except Exception:
                logger.exception("Failed to transform item record: %s", record)
                continue

        logger.info("Transformed %d item dimensions", len(item_dims))
        return item_dims

    def transform_locations(
        self,
        records: list[dict[str, object]],
    ) -> list[FlextDbtOracleWmsLocationDimension]:
        """Transform Oracle WMS records to location dimensions.

        Args:
        records: List of Oracle WMS location records

        Returns:
        List of location dimension models

        """
        logger.info(
            "Transforming %d Oracle WMS records to location dimensions",
            len(records),
        )

        location_dims = []
        for record in records:
            try:
                location_dim = (
                    FlextDbtOracleWmsLocationDimension.from_oracle_wms_record(record)
                )

                # Validate business rules
                validation_result: FlextResult[object] = (
                    location_dim.validate_business_rules()
                )
                if validation_result.is_success:
                    location_dims.append(location_dim)
                else:
                    logger.warning(
                        "Location dimension validation failed for %s: %s",
                        record.get("locationId", "unknown"),
                        validation_result.error,
                    )

            except Exception:
                logger.exception("Failed to transform location record: %s", record)
                continue

        logger.info("Transformed %d location dimensions", len(location_dims))
        return location_dims

    def transform_inventory(
        self,
        records: list[dict[str, object]],
    ) -> list[FlextDbtOracleWmsInventoryFact]:
        """Transform Oracle WMS records to inventory facts.

        Args:
        records: List of Oracle WMS inventory records

        Returns:
        List of inventory fact models

        """
        logger.info(
            "Transforming %d Oracle WMS records to inventory facts",
            len(records),
        )

        inventory_facts = []
        for record in records:
            try:
                inventory_fact = FlextDbtOracleWmsInventoryFact.from_oracle_wms_record(
                    record,
                )

                # Validate business rules
                validation_result: FlextResult[object] = (
                    inventory_fact.validate_business_rules()
                )
                if validation_result.is_success:
                    inventory_facts.append(inventory_fact)
                else:
                    logger.warning(
                        "Inventory fact validation failed for %s/%s: %s",
                        record.get("itemId", "unknown"),
                        record.get("locationId", "unknown"),
                        validation_result.error,
                    )

            except Exception:
                logger.exception("Failed to transform inventory record: %s", record)
                continue

        logger.info("Transformed %d inventory facts", len(inventory_facts))
        return inventory_facts

    def transform_shipments(
        self,
        records: list[dict[str, object]],
    ) -> list[FlextDbtOracleWmsShipmentFact]:
        """Transform Oracle WMS records to shipment facts.

        Args:
        records: List of Oracle WMS shipment records

        Returns:
        List of shipment fact models

        """
        logger.info(
            "Transforming %d Oracle WMS records to shipment facts",
            len(records),
        )

        shipment_facts = []
        for record in records:
            try:
                shipment_fact = FlextDbtOracleWmsShipmentFact.from_oracle_wms_record(
                    record,
                )

                # Validate business rules
                validation_result: FlextResult[object] = (
                    shipment_fact.validate_business_rules()
                )
                if validation_result.is_success:
                    shipment_facts.append(shipment_fact)
                else:
                    logger.warning(
                        "Shipment fact validation failed for %s: %s",
                        record.get("shipmentId", "unknown"),
                        validation_result.error,
                    )

            except Exception:
                logger.exception("Failed to transform shipment record: %s", record)
                continue

        logger.info("Transformed %d shipment facts", len(shipment_facts))
        return shipment_facts

    def transform_all_entities(
        self,
        entity_data: dict[str, list[dict[str, object]]],
    ) -> dict[str, list[object]]:
        """Transform all Oracle WMS entities to their respective DBT models.

        Args:
        entity_data: Dictionary of entity name -> records

        Returns:
        Dictionary of entity name -> transformed models

        """
        logger.info(
            "Transforming all Oracle WMS entities: %s",
            list(entity_data.keys()),
        )

        transformed_data: dict[str, list[object]] = {}

        for entity_name, records in entity_data.items():
            if entity_name == "items":
                transformed_data[entity_name] = list(self.transform_items(records))
            elif entity_name == "locations":
                transformed_data[entity_name] = list(self.transform_locations(records))
            elif entity_name == "inventory":
                transformed_data[entity_name] = list(self.transform_inventory(records))
            elif entity_name == "shipments":
                transformed_data[entity_name] = list(self.transform_shipments(records))
            else:
                logger.warning(
                    "Unknown entity type for transformation: %s",
                    entity_name,
                )
                transformed_data[entity_name] = []

        logger.info(
            "Transformed all entities: %s",
            {k: len(v) for k, v in transformed_data.items()},
        )

        return transformed_data


# Backward compatibility aliases
ItemDimension = FlextDbtOracleWmsItemDimension
LocationDimension = FlextDbtOracleWmsLocationDimension
InventoryFact = FlextDbtOracleWmsInventoryFact
ShipmentFact = FlextDbtOracleWmsShipmentFact
OracleWMSTransformer = FlextDbtOracleWmsTransformer


__all__: list[str] = [
    "FlextDbtOracleWmsInventoryFact",
    "FlextDbtOracleWmsItemDimension",
    "FlextDbtOracleWmsLocationDimension",
    "FlextDbtOracleWmsShipmentFact",
    "FlextDbtOracleWmsTransformer",
    # Re-exports from flext-oracle-wms for convenience
    "FlextOracleWmsEntity",
    # Backward compatibility
    "InventoryFact",
    "ItemDimension",
    "LocationDimension",
    "OracleWMSTransformer",
    "ShipmentFact",
]
