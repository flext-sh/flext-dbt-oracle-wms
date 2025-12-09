# FLEXT dbt Oracle WMS - Warehouse Management Analytics

**Type**: DBT Project | **Status**: 1.0.0 Release Preparation | **Dependencies**: Python 3.13+, dbt-core, dbt-oracle

dbt project for Oracle Warehouse Management System (WMS) data transformations and analytics. Built with Python 3.13+, dbt Core, and Clean Architecture patterns as part of the FLEXT data integration platform.

## Overview

FLEXT dbt Oracle WMS provides data transformations, dimensional modeling, and advanced analytics for Oracle WMS environments. The project transforms raw Oracle WMS data from Singer taps into business-ready analytical models with real-time operational metrics and historical trend analysis.

> For verified project capabilities and accurate status information, see the [Development Guide](docs/development/guidelines.md).

### Key Features

- **Oracle WMS Analytics**: Transformations for warehouse management data
- **Dimensional Modeling**: Star schema design for inventory, orders, and operational analytics
- **WMS-Specific Macros**: Custom dbt macros for WMS business logic and calculations
- **Operational Dashboards**: Real-time metrics for warehouse operations and KPIs
- **Historical Analytics**: Trend analysis and performance reporting
- **Clean Architecture**: Python components with domain-driven design patterns
- **Zero Tolerance Quality**: 90% test coverage with quality gates

## Quick Start

### Prerequisites

- **Python 3.13+** installed
- **dbt Core** with Oracle adapter
- **Oracle WMS database** access and connection credentials
- **WMS data source** via flext-tap-oracle-wms
- **Poetry** for dependency management

### Installation

```bash
# Clone and setup
git clone <repository-url>
cd flext-dbt-oracle-wms

# Install dependencies
poetry install

# Setup dbt profile
cp profiles.yml.example profiles.yml
# Edit profiles.yml with your Oracle connection details

# Test connection
dbt debug
```

### First Run

```bash
# Install dbt dependencies
dbt deps

# Run all models
dbt run

# Run tests
dbt test

# Generate documentation
dbt docs generate
dbt docs serve
```

## < - Architecture

FLEXT DBT Oracle WMS follows a **layered data architecture**:

```
Data Flow:
Oracle WMS   Singer Tap   Raw Tables   dbt Transformations   Analytics

dbt Project Structure:
models/
--- staging/           # Raw data standardization
-   --- stg_wms__allocation.sql
-   --- stg_wms__inventory.sql
-   --- stg_wms__order_hdr.sql
-   --- stg_wms__order_dtl.sql
--- marts/             # Business-ready data models
-   --- operational/   # Real-time operational metrics
-   --- analytical/    # Historical analysis models
-   --- metrics/       # KPI and dashboard models
--- analyses/          # Ad-hoc analysis queries
```

### Data Modeling Layers

#### =9 **Staging Layer** (`staging/`)

- **Purpose**: Standardize and clean raw Oracle WMS data
- **Materialization**: Views (for real-time data)
- **Transformations**: Data type casting, null handling, field renaming
- **Examples**: `stg_wms__allocation`, `stg_wms__inventory`

#### =8 **Marts Layer** (`marts/`)

- **Purpose**: Business-ready data models for analytics
- **Materialization**: Tables (for performance)
- **Types**:
  - **Operational**: Real-time dashboards and monitoring
  - **Analytical**: Historical analysis and reporting
  - **Metrics**: KPIs and executive dashboards

#### =6 **Analyses Layer** (`analyses/`)

- **Purpose**: Ad-hoc business analysis and data exploration
- **Output**: SQL queries for business stakeholders

## <- Features

### Oracle WMS Data Models

- - **Allocation Management** - Pick and pack allocation tracking
- - **Inventory Tracking** - Real-time inventory positions
- - **Order Management** - Header and detail order processing
- - **Warehouse Operations** - Location, item, and movement data
- - **Task Management** - Work task orchestration and tracking
- - **Wave Planning** - Wave-based picking optimization

### Enterprise Features

- - **Data Quality Testing** - Automated data validation and quality checks
- - **Incremental Models** - Efficient processing of large datasets
- - **Audit Logging** - Complete data lineage and change tracking
- - **Performance Optimization** - Partitioning and indexing strategies
- - **Documentation Generation** - Automated model and column documentation

### Integration Capabilities

