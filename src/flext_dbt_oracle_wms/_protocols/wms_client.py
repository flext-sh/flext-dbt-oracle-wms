"""Protocol for the consumed Oracle WMS client boundary."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import p

if TYPE_CHECKING:
    from flext_dbt_oracle_wms import m, t


class FlextDbtOracleWmsProtocolsWmsClient:
    """Namespace holder for the consumed Oracle WMS client boundary protocol."""

    @runtime_checkable
    class WmsClient(Protocol):
        """Protocol for the consumed Oracle WMS client boundary.

        Mirrors the public surface of the owning ``flext_oracle_wms`` client
        (``u.OracleWms.Client``) exactly, including its ``get_entity_data``
        boundary method, so the injected/real client satisfies this contract.
        """

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


__all__: list[str] = ["FlextDbtOracleWmsProtocolsWmsClient"]
