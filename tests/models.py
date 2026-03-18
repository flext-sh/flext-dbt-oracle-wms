"""Test models for flext-dbt-oracle-wms tests.

Provides TestsFlextDbtOracleWmsModels, extending m with
flext-dbt-oracle-wms-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import m

from flext_dbt_oracle_wms.models import FlextDbtOracleWmsModels


class TestsFlextDbtOracleWmsModels(m, FlextDbtOracleWmsModels):
    """Models for flext-dbt-oracle-wms tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. m - for test infrastructure (.Tests.*)
    2. FlextDbtOracleWmsModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from m)
    - tm.* (DBT Oracle WMS domain models)
    - m.* (production models via alternative alias)
    """

    class Tests(m.Tests):
        """Project-specific test fixtures namespace."""

        class DbtOracleWms:
            """DBT Oracle WMS-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextDbtOracleWmsModels

__all__ = [
    "TestsFlextDbtOracleWmsModels",
    "m",
    "tm",
]

m = TestsFlextDbtOracleWmsModels
