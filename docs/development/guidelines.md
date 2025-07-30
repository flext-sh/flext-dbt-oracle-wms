# Development Guidelines

**Best Practices for FLEXT DBT Oracle WMS Development**

This guide establishes development standards and best practices for creating and maintaining dbt models in the FLEXT DBT Oracle WMS project.

## 🏗️ Architecture Principles

### Clean Architecture Application

FLEXT DBT Oracle WMS follows **Clean Architecture** principles adapted for data transformations:

#### **Layer Separation**

```
┌─────────────────────────────────────────────────────────┐
│                    Business Intelligence                │
│     (External - Tableau, Power BI, Custom Apps)       │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                   Interface Layer                       │
│              (Metrics & Dashboard Models)               │
│  • met_wms__kpi_dashboard.sql                          │
│  • met_wms__executive_summary.sql                      │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                 Application Layer                       │
│                  (Business Marts)                       │
│  • opr_wms__allocation_summary.sql                     │
│  • ana_wms__inventory_analysis.sql                     │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                  Domain Layer                           │
│                (Staging Models)                         │
│  • stg_wms__allocation.sql                             │
│  • stg_wms__inventory.sql                              │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│              Infrastructure Layer                       │
│           (Raw Data Sources via Singer)                │
│  • Oracle WMS tables via flext-tap-oracle-wms         │
└─────────────────────────────────────────────────────────┘
```

#### **Dependency Rule**

- **Inward Dependencies Only**: Higher layers can depend on lower layers, never the reverse
- **Abstraction Increases Inward**: More abstract/business-focused as you move inward
- **Stable Dependencies**: Lower layers are more stable than higher layers

### Domain-Driven Design (DDD)

#### **Bounded Contexts**

```
WMS Analytics Domain
├── Allocation Context     # Pick/pack operations
├── Inventory Context      # Stock management
├── Order Context         # Order processing
├── Location Context      # Warehouse layout
└── Performance Context   # KPIs and metrics
```

#### **Ubiquitous Language**

Use WMS-specific business terms consistently:

- **Allocation** (not "assignment" or "reservation")
- **Wave** (not "batch" or "group")
- **Pick Location** (not "source location")
- **On-Hand Quantity** (not "available quantity")

## 📁 Project Structure Standards

### Directory Organization

```
models/
├── staging/                    # 🔵 Domain Layer
│   ├── _sources.yml           # Source definitions
│   ├── stg_wms__allocation.sql # Allocation standardization
│   ├── stg_wms__inventory.sql  # Inventory standardization
│   ├── stg_wms__order_hdr.sql  # Order header standardization
│   ├── stg_wms__order_dtl.sql  # Order detail standardization
│   └── schema.yml             # Staging tests and docs
│
├── marts/                      # 🟢 Application Layer
│   ├── operational/           # Real-time operational metrics
│   │   ├── opr_wms__allocation_summary.sql
│   │   ├── opr_wms__inventory_positions.sql
│   │   └── schema.yml
│   ├── analytical/            # Historical analysis models
│   │   ├── ana_wms__inventory_analysis.sql
│   │   ├── ana_wms__order_fulfillment.sql
│   │   └── schema.yml
│   └── metrics/               # 📊 Interface Layer
│       ├── met_wms__kpi_dashboard.sql
│       ├── met_wms__executive_summary.sql
│       └── schema.yml
│
├── intermediate/               # 🟡 Internal transformations
│   ├── int_wms__allocation_enriched.sql
│   └── schema.yml
│
└── analyses/                   # 🟠 Ad-hoc analysis
    ├── allocation_deep_dive.sql
    └── inventory_trend_analysis.sql
```

### File Naming Conventions

#### **Model Names**

```sql
-- Pattern: {layer}_{source}__{entity}[__{purpose}]

-- Staging models (standardization)
stg_wms__allocation.sql           -- Standard allocation data
stg_wms__inventory.sql            -- Standard inventory data
stg_wms__order_hdr.sql           -- Standard order headers

-- Intermediate models (internal logic)
int_wms__allocation_enriched.sql  -- Enriched allocation data
int_wms__order_summary.sql       -- Order aggregations

-- Mart models (business-ready)
opr_wms__allocation_summary.sql   -- Operational allocation summary
ana_wms__inventory_analysis.sql   -- Analytical inventory analysis
met_wms__kpi_dashboard.sql        -- Metrics for dashboards
```

#### **File Organization Rules**

- **One model per file** - Each `.sql` file contains exactly one model
- **Consistent prefixes** - Use standard layer prefixes (`stg_`, `int_`, `opr_`, `ana_`, `met_`)
- **Descriptive names** - Model names should clearly indicate purpose
- **No abbreviations** - Use full words for clarity (`allocation` not `alloc`)

