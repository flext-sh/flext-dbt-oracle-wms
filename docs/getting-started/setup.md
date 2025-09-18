# Setup Guide

**Complete Installation and Configuration for FLEXT DBT Oracle WMS**

This guide will walk you through setting up FLEXT DBT Oracle WMS from scratch, including all prerequisites and configuration steps.

## 📋 Prerequisites

### System Requirements

- **Python 3.13+** (required for modern typing and performance)
- **Git** (for version control)
- **Poetry** (recommended for dependency management)
- **Oracle Database** access (Oracle 12c+ or Oracle Cloud)
- **Oracle Client** libraries (Oracle Instant Client)

### Oracle WMS Requirements

- **Oracle WMS** system access
- **Database permissions** for WMS schemas
- **Singer tap** setup (flext-tap-oracle-wms)
- **Network connectivity** to Oracle database

## 🚀 Installation

### 1. Clone the Repository

```bash
# Clone the project
git clone <repository-url>
cd flext-dbt-oracle-wms

# Verify project structure
ls -la
```

### 2. Python Environment Setup

#### Option A: Using Poetry (Recommended)

```bash
# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
poetry install

# Activate virtual environment
poetry shell
```

#### Option B: Using pip and venv

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

### 3. Oracle Client Setup

#### Oracle Instant Client Installation

**Linux/Mac:**

```bash
# Download Oracle Instant Client
wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basic-linux.x64-21.0.9.9.0.zip

# Extract and setup
unzip instantclient-basic-linux.x64-21.0.9.9.0.zip
export ORACLE_HOME=/path/to/instantclient_21_1
export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH

# Add to your ~/.bashrc or ~/.zshrc
echo 'export ORACLE_HOME=/path/to/instantclient_21_1' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH' >> ~/.bashrc
```

**Windows:**

```powershell
# Download and extract Oracle Instant Client
# Set environment variables
$env:ORACLE_HOME = "C:\oracle\instantclient_21_1"
$env:PATH = "$env:ORACLE_HOME;$env:PATH"
```

#### Verify Oracle Client

```bash
# Test Oracle client installation
python -c "import cx_Oracle; print('Oracle client installed successfully')"
```

### 4. dbt Installation and Setup

```bash
# Install dbt with Oracle adapter
pip install dbt-oracle

# Verify dbt installation
dbt --version

# Expected output:
# Core:
#   - dbt-core: 1.6.x
# Plugins:
#   - dbt-oracle: 1.6.x
```

## ⚙️ Configuration

### 1. dbt Profile Configuration

Create your dbt profile for Oracle WMS connection:

```bash
# Create profiles directory if it doesn't exist
mkdir -p ~/.dbt

# Create profiles.yml
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
      keepalives_idle: 0
      search_path_prefix: "{{ env_var('ORACLE_SCHEMA') }}"

    staging:
      type: oracle
      host: "{{ env_var('ORACLE_HOST_STAGING') }}"
      port: "{{ env_var('ORACLE_PORT', '1521') }}"
      user: "{{ env_var('ORACLE_USER_STAGING') }}"
      pass: "{{ env_var('ORACLE_PASS_STAGING') }}"
      service: "{{ env_var('ORACLE_SERVICE_STAGING') }}"
      schema: "{{ env_var('ORACLE_SCHEMA_STAGING') }}"
      threads: 8

    prod:
      type: oracle
      host: "{{ env_var('ORACLE_HOST_PROD') }}"
      port: "{{ env_var('ORACLE_PORT', '1521') }}"
      user: "{{ env_var('ORACLE_USER_PROD') }}"
      pass: "{{ env_var('ORACLE_PASS_PROD') }}"
      service: "{{ env_var('ORACLE_SERVICE_PROD') }}"
      schema: "{{ env_var('ORACLE_SCHEMA_PROD') }}"
      threads: 16
EOF
```

### 2. Environment Variables

Create environment configuration:

