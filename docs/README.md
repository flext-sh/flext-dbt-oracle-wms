# FLEXT DBT Oracle WMS Documentation

**Enterprise Oracle WMS Data Transformations Documentation Hub**

Welcome to the comprehensive documentation for FLEXT DBT Oracle WMS - an enterprise-grade dbt project for Oracle Warehouse Management System data transformations.

## 📚 Documentation Structure

### 🚀 Getting Started
- **[Setup Guide](getting-started/setup.md)** - Complete installation and configuration
- **[Quick Start](getting-started/quickstart.md)** - Get running in 10 minutes
- **[First Models](getting-started/first-models.md)** - Build your first WMS data models
- **[Configuration](getting-started/configuration.md)** - Environment and profile setup

### 🏗️ Data Models
- **[Model Reference](models/reference.md)** - Complete model documentation
- **[Staging Models](models/staging.md)** - Raw data standardization
- **[Mart Models](models/marts.md)** - Business-ready analytics models
- **[Schema Reference](models/schema.md)** - Database schema documentation
- **[Data Lineage](models/lineage.md)** - Data flow and dependencies

### 🔌 Oracle WMS Integration
- **[WMS Overview](integration/oracle-wms.md)** - Oracle WMS system integration
- **[Data Sources](integration/data-sources.md)** - WMS tables and entities
- **[Singer Integration](integration/singer.md)** - flext-tap-oracle-wms setup
- **[Connection Setup](integration/connection.md)** - Oracle database configuration

### 🛠️ Development
- **[Development Setup](development/setup.md)** - Local development environment
- **[Model Guidelines](development/guidelines.md)** - dbt development best practices
- **[Testing Guide](development/testing.md)** - Data quality and model testing
- **[Code Standards](development/standards.md)** - SQL and Python coding standards
- **[Contributing](development/contributing.md)** - How to contribute to the project

### 🚀 Deployment
- **[Environment Setup](deployment/environments.md)** - Dev, staging, and production
- **[CI/CD Pipeline](deployment/cicd.md)** - Automated deployment pipeline
- **[Performance Tuning](deployment/performance.md)** - Optimization strategies
- **[Monitoring](deployment/monitoring.md)** - Data quality monitoring

### 📊 Business Intelligence
- **[Dashboard Models](bi/dashboards.md)** - BI-ready data models
- **[KPI Definitions](bi/kpis.md)** - Key performance indicators
- **[Reporting Guide](bi/reporting.md)** - Business reporting patterns
- **[Tableau Integration](bi/tableau.md)** - Tableau-specific setup

### 📖 Examples
- **[Basic Examples](examples/basic.md)** - Simple model examples
- **[Advanced Patterns](examples/advanced.md)** - Complex transformation patterns
- **[Use Cases](examples/use-cases.md)** - Real-world implementation examples
- **[Troubleshooting](examples/troubleshooting.md)** - Common issues and solutions

## 🎯 Quick Navigation

### For New Users
1. Start with **[Setup Guide](getting-started/setup.md)**
2. Follow **[Quick Start](getting-started/quickstart.md)**
3. Explore **[Model Reference](models/reference.md)**

### For Developers
1. Setup **[Development Environment](development/setup.md)**
2. Review **[Model Guidelines](development/guidelines.md)**
3. Follow **[Testing Guide](development/testing.md)**

### For Data Analysts
1. Review **[Business Models](models/marts.md)**
2. Check **[KPI Definitions](bi/kpis.md)**
3. Explore **[Dashboard Models](bi/dashboards.md)**

### For Operations
1. Setup **[Environment Configuration](deployment/environments.md)**
2. Configure **[CI/CD Pipeline](deployment/cicd.md)**
3. Monitor **[Data Quality](deployment/monitoring.md)**

## 🛠️ Technology Stack

### Core Technologies
- **dbt 1.6+** - Data transformation framework
- **Python 3.13** - Modern Python with enhanced performance
- **Oracle Database** - Enterprise data warehouse platform
- **Singer Protocol** - Data extraction and loading standard

### dbt Components
- **Models** - SQL transformations with Jinja templating
- **Tests** - Data quality validation and business rule checks
- **Macros** - Reusable SQL functions and utilities
- **Seeds** - Reference data management
- **Snapshots** - Slowly changing dimension tracking

### Oracle WMS Integration
- **WMS Entities** - Allocation, Inventory, Orders, Tasks, Waves
- **Business Logic** - WMS-specific transformations and calculations
- **Data Quality** - Enterprise-grade validation and testing
- **Performance** - Optimized for large-scale warehouse data

## 📊 Project Architecture

### Data Flow Architecture
```
Oracle WMS → Singer Tap → Raw Tables → dbt Models → Analytics

Data Layers:
┌─────────────────────────────────────────────────────────┐
│                    Business Intelligence                │
│     (Tableau, Power BI, Looker, Custom Dashboards)    │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                   Marts Layer                           │
│  • Operational (Real-time dashboards)                  │
│  • Analytical (Historical analysis)                    │
│  • Metrics (KPIs and executive dashboards)             │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                 Staging Layer                           │
│  • Data standardization and cleansing                  │
│  • Type casting and null handling                      │
│  • Business rule application                           │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                  Raw Data Layer                         │
│  • Oracle WMS tables via Singer tap                    │
│  • Minimal transformation, original structure          │
└─────────────────────────────────────────────────────────┘
```

