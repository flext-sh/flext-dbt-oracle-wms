"""Protocol for the consumed dbt transformation runner boundary.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Protocol, runtime_checkable

from flext_meltano import p


class FlextDbtOracleWmsProtocolsDbtRunner:
    """Namespace for the consumed dbt transformation runner boundary protocol."""

    @runtime_checkable
    class DbtRunner(Protocol):
        """Protocol for the consumed dbt transformation runner boundary."""

        def run_dbt_transformation(
            self,
            models: Sequence[str] | None = None,
            project_dir: Path | None = None,
        ) -> p.Result[p.Meltano.CommandExecutionResult]:
            """Run DBT transformations through the configured executor."""
            ...


__all__: list[str] = ["FlextDbtOracleWmsProtocolsDbtRunner"]