## 🎯 Model Development Standards

### Model Configuration

#### **Standard Configuration Template**

```sql
{{
  config(
    materialized='table',                    -- table, view, or incremental
    tags=['marts', 'operational', 'wms'],   -- for selective runs
    schema='wms_marts',                     -- target schema override
    alias='allocation_summary',             -- table name override
    pre_hook='{{ create_audit_log() }}',    -- pre-execution hooks
    post_hook='{{ update_model_stats() }}', -- post-execution hooks

    -- Performance optimizations
    partition_by='business_date',           -- Oracle partitioning
    cluster_by=['company_code', 'facility_code'], -- Oracle clustering

    -- Data quality
    on_schema_change='fail',                -- Fail on schema changes
    full_refresh=false,                     -- Prevent accidental full refresh

    -- Documentation
    description='Operational allocation summary for real-time dashboards'
  )
}}
```

#### **Materialization Strategy**

```yaml
# dbt_project.yml model configurations
models:
  flext_dbt_oracle_wms:
    staging:
      +materialized: view # Real-time, minimal transformation
      +schema: wms_staging

    intermediate:
      +materialized: view # Internal logic, not persisted
      +schema: wms_intermediate

    marts:
      operational:
        +materialized: table # Performance for real-time dashboards
        +schema: wms_operational

      analytical:
        +materialized: table # Complex historical analysis
        +schema: wms_analytical

      metrics:
        +materialized: view # Always current, computed from marts
        +schema: wms_metrics
```

### SQL Code Standards

#### **Model Structure Template**

```sql
{{
  config(
    materialized='table',
    tags=['operational', 'allocation', 'wms'],
    schema='wms_operational'
  )
}}

-- Dependencies and CTEs
WITH allocation_base AS (
  SELECT * FROM {{ ref('stg_wms__allocation') }}
),

allocation_metrics AS (
  SELECT
    wave_id,
    facility_code,
    COUNT(*) as total_allocations,
    SUM(allocated_quantity) as total_quantity,
    AVG(allocated_quantity) as avg_quantity_per_allocation
  FROM allocation_base
  WHERE business_date = CURRENT_DATE
  GROUP BY wave_id, facility_code
),

-- Final transformation
final AS (
  SELECT
    -- Primary keys and identifiers
    wave_id,
    facility_code,

    -- Business metrics
    total_allocations,
    total_quantity,
    avg_quantity_per_allocation,

    -- Calculated fields
    ROUND(total_quantity / NULLIF(total_allocations, 0), 2) as avg_quantity_calc,

    -- Audit fields
    CURRENT_TIMESTAMP as model_updated_at,
    '{{ run_started_at }}' as dbt_run_started_at

  FROM allocation_metrics
  WHERE total_allocations > 0  -- Data quality filter
)

SELECT * FROM final
```

#### **SQL Formatting Rules**

```sql
-- ✅ GOOD: Consistent formatting and structure
SELECT
    -- Primary identifiers
    allocation_id,
    company_code,
    facility_code,

    -- Business fields
    allocated_quantity,
    packed_quantity,

    -- Calculated fields
    CASE
        WHEN packed_quantity >= allocated_quantity THEN 'COMPLETE'
        WHEN packed_quantity > 0 THEN 'PARTIAL'
        ELSE 'PENDING'
    END as pack_status,

    -- Audit fields
    created_timestamp,
    modified_timestamp

FROM {{ ref('stg_wms__allocation') }}
WHERE company_code = '001'
  AND facility_code = 'DC001'
  AND business_date >= CURRENT_DATE - 7
ORDER BY created_timestamp DESC

-- ❌ BAD: Inconsistent formatting
SELECT allocation_id,company_code,allocated_quantity,CASE WHEN packed_quantity>=allocated_quantity THEN 'COMPLETE' ELSE 'PENDING' END pack_status FROM {{ ref('stg_wms__allocation') }} WHERE company_code='001'
```

#### **CTE (Common Table Expression) Standards**

```sql
-- Use CTEs for complex logic breakdown
WITH allocation_base AS (
  -- Base data selection with filters
  SELECT *
  FROM {{ ref('stg_wms__allocation') }}
  WHERE business_date >= '{{ var("start_date") }}'
),

allocation_enriched AS (
  -- Add business logic and enrichments
  SELECT
    a.*,
    o.order_number,
    i.item_description
  FROM allocation_base a
  LEFT JOIN {{ ref('stg_wms__order_hdr') }} o
    ON a.order_hdr_id = o.order_hdr_id
  LEFT JOIN {{ ref('stg_wms__item') }} i
    ON a.item_id = i.item_id
),

allocation_metrics AS (
  -- Calculate business metrics
  SELECT
    *,
    allocated_quantity - COALESCE(packed_quantity, 0) as remaining_quantity
  FROM allocation_enriched
)

-- Final selection
SELECT * FROM allocation_metrics
```

