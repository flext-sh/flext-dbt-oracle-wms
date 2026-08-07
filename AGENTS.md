# AGENTS.md — flext-dbt-oracle-wms

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_dbt_oracle_wms` · deps: `flext-core`, `flext-meltano`, `flext-oracle-wms`

## Overview

Oracle WMS data transformation with dbt. Thin driver over `flext-meltano` dbt runner (ADR-006).

## Structure

```text
src/flext_dbt_oracle_wms/
├── api.py cli.py     # FlextDbtOracleWms + CLI
├── base.py
├── services/         # base.py, metadata.py, models.py, workflow.py
├── _utilities/client.py
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextDbtOracleWms` | class | `api.py` | facade |
| `FlextDbtOracleWmsWorkflow` | class | `services/workflow.py` | `run_oracle_wms_to_dbt_workflow` |

## Conventions (specific to this package)

- Workflow branches between model generation and optional transformations, returning a typed `WorkflowResult`. Connection profile is a typed `m.DbtOracleWms.*` model.
- WMS access via `flext-oracle-wms`.
- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Commands

```bash
make check PROJECT=flext-dbt-oracle-wms
make test  PROJECT=flext-dbt-oracle-wms       # tests/{unit,data_quality,marts,staging}
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