- **=- Singer Integration** - Works with flext-tap-oracle-wms
- **= BI Tool Ready** - Optimized for Tableau, Power BI, Looker
- **=- Real-time Processing** - Supports near real-time analytics
- **= Scalable Architecture** - Handles enterprise-scale WMS data

## = Data Models

### Core WMS Entities

#### Allocation (`stg_wms__allocation`)

```sql
-- Standardized allocation data with business logic
select
    allocation_id,
    company_code,
    facility_code,
    order_dtl_id,
    allocated_quantity,
    packed_quantity,
    allocation_status_id,
    pick_location_string,
    is_picking_flag,
    created_timestamp,
    modified_timestamp
from {{ ref('stg_wms__allocation') }}
```

#### Inventory (`stg_wms__inventory`)

- Real-time inventory positions
- Location-based inventory tracking
- UOM and packaging information
- Lot and serial number tracking

#### Orders (`stg_wms__order_hdr`, `stg_wms__order_dtl`)

- Order header and detail information
- Customer and shipping details
- Order status and lifecycle tracking
- Fulfillment metrics

### Business Marts

#### Operational Dashboard (`marts/operational/`)

- **Inbound Operations**: Receiving performance, ASN tracking
- **Outbound Operations**: Shipping performance, order fulfillment
- **Inventory Management**: Stock levels, turnover rates
- **Labor Management**: Productivity metrics, task completion

#### Analytical Models (`marts/analytical/`)

- **Historical Trends**: Long-term performance analysis
- **Seasonality Analysis**: Demand patterns and forecasting
- **Cost Analysis**: Warehouse cost allocation and optimization
- **Customer Analytics**: Order patterns and service levels

## = - Development

### Project Setup

```bash
# Install development dependencies
make dev-install

# Setup pre-commit hooks
make pre-commit

# Run quality checks
make validate
```

### DBT Commands

```bash
# Model development
dbt run --select staging        # Run staging models only
dbt run --select marts          # Run marts models only
dbt run --select +stg_wms__allocation  # Run model and upstream

# Testing
dbt test                        # Run all tests
dbt test --select staging      # Test staging models
dbt test --data                 # Run data tests only

# Documentation
dbt docs generate              # Generate documentation
dbt docs serve                 # Serve documentation locally

# Debugging
dbt debug                      # Test connections
dbt compile                    # Compile without running
```

### Quality Gates

FLEXT DBT Oracle WMS enforces **enterprise quality standards**:

```bash
# Run all quality checks (must pass 100%)
make validate

# Individual checks
make lint          # SQL and Python linting
make type-check
make security      # Security scan
make test          # dbt tests + Python tests
make coverage      # Coverage report (90%+ required)
```

### Model Development Guidelines

#### 1. **Naming Conventions**

```sql
-- Staging models: stg_{source}__{entity}
-- Mart models: {mart_type}__{business_area}__{entity}

-- Examples:
stg_wms__allocation           -- Staging allocation data
opr_wms__allocation_summary   -- Operational allocation summary
ana_wms__inventory_analysis   -- Analytical inventory analysis
met_wms__kpi_dashboard       -- Metrics for KPI dashboard
```

#### 2. **Model Configuration**

```sql
{{
  config(
    materialized='table',        -- table, view, or incremental
    tags=['operational', 'wms'], -- for selective runs
    schema='wms_marts',          -- target schema
    pre_hook='{{ create_audit_log() }}',
    post_hook='{{ update_stats() }}'
  )
}}
```

#### 3. **Data Quality Tests**

```sql
-- Schema tests in schema.yml
models:
  - name: stg_wms__allocation
    tests:
      - unique:
          column_name: allocation_id
      - not_null:
          column_name: allocation_id
    columns:
      - name: allocated_quantity
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
```

## > Testing

### Test Types

#### **Schema Tests** (Built-in dbt tests)

```yaml
# models/staging/schema.yml
models:
  - name: stg_wms__allocation
    tests:
      - unique:
          column_name: allocation_id
      - not_null:
          column_name: [company_code, facility_code]
```

#### **Data Tests** (Custom SQL tests)

```sql
-- tests/staging/test_stg_wms__allocation_business_rules.sql
-- Test: Allocated quantity should never exceed ordered quantity
select *
from {{ ref('stg_wms__allocation') }} a
join {{ ref('stg_wms__order_dtl') }} o
  on a.order_dtl_id = o.order_dtl_id
where a.allocated_quantity > o.ordered_quantity
```

