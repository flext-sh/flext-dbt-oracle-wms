"""Domain-specific Oracle WMS DBT exceptions using factory pattern to eliminate duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextExceptions, FlextTypes


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
        # Store domain-specific attributes before extracting common kwargs
        self.item_code = item_code
        self.location = location
        self.operation = operation

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with inventory-specific fields
        context = self._build_context(
            base_context,
            item_code=item_code,
            location=location,
            operation=operation,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle WMS DBT inventory: {message}",
            code=error_code or "DBT_ORACLE_WMS_INVENTORY_ERROR",
            context=context,
            correlation_id=correlation_id,
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
        # Store domain-specific attributes before extracting common kwargs
        self.shipment_id = shipment_id
        self.carrier = carrier
        self.operation = operation

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with shipment-specific fields
        context = self._build_context(
            base_context,
            shipment_id=shipment_id,
            carrier=carrier,
            operation=operation,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle WMS DBT shipment: {message}",
            code=error_code or "DBT_ORACLE_WMS_SHIPMENT_ERROR",
            context=context,
            correlation_id=correlation_id,
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
        # Store domain-specific attributes before extracting common kwargs
        self.model_name = model_name
        self.model_type = model_type
        self.operation = operation

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with model-specific fields
        context = self._build_context(
            base_context,
            model_name=model_name,
            model_type=model_type,
            operation=operation,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle WMS DBT model: {message}",
            code=error_code or "DBT_ORACLE_WMS_MODEL_ERROR",
            context=context,
            correlation_id=correlation_id,
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
        # Store domain-specific attributes before extracting common kwargs
        self.test_name = test_name
        self.model_name = model_name

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with test-specific fields
        context = self._build_context(
            base_context,
            test_name=test_name,
            model_name=model_name,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle WMS DBT test: {message}",
            code=error_code or "DBT_ORACLE_WMS_TEST_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


__all__: FlextTypes.StringList = [
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
