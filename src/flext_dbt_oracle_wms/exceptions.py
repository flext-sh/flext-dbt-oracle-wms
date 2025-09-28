"""Domain-specific Oracle WMS DBT exceptions using factory pattern to eliminate duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextExceptions


# Base exception classes for Oracle WMS DBT operations
class FlextDbtOracleWmsError(FlextExceptions.Error):
    """Base exception for Oracle WMS DBT operations."""


class FlextDbtOracleWmsValidationError(FlextExceptions.ValidationError):
    """Oracle WMS DBT validation errors."""


class FlextDbtOracleWmsConfigurationError(FlextExceptions.ConfigurationError):
    """Oracle WMS DBT configuration errors."""


class FlextDbtOracleWmsConnectionError(FlextExceptions.ConnectionError):
    """Oracle WMS DBT connection errors."""


class FlextDbtOracleWmsProcessingError(FlextExceptions.ProcessingError):
    """Oracle WMS DBT processing errors."""


class FlextDbtOracleWmsAuthenticationError(FlextExceptions.AuthenticationError):
    """Oracle WMS DBT authentication errors."""


class FlextDbtOracleWmsTimeoutError(FlextExceptions.TimeoutError):
    """Oracle WMS DBT timeout errors."""


# Domain-specific exceptions for Oracle WMS DBT business logic
class FlextDbtOracleWmsInventoryError(FlextDbtOracleWmsProcessingError):
    """Oracle WMS DBT inventory-specific errors with WMS context."""

    @override
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

        super().__init__(
            f"Oracle WMS DBT inventory: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleWmsShipmentError(FlextDbtOracleWmsProcessingError):
    """Oracle WMS DBT shipment-specific errors with shipping context."""

    @override
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

        super().__init__(
            f"Oracle WMS DBT shipment: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleWmsModelError(FlextDbtOracleWmsProcessingError):
    """Oracle WMS DBT model-specific errors with dbt model context."""

    @override
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

        super().__init__(
            f"Oracle WMS DBT model: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleWmsTestError(FlextDbtOracleWmsValidationError):
    """Oracle WMS DBT test errors with test validation context."""

    @override
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
        super().__init__(
            f"Oracle WMS DBT test: {message}",
            validation_details=validation_details,
            context=context,
        )


__all__: list[str] = [
    "FlextDbtOracleWmsAuthenticationError",
    "FlextDbtOracleWmsConfigurationError",
    "FlextDbtOracleWmsConnectionError",
    "FlextDbtOracleWmsError",
    "FlextDbtOracleWmsInventoryError",
    "FlextDbtOracleWmsModelError",
    "FlextDbtOracleWmsProcessingError",
    "FlextDbtOracleWmsShipmentError",
    "FlextDbtOracleWmsTestError",
    "FlextDbtOracleWmsTimeoutError",
    "FlextDbtOracleWmsValidationError",
]