```bash
# Create .env file
cat > .env << 'EOF'
# Oracle WMS Database Connection - Development
ORACLE_HOST=your-oracle-host.com
ORACLE_PORT=1521
ORACLE_USER=wms_user
ORACLE_PASS=your-secure-password
ORACLE_SERVICE=XEPDB1
ORACLE_SCHEMA=WMS_DEV

# Oracle WMS Database Connection - Staging
ORACLE_HOST_STAGING=staging-oracle-host.com
ORACLE_USER_STAGING=wms_staging_user
ORACLE_PASS_STAGING=staging-password
ORACLE_SERVICE_STAGING=STAGING
ORACLE_SCHEMA_STAGING=WMS_STAGING

# Oracle WMS Database Connection - Production
ORACLE_HOST_PROD=prod-oracle-host.com
ORACLE_USER_PROD=wms_prod_user
ORACLE_PASS_PROD=prod-password
ORACLE_SERVICE_PROD=PROD
ORACLE_SCHEMA_PROD=WMS_PROD

# dbt Configuration
DBT_PROFILES_DIR=.
DBT_ORACLE_WMS_SCHEMA=wms_raw

# Singer Tap Configuration
TAP_ORACLE_WMS_HOST=your-oracle-host.com
TAP_ORACLE_WMS_PORT=1521
TAP_ORACLE_WMS_SERVICE=XEPDB1
TAP_ORACLE_WMS_USER=tap_user
TAP_ORACLE_WMS_PASSWORD=tap-password

# Data Quality Thresholds
DATA_QUALITY_COMPLETENESS_THRESHOLD=0.95
DATA_QUALITY_ACCURACY_THRESHOLD=0.98
DATA_QUALITY_CONSISTENCY_THRESHOLD=0.90

# Performance Settings
ENABLE_INCREMENTAL_MODELS=true
INCREMENTAL_LOOKBACK_DAYS=7
MAX_CONCURRENT_THREADS=4
EOF

# Load environment variables
source .env
```

### 3. Project Configuration

Verify and customize `dbt_project.yml`:

```yaml
# dbt_project.yml
name: "flext_dbt_oracle_wms"
version: "0.9.9"
config-version: 2

profile: "flext_oracle_wms"

model-paths: ["models"]
analysis-paths: ["analyses"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

clean-targets:
  - "target"
  - "dbt_packages"

# Model configurations
models:
  flext_dbt_oracle_wms:
    +materialized: table
    +schema: wms
    +tags: ["oracle_wms", "enterprise"]

    staging:
      +materialized: view
      +schema: wms_staging
      +tags: ["staging", "oracle_wms"]

    marts:
      +materialized: table
      +schema: wms_marts
      +tags: ["marts", "oracle_wms", "business"]

# Variables
vars:
  oracle_wms_schema: "{{ env_var('DBT_ORACLE_WMS_SCHEMA', 'wms_raw') }}"
  business_start_date: "2024-01-01"
  enable_incremental_models: true
  incremental_lookback_days: 7
```

## 🔍 Verification

### 1. Test Database Connection

```bash
# Test dbt connection
dbt debug

# Expected output:
# Connection test: [OK connection ok]
```

### 2. Install dbt Dependencies

```bash
# Install dbt packages
dbt deps

# This will install:
# - dbt-utils
# - dbt-date
# - dbt-expectations (optional)
```

### 3. Verify Project Structure

```bash
# List dbt models
dbt list

# Expected output:
# flext_dbt_oracle_wms.staging.stg_wms__allocation
# flext_dbt_oracle_wms.staging.stg_wms__inventory
# flext_dbt_oracle_wms.staging.stg_wms__order_hdr
# flext_dbt_oracle_wms.staging.stg_wms__order_dtl
# flext_dbt_oracle_wms.marts.operational.opr_wms__allocation_summary
# flext_dbt_oracle_wms.marts.analytical.ana_wms__inventory_analysis
# flext_dbt_oracle_wms.marts.metrics.met_wms__kpi_dashboard
```

### 4. Test Model Compilation

```bash
# Compile models without running
dbt compile

# Check compiled SQL
ls target/compiled/flext_dbt_oracle_wms/models/staging/
```

## 🎯 Quick Validation

### 1. Run a Simple Model

```bash
# Run a single staging model
dbt run --select stg_wms__allocation

# Expected output:
# Completed successfully
# 1 model, 0 tests, 0 snapshots, 0 analyses, 0 macros, 0 operations, 0 seed files, 0 sources, 0 exposures, 0 metrics
```

### 2. Run Basic Tests

```bash
# Run tests for staging models
dbt test --select staging

# Expected output should show all tests passing
```

### 3. Generate Documentation

```bash
# Generate documentation
dbt docs generate

# Serve documentation locally
dbt docs serve --port 8080

# View at: http://localhost:8080
```

## 🔧 Oracle WMS Data Setup

### 1. Source Data Validation

Verify your Oracle WMS source data:

