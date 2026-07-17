"""Metadata operations for the DBT Oracle WMS public facade."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core import r
from flext_dbt_oracle_wms import m, p, t, u
from flext_dbt_oracle_wms.services.base import FlextDbtOracleWmsBase

if TYPE_CHECKING:
    from collections.abc import Sequence

    from flext_dbt_oracle_wms._settings import FlextDbtOracleWmsSettings


class FlextDbtOracleWmsMetadata(FlextDbtOracleWmsBase):
    """Metadata and direct Oracle WMS entity lookup operations."""

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: u.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize metadata facade dependencies cooperatively."""
        super().__init__(settings=settings, client=client, service=service)

    def extract_wms_metadata(
        self,
        inventory_items: t.StrSequence | None = None,
        shipments: t.StrSequence | None = None,
        *,
        include_inventory_details: bool = True,
        include_shipment_tracking: bool = True,
    ) -> p.Result[p.DbtOracleWms.WmsMetadataResult]:
        """Extract Oracle WMS metadata from the real domain client."""
        self.logger.info("Extracting Oracle WMS metadata")
        available_entities_result = self.client.discover_oracle_wms_entities()
        if available_entities_result.failure:
            return r[p.DbtOracleWms.WmsMetadataResult].fail(
                available_entities_result.error or "Oracle WMS entity discovery failed",
            )
        inventory_records: Sequence[t.ConfigurationMapping] = []
        shipment_records: Sequence[t.ConfigurationMapping] = []
        if include_inventory_details:
            inventory_result = self._extract_entity_records(
                "items",
                inventory_items,
                ("item_id", "item_number", "id", "sku"),
            )
            if inventory_result.failure:
                return r[p.DbtOracleWms.WmsMetadataResult].fail(
                    inventory_result.error or "Inventory metadata extraction failed",
                )
            inventory_records = inventory_result.value
        if include_shipment_tracking:
            shipment_result = self._extract_entity_records(
                "shipments",
                shipments,
                ("shipment_id", "tracking_number", "id"),
            )
            if shipment_result.failure:
                return r[p.DbtOracleWms.WmsMetadataResult].fail(
                    shipment_result.error or "Shipment metadata extraction failed",
                )
            shipment_records = shipment_result.value
        return r[p.DbtOracleWms.WmsMetadataResult].ok(
            m.DbtOracleWms.WmsMetadataResult(
                available_entities=tuple(available_entities_result.value),
                inventory_count=len(inventory_records),
                shipment_count=len(shipment_records),
                include_inventory_details=include_inventory_details,
                include_shipment_tracking=include_shipment_tracking,
                status="metadata_extracted",
            ),
        )

    def fetch_wms_inventory_info(
        self,
        item_id: str,
    ) -> p.Result[p.OracleWms.InventoryItem]:
        """Get inventory item data from the Oracle WMS domain client."""
        self.logger.info("Getting WMS inventory info: %s", item_id)
        inventory_result = self._extract_entity_records(
            "items",
            [item_id],
            ("item_id", "item_number", "id", "sku"),
        )
        if inventory_result.failure:
            return r[p.OracleWms.InventoryItem].fail(
                inventory_result.error or "Inventory info retrieval failed",
            )
        return r[p.OracleWms.InventoryItem].ok(
            m.OracleWms.InventoryItem.model_validate(inventory_result.value[0]),
        )

    def fetch_wms_shipment_info(
        self,
        shipment_id: str,
    ) -> p.Result[p.OracleWms.Shipment]:
        """Get shipment data from the Oracle WMS domain client."""
        self.logger.info("Getting WMS shipment info: %s", shipment_id)
        shipment_result = self._extract_entity_records(
            "shipments",
            [shipment_id],
            ("shipment_id", "tracking_number", "id"),
        )
        if shipment_result.failure:
            return r[p.OracleWms.Shipment].fail(
                shipment_result.error or "Shipment info retrieval failed",
            )
        return r[p.OracleWms.Shipment].ok(
            m.OracleWms.Shipment.model_validate(shipment_result.value[0]),
        )


__all__: list[str] = ["FlextDbtOracleWmsMetadata"]
