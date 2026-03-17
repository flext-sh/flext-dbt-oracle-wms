"""Auto-generated centralized models."""

from __future__ import annotations

from pydantic import RootModel


class FlextAutoConstants:
    pass


class FlextAutoTypes:
    pass


class FlextAutoProtocols:
    pass


class FlextAutoUtilities:
    pass


class FlextAutoModels:
    pass


c = FlextAutoConstants
t = FlextAutoTypes
p = FlextAutoProtocols
u = FlextAutoUtilities
m = FlextAutoModels


class DBTOracleWMSAnalysisConfiguration(RootModel[dict[str, t.ContainerValue | None]]):
    pass


class DBTOracleWMSCompilationConfiguration(
    RootModel[dict[str, t.ContainerValue | None]]
):
    pass


class DBTOracleWMSDocumentationConfiguration(
    RootModel[dict[str, t.ContainerValue | None]]
):
    pass


class DBTOracleWMSExecutionConfiguration(RootModel[dict[str, t.ContainerValue | None]]):
    pass


class DBTOracleWMSProjectConfiguration(RootModel[dict[str, t.ContainerValue | None]]):
    pass


class DBTOracleWMSSnapshotConfiguration(RootModel[dict[str, t.ContainerValue | None]]):
    pass