```sql
-- Connect to Oracle WMS database
sqlplus wms_user/password@oracle-host:1521/XEPDB1

-- Check key WMS tables
SELECT table_name, num_rows
FROM user_tables
WHERE table_name IN ('ALLOCATION', 'INVENTORY', 'ORDER_HDR', 'ORDER_DTL')
ORDER BY table_name;

-- Verify data freshness
SELECT
    'ALLOCATION' as table_name,
    COUNT(*) as total_records,
    MAX(mod_ts) as latest_modified
FROM allocation
UNION ALL
SELECT
    'INVENTORY' as table_name,
    COUNT(*) as total_records,
    MAX(mod_ts) as latest_modified
FROM inventory;
```

### 2. Singer Tap Setup (Optional)

If using Singer tap for data extraction:

```bash
# Install flext-tap-oracle-wms
pip install flext-tap-oracle-wms

# Create tap configuration
cat > tap-config.json << 'EOF'
{
  "host": "your-oracle-host.com",
  "port": 1521,
  "service": "XEPDB1",
  "user": "tap_user",
  "password": "tap-password",
  "default_replication_method": "INCREMENTAL",
  "filter_schemas": ["WMS"]
}
EOF

# Test tap connection
flext-tap-oracle-wms --config tap-config.json --discover
```

## 🛠️ Development Setup

### 1. Pre-commit Hooks

```bash
# Install pre-commit hooks
poetry install --group dev
pre-commit install

# Test pre-commit hooks
pre-commit run --all-files
```

### 2. IDE Configuration

#### VS Code Setup

Create `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "files.associations": {
    "*.sql": "jinja-sql"
  },
  "sqltools.connections": [
    {
      "name": "Oracle WMS Dev",
      "driver": "Oracle",
      "server": "your-oracle-host.com",
      "port": 1521,
      "database": "XEPDB1",
      "username": "wms_user"
    }
  ]
}
```

### 3. Quality Checks

```bash
# Run all quality checks
make validate

# Individual checks
make lint          # SQL and Python linting
make type-check    # Python type checking
make security      # Security scanning
make test          # All tests
```

## 🐛 Troubleshooting

### Common Issues

#### Oracle Client Issues

**Problem**: `DPI-1047: Cannot locate a 64-bit Oracle Client library`

**Solution**:

```bash
# Ensure Oracle client is properly installed
export ORACLE_HOME=/path/to/instantclient_21_1
export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH

# Verify installation
ldconfig -p | grep oracle
```

#### Connection Issues

**Problem**: `ORA-12514: TNS:listener does not currently know of service`

**Solution**:

```bash
# Test connection with sqlplus
sqlplus wms_user/password@oracle-host:1521/XEPDB1

# Verify service name in profiles.yml
# Use SID instead of service name if needed
```

#### dbt Compilation Issues

**Problem**: `Compilation Error: Model not found`

**Solution**:

```bash
# Clean dbt artifacts
dbt clean

# Reinstall dependencies
dbt deps

# Check model references
dbt compile --parse-only
```

#### Performance Issues

**Problem**: Slow model execution

**Solution**:

```bash
# Increase threads in profiles.yml
# Add incremental materialization
# Use --fail-fast for debugging

dbt run --fail-fast --threads 1
```

### Getting Help

- **Check logs**: `logs/dbt.log`
- **Validate configuration**: `dbt debug`
- **Test individual models**: `dbt run --select model_name`
- **Check compiled SQL**: `target/compiled/`

## ✅ Next Steps

Now that you have FLEXT DBT Oracle WMS set up:

1. **Explore Models** - Check the [Model Reference](../models/reference.md)
2. **Run Your First Transformation** - Follow the [Quick Start Guide](quickstart.md)
3. **Understand the Data** - Review [Oracle WMS Integration](../integration/oracle-wms.md)
4. **Set Up Development** - Read the [Development Guide](../development/setup.md)

## 📚 Additional Resources

- **[dbt Documentation](https://docs.getdbt.com/)** - Official dbt docs
- **[Oracle dbt Adapter](https://github.com/oracle/dbt-oracle)** - Oracle-specific documentation
- **[Singer Protocol](https://hub.meltano.com/singer/spec)** - Data extraction standards
- **[Oracle WMS Documentation](https://docs.oracle.com/en/industries/food-beverage/wms/)** - Oracle WMS reference

---

**Installation Complete!** 🎉 You're ready to start transforming Oracle WMS data with dbt.
