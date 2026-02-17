# FLEXT-DBT-Oracle-WMS

[![dbt 1.6+](https://img.shields.io/badge/dbt-1.6+-orange.svg)](https://getdbt.com)
[![Oracle WMS](https://img.shields.io/badge/Oracle-WMS-red.svg)](https://www.oracle.com/scm/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-DBT-Oracle-WMS** is a purpose-built analytics suite for Oracle Warehouse Management Systems (WMS). It integrates deeply with `flext-dbt-oracle` to deliver comprehensive reporting on inventory, fulfillment, and warehouse operations.

## 🚀 Key Features

- **Pre-Built Domain Models**: Turn-key data models for essential WMS entities:
  - **Inventory**: `dim_items`, `fact_inventory_snapshot`, `fact_inventory_transactions`.
  - **Fulfillment**: `fact_outbound_orders`, `fact_shipments`, `dim_carriers`.
  - **Operations**: `fact_tasks`, `fact_labor_productivity`.
- **Real-time Metrics**: Capture critical KPIs like order cycle time, inventory accuracy, and picking efficiency.
- **Operational Dashboards**: Models designed specifically for high-speed operational reporting.
- **Historical Trends**: Analyze seasonal demand, stock turnover, and labor utilization over time.
- **WMS Logic Macros**: Encapsulated business logic for `allocation_efficiency`, `pick_productivity`, and `abc_classification`.

## 📦 Installation

To use in your dbt project, add to your `packages.yml`:

```yaml
packages:
  - git: "https://github.com/organization/flext.git"
    subdirectory: "flext-dbt-oracle-wms"
    revision: "main" 
```

Run dependencies:

```bash
dbt deps
```

## 🛠️ Usage

### Analyze Inventory Health

Quickly assess stock levels and potential issues:

```sql
SELECT
    warehouse_id,
    item_category,
    SUM(quantity_on_hand) as total_stock,
    SUM(quantity_allocated) as allocated_stock,
    {{ wms_inventory_turnover('quantity_shipped', 'avg_inventory') }} as turns
FROM {{ ref('fact_inventory_snapshot') }}
GROUP BY 1, 2
```

### Track Labor Productivity

Monitor warehouse efficiency metrics:

```sql
SELECT
    worker_id,
    shift_date,
    total_picks,
    total_putaways,
    {{ wms_labor_productivity('tasks_completed', 'hours_worked') }} as units_per_hour
FROM {{ ref('fact_labor_productivity') }}
WHERE shift_date = CURRENT_DATE
```

### Fulfillment Performance

Analyze order cycle times and shipping accuracy:

```sql
SELECT
    carrier_name,
    AVG(cycle_time_hours) as fast_ship_score,
    COUNT(CASE WHEN on_time_delivery = true THEN 1 END) / COUNT(*) as service_level
FROM {{ ref('fact_shipments') }}
GROUP BY carrier_name
```

## 🏗️ Architecture

FLEXT-DBT-Oracle-WMS leverages the full ecosystem:

- **Layered Design**: Clear separation of Staging (WMS raw), Intermediate (Business Logic), and Marts (Reporting).
- **Oracle Optimized**: Uses `flext-dbt-oracle` performance features like partitioning and parallel execution.
- **Observability**: Integrated audit logging for all major data transformations.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on adding new business logic macros and enhancing domain models.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
