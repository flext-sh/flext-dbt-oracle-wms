# Oracle WMS Integration Guide

**Complete Integration Guide for Oracle Warehouse Management System**

This guide covers the integration between FLEXT DBT and Oracle WMS, including data sources, connection setup, and WMS-specific considerations.

## 🏢 Oracle WMS Overview

### What is Oracle WMS

Oracle Warehouse Management System (WMS) is a comprehensive supply chain execution solution that provides:

- **Inventory Management** - Real-time inventory tracking and optimization
- **Order Fulfillment** - Pick, pack, and ship operations
- **Labor Management** - Task assignment and productivity tracking
- **Wave Planning** - Optimized picking waves and resource allocation
- **Quality Management** - Lot tracking and quality control

### FLEXT Integration Benefits

- **Real-time Analytics** - Live operational dashboards
- **Historical Analysis** - Trend analysis and forecasting
- **Data Quality** - Automated validation and cleansing
- **Scalability** - Handle enterprise-scale WMS data
- **Compliance** - Audit trails and regulatory reporting

## 📊 Oracle WMS Data Model

### Core Business Entities

#### **Allocation Management**

```sql
-- Primary allocation entity
ALLOCATION
├── allocation_id (PK)
├── company_code
├── facility_code
├── order_dtl_id (FK)
├── from_inventory_id (FK)
├── to_inventory_id (FK)
├── allocated_quantity
├── packed_quantity
├── allocation_status_id (FK)
├── wave_id (FK)
├── task_id (FK)
└── timestamps (created, modified)
```

#### **Inventory Management**

```sql
-- Real-time inventory positions
INVENTORY
├── inventory_id (PK)
├── company_code
├── facility_code
├── item_id (FK)
├── location_id (FK)
├── lot_number
├── serial_number
├── on_hand_quantity
├── allocated_quantity
├── available_quantity
├── inventory_status_id (FK)
└── expiration_date
```

#### **Order Management**

```sql
-- Order header information
ORDER_HDR
├── order_hdr_id (PK)
├── company_code
├── facility_code
├── customer_id (FK)
├── order_number
├── order_type_id (FK)
├── order_status_id (FK)
├── ship_to_address
├── requested_ship_date
└── timestamps

-- Order detail/line items
ORDER_DTL
├── order_dtl_id (PK)
├── order_hdr_id (FK)
├── line_number
├── item_id (FK)
├── ordered_quantity
├── shipped_quantity
├── unit_price
└── line_status_id (FK)
```

### Reference Data Entities

#### **Master Data**

- **ITEM** - Item master data and attributes
- **LOCATION** - Warehouse locations and zones
- **COMPANY** - Company and organization codes
- **FACILITY** - Warehouse facilities and sites
- **UOM** - Units of measure and conversions

#### **Status and Type Tables**

- **STATUS** - Various status codes (order, allocation, inventory)
- **TYPE** - Type classifications (order types, allocation types)
- **REASON** - Reason codes for adjustments and exceptions

## 🔌 Database Connection Setup

### Oracle Database Requirements

#### **Database Version**

- Oracle Database 12c or higher
- Oracle WMS application version 23.1.0+
- Oracle Client 19c or 21c

#### **Required Permissions**

```sql
-- Grant necessary permissions to dbt user
GRANT SELECT ON wms_schema.allocation TO dbt_user;
GRANT SELECT ON wms_schema.inventory TO dbt_user;
GRANT SELECT ON wms_schema.order_hdr TO dbt_user;
GRANT SELECT ON wms_schema.order_dtl TO dbt_user;
GRANT SELECT ON wms_schema.item TO dbt_user;
GRANT SELECT ON wms_schema.location TO dbt_user;

-- Grant system permissions for analytics
GRANT CREATE TABLE TO dbt_user;
GRANT CREATE VIEW TO dbt_user;
GRANT CREATE SEQUENCE TO dbt_user;
```

### Connection Configuration

#### **dbt profiles.yml**

```yaml
flext_oracle_wms:
  target: dev
  outputs:
    dev:
      type: oracle
      host: "{{ env_var('ORACLE_WMS_HOST') }}"
      port: "{{ env_var('ORACLE_WMS_PORT', '1521') }}"
      user: "{{ env_var('ORACLE_WMS_USER') }}"
      pass: "{{ env_var('ORACLE_WMS_PASS') }}"
      service: "{{ env_var('ORACLE_WMS_SERVICE') }}"
      schema: "{{ env_var('ORACLE_WMS_SCHEMA') }}"
      threads: 8
      keepalives_idle: 0
      search_path_prefix: "{{ env_var('ORACLE_WMS_SCHEMA') }}"

    prod:
      type: oracle
      host: "{{ env_var('ORACLE_WMS_HOST_PROD') }}"
      port: 1521
      user: "{{ env_var('ORACLE_WMS_USER_PROD') }}"
      pass: "{{ env_var('ORACLE_WMS_PASS_PROD') }}"
      service: "{{ env_var('ORACLE_WMS_SERVICE_PROD') }}"
      schema: "{{ env_var('ORACLE_WMS_SCHEMA_PROD') }}"
      threads: 16
      keepalives_idle: 0
```

