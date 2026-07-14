"""Base runtime for the DBT Oracle WMS public facade."""

from __future__ import annotations

from collections.abc import Sequence

from flext_core import s
from flext_dbt_oracle_wms import FlextDbtOracleWmsSettings, p, r, t, u


class FlextDbtOracleWmsBase(s[FlextDbtOracleWmsSettings]):
    """Shared runtime dependencies and low-level entity access."""

    _client: p.DbtOracleWms.Client | None = u.PrivateAttr(default_factory=lambda: None)
    _service: u.DbtOracleWms.Service | None = u.PrivateAttr(
        default_factory=lambda: None,
    )

    def __init__(
        self,
        settings: FlextDbtOracleWmsSettings | None = None,
        client: p.DbtOracleWms.Client | None = None,
        service: u.DbtOracleWms.Service | None = None,
    ) -> None:
        """Initialize the unified DBT Oracle WMS service."""
        # NOTE (multi-agent): mro-rn88 — pass the injected settings to the ServiceBase
        # runtime so settings resolves the override (not just the global singleton).
        super().__init__(
            runtime_settings=settings,
            settings_type=None,
            settings_overrides=None,
            initial_context=None,
        )
        self._client = client
        self._service = service

    @property
    def client(self) -> p.DbtOracleWms.Client:
        """The DBT Oracle WMS client instance."""
        if self._client is None:
            self._client = u.DbtOracleWms()
        return self._client

    @property
    def service(self) -> u.DbtOracleWms.Service:
        """The workflow service instance."""
        if self._service is None:
            self._service = u.DbtOracleWms.Service()
        return self._service

    def discover_oracle_wms_entities(self) -> p.Result[t.StrSequence]:
        """Discover Oracle WMS entities through the public domain facade."""
        discovered: p.Result[t.StrSequence] = self.client.discover_oracle_wms_entities()
        return discovered

    def extract_oracle_wms_data(
        self,
        entity_name: str,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        """Extract Oracle WMS entity records through the public domain facade."""
        extracted: p.Result[Sequence[t.ConfigurationMapping]] = (
            self.client.extract_oracle_wms_data(entity_name, filters)
        )
        return extracted

    @staticmethod
    def _resolve_entity_names(
        inventory_items: t.StrSequence | None,
        shipments: t.StrSequence | None,
    ) -> t.StrSequence | None:
        entity_names: t.MutableSequenceOf[str] = []
        if inventory_items is not None:
            entity_names.append("items")
        if shipments is not None:
            entity_names.append("shipments")
        return entity_names or None

    def _extract_entity_records(
        self,
        entity_name: str,
        requested_identifiers: t.StrSequence | None,
        identifier_fields: t.StrSequence,
    ) -> p.Result[Sequence[t.ConfigurationMapping]]:
        extract_result = self.client.extract_oracle_wms_data(entity_name)
        if extract_result.failure:
            return r[Sequence[t.ConfigurationMapping]].fail(
                extract_result.error or f"Failed to extract {entity_name}",
            )
        if requested_identifiers is None:
            return r[Sequence[t.ConfigurationMapping]].ok(extract_result.value)
        requested_values = {
            identifier.strip()
            for identifier in requested_identifiers
            if identifier.strip()
        }
        filtered_records = [
            record
            for record in extract_result.value
            if any(
                str(record.get(field, "")).strip() in requested_values
                for field in identifier_fields
            )
        ]
        if not filtered_records:
            return r[Sequence[t.ConfigurationMapping]].fail(
                f"No {entity_name} records matched the requested identifiers",
            )
        return r[Sequence[t.ConfigurationMapping]].ok(filtered_records)


__all__: list[str] = ["FlextDbtOracleWmsBase"]
