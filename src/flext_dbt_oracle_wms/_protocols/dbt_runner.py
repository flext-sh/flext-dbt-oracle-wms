"""Protocol for the consumed dbt transformation runner boundary."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import p

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import m, t


@runtime_checkable
class DbtRunner(Protocol):
    """Protocol for the consumed dbt transformation runner boundary."""

    def run_dbt_transformation(
        self,
        models: t.StrSequence | None = None,
        project_dir: Path | None = None,
    ) -> p.Result[m.Meltano.CommandExecutionResult]:
        """Run DBT transformations through the configured executor."""
        ...


__all__: list[str] = ["DbtRunner"]