### Business Logic Implementation

#### **WMS-Specific Calculations**

```sql
-- Allocation completion rate
CASE
  WHEN allocated_quantity = 0 THEN 0
  ELSE ROUND(
    COALESCE(packed_quantity, 0) / allocated_quantity * 100,
    2
  )
END as completion_rate_percent,

-- Available inventory calculation
on_hand_quantity - COALESCE(allocated_quantity, 0) as available_quantity,

-- Wave efficiency metrics
COUNT(*) OVER (PARTITION BY wave_id) as allocations_in_wave,
SUM(allocated_quantity) OVER (PARTITION BY wave_id) as wave_total_quantity,

-- Order fulfillment status
CASE
  WHEN SUM(shipped_quantity) >= SUM(ordered_quantity) THEN 'FULFILLED'
  WHEN SUM(shipped_quantity) > 0 THEN 'PARTIAL'
  ELSE 'PENDING'
END as fulfillment_status
```

#### **Data Quality and Validation**

```sql
-- Add data quality indicators
CASE
  WHEN company_code IS NULL OR facility_code IS NULL
    THEN 'MISSING_REQUIRED_FIELDS'
  WHEN allocated_quantity < 0
    THEN 'NEGATIVE_QUANTITY'
  WHEN packed_quantity > allocated_quantity
    THEN 'OVERPACK'
  WHEN picked_timestamp > modified_timestamp
    THEN 'INVALID_TIMESTAMP_ORDER'
  ELSE 'VALID'
END as data_quality_status,

-- Generate surrogate keys for dimensional modeling
{{ dbt_utils.generate_surrogate_key([
  'company_code',
  'facility_code',
  'allocation_id'
]) }} as allocation_sk
```

## 🧪 Testing Standards

### Test Categories

#### **1. Schema Tests (Built-in dbt)**

```yaml
# models/staging/schema.yml
models:
  - name: stg_wms__allocation
    description: "Standardized Oracle WMS allocation data"
    tests:
      - unique:
          column_name: allocation_id
      - not_null:
          column_name: allocation_id

    columns:
      - name: company_code
        description: "Company identifier"
        tests:
          - not_null
          - accepted_values:
              values: ["001", "002", "003"]

      - name: allocated_quantity
        description: "Quantity allocated for picking"
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 999999
              inclusive: true
```

#### **2. Custom Business Rule Tests**

```sql
-- tests/business_rules/test_allocation_quantity_logic.sql
-- Description: Allocated quantity should not exceed ordered quantity
SELECT *
FROM {{ ref('stg_wms__allocation') }} a
JOIN {{ ref('stg_wms__order_dtl') }} o
  ON a.order_dtl_id = o.order_dtl_id
WHERE a.allocated_quantity > o.ordered_quantity
```

#### **3. Data Quality Tests**

```sql
-- tests/data_quality/test_inventory_consistency.sql
-- Description: Available quantity should equal on-hand minus allocated
SELECT *
FROM {{ ref('stg_wms__inventory') }}
WHERE available_quantity != (on_hand_quantity - COALESCE(allocated_quantity, 0))
```

#### **4. Performance Tests**

```sql
-- tests/performance/test_model_row_count.sql
-- Description: Ensure reasonable data volumes
{{ config(severity='warn') }}

SELECT
  '{{ this }}' as model_name,
  COUNT(*) as row_count,
  CURRENT_TIMESTAMP as test_timestamp
FROM {{ this }}
HAVING COUNT(*) > 10000000  -- Warn if over 10M rows
```

### Test Execution Strategy

#### **Development Testing**

```bash
# Test individual model during development
dbt test --select stg_wms__allocation

# Test model and its dependencies
dbt test --select +stg_wms__allocation

# Test specific test types
dbt test --select "test_type:schema"
dbt test --select "test_type:data"
```

#### **CI/CD Testing**

```bash
# Full test suite for CI/CD
dbt test --store-failures

# Critical tests only (for fast feedback)
dbt test --select "tag:critical"

# Business rule tests
dbt test --select "path:tests/business_rules"
```

## 📊 Documentation Standards

### Model Documentation

#### **Model Description Template**