#### **Environment Variables**

```bash
# Oracle WMS Database Connection
export ORACLE_WMS_HOST="wms-prod.company.com"
export ORACLE_WMS_PORT="1521"
export ORACLE_WMS_USER="dbt_analytics"
export ORACLE_WMS_PASS="secure_password_here"
export ORACLE_WMS_SERVICE="WMSPROD"
export ORACLE_WMS_SCHEMA="WMS_ANALYTICS"

# WMS Business Configuration
export WMS_COMPANY_CODE="001"
export WMS_FACILITY_CODE="DC001"
export WMS_ORGANIZATION_ID="101"
```

### Connection Testing

#### **Test Basic Connectivity**

```bash
# Test Oracle connection
sqlplus $ORACLE_WMS_USER/$ORACLE_WMS_PASS@$ORACLE_WMS_HOST:$ORACLE_WMS_PORT/$ORACLE_WMS_SERVICE

# Test dbt connection
dbt debug --profiles-dir profiles --target dev
```

#### **Validate WMS Tables**

```sql
-- Check WMS table availability
SELECT table_name, num_rows
FROM user_tables
WHERE table_name IN ('ALLOCATION', 'INVENTORY', 'ORDER_HDR', 'ORDER_DTL')
ORDER BY table_name;

-- Verify data freshness
SELECT
    'ALLOCATION' as table_name,
    COUNT(*) as record_count,
    MAX(mod_ts) as latest_modified
FROM allocation
WHERE company_code = '001'
  AND facility_code = 'DC001';
```

## 📁 Source Configuration

### dbt Sources Definition

Create `models/staging/_sources.yml`:

```yaml
version: 2

sources:
  - name: oracle_wms_raw
    description: "Raw Oracle WMS data via Singer tap"
    database: "{{ env_var('ORACLE_WMS_DATABASE', 'WMSPROD') }}"
    schema: "{{ env_var('ORACLE_WMS_SCHEMA', 'wms_raw') }}"

    tables:
      - name: allocation
        description: "WMS allocation records for pick/pack operations"
        columns:
          - name: id
            description: "Primary key - allocation identifier"
            tests:
              - unique
              - not_null
          - name: company_code
            description: "Company identifier"
            tests:
              - not_null
          - name: facility_code
            description: "Facility/warehouse identifier"
            tests:
              - not_null
          - name: allocated_quantity
            description: "Quantity allocated for picking"
            tests:
              - not_null

        freshness:
          warn_after: { count: 2, period: hour }
          error_after: { count: 6, period: hour }

        loaded_at_field: mod_ts

      - name: inventory
        description: "WMS inventory positions and stock levels"
        columns:
          - name: id
            description: "Primary key - inventory record identifier"
            tests:
              - unique
              - not_null
          - name: item_id
            description: "Item master reference"
            tests:
              - not_null
          - name: on_hand_quantity
            description: "Physical inventory quantity"
            tests:
              - not_null

      - name: order_hdr
        description: "WMS order header information"
        columns:
          - name: id
            description: "Primary key - order header identifier"
            tests:
              - unique
              - not_null

      - name: order_dtl
        description: "WMS order detail/line information"
        columns:
          - name: id
            description: "Primary key - order detail identifier"
            tests:
              - unique
              - not_null
          - name: order_hdr_id
            description: "Reference to order header"
            tests:
              - not_null
              - relationships:
                  to: source('oracle_wms_raw', 'order_hdr')
                  field: id
```

## 🔄 Data Integration Patterns

### Singer Tap Integration

#### **flext-tap-oracle-wms Setup**

```bash
# Install Singer tap for Oracle WMS
pip install flext-tap-oracle-wms

# Create tap configuration
cat > tap-oracle-wms-settings.json << 'EOF'
{
  "host": "wms-prod.company.com",
  "port": 1521,
  "service": "WMSPROD",
  "user": "tap_user",
  "password": "tap_password",
  "filter_schemas": ["WMS"],
  "default_replication_method": "INCREMENTAL",
  "tables": {
    "WMS.ALLOCATION": {
      "replication_method": "INCREMENTAL",
      "replication_key": "mod_ts"
    },
    "WMS.INVENTORY": {
      "replication_method": "INCREMENTAL",
      "replication_key": "mod_ts"
    }
  }
}
EOF

# Test tap discovery
flext-tap-oracle-wms --config tap-oracle-wms-settings.json --discover
```