#### **Python Tests** (Component tests)

```bash
# Run Python component tests
pytest tests/

# Test specific components
pytest tests/test_basic.py
```

### Running Tests

```bash
# All tests
make test

# dbt tests only
dbt test

# Python tests only
pytest

# Test coverage
make coverage-html  # HTML report in reports/coverage/
```

## = Deployment

### Environment Setup

#### Development

```bash
# Local development
dbt run --target dev
dbt test --target dev
```

#### Staging

```bash
# Staging environment validation
dbt run --target staging
dbt test --target staging --store-failures
```

#### Production

```bash
# Production deployment
dbt run --target prod
dbt test --target prod --store-failures
dbt docs generate --target prod
```

### CI/CD Pipeline

```yaml
# .github/workflows/dbt.yml
name: dbt Oracle WMS Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"
      - name: Install dependencies
        run: poetry install
      - name: Run quality checks
        run: make validate
      - name: Run dbt tests
        run: dbt test --target ci
```

## = Oracle WMS Integration

### Data Sources

FLEXT DBT Oracle WMS integrates with Oracle WMS via Singer taps:

#### **Primary Tables**

- `ALLOCATION` - Pick/pack allocations
- `INVENTORY` - Inventory positions
- `ORDER_HDR` - Order headers
- `ORDER_DTL` - Order details
- `LOCATION` - Warehouse locations
- `ITEM` - Item master data
- `TASK` - Work tasks
- `WAVE` - Wave planning

#### **Reference Tables**

- `STATUS` - Status codes
- `UOM` - Units of measure
- `COMPANY` - Company codes
- `FACILITY` - Facility information

### Connection Configuration

```yaml
# profiles.yml
flext_oracle_wms:
  target: dev
  outputs:
    dev:
      type: oracle
      host: "{{ env_var('ORACLE_HOST') }}"
      port: 1521
      user: "{{ env_var('ORACLE_USER') }}"
      pass: "{{ env_var('ORACLE_PASS') }}"
      service: "{{ env_var('ORACLE_SERVICE') }}"
      schema: "{{ env_var('ORACLE_SCHEMA') }}"
      threads: 4
```

### Performance Optimization

#### **Partitioning Strategy**

```sql
-- Partition large tables by business date
{{
  config(
    materialized='table',
    partition_by='business_date',
    cluster_by=['company_code', 'facility_code']
  )
}}
```

#### **Incremental Processing**

```sql
-- Incremental models for large datasets
{{
  config(
    materialized='incremental',
    unique_key='allocation_id',
    on_schema_change='fail'
  )
}}

select * from {{ ref('stg_wms__allocation') }}

{% if is_incremental() %}
  where modified_timestamp > (select max(modified_timestamp) from {{ this }})
{% endif %}
```

## = Documentation

- **[Getting Started Guide](docs/getting-started/setup.md)** - Step-by-step setup instructions
- **[Data Model Reference](docs/models/reference.md)** - Complete data model documentation
- **[Oracle WMS Integration](docs/integration/oracle-wms.md)** - WMS-specific integration guide
- **[Development Guide](docs/development/guidelines.md)** - Development best practices

### Generated Documentation

```bash
# Generate and serve dbt docs
dbt docs generate
dbt docs serve --port 8080

# View at: http://localhost:8080
```

## =' Configuration

### DBT Variables

Configure behavior via `dbt_project.yml`:

```yaml
vars:
  # Oracle WMS schema configuration
  oracle_wms_schema: "wms_raw"

  # Data freshness thresholds
  freshness_warn_after: { count: 12, period: hour }
  freshness_error_after: { count: 24, period: hour }

  # Business configuration
  business_start_date: "2024-01-01"

  # Performance settings
  enable_incremental_models: true
  incremental_lookback_days: 7

  # Data quality thresholds
  data_quality_thresholds:
    completeness: 0.95
    accuracy: 0.98
    consistency: 0.90
```

### Environment Variables

```bash
# Oracle connection
export ORACLE_HOST="your-oracle-host"
export ORACLE_USER="your-username"
export ORACLE_PASS="your-password"
export ORACLE_SERVICE="your-service"
export ORACLE_SCHEMA="your-schema"

# dbt configuration
export DBT_PROFILES_DIR="."
export DBT_ORACLE_WMS_SCHEMA="wms_raw"
```

