"""Version information for flext-dbt-oracle-wms."""

from __future__ import annotations

from typing import Final

# Version components
MAJOR: Final[int] = 0
MINOR: Final[int] = 9
PATCH: Final[int] = 0

# Version string
__version__: Final[str] = f"{MAJOR}.{MINOR}.{PATCH}"
__version_info__: Final[tuple[int, int, int]] = (MAJOR, MINOR, PATCH)


class FlextDbtOracleWmsVersion:
    """Version information container for flext-dbt-oracle-wms."""

    def __init__(self) -> None:
        """Initialize version information."""
        self.major = MAJOR
        self.minor = MINOR
        self.patch = PATCH
        self.version = __version__
        self.version_info = __version_info__

    @classmethod
    def current(cls) -> FlextDbtOracleWmsVersion:
        """Return current version information."""
        return cls()


VERSION: Final[FlextDbtOracleWmsVersion] = FlextDbtOracleWmsVersion.current()

__all__ = ["VERSION", "FlextDbtOracleWmsVersion", "__version__", "__version_info__"]
