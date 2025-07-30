"""Oracle WMS DBT exception hierarchy using flext-core patterns.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for Oracle WMS DBT operations inheriting from flext-core.
"""

from __future__ import annotations

from flext_core.exceptions import (
    FlextAuthenticationError,
    FlextConfigurationError,
    FlextConnectionError,
    FlextError,
    FlextProcessingError,
    FlextTimeoutError,
    FlextValidationError,
)


class FlextDbtOracleWmsError(FlextError):
    """Base exception for Oracle WMS DBT operations."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT error",
        model_name: str | None = None,
        warehouse_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name
        if warehouse_name is not None:
            context["warehouse_name"] = warehouse_name

        super().__init__(message, error_code="ORACLE_WMS_DBT_ERROR", context=context)


class FlextDbtOracleWmsConnectionError(FlextConnectionError):
    """Oracle WMS DBT connection errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT connection failed",
        wms_endpoint: str | None = None,
        database_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT connection error with context."""
        context = kwargs.copy()
        if wms_endpoint is not None:
            context["wms_endpoint"] = wms_endpoint
        if database_name is not None:
            context["database_name"] = database_name

        super().__init__(f"Oracle WMS DBT connection: {message}", **context)


class FlextDbtOracleWmsAuthenticationError(FlextAuthenticationError):
    """Oracle WMS DBT authentication errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT authentication failed",
        username: str | None = None,
        warehouse_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT authentication error with context."""
        context = kwargs.copy()
        if username is not None:
            context["username"] = username
        if warehouse_name is not None:
            context["warehouse_name"] = warehouse_name

        super().__init__(f"Oracle WMS DBT auth: {message}", **context)


class FlextDbtOracleWmsValidationError(FlextValidationError):
    """Oracle WMS DBT validation errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT validation failed",
        field: str | None = None,
        value: object = None,
        entity_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT validation error with context."""
        validation_details = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if entity_type is not None:
            context["entity_type"] = entity_type

        super().__init__(
            f"Oracle WMS DBT validation: {message}",
            validation_details=validation_details,
            context=context,
        )


class FlextDbtOracleWmsConfigurationError(FlextConfigurationError):
    """Oracle WMS DBT configuration errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT configuration error",
        config_key: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key

        super().__init__(f"Oracle WMS DBT config: {message}", **context)


class FlextDbtOracleWmsProcessingError(FlextProcessingError):
    """Oracle WMS DBT processing errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT processing failed",
        entity_type: str | None = None,
        processing_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT processing error with context."""
        context = kwargs.copy()
        if entity_type is not None:
            context["entity_type"] = entity_type
        if processing_stage is not None:
            context["processing_stage"] = processing_stage

        super().__init__(f"Oracle WMS DBT processing: {message}", **context)


class FlextDbtOracleWmsTimeoutError(FlextTimeoutError):
    """Oracle WMS DBT timeout errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT operation timed out",
        operation: str | None = None,
        timeout_seconds: float | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT timeout error with context."""
        context = kwargs.copy()
        if operation is not None:
            context["operation"] = operation
        if timeout_seconds is not None:
            context["timeout_seconds"] = timeout_seconds

        super().__init__(f"Oracle WMS DBT timeout: {message}", **context)


class FlextDbtOracleWmsInventoryError(FlextDbtOracleWmsError):
    """Oracle WMS DBT inventory-specific errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT inventory error",
        item_code: str | None = None,
        location: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT inventory error with context."""
        context = kwargs.copy()
        if item_code is not None:
            context["item_code"] = item_code
        if location is not None:
            context["location"] = location

        super().__init__(f"Oracle WMS DBT inventory: {message}", **context)


class FlextDbtOracleWmsShipmentError(FlextDbtOracleWmsError):
    """Oracle WMS DBT shipment-specific errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT shipment error",
        shipment_id: str | None = None,
        carrier: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT shipment error with context."""
        context = kwargs.copy()
        if shipment_id is not None:
            context["shipment_id"] = shipment_id
        if carrier is not None:
            context["carrier"] = carrier

        super().__init__(f"Oracle WMS DBT shipment: {message}", **context)


class FlextDbtOracleWmsModelError(FlextDbtOracleWmsError):
    """Oracle WMS DBT model-specific errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT model error",
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT model error with context."""
        context = kwargs.copy()
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(
            f"Oracle WMS DBT model: {message}", model_name=model_name, **context,
        )


class FlextDbtOracleWmsTestError(FlextDbtOracleWmsError):
    """Oracle WMS DBT test errors."""

    def __init__(
        self,
        message: str = "Oracle WMS DBT test failed",
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS DBT test error with context."""
        context = kwargs.copy()
        if test_name is not None:
            context["test_name"] = test_name

        super().__init__(
            f"Oracle WMS DBT test: {message}", model_name=model_name, **context,
        )


__all__ = [
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