## > Contributing

We welcome contributions! Please see our [Development Guide](docs/development/guidelines.md) for development best practices.

### Development Workflow

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-model`)
3. Develop and test changes
4. Run quality gates (`make validate`)
5. Update documentation
6. Commit changes (`git commit -m 'Add new allocation model'`)
7. Push to branch (`git push origin feature/new-model`)
8. Open Pull Request

## = License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## = Performance

- **=% High Throughput** - Processes millions of WMS records efficiently
- **Incremental Updates** - Smart incremental processing for large datasets
- **= Scalable Architecture** - Handles enterprise-scale Oracle WMS data
- **= Optimized Storage** - Partitioning and clustering for query performance

## = Related Projects

- **[flext-core](https://github.com/organization/flext/tree/main/flext-core/)** - Core business logic and domain models
- **[flext-tap-oracle-wms](https://github.com/organization/flext/tree/main/flext-tap-oracle-wms/)** - Singer tap for Oracle WMS data extraction
- **[flext-target-oracle](https://github.com/organization/flext/tree/main/flext-target-oracle/)** - Singer target for Oracle database loading
- **[flext-dbt-oracle](https://github.com/organization/flext/tree/main/flext-dbt-oracle/)** - Base dbt Oracle transformations
- **[flext-observability](https://github.com/organization/flext/tree/main/flext-observability/)** - Monitoring and observability

## Configuration

### Database Connection

Configure Oracle WMS connection in `profiles.yml`:

```yaml
flext_oracle_wms:
  target: dev
  outputs:
    dev:
      type: oracle
      host: "{{ env_var('ORACLE_HOST') }}"
      port: "{{ env_var('ORACLE_PORT') | int }}"
      service_name: "{{ env_var('ORACLE_SERVICE_NAME') }}"
      username: "{{ env_var('ORACLE_USERNAME') }}"
      password: "{{ env_var('ORACLE_PASSWORD') }}"
      schema: "{{ env_var('ORACLE_SCHEMA', 'WMS_ANALYTICS') }}"
      threads: 4
    prod:
      type: oracle
      host: "{{ env_var('ORACLE_PROD_HOST') }}"
      service_name: "{{ env_var('ORACLE_PROD_SERVICE_NAME') }}"
      username: "{{ env_var('ORACLE_PROD_USERNAME') }}"
      password: "{{ env_var('ORACLE_PROD_PASSWORD') }}"
      schema: "{{ env_var('ORACLE_PROD_SCHEMA') }}"
      threads: 8
```

### Environment Variables

```bash
# Oracle WMS connection
export ORACLE_HOST=wms-prod.company.com
export ORACLE_PORT=1521
export ORACLE_SERVICE_NAME=WMSPROD
export ORACLE_USERNAME=wms_analytics
export ORACLE_PASSWORD=secure_password
export ORACLE_SCHEMA=WMS_ANALYTICS

# dbt settings
export DBT_PROFILES_DIR=profiles/
export DBT_TARGET=dev
export DBT_THREADS=4

# WMS Analytics
export WMS_SOURCE_SCHEMA=wms_raw
export WMS_TARGET_SCHEMA=wms_analytics
export WMS_ANALYTICS_TIMEZONE=UTC
```

### dbt Variables

Configure in `dbt_project.yml`:

```yaml
vars:
  # Oracle WMS Configuration
  oracle_wms_schema: "wms_raw"
  enable_incremental_models: true
  incremental_lookback_days: 7

  # WMS Business Configuration
  wms_companies: ["ACME", "CORP"]
  wms_facilities: ["DC01", "DC02", "DC03"]

  # Data Quality Thresholds
  data_quality_thresholds:
    completeness: 0.95
    accuracy: 0.98
    consistency: 0.90

  # Performance Settings
  enable_parallel_processing: true
  default_parallel_degree: 4
```

## WMS-Specific Macros

### Allocation Macros

```sql
-- Calculate allocation efficiency
{{ wms_allocation_efficiency('allocated_qty', 'ordered_qty') }}

-- Determine allocation status
{{ wms_allocation_status('status_id') }}

