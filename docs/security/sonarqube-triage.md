# Triagem SonarCloud — flext-sh/flext-dbt-oracle-wms

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.5`

## Resumo

**11 issues** — BLOCKER 0, CRITICAL 6, MAJOR 4, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 7 · **Debt total: 51min**

| regra | issues |
|---|---|
| `plsql:S1192` | 5 |
| `githubactions:S8233` | 2 |
| `python:S1192` | 1 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_dbt_oracle_wms/_utilities/client.py:39` · **Effort**: 6min

> Define a constant instead of duplicating this literal "WMS client unavailable" 3 times.

```python
       35          """Discover Oracle WMS entities through the owning domain client."""
       36          client_result = self._get_wms_client()
       37          if client_result.failure:
       38              return r[t.StrSequence].fail(
>>>    39                  client_result.error or "WMS client unavailable"
       40              )
       41          return client_result.value.discover_entities()
       42  
       43      def extract_oracle_wms_data(
```

**Decisão**: pendente

### 2 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/data_quality/test_cross_model_consistency.sql:11` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        7      a.facility_code,
        8      a.allocation_id,
        9      a.order_dtl_id,
       10      'ORPHANED_ALLOCATION' as issue_type
>>>    11  from {{ ref('stg_wms__allocation') }} a
       12  left join {{ ref('stg_wms__order_dtl') }} od
       13      on a.company_code = od.company_code
       14      and a.facility_code = od.facility_code
       15      and a.order_dtl_id = od.order_detail_id
```

**Decisão**: pendente

### 3 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/data_quality/test_cross_model_consistency.sql:12` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        8      a.allocation_id,
        9      a.order_dtl_id,
       10      'ORPHANED_ALLOCATION' as issue_type
       11  from {{ ref('stg_wms__allocation') }} a
>>>    12  left join {{ ref('stg_wms__order_dtl') }} od
       13      on a.company_code = od.company_code
       14      and a.facility_code = od.facility_code
       15      and a.order_dtl_id = od.order_detail_id
       16  where od.order_detail_id is null
```

**Decisão**: pendente

### 4 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/data_quality/test_cross_model_consistency.sql:18` · **Effort**: 4min

> Define a constant instead of duplicating this literal 6 times.

```sql
       14      and a.facility_code = od.facility_code
       15      and a.order_dtl_id = od.order_detail_id
       16  where od.order_detail_id is null
       17    and a.order_dtl_id is not null
>>>    18    and a.data_quality_status = 'VALID'
       19  
       20  union all
       21  
       22  -- Test 2: Inventory allocations should not exceed available quantity
```

**Decisão**: pendente

### 5 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/marts/test_opr_wms__allocation_summary_kpis.sql:6` · **Effort**: 4min

> Define a constant instead of duplicating this literal 5 times.

```sql
        2  -- Ensures enterprise metrics accuracy and consistency
        3  
        4  -- Test 1: Pack efficiency should be between 0 and 100%
        5  select *
>>>     6  from {{ ref('opr_wms__allocation_summary') }}
        7  where pack_efficiency_percent < 0 
        8     or pack_efficiency_percent > 100
        9  
       10  union all
```

**Decisão**: pendente

### 6 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/staging/test_stg_wms__allocation_business_rules.sql:6` · **Effort**: 4min

> Define a constant instead of duplicating this literal 5 times.

```sql
        2  -- Validates enterprise business logic and data consistency
        3  
        4  -- Test 1: Allocated quantity should not be negative
        5  select *
>>>     6  from {{ ref('stg_wms__allocation') }}
        7  where allocated_quantity < 0
        8  
        9  union all
       10  
```

**Decisão**: pendente

### 7 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 8 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 9 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 10 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.

**Decisão**: pendente

### 11 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente
