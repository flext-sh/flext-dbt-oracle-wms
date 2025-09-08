"""Basic tests for FLEXT DBT Oracle WMS.

Since this is a DBT project with only SQL tests,
this minimal Python test file ensures mypy can process the tests directory.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import importlib
import pathlib

import tests


def test_package_import() -> None:
    """Ensure package imports so coverage collects module execution."""
    mod = importlib.import_module("flext_dbt_oracle_wms")
    assert mod is not None


def test_basic_import() -> None:
    """Test basic import functionality."""
    assert tests is not None


def test_package_structure() -> None:
    """Test that this is a valid Python package."""
    tests_dir = pathlib.Path(__file__).parent
    if tests_dir.name != "tests":
        msg: str = f"Expected {'tests'}, got {tests_dir.name}"
        raise AssertionError(msg)
    assert (tests_dir / "__init__.py").exists()