#### **Data Pipeline Flow**

```
Oracle WMS Database
        ↓
Singer Tap (flext-tap-oracle-wms)
        ↓
Raw Data Tables (staging database)
        ↓
dbt Transformations (FLEXT DBT Oracle WMS)
        ↓
Analytics Tables (data warehouse)
        ↓
Business Intelligence Tools
```

### Real-time Data Considerations

#### **Change Data Capture (CDC)**

```sql
-- Enable CDC for critical WMS tables
-- (Requires Oracle GoldenGate or similar)

-- Track allocation changes
CREATE TRIGGER allocation_cdc_trigger
AFTER UPDATE OR INSERT OR DELETE ON allocation
FOR EACH ROW
BEGIN
  INSERT INTO allocation_cdc_log (
    operation_type,
    allocation_id,
    old_values,
    new_values,
    change_timestamp,
    user_name
  ) VALUES (
    CASE
      WHEN INSERTING THEN 'INSERT'
      WHEN UPDATING THEN 'UPDATE'
      WHEN DELETING THEN 'DELETE'
    END,
    COALESCE(:NEW.id, :OLD.id),
    -- JSON representation of old values
    -- JSON representation of new values
    CURRENT_TIMESTAMP,
    USER
  );
END;
```

#### **Incremental Loading Strategy**

```sql
-- dbt incremental model example
{{
  settings(
    materialized='incremental',
    unique_key='allocation_id',
    on_schema_change='fail'
  )
}}

SELECT
  id as allocation_id,
  company_code,
  facility_code,
  allocated_quantity,
  mod_ts as modified_timestamp
FROM {{ source('oracle_wms_raw', 'allocation') }}

{% if is_incremental() %}
  -- Only process records modified since last run
  WHERE mod_ts > (SELECT MAX(modified_timestamp) FROM {{ this }})
{% endif %}
```

## 🏗️ WMS-Specific Transformations

### Business Logic Implementation

#### **Allocation Status Processing**

```sql
-- Standardize allocation status codes
CASE allocation_status_id
  WHEN '10' THEN 'CREATED'
  WHEN '20' THEN 'RELEASED'
  WHEN '30' THEN 'PICKING'
  WHEN '40' THEN 'PICKED'
  WHEN '50' THEN 'PACKED'
  WHEN '60' THEN 'SHIPPED'
  WHEN '90' THEN 'CANCELLED'
  ELSE 'UNKNOWN'
END as allocation_status
```

#### **Inventory Classification**

```sql
-- Calculate available inventory
on_hand_quantity - COALESCE(allocated_quantity, 0) as available_quantity,

-- Classify inventory status
CASE
  WHEN on_hand_quantity - COALESCE(allocated_quantity, 0) > 0 THEN 'AVAILABLE'
  WHEN on_hand_quantity > 0 AND allocated_quantity >= on_hand_quantity THEN 'ALLOCATED'
  WHEN on_hand_quantity = 0 THEN 'OUT_OF_STOCK'
  ELSE 'UNKNOWN'
END as inventory_classification
```

#### **Order Fulfillment Metrics**

```sql
-- Calculate order fulfillment rates
SELECT
  order_hdr_id,
  SUM(ordered_quantity) as total_ordered,
  SUM(shipped_quantity) as total_shipped,
  CASE
    WHEN SUM(ordered_quantity) = 0 THEN 0
    ELSE ROUND(SUM(shipped_quantity) / SUM(ordered_quantity) * 100, 2)
  END as fulfillment_rate_percent
FROM {{ ref('stg_wms__order_dtl') }}
GROUP BY order_hdr_id
```

## 📊 Performance Optimization

### Oracle-Specific Optimizations

#### **Partitioning Strategy**

```sql
-- Partition large fact tables by business date
{{
  settings(
    materialized='table',
    partition_by='business_date',
    cluster_by=['company_code', 'facility_code']
  )
}}
```

#### **Indexing Recommendations**

```sql
-- Suggested indexes for Oracle WMS tables
CREATE INDEX idx_allocation_wave_status ON allocation (wave_id, allocation_status_id);
CREATE INDEX idx_inventory_item_location ON inventory (item_id, location_id);
CREATE INDEX idx_order_dtl_status ON order_dtl (order_hdr_id, line_status_id);
```

#### **Query Optimization**