### Model Organization
```
models/
├── staging/                    # 🔵 Data Standardization
│   ├── _sources.yml           # Source definitions
│   ├── stg_wms__allocation.sql # Allocation standardization
│   ├── stg_wms__inventory.sql  # Inventory standardization
│   ├── stg_wms__order_hdr.sql  # Order header standardization
│   └── stg_wms__order_dtl.sql  # Order detail standardization
│
├── marts/                      # 🟢 Business-Ready Models
│   ├── operational/            # Real-time operational metrics
│   │   └── opr_wms__allocation_summary.sql
│   ├── analytical/             # Historical analysis models
│   │   └── ana_wms__inventory_analysis.sql
│   └── metrics/                # KPI and dashboard models
│       └── met_wms__kpi_dashboard.sql
│
└── analyses/                   # 🟡 Ad-hoc Analysis
    └── inventory_deep_dive.sql
```

## 📈 Oracle WMS Domain Model

### Core Business Entities

#### **Allocation Management**
- **Allocations** - Pick and pack allocations
- **Tasks** - Work task assignments and completion
- **Waves** - Wave-based picking optimization
- **Locations** - Pick and storage location management

#### **Inventory Management**
- **Inventory** - Real-time inventory positions
- **Items** - Master item data and attributes
- **UOM** - Unit of measure conversions
- **Lots/Serials** - Traceability and quality tracking

#### **Order Management**
- **Order Headers** - Customer and shipping information
- **Order Details** - Line item specifications
- **Shipments** - Outbound shipment tracking
- **Receipts** - Inbound receipt processing

### Key Performance Indicators

#### **Operational KPIs**
- **Pick Rate** - Lines/hour picking performance
- **Order Cycle Time** - Order-to-ship timeframes
- **Inventory Accuracy** - Cycle count precision
- **Space Utilization** - Warehouse capacity usage

#### **Analytical KPIs**
- **Demand Patterns** - Seasonal and trend analysis
- **ABC Classification** - Item velocity analysis
- **Cost Analysis** - Labor and operational costs
- **Service Levels** - Customer fulfillment metrics

## 🧪 Data Quality Framework

### Testing Strategy
- **Schema Tests** - Data type and constraint validation
- **Business Rule Tests** - WMS-specific business logic
- **Data Quality Tests** - Completeness, accuracy, consistency
- **Performance Tests** - Query optimization validation

### Quality Thresholds
- **Completeness**: 95%+ required fields populated
- **Accuracy**: 98%+ data matches source system
- **Consistency**: 90%+ cross-model data alignment
- **Timeliness**: <4 hour data freshness requirement

## 🚀 Performance Optimization

### Optimization Strategies
- **Incremental Processing** - Process only changed data
- **Partitioning** - Partition by business date and facility
- **Clustering** - Cluster on frequently queried columns
- **Indexing** - Strategic index creation for performance

### Scaling Considerations
- **Model Parallelization** - Concurrent model execution
- **Resource Management** - Memory and CPU optimization
- **Data Retention** - Archive strategies for historical data
- **Query Optimization** - SQL performance tuning

## 📊 Business Impact

### Operational Benefits
- **Real-time Visibility** - Live warehouse operations monitoring
- **Data-Driven Decisions** - Analytics-based operational choices
- **Process Optimization** - Identify and eliminate inefficiencies
- **Compliance Reporting** - Automated regulatory compliance

### Strategic Benefits
- **Cost Reduction** - Optimize labor and operational costs
- **Service Improvement** - Enhance customer fulfillment
- **Scalability** - Support business growth and expansion
- **Innovation** - Enable new business capabilities

## 🤝 Community & Support

### Getting Help
- **Documentation** - Comprehensive guides and references
- **Issues** - Report bugs or request features via GitHub Issues
- **Discussions** - Ask questions in GitHub Discussions
- **Examples** - Real-world implementation patterns

### Contributing
- **[Contributing Guide](development/contributing.md)** - How to contribute
- **[Development Setup](development/setup.md)** - Local development
- **[Code Standards](development/standards.md)** - Coding conventions

## 📈 Roadmap

### Current Version (v0.7.0)
- ✅ Complete Oracle WMS entity coverage
- ✅ Staging and marts layer models
- ✅ Data quality testing framework
- ✅ Performance optimization features

### Upcoming Features
- 🔄 Real-time streaming integration
- 🔄 Advanced ML analytics models
- 🔄 Multi-tenant architecture support
- 🔄 Enhanced monitoring dashboard
- 🔄 Automated data governance

---

**Need Help?** Check our [Troubleshooting Guide](examples/troubleshooting.md) or [open an issue](https://github.com/flext-sh/flext/issues).

**Ready to Start?** Jump to the [Setup Guide](getting-started/setup.md)!