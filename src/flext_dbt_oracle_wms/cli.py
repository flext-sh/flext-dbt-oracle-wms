"""CLI for FLEXT DBT Oracle WMS package using consolidated DBT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio

import click
from flext_core import FlextLogger

from flext_dbt_oracle_wms import (
    FlextDbtOracleWmsConfig,
    __version__,
    create_oracle_wms_workflow_service,
)

logger = FlextLogger(__name__)


@click.group()
@click.version_option()
@click.pass_context
def main(ctx: click.Context) -> None:
    """FLEXT DBT Oracle WMS - Oracle WMS data transformation with DBT using consolidated patterns."""
    ctx.ensure_object(dict)


@main.command()
def discover() -> None:
    """Discover Oracle WMS entities."""
    try:
        config = FlextDbtOracleWmsConfig()
        workflow_service = create_oracle_wms_workflow_service(config)

        click.echo("Discovering Oracle WMS entities...")
        result = asyncio.run(workflow_service.run_entity_discovery_workflow())

        if result.is_success:
            data = result.data or {}
            click.echo("✅ Discovery completed successfully!")
            click.echo(f"📊 Discovered {data.get('discovered_entities', 0)} entities")
            entity_types = data.get("entity_types", [])
            if isinstance(entity_types, list):
                click.echo(f"🏷️  Entity types: {', '.join(entity_types)}")
            else:
                click.echo(f"🏷️  Entity types: {entity_types}")
        else:
            click.echo(f"❌ Discovery failed: {result.error}", err=True)

    except Exception as e:
        logger.exception("Unexpected error in discovery command")
        click.echo(f"❌ Unexpected error: {e}", err=True)


@main.command()
@click.option("--entity", multiple=True, help="Oracle WMS entity to extract")
@click.option("--limit", type=int, help="Maximum records per entity")
def extract(
    entity: tuple[str, ...],
    limit: int | None,
) -> None:
    """Extract data from Oracle WMS entities."""
    try:
        config = FlextDbtOracleWmsConfig()
        workflow_service = create_oracle_wms_workflow_service(config)
        entity_names = list(entity) if entity else None
        limits = dict.fromkeys(entity_names, limit) if entity_names and limit else None

        click.echo(f"Extracting Oracle WMS data: {entity_names or 'all discovered'}")
        result = asyncio.run(
            workflow_service.run_data_extraction_workflow(
                entity_names or [],
                None,
                limits,
            ),
        )

        if result.is_success:
            data = result.data or {}
            click.echo("✅ Extraction completed successfully!")
            click.echo(f"📊 Total records: {data.get('total_records', 0)}")
        else:
            click.echo(f"❌ Extraction failed: {result.error}", err=True)

    except Exception as e:
        logger.exception("Unexpected error in extraction command")
        click.echo(f"❌ Unexpected error: {e}", err=True)


@main.command()
@click.option("--entity", multiple=True, help="Oracle WMS entity to process")
@click.option("--model", multiple=True, help="DBT model to run")
def pipeline(
    entity: tuple[str, ...],
    model: tuple[str, ...],
) -> None:
    """Run full Oracle WMS to DBT transformation pipeline."""
    try:
        config = FlextDbtOracleWmsConfig()
        workflow_service = create_oracle_wms_workflow_service(config)
        entity_names = list(entity) if entity else None
        model_names = list(model) if model else None

        click.echo("🚀 Starting full Oracle WMS to DBT pipeline...")
        result = asyncio.run(
            workflow_service.run_full_transformation_pipeline(
                entity_names,
                None,
                model_names,
            ),
        )

        if result.is_success:
            data = result.data or {}
            summary = data.get("summary", {})
            if isinstance(summary, dict):
                click.echo("✅ Pipeline completed successfully!")
                click.echo(
                    f"📊 Processed: {summary.get('entities_processed', 0)} entities",
                )
            else:
                click.echo("✅ Pipeline completed successfully!")
                click.echo(f"📊 Summary: {summary}")
        else:
            click.echo(f"❌ Pipeline failed: {result.error}", err=True)

    except Exception as e:
        logger.exception("Unexpected error in pipeline command")
        click.echo(f"❌ Unexpected error: {e}", err=True)


@main.command()
def info() -> None:
    """Show FLEXT DBT Oracle WMS information."""
    try:
        click.echo("🏢 FLEXT DBT Oracle WMS")
        click.echo(f"📦 Version: {__version__}")
        click.echo("🎯 Purpose: Oracle WMS data transformation with DBT")
        click.echo("🔧 Architecture: flext-core + flext-oracle-wms + flext-meltano")
        click.echo("")
        click.echo("Available commands:")
        click.echo("  discover   - Discover Oracle WMS entities")
        click.echo("  extract    - Extract data from Oracle WMS")
        click.echo("  pipeline   - Run full transformation pipeline")
        click.echo("")
        click.echo("Use --help with any command for more details")

    except Exception as e:
        logger.exception("Unexpected error in info command")
        click.echo(f"❌ Unexpected error: {e}", err=True)


if __name__ == "__main__":
    main()
