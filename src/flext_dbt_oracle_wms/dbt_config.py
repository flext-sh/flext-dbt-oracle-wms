"""FLEXT Module.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano.config import FlextMeltanoConfig
from flext_oracle_wms.wms_config import FlextOracleWmsClientConfig

from flext_core import FlextConfig, FlextLogger, FlextTypes

logger = FlextLogger(__name__)


class FlextDbtOracleWmsConfig(FlextConfig):
    """Configuration for DBT Oracle WMS transformations.

    Combines Oracle WMS connection settings with DBT execution configuration.
    Uses composition to integrate flext-oracle-wms and flext-meltano configurations.
    """

    # Oracle WMS Connection Settings (from flext-oracle-wms)
    oracle_wms_base_url: str = "https://your-wms.oraclecloud.com"
    oracle_wms_username: str = ""
    oracle_wms_password: str = ""
    oracle_wms_timeout: int = 30
    oracle_wms_page_size: int = 1000
    oracle_wms_max_retries: int = 3
    oracle_wms_environment: str = "production"

    # DBT Execution Settings (from flext-meltano)
    dbt_project_dir: str = "."
    dbt_profiles_dir: str = "."
    dbt_target: str = "dev"
    dbt_threads: int = 4
    dbt_log_level: str = "info"

    # Oracle WMS-specific DBT Settings
    oracle_wms_entity_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "items": "stg_wms_items",
        "locations": "stg_wms_locations",
        "inventory": "stg_wms_inventory",
        "shipments": "stg_wms_shipments",
        "receipts": "stg_wms_receipts",
        "orders": "stg_wms_orders",
    }

    oracle_wms_field_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "itemId": "item_id",
        "itemNumber": "item_number",
        "itemDescription": "item_description",
        "locationId": "location_id",
        "facilityId": "facility_id",
        "orderId": "order_id",
        "shipmentId": "shipment_id",
        "receiptId": "receipt_id",
    }

    # Oracle WMS Business Logic Settings
    oracle_wms_business_rules: ClassVar[FlextTypes.Core.Dict] = {
        "inventory_thresholds": {
            "min_quantity": 0,
            "max_quantity": 999999,
            "reorder_point": 10,
        },
        "shipment_validation": {
            "required_fields": ["shipmentId", "orderId", "carrier"],
            "status_hierarchy": ["CREATED", "PICKED", "PACKED", "SHIPPED", "DELIVERED"],
        },
        "location_constraints": {
            "allow_negative_inventory": False,
            "enforce_capacity_limits": True,
        },
    }

    # Data Quality Settings
    min_quality_threshold: float = 0.85
    required_fields_per_entity: ClassVar[dict[str, FlextTypes.Core.StringList]] = {
        "items": ["itemId", "itemNumber", "itemDescription"],
        "locations": ["locationId", "facilityId", "locationName"],
        "inventory": ["itemId", "locationId", "quantityOnHand"],
        "shipments": ["shipmentId", "orderId", "shipmentStatus"],
        "orders": ["orderId", "customerId", "orderStatus"],
    }
    # Flag handled as a field, not overriding base class method type
    validate_business_rules_flag: bool = True

    def get_oracle_wms_config(self) -> FlextOracleWmsClientConfig:
        """Get Oracle WMS configuration for flext-oracle-wms integration."""
        return FlextOracleWmsClientConfig(
            base_url=self.oracle_wms_base_url,
            username=self.oracle_wms_username,
            password=self.oracle_wms_password,
            timeout=float(self.oracle_wms_timeout),
            max_retries=int(self.oracle_wms_max_retries),
            environment=self.oracle_wms_environment,
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        return FlextMeltanoConfig(
            project_root=self.dbt_project_dir,
            environment=self.dbt_target,
            dbt_project_dir=self.dbt_project_dir,
            dbt_profiles_dir=self.dbt_profiles_dir,
        )

    def get_oracle_wms_quality_config(self) -> FlextTypes.Core.Dict:
        """Get data quality configuration for Oracle WMS validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_fields_per_entity": self.required_fields_per_entity,
            "validate_business_rules": self.validate_business_rules,
            "business_rules": self.oracle_wms_business_rules,
        }

    def get_entity_dbt_mapping(self, entity_name: str) -> str:
        """Get DBT staging table name for Oracle WMS entity."""
        return self.oracle_wms_entity_mapping.get(entity_name, f"stg_wms_{entity_name}")

    def get_field_dbt_mapping(self, field_name: str) -> str:
        """Get DBT field name for Oracle WMS field."""
        return self.oracle_wms_field_mapping.get(field_name, field_name.lower())

    def validate_oracle_wms_connection(self) -> bool:
        """Validate Oracle WMS connection configuration."""
        required_fields = [
            self.oracle_wms_base_url,
            self.oracle_wms_username,
            self.oracle_wms_password,
        ]
        return all(field.strip() for field in required_fields)

    def get_business_rule(self, entity_name: str, rule_name: str) -> object | None:
        """Get business rule for specific Oracle WMS entity."""
        entity_rules = self.oracle_wms_business_rules.get(entity_name, {})
        return entity_rules.get(rule_name) if isinstance(entity_rules, dict) else None

    def get_required_fields(self, entity_name: str) -> FlextTypes.Core.StringList:
        """Get required fields for specific Oracle WMS entity."""
        return self.required_fields_per_entity.get(entity_name, [])


__all__: FlextTypes.Core.StringList = [
    "FlextDbtOracleWmsConfig",
]
