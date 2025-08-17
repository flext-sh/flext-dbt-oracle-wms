# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

FLEXT DBT Oracle WMS is an enterprise-grade dbt project that provides data transformations for Oracle Warehouse Management System (WMS) data. It follows Clean Architecture principles and implements dimensional modeling patterns for WMS analytics. The project transforms raw Oracle WMS data from Singer taps into business-ready analytical models.

## Architecture

### Layered Data Architecture

The project follows a layered approach with clear data flow:

```
Oracle WMS → Singer Tap → Raw Tables → dbt Transformations → Analytics
```

### dbt Project Structure

- **`models/staging/`** - Raw data standardization (materialized as views)
  - Standardizes Oracle WMS data types, handles nulls, and cleans raw data
  - Example: `stg_wms__allocation.sql`, `stg_wms__inventory.sql`
- **`models/marts/`** - Business-ready data models (materialized as tables)

  - **`operational/`** - Real-time operational metrics for dashboards
  - **`analytical/`** - Historical analysis and reporting models
  - **`metrics/`** - KPI and dashboard models

- **`macros/oracle_wms_utils.sql`** - Custom Oracle WMS utility macros

  - Status code mapping, timestamp standardization, data quality checks
  - WMS-specific business logic and transformations

- **`tests/`** - Data quality and business rule tests
  - Cross-model consistency tests, staging quality tests
  - Business rule validation for WMS entities

### Key Design Patterns

- **Surrogate Keys**: Uses `dbt_utils.generate_surrogate_key()` for dimensional modeling
- **Data Quality Flags**: Each staging model includes `data_quality_status` field
- **Incremental Processing**: Support for incremental models with timestamp-based processing
- **Oracle-Specific Macros**: Custom macros for Oracle WMS status mapping and data handling
- **Enterprise Hooks**: Audit logging and data quality metric tracking

## Development Commands

### Essential Quality Gates (Zero Tolerance)

```bash
make validate           # Complete validation (lint + type + security + test + dbt-test)
make check             # Essential checks (lint + type + test + dbt-compile)
```

### dbt Operations

```bash
# Setup and dependencies
make setup             # Complete development setup
make dbt-deps          # Install dbt dependencies
make dbt-debug         # Debug dbt configuration

# Core dbt workflow
make dbt-compile       # Compile dbt models
make dbt-run          # Run dbt models
make dbt-test         # Run dbt data tests
make dbt-docs         # Generate documentation

# Development workflow
make dbt-run --select staging        # Run staging models only
make dbt-run --select marts          # Run marts models only
make dbt-test --select staging       # Test staging models
```

### WMS-Specific Operations

```bash
# WMS model testing and execution
make wms-test                     # Test WMS-specific models
make wms-inventory                # Run WMS inventory models
make wms-shipment                 # Run WMS shipment models
make wms-analytics                # Run WMS analytics models
make wms-full-refresh             # Full refresh WMS models

# Makefile aliases for quick access
make wi                          # wms-inventory
make ws                          # wms-shipment
make wa                          # wms-analytics
make wt                          # wms-test
make wfr                         # wms-full-refresh
```

### Python Development

```bash
# Quality checks
make lint              # Ruff linting (ALL rules enabled)
make type-check        # MyPy strict type checking
make security          # Security scans (bandit + pip-audit)
make format            # Format code with ruff
make fix               # Auto-fix code issues

# Testing
make test              # Run pytest with 90% coverage requirement
make test-unit         # Unit tests only
make test-integration  # Integration tests only
make test-fast         # Run tests without coverage
make coverage-html     # Generate HTML coverage report
```

### Development Setup

```bash
make install           # Install dependencies with Poetry
make setup             # Complete development setup (includes dev dependencies and pre-commit)
make clean             # Clean build artifacts
make clean-all         # Deep clean including venv
make reset             # Complete project reset
```

### Diagnostics and Build

```bash
# Diagnostics
make diagnose          # Show environment diagnostics
make doctor            # Full health check (diagnose + check)

# Build and documentation
make build             # Build package
make docs              # Build all documentation  
make docs-serve        # Serve documentation locally

# Dependencies
make deps-update       # Update all dependencies
make deps-audit        # Security audit dependencies

# Common aliases (for faster development)
make t                 # test
make l                 # lint
make f                 # format
make tc                # type-check
make c                 # clean
make i                 # install
make v                 # validate
make dr                # dbt-run
make dt                # dbt-test
make dc                # dbt-compile
```

## Configuration

### dbt Configuration (`dbt_project.yml`)

- **Profile**: `flext_oracle_wms` (configure in `profiles.yml`)
- **Models**: Organized by layers with proper materialization
- **Variables**: Oracle WMS specific configuration including entity types and quality thresholds
- **Hooks**: Enterprise audit logging on run start/end

### Key Variables

```yaml
vars:
  oracle_wms_schema: "wms_raw" # Source schema from Singer tap
  enable_incremental_models: true # Enable incremental processing
  incremental_lookback_days: 7 # Lookback window for incremental models
  data_quality_thresholds: # Quality gate thresholds
    completeness: 0.95
    accuracy: 0.98
    consistency: 0.90
```

### Python Configuration (`pyproject.toml`)

- **Python**: 3.13+ required
- **Dependencies**: Links to `flext-core`, `flext-oracle-wms`, `flext-meltano`
- **Quality Tools**: Ruff (ALL rules), MyPy (strict), Bandit, pytest
- **Coverage**: 90% minimum requirement