```yaml
# models/staging/schema.yml
models:
  - name: stg_wms__allocation
    description: |
      Standardized Oracle WMS allocation data for pick and pack operations.

      This model performs the following transformations:
      - Standardizes data types and formats from raw Oracle WMS data
      - Applies business rules and data quality validation
      - Generates surrogate keys for dimensional modeling
      - Adds audit fields and data quality indicators

      **Business Context**: 
      Allocations represent the assignment of inventory to fulfill order requirements.
      They drive the picking process and track fulfillment progress through the warehouse.

      **Data Sources**: 
      - oracle_wms_raw.allocation (via Singer tap-oracle-wms)

      **Update Frequency**: Real-time via view materialization

      **Data Quality**: 95%+ completeness required for operational dashboards

    columns:
      - name: allocation_id
        description: |
          Unique identifier for the allocation record.
          Format: Alphanumeric, typically 10-12 characters.
          Example: 'ALLOC123456'
        tests:
          - unique
          - not_null

      - name: allocated_quantity
        description: |
          Quantity of the item allocated for picking.
          Business Rule: Must be > 0 and <= ordered_quantity.
          Unit: Matches item's primary UOM.
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 999999
```

#### **Inline Comments**

```sql
-- Model: Operational allocation summary for real-time dashboards
-- Purpose: Provides wave-level allocation metrics for warehouse operations
-- Update: Every 15 minutes via incremental processing

{{ config(materialized='table') }}

WITH allocation_base AS (
  -- Source: Standardized allocation data from staging layer
  -- Filter: Last 30 days for operational relevance
  SELECT *
  FROM {{ ref('stg_wms__allocation') }}
  WHERE business_date >= CURRENT_DATE - 30
),

wave_metrics AS (
  -- Business Logic: Calculate key performance indicators per wave
  -- Metrics: Completion rates, productivity, and exception tracking
  SELECT
    wave_id,
    facility_code,

    -- Volume metrics
    COUNT(*) as total_allocations,
    COUNT(CASE WHEN packed_quantity >= allocated_quantity THEN 1 END) as completed_allocations,

    -- Performance calculation: Pick completion rate
    ROUND(
      COUNT(CASE WHEN packed_quantity >= allocated_quantity THEN 1 END) * 100.0 /
      NULLIF(COUNT(*), 0),
      2
    ) as completion_rate_percent

  FROM allocation_base
  GROUP BY wave_id, facility_code
)

SELECT * FROM wave_metrics
```

### Documentation Generation

#### **Automated Documentation**

```bash
# Generate comprehensive documentation
dbt docs generate --profiles-dir profiles

# Include source freshness information
dbt docs generate --profiles-dir profiles --include-sources

# Serve documentation locally
dbt docs serve --profiles-dir profiles --port 8080
```

#### **Custom Documentation Blocks**

```markdown
<!-- docs/allocation_business_rules.md -->

{% docs allocation_business_rules %}

## Allocation Business Rules

### Quantity Validation

- Allocated quantity must be positive
- Allocated quantity cannot exceed ordered quantity
- Packed quantity cannot exceed allocated quantity

### Status Progression

Valid status transitions:

- CREATED → RELEASED → PICKING → PICKED → PACKED → SHIPPED
- Any status → CANCELLED (exception handling)

### Wave Assignment

- All allocations must belong to a valid wave
- Wave status must allow allocation modifications
- Cross-wave allocations are not permitted

{% enddocs %}
```

## 🚀 Performance Optimization

### Oracle-Specific Optimizations

#### **Partitioning Strategy**

```sql
-- Large fact tables partitioned by business date
{{
  config(
    materialized='table',
    partition_by='business_date',
    cluster_by=['company_code', 'facility_code', 'wave_id']
  )
}}

-- Partition pruning in queries
SELECT *
FROM {{ ref('opr_wms__allocation_summary') }}
WHERE business_date = CURRENT_DATE  -- Enables partition pruning
```

#### **Incremental Processing**

```sql
-- Incremental models for large datasets
{{
  config(
    materialized='incremental',
    unique_key='allocation_id',
    on_schema_change='fail',
    partition_by='business_date'
  )
}}

SELECT
  allocation_id,
  business_date,
  allocated_quantity,
  modified_timestamp
FROM {{ ref('stg_wms__allocation') }}

{% if is_incremental() %}
  -- Process only new/changed records
  WHERE modified_timestamp > (
    SELECT MAX(modified_timestamp)
    FROM {{ this }}
  )
{% endif %}
```

#### **Query Optimization**

