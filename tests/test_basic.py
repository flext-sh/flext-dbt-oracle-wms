"""Basic tests for FLEXT DBT Oracle WMS.

Since this is a DBT project with only SQL tests,
this minimal Python test file ensures mypy can process the tests directory.
"""

import pathlib

import tests


def test_basic_import() -> None:
    """Test basic import functionality."""
    # Simple test to ensure the package can be imported

    assert tests is not None


def test_package_structure() -> None:
    """Test that this is a valid Python package."""
    # Verify this directory is a valid Python package

    tests_dir = pathlib.Path(__file__).parent
    if tests_dir.name != "tests":
        msg = f"Expected {"tests"}, got {tests_dir.name}"
        raise AssertionError(msg)
    assert (tests_dir / "__init__.py").exists()
