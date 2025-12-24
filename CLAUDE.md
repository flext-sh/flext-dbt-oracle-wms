# flext-dbt-oracle-wms - FLEXT DBT Adapters

**Hierarchy**: PROJECT
**Parent**: [../CLAUDE.md](../CLAUDE.md) - Workspace standards
**Last Update**: 2025-12-07

---

## Project Overview

**FLEXT-DBT-Oracle-WMS** is the dbt project for Oracle Warehouse Management System data transformations with dimensional modeling.

**Version**: 2.1.0  
**Status**: Production-ready  
**Python**: 3.13+

**CRITICAL INTEGRATION DEPENDENCIES**:

- **flext-meltano**: MANDATORY for ALL DBT operations (ZERO TOLERANCE for direct dbt imports)
- **flext-oracle-wms**: MANDATORY for ALL Oracle WMS operations (ZERO TOLERANCE for bypassing WMS domain)
- **flext-db-oracle**: MANDATORY for ALL Oracle Database operations (ZERO TOLERANCE for direct SQLAlchemy/oracledb imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)
- **flext-cli**: MANDATORY for ALL CLI operations (ZERO TOLERANCE for direct click/rich imports)

---

## Essential Commands

```bash
# Setup and validation
make setup                    # Complete development environment setup
make validate                 # Complete validation (lint + type + security + test)
make check                    # Quick check (lint + type)

# Quality gates
make lint                     # Ruff linting
make type-check               # Pyrefly type checking
make security                 # Bandit security scan
make test                     # Run tests
```

---

## Key Patterns

### DBT Oracle WMS Transformation

```python
from flext_core import FlextResult
from flext_dbt_oracle_wms import FlextDbtOracleWms

dbt = FlextDbtOracleWms()

# Run DBT models
result = dbt.run_models(models=["model1", "model2"])
if result.is_success:
    output = result.unwrap()
```

---

## Critical Development Rules

### ZERO TOLERANCE Policies

**ABSOLUTELY FORBIDDEN**:

- ❌ Direct dbt imports (use flext-meltano)
- ❌ Direct Oracle WMS operations (use flext-oracle-wms)
- ❌ Direct SQLAlchemy/oracledb imports (use flext-db-oracle)
- ❌ Direct click/rich imports (use flext-cli)
- ❌ Exception-based error handling (use FlextResult)
- ❌ Type ignores or `Any` types

**MANDATORY**:

- ✅ Use `FlextResult[T]` for all operations
- ✅ Use flext-meltano for DBT operations
- ✅ Use flext-oracle-wms for WMS operations
- ✅ Use flext-db-oracle for Oracle operations
- ✅ Use flext-cli for CLI operations
- ✅ Complete type annotations
- ✅ Zero Ruff violations

---

**See Also**:

- [Workspace Standards](../CLAUDE.md)
- [flext-core Patterns](../flext-core/CLAUDE.md)
- [flext-oracle-wms Patterns](../flext-oracle-wms/CLAUDE.md)
- [flext-dbt-oracle Patterns](../flext-dbt-oracle/CLAUDE.md)
