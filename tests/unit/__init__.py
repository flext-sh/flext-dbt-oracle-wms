# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle Wms package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_dbt_oracle_wms.test_basic import (
        test_basic_import,
        test_package_import,
        test_package_structure,
    )
    from flext_dbt_oracle_wms.test_cli import (
        test_cli_executes_discover_command,
        test_cli_executes_extract_command_through_public_facade,
        test_cli_main_defaults_to_info,
        test_cli_returns_failure_for_pipeline_errors,
        test_cli_returns_failure_for_unknown_command,
        test_cli_runs_pipeline_through_public_facade,
        test_module_main_uses_public_cli_entrypoint,
        testuses_default_extract_entity,
    )
    from flext_dbt_oracle_wms.test_module_governance import (
        test_package_root_exposes_canonical_public_entrypoints,
    )
    from flext_dbt_oracle_wms.test_simple_api import (
        test_discover_oracle_wms_entities_uses_public_client_protocol,
        test_extract_oracle_wms_data_uses_public_client_protocol,
        test_run_oracle_wms_to_dbt_workflow_uses_public_protocols,
        test_validate_wms_connection_uses_public_client_protocol,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": (
            "test_basic_import",
            "test_package_import",
            "test_package_structure",
        ),
        ".test_cli": (
            "test_cli_executes_discover_command",
            "test_cli_executes_extract_command_through_public_facade",
            "test_cli_main_defaults_to_info",
            "test_cli_returns_failure_for_pipeline_errors",
            "test_cli_returns_failure_for_unknown_command",
            "test_cli_runs_pipeline_through_public_facade",
            "test_module_main_uses_public_cli_entrypoint",
            "testuses_default_extract_entity",
        ),
        ".test_module_governance": (
            "test_package_root_exposes_canonical_public_entrypoints",
        ),
        ".test_simple_api": (
            "test_discover_oracle_wms_entities_uses_public_client_protocol",
            "test_extract_oracle_wms_data_uses_public_client_protocol",
            "test_run_oracle_wms_to_dbt_workflow_uses_public_protocols",
            "test_validate_wms_connection_uses_public_client_protocol",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "test_basic_import",
    "test_cli_executes_discover_command",
    "test_cli_executes_extract_command_through_public_facade",
    "test_cli_main_defaults_to_info",
    "test_cli_returns_failure_for_pipeline_errors",
    "test_cli_returns_failure_for_unknown_command",
    "test_cli_runs_pipeline_through_public_facade",
    "test_discover_oracle_wms_entities_uses_public_client_protocol",
    "test_extract_oracle_wms_data_uses_public_client_protocol",
    "test_module_main_uses_public_cli_entrypoint",
    "test_package_import",
    "test_package_root_exposes_canonical_public_entrypoints",
    "test_package_structure",
    "test_run_oracle_wms_to_dbt_workflow_uses_public_protocols",
    "test_validate_wms_connection_uses_public_client_protocol",
    "testuses_default_extract_entity",
]