```sql
-- Use Oracle-specific hints for performance
/*+ USE_HASH(a, o) PARALLEL(4) */
SELECT /*+ FIRST_ROWS(100) */
  a.allocation_id,
  o.order_number
FROM {{ ref('stg_wms__allocation') }} a
JOIN {{ ref('stg_wms__order_hdr') }} o
  ON a.order_hdr_id = o.order_hdr_id
WHERE a.business_date >= CURRENT_DATE - 7
```

## 🧪 WMS Data Quality Rules

### Business Rule Validation

#### **Allocation Business Rules**

```sql
-- Test: Allocated quantity should not exceed ordered quantity
-- tests/business_rules/test_allocation_quantity_logic.sql
SELECT *
FROM {{ ref('stg_wms__allocation') }} a
JOIN {{ ref('stg_wms__order_dtl') }} o
  ON a.order_dtl_id = o.order_dtl_id
WHERE a.allocated_quantity > o.ordered_quantity
```

#### **Inventory Consistency Rules**

```sql
-- Test: Inventory quantities should be non-negative
-- tests/business_rules/test_inventory_non_negative.sql
SELECT *
FROM {{ ref('stg_wms__inventory') }}
WHERE on_hand_quantity < 0
   OR allocated_quantity < 0
   OR available_quantity < 0
```

#### **Order Status Progression**

```sql
-- Test: Order status should follow logical progression
-- tests/business_rules/test_order_status_progression.sql
WITH status_progression AS (
  SELECT
    order_hdr_id,
    order_status_id,
    LAG(order_status_id) OVER (
      PARTITION BY order_hdr_id
      ORDER BY modified_timestamp
    ) as previous_status
  FROM {{ ref('stg_wms__order_hdr') }}
)
SELECT *
FROM status_progression
WHERE (previous_status = '60' AND order_status_id = '10') -- Shipped to Created (invalid)
   OR (previous_status = '90' AND order_status_id != '90') -- Cancelled to anything (invalid)
```

## 📈 Monitoring and Alerting

### Data Quality Monitoring

#### **Freshness Monitoring**

```yaml
# models/staging/_sources.yml
sources:
  - name: oracle_wms_raw
    tables:
      - name: allocation
        freshness:
          warn_after: { count: 2, period: hour }
          error_after: { count: 6, period: hour }
        loaded_at_field: mod_ts
```

#### **Volume Anomaly Detection**

```sql
-- Detect significant volume changes
WITH daily_volumes AS (
  SELECT
    DATE(created_timestamp) as business_date,
    COUNT(*) as allocation_count
  FROM {{ ref('stg_wms__allocation') }}
  WHERE created_timestamp >= CURRENT_DATE - 30
  GROUP BY DATE(created_timestamp)
),
volume_stats AS (
  SELECT
    AVG(allocation_count) as avg_volume,
    STDDEV(allocation_count) as stddev_volume
  FROM daily_volumes
)
SELECT *
FROM daily_volumes d
CROSS JOIN volume_stats s
WHERE d.allocation_count > s.avg_volume + (2 * s.stddev_volume)
   OR d.allocation_count < s.avg_volume - (2 * s.stddev_volume)
```

## 🔧 Troubleshooting

### Common Integration Issues

#### **Connection Problems**

```bash
# Test Oracle connectivity
tnsping $ORACLE_WMS_SERVICE

# Check Oracle listener
lsnrctl status

# Verify user permissions
sqlplus $ORACLE_WMS_USER/$ORACLE_WMS_PASS@$ORACLE_WMS_SERVICE
SQL> SELECT * FROM user_tab_privs WHERE table_name = 'ALLOCATION';
```

#### **Data Type Issues**

```sql
-- Common Oracle to dbt type mappings
Oracle NUMBER(15,4) → DECIMAL(15,4)
Oracle VARCHAR2(100) → STRING
Oracle DATE → TIMESTAMP
Oracle CLOB → STRING
Oracle TIMESTAMP → TIMESTAMP
```

#### **Performance Issues**

```sql
-- Check table statistics
SELECT table_name, num_rows, blocks, avg_row_len
FROM user_tables
WHERE table_name IN ('ALLOCATION', 'INVENTORY', 'ORDER_HDR');

-- Update statistics if needed
EXEC DBMS_STATS.GATHER_TABLE_STATS('WMS_SCHEMA', 'ALLOCATION');
```

## 📚 Additional Resources

- **[Oracle WMS Documentation](https://docs.oracle.com/en/industries/food-beverage/wms/)**
- **[dbt Oracle Adapter](https://github.com/oracle/dbt-oracle)**
- **[Singer Oracle Tap](https://hub.meltano.com/extractors/tap-oracle)**
- **[Oracle Performance Tuning](https://docs.oracle.com/en/database/oracle/oracle-database/21/tgdba/)**

______________________________________________________________________

This integration guide provides the foundation for connecting FLEXT DBT with Oracle WMS.
