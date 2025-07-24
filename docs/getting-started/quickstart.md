# Quick Start Guide

**Get FLEXT DBT Oracle WMS running in 10 minutes**

This guide gets you up and running with FLEXT DBT Oracle WMS quickly. For detailed setup, see the [Setup Guide](setup.md).

## 🚀 Prerequisites Check

Ensure you have:
- ✅ **Python 3.13+** installed (`python --version`)
- ✅ **Poetry** installed (`poetry --version`)
- ✅ **Oracle database** access
- ✅ **Oracle Client** libraries installed

## ⚡ Quick Installation

### 1. Clone and Setup (2 minutes)

```bash
# Clone the project
git clone <repository-url>
cd flext-dbt-oracle-wms

# Install dependencies
poetry install

# Activate environment
poetry shell
```

### 2. Configure Oracle Connection (3 minutes)

```bash
# Create environment file
cat > .env << 'EOF'
ORACLE_HOST=your-oracle-host.com
ORACLE_PORT=1521
ORACLE_USER=wms_user
ORACLE_PASS=your-password
ORACLE_SERVICE=XEPDB1
ORACLE_SCHEMA=WMS_DEV
EOF

# Load environment
source .env
```

### 3. Setup dbt Profile (2 minutes)

```bash
# Create dbt profile
mkdir -p ~/.dbt
cat > ~/.dbt/profiles.yml << 'EOF'
flext_oracle_wms:
  target: dev
  outputs:
    dev:
      type: oracle
      host: "{{ env_var('ORACLE_HOST') }}"
      port: "{{ env_var('ORACLE_PORT', '1521') }}"
      user: "{{ env_var('ORACLE_USER') }}"
      pass: "{{ env_var('ORACLE_PASS') }}"
      service: "{{ env_var('ORACLE_SERVICE') }}"
      schema: "{{ env_var('ORACLE_SCHEMA') }}"
      threads: 4
EOF
```

### 4. Test Connection (1 minute)

```bash
# Test dbt connection
dbt debug

# Expected output:
# Connection test: [OK connection ok]
```

### 5. Run Your First Models (2 minutes)

```bash
# Install dbt dependencies
dbt deps

# Run staging models
dbt run --select staging

# Run a single model
dbt run --select stg_wms__allocation

# Test the model
dbt test --select stg_wms__allocation
```

## 🎯 Quick Validation

### Check Your Data

```sql
-- Query your first model
SELECT 
    allocation_id,
    company_code,
    facility_code,
    allocated_quantity,
    allocation_status_id
FROM {{ ref('stg_wms__allocation') }}
LIMIT 10;
```

### Verify Model Count

```bash
# List all models
dbt list

# Should show:
# flext_dbt_oracle_wms.staging.stg_wms__allocation
# flext_dbt_oracle_wms.staging.stg_wms__inventory
# flext_dbt_oracle_wms.staging.stg_wms__order_hdr
# flext_dbt_oracle_wms.staging.stg_wms__order_dtl
```

## 📊 Quick Dashboard

### Generate Documentation

```bash
# Create interactive documentation
dbt docs generate
dbt docs serve --port 8080

# Open: http://localhost:8080
```

### Key Views to Check:
1. **Data Lineage** - See model dependencies
2. **Column Details** - Review data types and descriptions
3. **Model Performance** - Check execution times

## 🧪 Quick Quality Check

```bash
# Run all tests
dbt test

# Expected: All tests should pass
# If tests fail, check Oracle WMS data quality
```

## 🎨 Common First Tasks

### 1. Explore Staging Data

```bash
# Check allocation data
dbt run --select stg_wms__allocation
```

### 2. Build Operational Marts

```bash
# Build operational dashboard models
dbt run --select marts.operational
```

### 3. Generate KPI Models

```bash
# Build metrics and KPIs
dbt run --select marts.metrics
```

## 🚨 Quick Troubleshooting

### Connection Issues
```bash
# Test Oracle connection directly
sqlplus $ORACLE_USER/$ORACLE_PASS@$ORACLE_HOST:$ORACLE_PORT/$ORACLE_SERVICE
```

### Model Compilation Issues
```bash
# Check compiled SQL
dbt compile --select stg_wms__allocation

# View compiled files
ls target/compiled/flext_dbt_oracle_wms/models/staging/
```

### Data Issues
```bash
# Check source data
dbt source freshness

# Validate specific model
dbt test --select stg_wms__allocation
```

## 🎯 Next Steps

### Immediate Actions (Next 30 minutes)
1. **Explore Models** - Check [Model Reference](../models/reference.md)
2. **Review Data Quality** - Run `dbt test` and investigate failures
3. **Check Performance** - Monitor model execution times

### This Week
1. **Configure Environments** - Setup staging and production profiles
2. **Customize Models** - Modify models for your specific WMS configuration
3. **Setup Monitoring** - Configure data quality alerts

### This Month
1. **Build Custom Analytics** - Create business-specific marts
2. **Integrate BI Tools** - Connect Tableau/Power BI
3. **Setup CI/CD** - Automate deployment pipeline

## 📚 Key Resources

### Essential Documentation
- **[Model Reference](../models/reference.md)** - Complete model documentation
- **[Setup Guide](setup.md)** - Detailed installation instructions
- **[Oracle WMS Integration](../integration/oracle-wms.md)** - WMS-specific guidance

### Common Commands
```bash
# Development workflow
dbt run --select staging        # Build staging layer
dbt run --select marts          # Build marts layer
dbt test                        # Run all tests
dbt docs generate              # Update documentation

# Production deployment
dbt run --target prod          # Deploy to production
dbt test --target prod         # Validate production data
```

### Configuration Files
- **`dbt_project.yml`** - Project configuration
- **`profiles.yml`** - Database connections
- **`.env`** - Environment variables
- **`schema.yml`** - Model tests and documentation

## 🎉 Success Checklist

After completing this guide, you should have:

- ✅ **Working dbt connection** to Oracle WMS
- ✅ **Staging models running** successfully
- ✅ **Tests passing** with good data quality
- ✅ **Documentation generated** and accessible
- ✅ **Understanding of** the model structure

## 🆘 Getting Stuck?

### Common Issues
1. **Oracle Client not found** - Install Oracle Instant Client
2. **Connection timeout** - Check Oracle host/port/service
3. **Permission denied** - Verify Oracle user permissions
4. **Model compilation error** - Check table/column names in Oracle

### Get Help
- **Check Logs** - `logs/dbt.log` for detailed errors
- **Debug Mode** - `dbt debug` for connection issues
- **Compile Check** - `dbt compile` for SQL issues
- **Documentation** - [Troubleshooting Guide](../examples/troubleshooting.md)

---

**Congratulations!** 🎉 You now have FLEXT DBT Oracle WMS running locally. Ready for the next level? Check out the [Development Guide](../development/guidelines.md).