-- Calculate pick productivity
{{ wms_pick_productivity('task_start', 'task_end', 'qty_picked') }}
```

### Inventory Macros

```sql
-- Calculate inventory turnover
{{ wms_inventory_turnover('usage_qty', 'avg_on_hand') }}

-- Determine ABC classification
{{ wms_abc_classification('annual_usage', 'unit_cost') }}

-- Calculate safety stock levels
{{ wms_safety_stock('demand_variance', 'lead_time') }}
```

### Performance Macros

```sql
-- Calculate warehouse KPIs
{{ wms_kpi_calculation('metric_type', 'numerator', 'denominator') }}

-- Determine SLA compliance
{{ wms_sla_compliance('actual_time', 'target_time') }}

-- Calculate labor productivity
{{ wms_labor_productivity('tasks_completed', 'hours_worked') }}
```

## Advanced WMS Models

### Real-Time Inventory Dashboard

```sql
-- models/marts/operational/opr_wms__inventory_realtime.sql
-- Real-time inventory positions with alerts
{{ config(
    materialized='table',
    indexes=['facility_code', 'item_code', 'location'],
    tags=['operational', 'realtime', 'inventory']
) }}

WITH inventory_current AS (
    SELECT
        facility_code,
        item_code,
        location,
        SUM(on_hand_qty) as total_on_hand,
        SUM(allocated_qty) as total_allocated,
        SUM(available_qty) as total_available,
        MAX(last_movement_date) as last_activity,
        COUNT(DISTINCT location) as location_count
    FROM {{ ref('stg_wms__inventory') }}
    WHERE is_active = 'Y'
    GROUP BY facility_code, item_code
),

inventory_metrics AS (
    SELECT
        *,
        {{ wms_inventory_turnover('total_on_hand', 'avg_daily_usage') }} as turnover_rate,
        {{ wms_abc_classification('annual_usage', 'unit_cost') }} as abc_class,
        CASE
            WHEN total_available <= reorder_point THEN 'LOW_STOCK'
            WHEN total_on_hand >= max_stock_level THEN 'OVERSTOCK'
            ELSE 'NORMAL'
        END as stock_status
    FROM inventory_current
    LEFT JOIN {{ ref('stg_wms__item_master') }} USING (item_code)
)

SELECT
    facility_code,
    item_code,
    location,
    total_on_hand,
    total_allocated,
    total_available,
    turnover_rate,
    abc_class,
    stock_status,
    CASE
        WHEN stock_status = 'LOW_STOCK' THEN 'HIGH'
        WHEN stock_status = 'OVERSTOCK' THEN 'MEDIUM'
        ELSE 'LOW'
    END as alert_priority,
    last_activity,
    current_timestamp as report_timestamp
FROM inventory_metrics
```

### WMS Performance Analytics

```sql
-- models/marts/analytical/ana_wms__performance_trends.sql
-- Historical WMS performance analysis
{{ config(
    materialized='table',
    partition_by='business_date',
    tags=['analytical', 'performance', 'trends']
) }}

WITH daily_metrics AS (
    SELECT
        business_date,
        facility_code,

        -- Inbound Performance
        SUM(receipts_processed) as total_receipts,
        AVG(receipt_cycle_time) as avg_receipt_time,
        {{ wms_sla_compliance('receipt_actual_time', 'receipt_target_time') }} as receipt_sla,

        -- Outbound Performance
        SUM(orders_shipped) as total_shipments,
        AVG(order_cycle_time) as avg_fulfillment_time,
        {{ wms_sla_compliance('ship_actual_time', 'ship_target_time') }} as ship_sla,

        -- Labor Performance
        SUM(labor_hours) as total_labor_hours,
        {{ wms_labor_productivity('tasks_completed', 'labor_hours') }} as labor_productivity,

        -- Accuracy Metrics
        AVG(pick_accuracy) as avg_pick_accuracy,
        AVG(cycle_count_accuracy) as avg_count_accuracy

    FROM {{ ref('stg_wms__daily_summary') }}
    WHERE business_date >= CURRENT_DATE - INTERVAL '90' DAY
    GROUP BY business_date, facility_code
),

