"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import ClassVar, Literal, Self, override

from flext_core import FlextConstants, FlextResult, FlextSettings, t
from flext_meltano import FlextMeltanoSettings
from flext_oracle_wms.settings import FlextOracleWmsSettings
from pydantic import (
    Field,
    SecretStr,
    TypeAdapter,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_settings import SettingsConfigDict

from flext_dbt_oracle_wms.constants import FlextDbtOracleWmsConstants, c

_STRING_ADAPTER = TypeAdapter(str)


class FlextDbtOracleWmsSettings(FlextSettings):
    """Configuration for DBT Oracle WMS transformations.

    Follows standardized [Project]Config pattern:
    - Extends FlextSettings from flext-core
    - Uses SecretStr for sensitive data
    - All defaults from FlextConstants
    - Proper Pydantic 2 validation
    - Enhanced singleton pattern with inverse dependency injection

    Combines Oracle WMS connection settings with DBT execution configuration.
    Uses composition to integrate flext-oracle-wms and flext-meltano configurations.
    """

    def __init__(self, **kwargs: t.GeneralValueType) -> None:
        """Initialize with typed constructor to satisfy strict type checking."""
        super().__init__(**kwargs)

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_WMS_",
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        arbitrary_types_allowed=True,
        populate_by_name=True,
        use_enum_values=True,
        str_strip_whitespace=True,
        validate_default=True,
        # frozen=False,
    )

    # Oracle WMS Connection Settings - using Field() with proper defaults
    oracle_wms_base_url: str = Field(
        default="https://your-wms.oraclecloud.com",
        description="Oracle WMS base URL",
    )

    oracle_wms_username: str = Field(default="", description="Oracle WMS username")

    oracle_wms_password: SecretStr = Field(
        default_factory=lambda: SecretStr(""),
        description="Oracle WMS password (sensitive)",
    )

    oracle_wms_timeout: int = Field(
        default=FlextDbtOracleWmsConstants.DbtOracleWms.DbtOracleWmsProcessing.DEFAULT_BATCH_SIZE,
        ge=1,
        description="Oracle WMS timeout in seconds",
    )

    oracle_wms_page_size: int = Field(
        default=FlextDbtOracleWmsConstants.DbtOracleWms.DbtOracleWmsProcessing.DEFAULT_BATCH_SIZE,
        ge=1,
        description="Oracle WMS page size",
    )

    oracle_wms_max_retries: int = Field(
        default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
        ge=0,
        description="Oracle WMS maximum retries",
    )

    oracle_wms_environment: str = Field(
        default="dev",
        description="Oracle WMS environment",
    )

    # DBT Execution Settings - using Field() with proper defaults
    dbt_project_dir: str = Field(default=".", description="DBT project directory")

    dbt_profiles_dir: str = Field(default=".", description="DBT profiles directory")

    dbt_target: str = Field(default="dev", description="DBT target environment")

    dbt_threads: int = Field(
        default=FlextConstants.Container.DEFAULT_WORKERS,
        ge=1,
        description="Number of DBT threads",
    )

    dbt_log_level: Literal["debug", "info", "warn", "error"] = Field(
        default="info",
        description="DBT logging level",
    )

    # Data Quality Settings
    min_quality_threshold: float = Field(
        default=FlextDbtOracleWmsConstants.DbtOracleWms.DbtOracleWmsProcessing.DATA_QUALITY_THRESHOLD,
        ge=0.0,
        le=1.0,
        description="Minimum data quality threshold",
    )

    validate_business_rules_flag: bool = Field(
        default=True,
        description="Enable business rules validation",
    )

    # Oracle WMS-specific mappings (ClassVar - not configurable)
    oracle_wms_entity_mapping: ClassVar[dict[str, str]] = {
        "items": "stg_wms_items",
        "locations": "stg_wms_locations",
        "inventory": "stg_wms_inventory",
        "shipments": "stg_wms_shipments",
        "receipts": "stg_wms_receipts",
        "orders": "stg_wms_orders",
    }

    oracle_wms_field_mapping: ClassVar[dict[str, str]] = {
        "itemId": "item_id",
        "itemNumber": "item_number",
        "itemDescription": "item_description",
        "locationId": "location_id",
        "facilityId": "facility_id",
        "orderId": "order_id",
        "shipmentId": "shipment_id",
        "receiptId": "receipt_id",
    }

    oracle_wms_business_rules: ClassVar[dict[str, t.GeneralValueType]] = {
        "inventory_thresholds": {
            "min_quantity": 0,
            "max_quantity": 999999,
            "reorder_point": 10,
        },
        "shipment_validation": {
            "required_fields": ["shipmentId", "orderId", "carrier"],
            "status_hierarchy": FlextDbtOracleWmsConstants.DbtOracleWms.DbtOracleWmsProcessing.PROCESSING_STATUSES,
        },
        "location_constraints": {
            "allow_negative_inventory": False,
            "enforce_capacity_limits": True,
        },
    }

    required_fields_per_entity: ClassVar[dict[str, list[str]]] = {
        "items": ["itemId", "itemNumber", "itemDescription"],
        "locations": ["locationId", "facilityId", "locationName"],
        "inventory": ["itemId", "locationId", "quantityOnHand"],
        "shipments": ["shipmentId", "orderId", "shipmentStatus"],
        "orders": ["orderId", "customerId", "orderStatus"],
    }

    # Pydantic 2 field validators
    @field_validator("dbt_target")
    @classmethod
    def validate_dbt_target(cls, v: str) -> str:
        """Validate DBT target environment."""
        valid_targets = {member.value for member in c.DbtOracleWms.DbtTargets}
        if v.lower() not in valid_targets:
            valid_list = ", ".join(sorted(valid_targets))
            msg = f"Invalid DBT target: {v}. Must be one of: {valid_list}"
            raise ValueError(msg)
        return v.lower()

    @field_validator("oracle_wms_environment")
    @classmethod
    def validate_oracle_wms_environment(cls, v: str) -> str:
        """Validate Oracle WMS environment."""
        valid_environments = {
            member.value for member in c.DbtOracleWms.OracleWmsEnvironments
        }
        if v.lower() not in valid_environments:
            valid_list = ", ".join(sorted(valid_environments))
            msg = f"Invalid Oracle WMS environment: {v}. Must be one of: {valid_list}"
            raise ValueError(msg)
        return v.lower()

    @model_validator(mode="after")
    def validate_oracle_wms_connection_config(self) -> Self:
        """Validate Oracle WMS connection configuration."""
        # Base URL must be provided
        if not self.oracle_wms_base_url.strip():
            msg = "Oracle WMS base URL must be provided"
            raise ValueError(msg)

        # Username must be provided
        if not self.oracle_wms_username.strip():
            msg = "Oracle WMS username must be provided"
            raise ValueError(msg)

        return self

    # Configuration helper methods
    def get_oracle_wms_config(self) -> FlextOracleWmsSettings:
        """Get Oracle WMS configuration for flext-oracle-wms integration."""
        return FlextOracleWmsSettings(
            base_url=self.oracle_wms_base_url,
            username=self.oracle_wms_username,
            password=self.oracle_wms_password.get_secret_value(),
            timeout=int(self.oracle_wms_timeout),
            retry_attempts=int(self.oracle_wms_max_retries),
            environment=self.oracle_wms_environment,
        )

    def get_meltano_config(self) -> FlextMeltanoSettings:
        """Get Meltano configuration for flext-meltano integration."""
        return FlextMeltanoSettings(
            project_root=Path(self.dbt_project_dir),
            environment=self.dbt_target,
        )

    def get_oracle_wms_quality_config(self) -> Mapping[str, t.GeneralValueType]:
        """Get data quality configuration for Oracle WMS validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_fields_per_entity": self.required_fields_per_entity,
            "validate_business_rules": self.validate_business_rules_flag,
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
            bool(self.oracle_wms_password.get_secret_value()),
        ]
        return all(self._has_required_value(field) for field in required_fields)

    @staticmethod
    def _has_required_value(field: t.GeneralValueType) -> bool:
        """Normalize required field values for connection validation."""
        try:
            return bool(_STRING_ADAPTER.validate_python(field).strip())
        except ValidationError:
            return bool(field)

    def get_business_rule(
        self, entity_name: str, rule_name: str
    ) -> t.GeneralValueType | None:
        """Get business rule for specific Oracle WMS entity."""
        entity_rules = self.oracle_wms_business_rules.get(entity_name)
        if entity_rules is None:
            return None
        try:
            validated_rules = t.Dict.model_validate(entity_rules)
        except ValidationError:
            return None
        return validated_rules.get(rule_name)

    def get_required_fields(self, entity_name: str) -> list[str]:
        """Get required fields for specific Oracle WMS entity."""
        return self.required_fields_per_entity.get(entity_name, [])

    @classmethod
    def get_or_create_shared_instance(
        cls,
        project_name: str | None = None,
        **overrides: t.GeneralValueType,
    ) -> Self:
        """Get or create a shared singleton settings instance."""
        _ = project_name
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = cls()

        raw_instance = cls._instances[cls]
        try:
            validated_instance = cls.model_validate(raw_instance)
        except ValidationError as exc:
            msg = f"Singleton instance is not of expected type {cls}"
            raise TypeError(msg) from exc

        if overrides:
            for key, value in overrides.items():
                if key in cls.model_fields:
                    setattr(validated_instance, key, value)

        return validated_instance

    @classmethod
    def reset_shared_instance(cls, project_name: str | None = None) -> None:
        """Reset the shared singleton settings instance."""
        _ = project_name
        with cls._lock:
            _ = cls._instances.pop(cls, None)

    @classmethod
    def create_for_development(
        cls,
        **overrides: t.GeneralValueType,
    ) -> FlextResult[Self]:
        """Create configuration optimized for development environment."""
        dev_config: dict[str, t.GeneralValueType] = {
            "dbt_target": "development",
            "dbt_threads": 2,
            "oracle_wms_environment": "dev",
            "validate_business_rules_flag": False,
            "min_quality_threshold": 0.5,  # Lower threshold for dev
        }
        config_data: dict[str, t.GeneralValueType] = {**dev_config, **overrides}
        try:
            instance = cls.get_or_create_shared_instance(
                project_name="flext-dbt-oracle-wms",
                **config_data,
            )
            return FlextResult[Self].ok(instance)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return FlextResult[Self].fail(f"Development config creation failed: {e}")

    @classmethod
    def create_for_production(
        cls,
        **overrides: t.GeneralValueType,
    ) -> FlextResult[Self]:
        """Create configuration optimized for production environment."""
        prod_config: dict[str, t.GeneralValueType] = {
            "dbt_target": "production",
            "dbt_threads": 8,
            "oracle_wms_environment": "prod",
            "validate_business_rules_flag": True,
            "min_quality_threshold": 0.95,  # Higher threshold for prod
            "oracle_wms_max_retries": 5,
        }
        config_data: dict[str, t.GeneralValueType] = {**prod_config, **overrides}
        try:
            instance = cls.get_or_create_shared_instance(
                project_name="flext-dbt-oracle-wms",
                **config_data,
            )
            return FlextResult[Self].ok(instance)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return FlextResult[Self].fail(f"Production config creation failed: {e}")

    @classmethod
    def create_for_testing(
        cls,
        **overrides: t.GeneralValueType,
    ) -> FlextResult[Self]:
        """Create configuration optimized for testing environment."""
        test_config: dict[str, t.GeneralValueType] = {
            "dbt_target": "test",
            "dbt_threads": 1,
            "oracle_wms_environment": "test",
            "validate_business_rules_flag": True,
            "min_quality_threshold": 0.8,
            "oracle_wms_max_retries": 1,
        }
        config_data: dict[str, t.GeneralValueType] = {**test_config, **overrides}
        try:
            instance = cls.get_or_create_shared_instance(
                project_name="flext-dbt-oracle-wms",
                **config_data,
            )
            return FlextResult[Self].ok(instance)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return FlextResult[Self].fail(f"Testing config creation failed: {e}")

    @classmethod
    def create_for_environment(
        cls,
        environment: str,
        **overrides: t.GeneralValueType,
    ) -> FlextResult[Self]:
        """Create configuration for specific environment."""
        if environment == "production":
            return cls.create_for_production(**overrides)
        if environment == "development":
            return cls.create_for_development(**overrides)
        if environment == "testing":
            return cls.create_for_testing(**overrides)
        return FlextResult[Self].fail(f"Unknown environment: {environment}")

    @classmethod
    @override
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextSettings pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-dbt-oracle-wms")

    @classmethod
    @override
    def reset_global_instance(cls) -> None:
        """Reset the global instance (mainly for testing)."""
        cls.reset_shared_instance(project_name="flext-dbt-oracle-wms")


__all__ = [
    "FlextDbtOracleWmsSettings",
]
