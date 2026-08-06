# Triagem SonarCloud — flext-sh/flext-dbt-oracle-wms

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.5`

## Resumo

**11 issues** — BLOCKER 0, CRITICAL 6, MAJOR 4, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 7

| regra | issues |
|---|---|
| `plsql:S1192` | 5 |
| `githubactions:S8233` | 2 |
| `python:S1192` | 1 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_dbt_oracle_wms/_utilities/client.py` | 39 | |
| 2 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/data_quality/test_cross_model_consistency.sql` | 11 | |
| 3 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/data_quality/test_cross_model_consistency.sql` | 12 | |
| 4 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/data_quality/test_cross_model_consistency.sql` | 18 | |
| 5 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/marts/test_opr_wms__allocation_summary_kpis.sql` | 6 | |
| 6 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/staging/test_stg_wms__allocation_business_rules.sql` | 6 | |
| 7 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 8 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 9 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 10 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 11 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-dbt-oracle-wms.json`

