"""Oracle WMS DBT Exception Hierarchy.

Exception hierarchy following FLEXT patterns using factory pattern from flext-core.
Eliminates code duplication by using create_module_exception_classes() factory.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core.exceptions import create_module_exception_classes

# Create Oracle WMS DBT-specific exception classes using flext-core factory
# This eliminates the need for manual exception class creation and duplicated __init__ methods
_dbt_wms_exceptions = create_module_exception_classes("flext_dbt_oracle_wms")

# Extract factory-created exception classes
FlextDbtOracleWmsError = _dbt_wms_exceptions["FlextDbtOracleWmsError"]
FlextDbtOracleWmsValidationError = _dbt_wms_exceptions[
    "FlextDbtOracleWmsValidationError"
]
FlextDbtOracleWmsConfigurationError = _dbt_wms_exceptions[
    "FlextDbtOracleWmsConfigurationError"
]
FlextDbtOracleWmsConnectionError = _dbt_wms_exceptions[
    "FlextDbtOracleWmsConnectionError"
]
FlextDbtOracleWmsProcessingError = _dbt_wms_exceptions[
    "FlextDbtOracleWmsProcessingError"
]
FlextDbtOracleWmsAuthenticationError = _dbt_wms_exceptions[
    "FlextDbtOracleWmsAuthenticationError"
]
FlextDbtOracleWmsTimeoutError = _dbt_wms_exceptions["FlextDbtOracleWmsTimeoutError"]


# Domain-specific exceptions for Oracle WMS DBT business logic
class FlextDbtOracleWmsInventoryError(FlextDbtOracleWmsProcessingError):
    """Oracle WMS DBT inventory-specific errors with WMS context."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT inventory error",
        *,
        item_code: str | None = None,
        location: str | None = None,
        operation: str = "inventory_processing",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT inventory error with WMS context."""
        context = dict(kwargs)
        if item_code is not None:
            context["item_code"] = item_code
        if location is not None:
            context["location"] = location

        super().__init__(message, operation=operation, **context)


class FlextDbtOracleWmsShipmentError(FlextDbtOracleWmsProcessingError):
    """Oracle WMS DBT shipment-specific errors with shipping context."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT shipment error",
        *,
        shipment_id: str | None = None,
        carrier: str | None = None,
        operation: str = "shipment_processing",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT shipment error with shipping context."""
        context = dict(kwargs)
        if shipment_id is not None:
            context["shipment_id"] = shipment_id
        if carrier is not None:
            context["carrier"] = carrier

        super().__init__(message, operation=operation, **context)


class FlextDbtOracleWmsModelError(FlextDbtOracleWmsProcessingError):
    """Oracle WMS DBT model-specific errors with dbt model context."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        operation: str = "dbt_model_processing",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT model error with dbt context."""
        context = dict(kwargs)
        if model_name is not None:
            context["model_name"] = model_name
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(message, operation=operation, **context)


class FlextDbtOracleWmsTestError(FlextDbtOracleWmsValidationError):
    """Oracle WMS DBT test errors with test validation context."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT test failed",
        *,
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT test error with test context."""
        validation_details: dict[str, object] = {}
        if test_name is not None:
            validation_details["test_name"] = test_name
        if model_name is not None:
            validation_details["model_name"] = model_name

        context = dict(kwargs)
        super().__init__(message, validation_details=validation_details, **context)


# Export all exceptions - factory-created + domain-specific
__all__ = [
    "FlextDbtOracleWmsAuthenticationError",
    "FlextDbtOracleWmsConfigurationError",
    "FlextDbtOracleWmsConnectionError",
    # Factory-created base exceptions (from flext-core)
    "FlextDbtOracleWmsError",
    # Domain-specific Oracle WMS DBT business logic exceptions
    "FlextDbtOracleWmsInventoryError",
    "FlextDbtOracleWmsModelError",
    "FlextDbtOracleWmsProcessingError",
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsValidationError",
]
