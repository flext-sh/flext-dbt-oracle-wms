# Model Reference

<!-- TOC START -->

- [📊 Model Architecture Overview](#model-architecture-overview)
- [🔵 Staging Models](#staging-models)
  - [stg_wms\_\_allocation](#stgwmsallocation)
  - [stg_wms\_\_inventory](#stgwmsinventory)
  - [stg_wms\_\_order_hdr](#stgwmsorderhdr)
  - [stg_wms\_\_order_dtl](#stgwmsorderdtl)
- [🟢 Mart Models](#mart-models)
  - [marts/operational/opr_wms\_\_allocation_summary](#martsoperationaloprwmsallocationsummary)
  - [marts/analytical/ana_wms\_\_inventory_analysis](#martsanalyticalanawmsinventoryanalysis)
  - [marts/metrics/met_wms\_\_kpi_dashboard](#martsmetricsmetwmskpidashboard)
- [🔗 Model Dependencies](#model-dependencies)
  - [Dependency Graph](#dependency-graph)
- [📈 Performance Considerations](#performance-considerations)
  - [Materialization Strategy](#materialization-strategy)
  - [Incremental Processing](#incremental-processing)
  - [Partitioning Strategy](#partitioning-strategy)
- [🧪 Testing Strategy](#testing-strategy)
  - [Data Quality Tests](#data-quality-tests)
  - [Performance Tests](#performance-tests)
- [📊 Usage Patterns](#usage-patterns)
  - [Common Query Patterns](#common-query-patterns)
- [🔄 Data Refresh Strategy](#data-refresh-strategy)
  - [Refresh Schedule](#refresh-schedule)
  - [Refresh Commands](#refresh-commands)
- [📚 Documentation](#documentation)
  - [Model Documentation](#model-documentation)
  - [Automated Documentation Generation](#automated-documentation-generation)

<!-- TOC END -->

**Complete Data Model Documentation for FLEXT DBT Oracle WMS**

This reference provides comprehensive documentation for all data models in the FLEXT DBT Oracle WMS project, including staging models, mart models, and their relationships.

## 📊 Model Architecture Overview

```
Data Flow Architecture:
Oracle WMS Raw → Staging Models → Mart Models → Business Intelligence

Model Layers:
┌─────────────────────────────────────────────────────────┐
│                    Mart Models                          │
│  Business-ready analytics and reporting models         │
│  • Operational (Real-time dashboards)                  │
│  • Analytical (Historical analysis)                    │
│  • Metrics (KPIs and executive dashboards)             │
└─────────────────────┬───────────────────────────────────┘
                      │ Depends on
┌─────────────────────▼───────────────────────────────────┐
│                 Staging Models                          │
│  Standardized and cleansed WMS entity data             │
│  • Data type normalization                             │
│  • Business rule application                           │
│  • Data quality validation                             │
└─────────────────────┬───────────────────────────────────┘
                      │ Sources from
┌─────────────────────▼───────────────────────────────────┐
│                Source Tables                            │
│  Raw Oracle WMS data via Singer tap                    │
│  • Allocation, Inventory, Orders, Tasks, etc.          │
└─────────────────────────────────────────────────────────┘
```

## 🔵 Staging Models

Staging models standardize and cleanse raw Oracle WMS data for downstream consumption.

### stg_wms\_\_allocation

**Purpose**: Standardizes Oracle WMS allocation data for pick and pack operations.

**Materialization**: View\
**Schema**: `wms_staging`\
**Tags**: `["staging", "allocation", "oracle_wms"]`

#### Columns

| Column                 | Type          | Description                    | Business Logic                     |
| ---------------------- | ------------- | ------------------------------ | ---------------------------------- |
| `allocation_id`        | STRING        | Primary allocation identifier  | Direct from source `id`            |
| `company_code`         | STRING        | Company identifier             | Required field validation          |
| `facility_code`        | STRING        | Facility/warehouse identifier  | Required field validation          |
| `order_dtl_id`         | STRING        | Reference to order detail      | Foreign key to order details       |
| `from_inventory_id`    | STRING        | Source inventory location      | Pick location reference            |
| `to_inventory_id`      | STRING        | Destination inventory location | Put-away location reference        |
| `allocated_quantity`   | DECIMAL(15,4) | Quantity allocated for picking | Cast to decimal, default 0 if null |
| `packed_quantity`      | DECIMAL(15,4) | Quantity packed/completed      | Cast to decimal, default 0 if null |
| `allocation_status_id` | STRING        | Status code for allocation     | Reference to status master         |
| `allocation_type_id`   | STRING        | Type of allocation             | Reference to type master           |
| `wave_id`              | STRING        | Wave planning identifier       | Wave management reference          |
| `task_id`              | STRING        | Associated task identifier     | Work task reference                |
| `task_sequence_number` | INTEGER       | Task sequence in wave          | Ordering within wave               |
| `allocation_uom_id`    | STRING        | Unit of measure for allocation | UOM reference                      |
| `pick_location_string` | STRING        | Human-readable pick location   | Location display format            |
| `is_picking_flag`      | BOOLEAN       | Indicates if currently picking | Y/N to boolean conversion          |
| `picked_timestamp`     | TIMESTAMP     | When allocation was picked     | Cast to timestamp                  |
| `created_timestamp`    | TIMESTAMP     | Record creation time           | Audit field                        |
| `modified_timestamp`   | TIMESTAMP     | Last modification time         | Audit field                        |
| `data_quality_status`  | STRING        | Data quality indicator         | Business rule validation           |
| `business_date`        | DATE          | Business processing date       | Derived from timestamps            |
| `allocation_sk`        | STRING        | Surrogate key for dimensions   | Generated hash key                 |
| `row_hash`             | STRING        | Row-level change detection     | Change data capture                |

#### Business Rules

```sql
-- Data Quality Validation
CASE
    WHEN company_code IS NULL OR facility_code IS NULL
        THEN 'MISSING_REQUIRED_FIELDS'
    WHEN allocated_quantity < 0
        THEN 'NEGATIVE_QUANTITY'
    WHEN picked_timestamp > modified_timestamp
        THEN 'INVALID_TIMESTAMP_ORDER'
    ELSE 'VALID'
END as data_quality_status
```

#### Usage Example

```sql
-- Get allocations for a specific wave
SELECT
    allocation_id,
    order_dtl_id,
    allocated_quantity,
    packed_quantity,
    allocation_status_id,
    pick_location_string,
    picked_timestamp
FROM {{ ref('stg_wms__allocation') }}
WHERE wave_id = 'WAVE_12345'
    AND data_quality_status = 'VALID'
ORDER BY task_sequence_number;
```

### stg_wms\_\_inventory

**Purpose**: Standardizes Oracle WMS inventory position data.

**Materialization**: View\
**Schema**: `wms_staging`\
**Tags**: `["staging", "inventory", "oracle_wms"]`

#### Key Features

- Real-time inventory position tracking
- Location-based inventory management
- UOM and packaging standardization
- Lot and serial number handling
- Inventory status classification

#### Columns

| Column                | Type          | Description                  | Business Logic              |
| --------------------- | ------------- | ---------------------------- | --------------------------- |
| `inventory_id`        | STRING        | Primary inventory identifier | Direct from source          |
| `company_code`        | STRING        | Company identifier           | Required validation         |
| `facility_code`       | STRING        | Facility identifier          | Required validation         |
| `item_id`             | STRING        | Item master reference        | Foreign key to items        |
| `location_id`         | STRING        | Storage location identifier  | Physical location reference |
| `lot_number`          | STRING        | Lot/batch identifier         | Traceability tracking       |
| `serial_number`       | STRING        | Serial number                | Individual item tracking    |
| `on_hand_quantity`    | DECIMAL(15,4) | Available quantity           | Physical inventory          |
| `allocated_quantity`  | DECIMAL(15,4) | Allocated/reserved quantity  | Committed inventory         |
| `available_quantity`  | DECIMAL(15,4) | Available for allocation     | Calculated field            |
| `inventory_status_id` | STRING        | Status classification        | Available, damaged, etc.    |
| `uom_id`              | STRING        | Unit of measure              | Inventory UOM               |
| `received_timestamp`  | TIMESTAMP     | When inventory was received  | Receipt date                |
| `expiration_date`     | DATE          | Product expiration date      | Quality management          |

#### Business Rules

```sql
-- Calculate available quantity
on_hand_quantity - COALESCE(allocated_quantity, 0) as available_quantity

-- Inventory classification
CASE
    WHEN available_quantity > 0 THEN 'AVAILABLE'
    WHEN on_hand_quantity > 0 AND allocated_quantity >= on_hand_quantity THEN 'ALLOCATED'
    WHEN on_hand_quantity = 0 THEN 'OUT_OF_STOCK'
    ELSE 'UNKNOWN'
END as inventory_classification
```

### stg_wms\_\_order_hdr

**Purpose**: Standardizes Oracle WMS order header information.

**Materialization**: View\
**Schema**: `wms_staging`\
**Tags**: `["staging", "orders", "oracle_wms"]`

#### Key Features

- Customer order management
- Shipping and billing information
- Order lifecycle tracking
- Priority and service level handling

### stg_wms\_\_order_dtl

**Purpose**: Standardizes Oracle WMS order detail/line information.

**Materialization**: View\
**Schema**: `wms_staging`\
**Tags**: `["staging", "orders", "oracle_wms"]`

#### Key Features

- Order line item details
- Item quantities and specifications
- Fulfillment tracking
- Shipment preparation data

## 🟢 Mart Models

Mart models provide business-ready data for analytics and reporting.

### marts/operational/opr_wms\_\_allocation_summary

**Purpose**: Real-time allocation summary for operational dashboards.

**Materialization**: Table\
**Schema**: `wms_marts`\
**Tags**: `["marts", "operational", "allocation", "real_time"]`

#### Features

- Wave-level allocation summaries
- Pick rate and productivity metrics
- Exception and bottleneck monitoring
- Real-time operational KPIs

#### Key Metrics

| Metric                | Description               | Calculation                                   |
| --------------------- | ------------------------- | --------------------------------------------- |
| `total_allocations`   | Total allocations in wave | COUNT(\*)                                     |
| `picked_allocations`  | Completed picks           | COUNT() WHERE picked_timestamp IS NOT NULL    |
| `pick_rate_percent`   | Pick completion rate      | picked_allocations / total_allocations \* 100 |
| `avg_pick_time`       | Average time per pick     | AVG(picked_timestamp - created_timestamp)     |
| `pending_allocations` | Outstanding picks         | total_allocations - picked_allocations        |

#### Usage Example

```sql
-- Operational dashboard query
SELECT
    wave_id,
    facility_code,
    total_allocations,
    picked_allocations,
    pick_rate_percent,
    avg_pick_time_minutes,
    pending_allocations,
    last_updated
FROM {{ ref('opr_wms__allocation_summary') }}
WHERE business_date = CURRENT_DATE
    AND pick_rate_percent < 90  -- Focus on underperforming waves
ORDER BY pick_rate_percent ASC;
```

### marts/analytical/ana_wms\_\_inventory_analysis

**Purpose**: Historical inventory analysis for strategic planning.

**Materialization**: Table\
**Schema**: `wms_marts`\
**Tags**: `["marts", "analytical", "inventory", "historical"]`

#### Features

- Inventory trend analysis
- ABC classification and velocity analysis
- Seasonal pattern identification
- Space utilization analytics

#### Key Dimensions

- **Time**: Daily, weekly, monthly aggregations
- **Product**: Item, category, ABC classification
- **Location**: Zone, aisle, location type
- **Status**: Available, allocated, damaged inventory · 1.0.0 Release Preparation

### marts/metrics/met_wms\_\_kpi_dashboard

**Purpose**: Executive KPI dashboard for warehouse performance.

**Materialization**: View\
**Schema**: `wms_metrics`\
**Tags**: `["metrics", "kpi", "dashboard", "executive"]`

#### Key Performance Indicators

| KPI Category      | Metrics                                     |
| ----------------- | ------------------------------------------- |
| **Productivity**  | Orders/hour, Lines/hour, Pick rate          |
| **Accuracy**      | Pick accuracy %, Inventory accuracy %       |
| **Utilization**   | Space utilization %, Labor utilization %    |
| **Service Level** | On-time shipment %, Order cycle time        |
| **Cost**          | Cost per order, Cost per line, Labor cost % |

## 🔗 Model Dependencies

### Dependency Graph

```
Staging Layer:
├── stg_wms__allocation
├── stg_wms__inventory
├── stg_wms__order_hdr
└── stg_wms__order_dtl

Operational Marts:
├── opr_wms__allocation_summary
│   └── depends_on: stg_wms__allocation
└── opr_wms__inventory_positions
    └── depends_on: stg_wms__inventory

Analytical Marts:
├── ana_wms__inventory_analysis
│   ├── depends_on: stg_wms__inventory
│   └── depends_on: stg_wms__order_dtl
└── ana_wms__order_fulfillment
    ├── depends_on: stg_wms__order_hdr
    ├── depends_on: stg_wms__order_dtl
    └── depends_on: stg_wms__allocation

Metrics:
└── met_wms__kpi_dashboard
    ├── depends_on: opr_wms__allocation_summary
    ├── depends_on: opr_wms__inventory_positions
    └── depends_on: ana_wms__order_fulfillment
```

## 📈 Performance Considerations

### Materialization Strategy

| Model Type            | Materialization | Rationale                                     |
| --------------------- | --------------- | --------------------------------------------- |
| **Staging**           | View            | Real-time data access, minimal transformation |
| **Operational Marts** | Table           | Performance for dashboards, frequent queries  |
| **Analytical Marts**  | Table           | Complex transformations, historical data      |
| **Metrics**           | View            | Aggregated from marts, always current         |

### Incremental Processing

Large models use incremental materialization:

```sql
{{
  config(
    materialized='incremental',
    unique_key='allocation_id',
    on_schema_change='fail'
  )
}}

SELECT * FROM {{ ref('stg_wms__allocation') }}

{% if is_incremental() %}
  WHERE modified_timestamp > (
    SELECT MAX(modified_timestamp) FROM {{ this }}
  )
{% endif %}
```

### Partitioning Strategy

```sql
{{
  config(
    materialized='table',
    partition_by='business_date',
    cluster_by=['company_code', 'facility_code']
  )
}}
```

## 🧪 Testing Strategy

### Data Quality Tests

#### Schema Tests (models/staging/schema.yml)

```yaml
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
        tests:
          - not_null
          - accepted_values:
              values: ["001", "002", "003"]

      - name: allocated_quantity
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 999999
```

#### Custom Business Rule Tests

```sql
-- tests/staging/test_allocation_business_rules.sql
-- Test: Allocated quantity should not exceed ordered quantity
SELECT *
FROM {{ ref('stg_wms__allocation') }} a
JOIN {{ ref('stg_wms__order_dtl') }} o
  ON a.order_dtl_id = o.order_dtl_id
WHERE a.allocated_quantity > o.ordered_quantity
```

### Performance Tests

```sql
-- tests/performance/test_model_execution_time.sql
-- Ensure models complete within acceptable time limits
{% set start_time = run_started_at %}

SELECT
  '{{ this }}' as model_name,
  CURRENT_TIMESTAMP as test_timestamp,
  CURRENT_TIMESTAMP - TIMESTAMP '{{ start_time }}' as execution_duration
HAVING execution_duration > INTERVAL '10 minutes'
```

## 📊 Usage Patterns

### Common Query Patterns

#### Real-time Operational Queries

```sql
-- Current wave status
SELECT
    w.wave_id,
    w.status,
    COUNT(*) as total_allocations,
    SUM(CASE WHEN a.picked_timestamp IS NOT NULL THEN 1 ELSE 0 END) as picked,
    AVG(a.allocated_quantity) as avg_quantity
FROM {{ ref('stg_wms__allocation') }} a
JOIN {{ ref('stg_wms__wave') }} w ON a.wave_id = w.wave_id
WHERE w.status IN ('RELEASED', 'PICKING')
GROUP BY w.wave_id, w.status;
```

#### Historical Analysis Queries

```sql
-- Monthly inventory trends
SELECT
    DATE_TRUNC('month', business_date) as month,
    item_category,
    AVG(on_hand_quantity) as avg_inventory,
    SUM(allocated_quantity) as total_allocated
FROM {{ ref('ana_wms__inventory_analysis') }}
WHERE business_date >= CURRENT_DATE - INTERVAL '12 months'
GROUP BY 1, 2
ORDER BY 1, 2;
```

#### Executive Dashboard Queries

```sql
-- Executive KPI summary
SELECT
    kpi_category,
    kpi_name,
    kpi_value,
    target_value,
    CASE
        WHEN kpi_value >= target_value THEN 'ABOVE_TARGET'
        WHEN kpi_value >= target_value * 0.9 THEN 'NEAR_TARGET'
        ELSE 'BELOW_TARGET'
    END as performance_status
FROM {{ ref('met_wms__kpi_dashboard') }}
WHERE report_date = CURRENT_DATE
ORDER BY kpi_category, kpi_name;
```

## 🔄 Data Refresh Strategy

### Refresh Schedule

| Model Layer     | Refresh Frequency | Method               |
| --------------- | ----------------- | -------------------- |
| **Staging**     | Real-time         | View materialization |
| **Operational** | Every 15 minutes  | Incremental dbt run  |
| **Analytical**  | Daily             | Full refresh         |
| **Metrics**     | Hourly            | View re-computation  |

### Refresh Commands

```bash
# Incremental refresh (operational models)
dbt run --select marts.operational --incremental

# Daily refresh (analytical models)
dbt run --select marts.analytical --full-refresh

# Emergency full refresh
dbt run --full-refresh --select staging marts
```

## 📚 Documentation

### Model Documentation

Each model includes comprehensive documentation:

```yaml
# models/staging/schema.yml
models:
  - name: stg_wms__allocation
    description: |
      Standardized Oracle WMS allocation data for pick and pack operations.

      This model performs the following transformations:
      - Standardizes data types and formats
      - Applies business rules and validation
      - Generates surrogate keys for dimensional modeling
      - Adds data quality indicators

      **Business Context**: 
      Allocations represent the assignment of inventory to fulfill order requirements.
      They drive the picking process and track fulfillment progress.

      **Data Sources**: 
      - oracle_wms_raw.allocation (via Singer tap)

      **Update Frequency**: Real-time via view materialization

    columns:
      - name: allocation_id
        description: "Unique identifier for the allocation record"
        tests:
          - unique
          - not_null
```

### Automated Documentation Generation

```bash
# Generate comprehensive documentation
dbt docs generate

# Include model performance metrics
dbt docs generate --include-sources --include-performance

# Serve documentation locally
dbt docs serve --port 8080
```

---

This model reference provides the foundation for understanding and working with FLEXT DBT Oracle WMS data models. For implementation details, see the [Development Guide](../development/guidelines.md).
