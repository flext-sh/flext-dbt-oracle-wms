"""Protocol for the consumed Oracle WMS client boundary."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import p

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import m, t


@runtime_checkable
class WmsClient(Protocol):
    """Protocol for the consumed Oracle WMS client boundary."""

    def discover_entities(self) -> p.Result[t.StrSequence]:
        """Discover available Oracle WMS entities."""
        ...

    def get_entity_data(
        self,
        entity_name: str,
        limit: int | None = None,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[t.SequenceOf[t.StrMapping]]:
        """Get data for a specific Oracle WMS entity."""
        ...

    def start(self) -> p.Result[bool]:
        """Start the Oracle WMS client."""
        ...

    def health_check(self) -> p.Result[m.Api.HttpResponse]:
        """Check Oracle WMS API health."""
        ...


__all__: list[str] = ["WmsClient"]