## Data Models

### Core WMS Entities

The project transforms these Oracle WMS entities:

- **Allocation** - Pick/pack allocation tracking
- **Inventory** - Real-time inventory positions
- **Orders** - Header and detail order processing
- **Location** - Warehouse location management
- **Item** - Item master data
- **Shipment/Receipt** - Inbound/outbound operations
- **Task** - Work task orchestration
- **Wave** - Wave-based picking optimization

### Staging Layer Pattern

Staging models follow consistent patterns:

- Standardize data types and handle nulls
- Generate surrogate keys for dimensional modeling
- Add data quality status flags
- Include Singer extraction metadata
- Derive business dates from timestamps

### Marts Layer Pattern

Marts models provide business-ready analytics:

- **Operational**: Real-time metrics for dashboards with alert flags
- **Analytical**: Historical trends and performance analysis
- **Metrics**: KPI calculations with proper error handling

## Testing Strategy

### dbt Tests

- **Schema Tests**: Built-in dbt tests (unique, not_null, relationships)
- **Data Tests**: Custom SQL tests for business rules validation
- **Cross-Model Tests**: Consistency checks between related models

### Python Tests

- **Unit Tests**: Component testing with pytest
- **Integration Tests**: End-to-end pipeline testing
- **Coverage**: 90% minimum requirement enforced

### Data Quality

- Automated data quality checks in staging models
- Business rule validation in custom tests
- Operational alerting in marts models

## Oracle WMS Integration

### Connection Setup

Configure Oracle connection in `profiles.yml`:

```yaml
flext_oracle_wms:
  outputs:
    dev:
      type: oracle
      host: "{{ env_var('ORACLE_HOST') }}"
      # ... other Oracle connection parameters
```

### Performance Optimization

- Incremental models for large datasets
- Proper indexing on marts tables
- Partitioning by business_date where appropriate
- Oracle-specific query hints in macros

## Common Workflows

### Adding New WMS Entity

1. Create staging model following `stg_wms__allocation.sql` pattern
2. Add source definition in `_sources.yml`
3. Create corresponding marts models as needed
4. Add data quality tests
5. Update documentation

### Creating New Analytics Model

1. Follow marts layer conventions in `opr_wms__allocation_summary.sql`
2. Include proper indexes and materialization strategy
3. Add operational alerting logic
4. Create corresponding tests
5. Tag appropriately for selective runs

## TODO: GAPS DE ARQUITETURA IDENTIFICADOS - PRIORIDADE ALTA

### 🚨 GAP 1: Oracle WMS Integration Efficiency

**Status**: ALTO - Integration com flext-oracle-wms pode ser optimized
**Problema**:

- Python components em dbt project podem duplicate flext-oracle-wms functionality
- WMS API connectivity patterns podem divergir between projects
- Business logic duplication para WMS operations

**TODO**:

- [ ] Optimize integration com flext-oracle-wms library
- [ ] Eliminate duplication de WMS API functionality
- [ ] Align WMS connectivity patterns com shared library
- [ ] Consolidate WMS business logic em appropriate layer

### 🚨 GAP 2: DBT-Python WMS Hybrid Architecture Complexity

**Status**: ALTO - Hybrid dbt-Python architecture para WMS pode ser over-engineered
**Problema**:

- Python infrastructure/ directory em dbt project pode criar maintenance overhead
- WMS integration logic duplicated com flext-oracle-wms library
- Complex layered architecture pode não justify benefits para dbt context

**TODO**:

- [ ] Simplify dbt-Python integration architecture para WMS
- [ ] Leverage flext-oracle-wms library mais efficiently
- [ ] Review architectural complexity vs benefits
- [ ] Document WMS integration patterns clearly

### 🚨 GAP 3: WMS Business Logic Layer Placement

**Status**: ALTO - WMS business logic pode belong em wrong layer
**Problema**:

- WMS-specific business logic em dbt macros pode belong em flext-oracle-wms
- Inventory calculations e warehouse logic podem be misplaced
- Domain knowledge scattered between dbt e library layers

**TODO**:

- [ ] Move WMS business logic to appropriate layer (flext-oracle-wms)
- [ ] Keep dbt layer focused em data transformation patterns
- [ ] Refactor to proper layered architecture para WMS domain
- [ ] Document clear boundaries entre dbt e WMS business logic

### 🚨 GAP 4: Singer WMS Ecosystem Integration Incomplete

**Status**: ALTO - Integration com WMS Singer ecosystem não clearly defined
**Problema**:

- dbt project relationship com flext-tap-oracle-wms patterns podem be suboptimal
- Data flow from WMS taps → dbt → targets não comprehensively documented
- WMS-specific Meltano integration patterns podem be incomplete

**TODO**:

- [ ] Define comprehensive integration patterns com flext-meltano para WMS
- [ ] Document detailed data flow from flext-tap-oracle-wms to dbt models
- [ ] Optimize integration com complete WMS Singer ecosystem
- [ ] Create integrated WMS pipeline documentation com examples

## Quality Standards

- **Zero Tolerance**: All quality gates must pass (make validate)
- **Coverage**: 90% minimum test coverage required
- **Type Safety**: Strict MyPy configuration
- **Security**: Bandit scanning for vulnerabilities
- **Documentation**: All models must be documented with business context
