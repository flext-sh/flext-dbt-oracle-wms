"""Basic tests for FLEXT DBT Oracle WMS.

Since this is a DBT project with only SQL tests,
this minimal Python test file ensures mypy can process the tests directory.
"""


def test_basic_import() -> None:
    """Test basic import functionality."""
    # Simple test to ensure the package can be imported
    import tests
    assert tests is not None


def test_package_structure() -> None:
    """Test that this is a valid Python package."""
    # Verify this directory is a valid Python package
    import pathlib

    tests_dir = pathlib.Path(__file__).parent
    assert tests_dir.name == "tests"
    assert (tests_dir / "__init__.py").exists()
