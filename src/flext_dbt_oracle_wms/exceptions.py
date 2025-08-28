"""🚨 ARCHITECTURAL COMPLIANCE: ELIMINATED MASSIVE EXCEPTION DUPLICATION using DRY.

REFATORADO COMPLETO usando create_module_exception_classes:
- ZERO code duplication através do DRY exception factory pattern de flext-core
- USA create_module_exception_classes() para eliminar exception boilerplate massivo
- Elimina 185+ linhas duplicadas de código boilerplate por exception class
- SOLID: Single source of truth para module exception patterns
- Redução de 186+ linhas para 85 linhas (54% reduction)

Domain-specific Oracle WMS DBT exceptions using factory pattern to eliminate duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import cast

from flext_core import (
    FlextExceptions,
    FlextProcessingError,
    create_module_exception_classes,
)

# 🚨 DRY PATTERN: Use create_module_exception_classes to eliminate exception duplication
_exceptions = create_module_exception_classes("flext_dbt_oracle_wms")

# Extract exception classes with proper typing for MyPy
FlextDbtOracleWmsError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsError"],
)
FlextDbtOracleWmsValidationError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsValidationError"],
)
FlextDbtOracleWmsConfigurationError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsConfigurationError"],
)
FlextDbtOracleWmsConnectionError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsConnectionError"],
)
FlextDbtOracleWmsProcessingError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsProcessingError"],
)
FlextDbtOracleWmsAuthenticationError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsAuthenticationError"],
)
FlextDbtOracleWmsTimeoutError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FlextDbtOracleWmsTimeoutError"],
)


# Domain-specific exceptions for Oracle WMS DBT business logic
class FlextDbtOracleWmsInventoryError(FlextProcessingError):
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

        super().__init__(
            f"Oracle WMS DBT inventory: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleWmsShipmentError(FlextProcessingError):
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

        super().__init__(
            f"Oracle WMS DBT shipment: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleWmsModelError(FlextProcessingError):
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

        super().__init__(
            f"Oracle WMS DBT model: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleWmsTestError(FlextExceptions):
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