trending_analysis AS (
    SELECT
        *,
        -- Calculate trends (7-day moving averages)
        AVG(total_receipts) OVER (
            PARTITION BY facility_code
            ORDER BY business_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as receipts_7day_avg,

        AVG(labor_productivity) OVER (
            PARTITION BY facility_code
            ORDER BY business_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as productivity_7day_avg,

        -- Performance scoring
        {{ wms_kpi_calculation('overall_performance',
            'receipt_sla + ship_sla + labor_productivity', '3') }} as performance_score

    FROM daily_metrics
)

SELECT
    business_date,
    facility_code,
    total_receipts,
    receipts_7day_avg,
    total_shipments,
    avg_fulfillment_time,
    receipt_sla,
    ship_sla,
    labor_productivity,
    productivity_7day_avg,
    performance_score,
    CASE
        WHEN performance_score >= 95 THEN 'EXCELLENT'
        WHEN performance_score >= 85 THEN 'GOOD'
        WHEN performance_score >= 75 THEN 'FAIR'
        ELSE 'NEEDS_IMPROVEMENT'
    END as performance_rating,
    current_timestamp as dbt_updated_at
FROM trending_analysis
ORDER BY business_date DESC, facility_code
```

## Quality Standards

### Quality Targets

- **Test Coverage**: 90% Python coverage target for supporting code
- **Type Safety**: MyPy strict mode adoption for Python components
- **Linting**: Ruff with rules (continuous improvement)
- **Security**: Bandit scanning + pip-audit
- **dbt Tests**: Data quality tests should pass before release
- **WMS Business Rules**: Validation tests tracked and improved over time
- **Pre-commit**: Use hooks to automate quality checks

### Code Standards

- **Python 3.13+**: Latest Python with modern type hints
- **Clean Architecture**: Strict layer separation following FLEXT patterns
- **Domain-Driven Design**: Rich domain entities with WMS business logic
- **dbt Best Practices**: Proper layering, testing, and documentation

## Dependencies

### FLEXT Ecosystem Dependencies

- **flext-core**: Base patterns and utilities
- **flext-oracle-wms**: Oracle WMS connectivity and business logic
- **flext-meltano**: dbt/Singer/Meltano integration
- **flext-observability**: Monitoring and logging

### External Dependencies

- **dbt-core**: Data transformation framework
- **dbt-oracle**: Oracle Database adapter
- **dbt-utils**: Utility macros for data transformations

## Troubleshooting

### Common WMS Issues

```bash
# Connection problems
make dbt-debug                   # Check profiles and connections

# WMS-specific validation
make wms-validate               # Validate WMS data integrity

# Performance issues
make wms-performance-report     # Generate performance analysis

# Data quality issues
make wms-data-quality-check     # Check WMS data quality metrics
```

### Quality Gate Failures

```bash
# Fix linting automatically
make format

# Type checking issues
poetry run mypy src/ --show-error-codes

# Security vulnerabilities
poetry run pip-audit --fix

# Test coverage below 90%
make coverage-html              # View detailed coverage report
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-wms-analytics`)
3. Develop and test changes
4. Run quality gates (`make validate`)
5. Update documentation
6. Commit changes (`git commit -m 'Add new WMS analytics model'`)
7. Push to branch (`git push origin feature/new-wms-analytics`)
8. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Documentation

### Architecture & Development

- [CLAUDE.md](CLAUDE.md) - Development guidance and architectural patterns
- [docs/](docs/) - Project documentation

### Generated Documentation

```bash
# Generate and serve dbt docs
dbt docs generate
dbt docs serve --port 8080

# View at: http://localhost:8080
```

### Related Projects

- [flext-core](https://github.com/organization/flext/tree/main/flext-core/) - Foundation library with shared patterns
- [flext-oracle-wms](https://github.com/organization/flext/tree/main/flext-oracle-wms/) - Oracle WMS connectivity infrastructure
- [flext-tap-oracle-wms](https://github.com/organization/flext/tree/main/flext-tap-oracle-wms/) - Singer tap for Oracle WMS data extraction
- [flext-target-oracle-wms](https://github.com/organization/flext/tree/main/flext-target-oracle-wms/) - Singer target for Oracle WMS data loading

### Ecosystem Integration

- [flext-meltano](https://github.com/organization/flext/tree/main/flext-meltano/) - Orchestration platform
- [flext-observability](https://github.com/organization/flext/tree/main/flext-observability/) - Monitoring and logging

---

**Framework**: FLEXT Ecosystem | **Technology**: dbt Core + Oracle WMS | **Architecture**: Clean Architecture + DDD | **Updated**: 2025-08-13