```sql
-- Oracle-specific performance hints
SELECT /*+ USE_HASH(a,o) PARALLEL(4) FIRST_ROWS(1000) */
  a.allocation_id,
  o.order_number,
  a.allocated_quantity
FROM {{ ref('stg_wms__allocation') }} a
JOIN {{ ref('stg_wms__order_hdr') }} o
  ON a.order_hdr_id = o.order_hdr_id
WHERE a.business_date >= CURRENT_DATE - 7
  AND a.facility_code = 'DC001'  -- Leverage clustering
```

### Model Performance Guidelines

#### **Avoid Anti-Patterns**

```sql
-- ❌ BAD: Expensive operations in WHERE clause
SELECT *
FROM {{ ref('stg_wms__allocation') }}
WHERE UPPER(facility_code) = 'DC001'  -- Function in WHERE prevents index usage

-- ✅ GOOD: Index-friendly filtering
SELECT *
FROM {{ ref('stg_wms__allocation') }}
WHERE facility_code = 'DC001'

-- ❌ BAD: Unnecessary subqueries
SELECT a.*
FROM {{ ref('stg_wms__allocation') }} a
WHERE allocation_id IN (
  SELECT allocation_id
  FROM {{ ref('stg_wms__allocation') }}
  WHERE packed_quantity > 0
)

-- ✅ GOOD: Direct filtering
SELECT *
FROM {{ ref('stg_wms__allocation') }}
WHERE packed_quantity > 0
```

## 🔄 Development Workflow

### Local Development Process

#### **1. Environment Setup**

```bash
# Setup development environment
make dev-install

# Setup pre-commit hooks
make pre-commit

# Test connection
dbt debug --profiles-dir profiles --target dev
```

#### **2. Model Development Cycle**

```bash
# Create new model
touch models/staging/stg_wms__new_entity.sql

# Develop model iteratively
dbt run --select stg_wms__new_entity --target dev

# Test as you develop
dbt test --select stg_wms__new_entity --target dev

# Check compiled SQL
dbt compile --select stg_wms__new_entity
cat target/compiled/flext_dbt_oracle_wms/models/staging/stg_wms__new_entity.sql
```

#### **3. Quality Gates**

```bash
# Run all quality checks before committing
make validate

# Individual quality checks
make lint        # SQL and Python linting
make type-check  # Type checking
make security    # Security scans
make test        # All tests including dbt
```

### Git Workflow

#### **Branch Strategy**

```bash
# Feature development
git checkout -b feature/new-allocation-metrics
git add models/marts/operational/opr_wms__allocation_metrics.sql
git commit -m "feat: add allocation performance metrics model"

# Quality validation
make validate

# Push and create PR
git push origin feature/new-allocation-metrics
# Create PR with description and test results
```

#### **Commit Message Standards**

```bash
# Format: type(scope): description
feat(allocation): add real-time allocation dashboard model
fix(inventory): correct available quantity calculation logic
docs(setup): update Oracle connection configuration guide
test(business-rules): add order fulfillment validation tests
perf(marts): optimize allocation summary query performance
```

### Code Review Guidelines

#### **Review Checklist**

- **Model Logic**: Business rules correctly implemented
- **Performance**: Efficient SQL and appropriate materialization
- **Testing**: Adequate test coverage (>90% for business logic)
- **Documentation**: Clear descriptions and inline comments
- **Standards**: Follows naming conventions and code style
- **Dependencies**: Appropriate model references and layering

#### **Review Focus Areas**

1. **Business Accuracy** - Verify WMS business logic
2. **Data Quality** - Check validation rules and error handling
3. **Performance** - Review query efficiency and materialization
4. **Maintainability** - Assess code clarity and documentation
5. **Testing** - Ensure comprehensive test coverage

## 📚 Additional Resources

### dbt Resources

- **[dbt Style Guide](https://github.com/dbt-labs/corp/blob/main/dbt_style_guide.md)** - Official dbt style guide
- **[dbt Best Practices](https://docs.getdbt.com/guides/best-practices)** - dbt development best practices
- **[dbt Oracle Adapter](https://github.com/oracle/dbt-oracle)** - Oracle-specific documentation

### Oracle WMS Resources

- **[Oracle WMS Documentation](https://docs.oracle.com/en/industries/food-beverage/wms/)** - Official Oracle WMS docs
- **[WMS Data Model](../integration/oracle-wms.md)** - FLEXT WMS integration guide

### FLEXT Framework

- **[Clean Architecture Guide](../../flext-core/docs/architecture/clean-architecture.md)** - Clean Architecture principles
- **[Domain-Driven Design](../../flext-core/docs/architecture/domain-driven-design.md)** - DDD implementation patterns

---

Following these development guidelines ensures consistent, high-quality, and maintainable dbt models for Oracle WMS analytics. For specific implementation examples, see the [Examples](../examples/basic.md) section.
