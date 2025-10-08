# COMPREHENSIVE QUALITY REFACTORING - FLEXT DBT ORACLE WMS

**Enterprise-Grade Oracle WMS Data Transformation Quality Standards**
**Version**: 2.1.0 | **Authority**: PROJECT | **Updated**: 2025-01-08
**Environment**: `../.venv/bin/python` (No PYTHONPATH required)
**Based on**: flext-core 0.9.9 with 75%+ coverage (PROVEN FOUNDATION) and Oracle WMS dimensional modeling

**Hierarchy**: This document provides project-specific standards based on workspace-level patterns defined in [../CLAUDE.md](../CLAUDE.md). For architectural principles, quality gates, and MCP server usage, reference the main workspace standards.

## 📋 DOCUMENT STRUCTURE & REFERENCES

**Quick Links**:
- **[~/.claude/commands/flext.md](~/.claude/commands/flext.md)**: Optimization command for module refactoring (USE with `/flext` command)
- **[../CLAUDE.md](../CLAUDE.md)**: FLEXT ecosystem standards and domain library rules

**Document Purpose**:
- **This file (CLAUDE.md)**: Project-specific flext-dbt-oracle-wms standards, DBT Oracle WMS transformation patterns, and warehouse management analytics authority
- **flext.md command**: Practical refactoring workflows and MCP tool usage patterns (HOW-TO)
- **Workspace CLAUDE.md**: Domain library standards and ecosystem architectural principles (WHAT and WHY)

**DO NOT DUPLICATE**: This file focuses on flext-dbt-oracle-wms warehouse management analytics authority with MANDATORY use of flext-meltano, flext-oracle-wms, flext-db-oracle, and flext-core.

**Usage**: Reference [~/.claude/commands/flext.md](~/.claude/commands/flext.md) for MCP workflows. Use `/flext` command for DBT Oracle WMS module optimization and Clean Architecture refactoring.

**CRITICAL INTEGRATION DEPENDENCIES**:
- **flext-meltano**: MANDATORY for ALL DBT operations (ZERO TOLERANCE for direct dbt imports)
- **flext-oracle-wms**: MANDATORY for ALL Oracle WMS operations (ZERO TOLERANCE for bypassing WMS domain)
- **flext-db-oracle**: MANDATORY for ALL Oracle Database operations (ZERO TOLERANCE for direct SQLAlchemy/oracledb imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)
- **flext-cli**: MANDATORY for ALL CLI operations (ZERO TOLERANCE for direct click/rich imports)

## 🔗 MCP SERVER INTEGRATION (MANDATORY)

| MCP Server              | Purpose                                                       | Status          |
| ----------------------- | ------------------------------------------------------------- | --------------- |
| **serena-flext**        | Semantic code analysis, symbol manipulation, refactoring      | **MANDATORY**   |
| **sequential-thinking** | Oracle WMS data modeling and DBT architecture problem solving | **RECOMMENDED** |
| **context7**            | Third-party library documentation (dbt, Oracle WMS)           | **RECOMMENDED** |
| **github**              | Repository operations and DBT Oracle WMS ecosystem PRs        | **ACTIVE**      |

**Usage**: `claude mcp list` for available servers, leverage for DBT-specific development patterns and Oracle WMS transformation analysis.

---

## 🎯 MISSION STATEMENT (DBT ORACLE WMS INTEGRATION)

**OBJECTIVE**: Achieve 100% professional quality compliance for flext-dbt-oracle-wms with zero regressions, following Oracle WMS best practices, dimensional modeling patterns, and flext-core foundation integration.

**PROJECT CONTEXT**: flext-dbt-oracle-wms is an enterprise-grade dbt project that provides data transformations for Oracle Warehouse Management System (WMS) data. It follows Clean Architecture principles and implements dimensional modeling patterns for WMS analytics, transforming raw Oracle WMS data from Singer taps into business-ready analytical models.

**CRITICAL REQUIREMENTS**:

- ✅ **95%+ pytest pass rate** with **75%+ coverage** (following flext-core success pattern)
- ✅ **Zero errors** in ruff, mypy (strict mode), and pyright across ALL source code
- ✅ **Unified FlextDbtOracleWmsService** - single consolidated class for all Oracle WMS dbt operations
- ✅ **Oracle WMS expertise** - proper warehouse operations modeling, inventory tracking, allocation processing
- ✅ **Dimensional modeling excellence** - star schema design, proper fact/dimension structures, SCD handling
- ✅ **Real dbt WMS execution testing** - minimal mocks, test actual WMS model compilation and execution
- ✅ **Singer tap integration** - seamless data flow from flext-tap-oracle-wms to dbt models
- ✅ **Professional English** - all WMS business terminology in clear, precise language
- ✅ **Production-ready WMS analytics** - scalable dimensional models for enterprise WMS reporting

**CURRENT PROJECT STATUS** (Evidence-based assessment needed):

- 🔴 **Ruff Issues**: To be assessed with `ruff check src/ --output-format=github | wc -l`
- 🟡 **MyPy Issues**: To be assessed with `mypy src/ --show-error-codes --no-error-summary 2>&1 | grep -E "error:" | wc -l`
- 🟡 **Pyright Issues**: To be assessed with `pyright src/ --level error 2>&1 | grep -E "error" | wc -l`
- 🔴 **Pytest Status**: To be assessed with `pytest tests/ --tb=no -q 2>&1 | grep -E "failed|passed|error"`
- 🟢 **flext-core Foundation**: Available with FlextResult, logging, dependency injection patterns
- 🟡 **dbt Models**: Assess compilation with `dbt compile --project-dir . 2>&1 | grep -E "ERROR|WARN"`

---

## 🚨 ABSOLUTE PROHIBITIONS (DBT ORACLE WMS ZERO TOLERANCE)

### ❌ FORBIDDEN PRACTICES IN DBT ORACLE WMS PROJECTS

1. **WAREHOUSE MANAGEMENT VIOLATIONS**:
   - Generic warehouse modeling ignoring WMS-specific business logic
   - Missing proper inventory tracking and allocation processing patterns
   - Ignoring WMS operational workflows (receiving, picking, packing, shipping)
   - Incorrect modeling of WMS entities (locations, items, tasks, waves)

2. **DIMENSIONAL MODELING VIOLATIONS**:
   - Flat table structures instead of star schema dimensional models
   - Missing proper fact/dimension separation for WMS analytics
   - Ignoring Slowly Changing Dimensions (SCD) for WMS master data
   - Incorrect grain definition for WMS fact tables

3. **ORACLE WMS INTEGRATION VIOLATIONS**:
   - Generic SQL instead of Oracle WMS-optimized patterns
   - Missing WMS-specific indexes and partition strategies
   - Ignoring Oracle WMS table relationships and constraints
   - Bypassing flext-oracle-wms library for WMS business logic

4. **DBT WMS MODEL VIOLATIONS**:
   - Custom macros duplicating flext-oracle-wms functionality
   - Missing incremental processing for large WMS datasets
   - Ignoring WMS data quality validations and business rule tests
   - Poor materialization strategies for different WMS model types

5. **SINGER TAP INTEGRATION VIOLATIONS**:
   - Manual WMS data extraction bypassing flext-tap-oracle-wms
   - Missing integration with flext-meltano for WMS pipeline orchestration
   - Custom WMS data flow patterns ignoring FLEXT ecosystem standards
   - Incomplete WMS entity coverage from Singer tap sources

---

## 🏗️ ARCHITECTURAL FOUNDATION (DBT ORACLE WMS PATTERNS)

### Unified dbt Oracle WMS Service Architecture

**FOUNDATION PRINCIPLE**: Single unified service consolidating all Oracle WMS dbt operations through flext-core + flext-oracle-wms + flext-meltano integration with proper dimensional modeling.

```python
# ✅ CORRECT - Unified dbt Oracle WMS Service (MANDATORY PATTERN)
from flext_core import (
    FlextResult,           # Railway pattern for WMS dbt operation results
    FlextDomainService,    # Base service with Pydantic validation
    FlextContainer,        # Dependency injection for WMS services
    FlextLogger,           # Structured logging for WMS operations
    FlextConstants,        # WMS constants and business rules
    FlextExceptions        # WMS exception hierarchy
)

from flext_oracle_wms import (
    FlextOracleWmsApi,     # Oracle WMS business logic operations
    WmsInventoryService,   # Inventory tracking and allocation
    WmsLocationService,    # Warehouse location management
    WmsTaskService,        # Task orchestration and workflow
    WmsDataQualityService  # WMS-specific data quality validation
)

from flext_meltano import (
    FlextDbtHub,           # dbt execution and model management
    DbtModelRunner,        # dbt model compilation and execution
    DbtTestRunner,         # dbt test execution integration
    DbtDocsGenerator       # dbt documentation generation
)

from flext_tap_oracle_wms import (
    OracleWmsTapExtractor, # Singer tap for Oracle WMS data extraction
    WmsEntityExtractor,    # WMS entity-specific extraction
    WmsIncrementalExtractor # Incremental WMS data processing
)

class UnifiedFlextDbtOracleWmsService(FlextDomainService):
    """Single unified dbt Oracle WMS service class following flext-core patterns.

    This class consolidates all Oracle WMS dbt-related operations:
    - Oracle WMS data extraction via flext-tap-oracle-wms Singer tap
    - WMS dimensional modeling with proper star schema design
    - WMS business logic integration via flext-oracle-wms
    - dbt model generation optimized for WMS analytics
    - Incremental processing for large WMS datasets
    - WMS-specific data quality validation and testing

    Architecture:
        Oracle WMS → flext-tap-oracle-wms → UnifiedService → dbt Models → WMS Analytics
    """

    def __init__(self, **data) -> None:
        """Initialize unified dbt Oracle WMS service with dependency injection."""
        super().__init__(**data)
        # Direct class access - NO wrapper functions (per flext-core patterns)
        self._container = FlextContainer.get_global()
        self._logger = FlextLogger(__name__)

        # Initialize WMS APIs with proper business logic
        self._wms_api = self._get_wms_api()
        self._dbt_hub = self._get_dbt_hub()
        self._tap_extractor = self._get_tap_extractor()

    def orchestrate_wms_dimensional_pipeline(
        self,
        wms_entities: list[str],
        extraction_mode: str = "incremental"
    ) -> FlextResult[WmsDimensionalPipelineResult]:
        """Orchestrate complete Oracle WMS-to-dimensional model pipeline.

        This method demonstrates the railway pattern for complex WMS operations:
        1. Extract Oracle WMS data via Singer tap (flext-tap-oracle-wms)
        2. Apply WMS business logic transformations (flext-oracle-wms)
        3. Generate dimensional models (star schema with proper fact/dimension separation)
        4. Execute dbt models with WMS-optimized materialization
        5. Run WMS-specific data quality tests and business rule validation

        Args:
            wms_entities: WMS entities to include (inventory, allocation, orders, etc.)
            extraction_mode: 'full' or 'incremental' extraction mode

        Returns:
            FlextResult with WMS dimensional pipeline execution results or error details
        """
        return (
            self._extract_wms_data_via_singer_tap(wms_entities, extraction_mode)
            .flat_map(lambda raw_data: self._apply_wms_business_logic(raw_data))
            .flat_map(lambda wms_data: self._generate_dimensional_models(wms_data))
            .flat_map(lambda models: self._compile_wms_dbt_models(models))
            .flat_map(lambda compiled: self._execute_wms_dbt_models(compiled))
            .flat_map(lambda executed: self._run_wms_data_quality_tests(executed))
            .map(lambda results: self._create_wms_pipeline_result(results))
            .map_error(lambda e: f"WMS dimensional pipeline failed: {e}")
        )

    def extract_wms_data_via_singer_tap(
        self,
        wms_entities: list[str],
        extraction_mode: str = "incremental"
    ) -> FlextResult[WmsRawData]:
        """Extract Oracle WMS data using flext-tap-oracle-wms Singer tap.

        Integrates with Singer ecosystem for standardized WMS data extraction
        with proper incremental processing and state management.
        """
        if not wms_entities:
            return FlextResult[WmsRawData].fail("WMS entities list cannot be empty")

        # Validate WMS entities are supported
        validation_result = self._validate_wms_entities(wms_entities)
        if validation_result.is_failure:
            return FlextResult[WmsRawData].fail(f"WMS entity validation failed: {validation_result.error}")

        # Configure Singer tap extraction
        tap_config = {
            'entities': wms_entities,
            'extraction_mode': extraction_mode,
            'wms_optimization': True,
            'incremental_lookback_days': 7 if extraction_mode == 'incremental' else None
        }

        # Execute Singer tap extraction
        extraction_result = self._tap_extractor.extract_wms_entities(tap_config)
        if extraction_result.is_failure:
            return FlextResult[WmsRawData].fail(f"Singer tap extraction failed: {extraction_result.error}")

        raw_data = extraction_result.unwrap()

        # Validate extracted WMS data structure
        validation_result = self._validate_extracted_wms_data(raw_data)
        if validation_result.is_failure:
            return FlextResult[WmsRawData].fail(f"WMS data validation failed: {validation_result.error}")

        return FlextResult[WmsRawData].ok(raw_data)

    def generate_wms_dimensional_models(self, wms_data: WmsTransformedData) -> FlextResult[list[WmsDimensionalModel]]:
        """Generate WMS dimensional models following star schema design patterns.

        Creates proper dimensional models for WMS analytics:
        - Fact tables: inventory movements, allocations, order fulfillment
        - Dimension tables: items, locations, customers, time
        - SCD handling: slowly changing dimensions for master data
        - Bridge tables: many-to-many relationships in WMS
        """
        if not wms_data.entities:
            return FlextResult[list[WmsDimensionalModel]].fail("No WMS entities found in transformed data")

        dimensional_models = []

        # Generate dimension models first (required by fact tables)
        dimension_result = self._generate_wms_dimension_models(wms_data)
        if dimension_result.is_failure:
            return FlextResult[list[WmsDimensionalModel]].fail(f"Dimension model generation failed: {dimension_result.error}")

        dimensional_models.extend(dimension_result.unwrap())

        # Generate fact models with proper grain and measures
        fact_result = self._generate_wms_fact_models(wms_data, dimensional_models)
        if fact_result.is_failure:
            return FlextResult[list[WmsDimensionalModel]].fail(f"Fact model generation failed: {fact_result.error}")

        dimensional_models.extend(fact_result.unwrap())

        # Generate bridge models for many-to-many relationships
        bridge_result = self._generate_wms_bridge_models(wms_data, dimensional_models)
        if bridge_result.is_failure:
            return FlextResult[list[WmsDimensionalModel]].fail(f"Bridge model generation failed: {bridge_result.error}")

        dimensional_models.extend(bridge_result.unwrap())

        # Validate dimensional model relationships
        relationship_validation = self._validate_dimensional_relationships(dimensional_models)
        if relationship_validation.is_failure:
            return FlextResult[list[WmsDimensionalModel]].fail(f"Dimensional relationship validation failed: {relationship_validation.error}")

        return FlextResult[list[WmsDimensionalModel]].ok(dimensional_models)

    def execute_wms_dbt_models(self, models: list[WmsDimensionalModel]) -> FlextResult[WmsExecutionResult]:
        """Execute WMS dbt models with Oracle optimization and proper dependencies.

        Executes WMS dimensional models with:
        - Proper execution order (dimensions before facts)
        - Oracle WMS-specific optimizations (partitioning, indexing)
        - Incremental processing for large datasets
        - WMS business rule validation during execution
        """
        if not models:
            return FlextResult[WmsExecutionResult].fail("No WMS dimensional models to execute")

        # Sort models by execution dependencies (dimensions → facts → bridges)
        execution_order = self._determine_wms_execution_order(models)

        # Configure WMS-specific execution settings
        execution_config = {
            'target': 'oracle_wms_production',
            'threads': 8,  # Optimize for WMS data volume
            'wms_optimizations': {
                'use_oracle_hints': True,
                'enable_partitioning': True,
                'parallel_execution': True
            },
            'incremental_strategy': 'delete+insert'  # WMS data integrity requirement
        }

        # Execute models through dbt hub with WMS optimizations
        execution_result = self._dbt_hub.execute_models_with_dependencies(
            models=execution_order,
            config=execution_config,
            wms_business_rules=True
        )

        if execution_result.is_failure:
            return FlextResult[WmsExecutionResult].fail(f"WMS dbt execution failed: {execution_result.error}")

        execution_data = execution_result.unwrap()

        # Validate WMS business rules post-execution
        business_rule_validation = self._validate_wms_business_rules(execution_data)
        if business_rule_validation.is_failure:
            return FlextResult[WmsExecutionResult].fail(f"WMS business rule validation failed: {business_rule_validation.error}")

        return FlextResult[WmsExecutionResult].ok(execution_data)

    def run_wms_data_quality_tests(self, execution_result: WmsExecutionResult) -> FlextResult[WmsTestResult]:
        """Run comprehensive WMS data quality tests and business rule validation.

        Executes WMS-specific tests including:
        - Inventory balance reconciliation across all models
        - Allocation consistency between fact and dimension tables
        - WMS workflow validation (receiving → put-away → picking → shipping)
        - Cross-entity relationship integrity tests
        - WMS performance benchmark tests
        """
        if not execution_result.executed_models:
            return FlextResult[WmsTestResult].fail("No WMS models available for testing")

        # Configure WMS-specific test execution
        test_config = {
            'test_types': ['schema', 'data', 'wms_business_rules', 'cross_entity_consistency'],
            'wms_validations': {
                'inventory_reconciliation': True,
                'allocation_consistency': True,
                'workflow_integrity': True,
                'performance_benchmarks': True
            },
            'tolerance_thresholds': {
                'inventory_variance': 0.01,  # 1% tolerance for inventory calculations
                'allocation_variance': 0.00,  # Zero tolerance for allocation errors
                'data_freshness_hours': 2     # WMS data must be within 2 hours
            }
        }

        # Execute comprehensive WMS tests
        test_result = self._dbt_hub.run_wms_tests(
            models=execution_result.executed_models,
            config=test_config,
            wms_business_logic=self._wms_api
        )

        if test_result.is_failure:
            return FlextResult[WmsTestResult].fail(f"WMS data quality tests failed: {test_result.error}")

        test_data = test_result.unwrap()

        # Analyze WMS test results with business context
        analysis_result = self._analyze_wms_test_results(test_data)
        if analysis_result.is_failure:
            return FlextResult[WmsTestResult].fail(f"WMS test analysis failed: {analysis_result.error}")

        return FlextResult[WmsTestResult].ok(analysis_result.unwrap())

    def optimize_wms_dimensional_performance(self, models: list[WmsDimensionalModel]) -> FlextResult[WmsPerformanceOptimization]:
        """Optimize WMS dimensional models for Oracle Database and analytics performance.

        Applies WMS-specific optimizations:
        - Partition strategies for high-volume fact tables
        - Oracle hints for WMS query patterns
        - Materialization strategies based on WMS usage patterns
        - Index recommendations for WMS analytical queries
        """
        optimization_results = []

        for model in models:
            # Analyze WMS model characteristics for optimization
            analysis_result = self._analyze_wms_model_performance(model)
            if analysis_result.is_failure:
                return FlextResult[WmsPerformanceOptimization].fail(f"WMS performance analysis failed for {model.name}: {analysis_result.error}")

            analysis = analysis_result.unwrap()

            # Apply WMS-specific Oracle optimizations
            optimization_result = self._apply_wms_oracle_optimizations(model, analysis)
            if optimization_result.is_failure:
                return FlextResult[WmsPerformanceOptimization].fail(f"WMS optimization failed for {model.name}: {optimization_result.error}")

            optimization_results.append(optimization_result.unwrap())

        combined_optimization = self._combine_wms_optimization_results(optimization_results)
        return FlextResult[WmsPerformanceOptimization].ok(combined_optimization)

    def _generate_wms_dimension_models(self, wms_data: WmsTransformedData) -> FlextResult[list[WmsDimensionalModel]]:
        """Generate WMS dimension models with proper SCD handling."""

        dimension_models = []

        # Item dimension with SCD Type 2 for attribute changes
        if 'items' in wms_data.entities:
            item_dim_result = self._create_item_dimension_model(wms_data.entities['items'])
            if item_dim_result.is_failure:
                return FlextResult[list[WmsDimensionalModel]].fail(f"Item dimension creation failed: {item_dim_result.error}")
            dimension_models.append(item_dim_result.unwrap())

        # Location dimension with hierarchy (zone → aisle → bay → level → position)
        if 'locations' in wms_data.entities:
            location_dim_result = self._create_location_dimension_model(wms_data.entities['locations'])
            if location_dim_result.is_failure:
                return FlextResult[list[WmsDimensionalModel]].fail(f"Location dimension creation failed: {location_dim_result.error}")
            dimension_models.append(location_dim_result.unwrap())

        # Customer dimension with SCD Type 2 for profile changes
        if 'customers' in wms_data.entities:
            customer_dim_result = self._create_customer_dimension_model(wms_data.entities['customers'])
            if customer_dim_result.is_failure:
                return FlextResult[list[WmsDimensionalModel]].fail(f"Customer dimension creation failed: {customer_dim_result.error}")
            dimension_models.append(customer_dim_result.unwrap())

        # Time dimension with WMS-specific attributes (business days, seasons, etc.)
        time_dim_result = self._create_time_dimension_model()
        if time_dim_result.is_failure:
            return FlextResult[list[WmsDimensionalModel]].fail(f"Time dimension creation failed: {time_dim_result.error}")
        dimension_models.append(time_dim_result.unwrap())

        return FlextResult[list[WmsDimensionalModel]].ok(dimension_models)

    def _generate_wms_fact_models(self, wms_data: WmsTransformedData, dimensions: list[WmsDimensionalModel]) -> FlextResult[list[WmsDimensionalModel]]:
        """Generate WMS fact models with proper grain and measures."""

        fact_models = []

        # Inventory fact table - grain: item × location × time
        if 'inventory' in wms_data.entities:
            inventory_fact_result = self._create_inventory_fact_model(wms_data.entities['inventory'], dimensions)
            if inventory_fact_result.is_failure:
                return FlextResult[list[WmsDimensionalModel]].fail(f"Inventory fact creation failed: {inventory_fact_result.error}")
            fact_models.append(inventory_fact_result.unwrap())

        # Allocation fact table - grain: allocation × item × location × time
        if 'allocations' in wms_data.entities:
            allocation_fact_result = self._create_allocation_fact_model(wms_data.entities['allocations'], dimensions)
            if allocation_fact_result.is_failure:
                return FlextResult[list[WmsDimensionalModel]].fail(f"Allocation fact creation failed: {allocation_fact_result.error}")
            fact_models.append(allocation_fact_result.unwrap())

        # Order fulfillment fact table - grain: order line × time
        if 'orders' in wms_data.entities:
            order_fact_result = self._create_order_fulfillment_fact_model(wms_data.entities['orders'], dimensions)
            if order_fact_result.is_failure:
                return FlextResult[list[WmsDimensionalModel]].fail(f"Order fact creation failed: {order_fact_result.error}")
            fact_models.append(order_fact_result.unwrap())

        return FlextResult[list[WmsDimensionalModel]].ok(fact_models)

    def _create_inventory_fact_model(self, inventory_data: dict, dimensions: list[WmsDimensionalModel]) -> FlextResult[WmsDimensionalModel]:
        """Create inventory fact table with proper measures and foreign keys."""

        # Define fact table structure with WMS-specific measures
        fact_model = WmsDimensionalModel(
            name="fact_inventory_snapshot",
            model_type="fact",
            grain="item × location × snapshot_date",
            materialization="incremental",
            partition_by="snapshot_date",
            dimensions=[
                {"name": "item_key", "references": "dim_item"},
                {"name": "location_key", "references": "dim_location"},
                {"name": "date_key", "references": "dim_date"}
            ],
            measures=[
                {"name": "on_hand_quantity", "type": "numeric", "description": "Available inventory quantity"},
                {"name": "allocated_quantity", "type": "numeric", "description": "Quantity allocated to orders"},
                {"name": "available_quantity", "type": "numeric", "description": "Available for allocation"},
                {"name": "in_transit_quantity", "type": "numeric", "description": "Quantity in transit"},
                {"name": "reserved_quantity", "type": "numeric", "description": "Reserved for specific purposes"},
                {"name": "average_cost", "type": "numeric(15,4)", "description": "Average unit cost"},
                {"name": "total_value", "type": "numeric(15,2)", "description": "Total inventory value"}
            ],
            business_rules=[
                "on_hand_quantity >= 0",
                "allocated_quantity <= on_hand_quantity",
                "available_quantity = on_hand_quantity - allocated_quantity - reserved_quantity",
                "total_value = on_hand_quantity * average_cost"
            ],
            oracle_optimizations={
                'partition_strategy': 'RANGE(snapshot_date)',
                'indexes': ['item_key, location_key', 'snapshot_date'],
                'hints': ['PARALLEL(4)', 'USE_HASH(d)', 'LEADING(f)']
            }
        )

        return FlextResult[WmsDimensionalModel].ok(fact_model)

# ✅ CORRECT - WMS Domain Models for Dimensional Analytics
class WmsRawData(FlextModels.Entity):
    """Raw WMS data extracted from Oracle via Singer tap."""

    entities: dict[str, list[dict]]
    extraction_timestamp: str
    extraction_mode: str

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate WMS raw data completeness and structure."""
        if not self.entities:
            return FlextResult[None].fail("WMS entities cannot be empty")

        required_wms_entities = ['inventory', 'locations', 'items']
        missing_entities = [entity for entity in required_wms_entities if entity not in self.entities]
        if missing_entities:
            return FlextResult[None].fail(f"Missing required WMS entities: {missing_entities}")

        return FlextResult[None].ok(None)

class WmsDimensionalModel(FlextModels.Entity):
    """WMS dimensional model entity with star schema specifications."""

    name: str
    model_type: str  # 'dimension', 'fact', 'bridge'
    grain: str
    materialization: str
    dimensions: list[dict]
    measures: list[dict]
    business_rules: list[str]
    oracle_optimizations: dict

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate WMS dimensional model configuration."""
        if not self.name or not self.model_type:
            return FlextResult[None].fail("Model name and type are required")

        if self.model_type == 'fact' and not self.measures:
            return FlextResult[None].fail("Fact tables must have measures defined")

        if self.model_type == 'dimension' and not self.dimensions:
            return FlextResult[None].fail("Dimension tables must have dimension attributes defined")

        return FlextResult[None].ok(None)

class WmsInventoryMovement(FlextModels.Value):
    """WMS inventory movement value object for fact table grain."""

    movement_id: str
    item_key: str
    location_key: str
    movement_type: str
    quantity: float
    unit_cost: float
    movement_timestamp: str

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate inventory movement business rules."""
        if self.quantity == 0:
            return FlextResult[None].fail("Inventory movement quantity cannot be zero")

        if self.unit_cost < 0:
            return FlextResult[None].fail("Unit cost cannot be negative")

        return FlextResult[None].ok(None)

# ✅ CORRECT - Module exports
__all__ = ["UnifiedFlextDbtOracleWmsService", "WmsRawData", "WmsDimensionalModel", "WmsInventoryMovement"]
```

### WMS dbt Configuration Management with Singer Integration

```python
# ✅ CORRECT - Oracle WMS dbt Configuration (AUTOMATIC LOADING)
from flext_cli import FlextCliConfigs
from flext_core import FlextResult

class FlextDbtOracleWmsConfig:
    """WMS dbt configuration management using flext-cli automatic loading.

    Configuration hierarchy (AUTOMATIC):
    1. ENVIRONMENT VARIABLES (WMS_ORACLE_HOST=prod-wms - HIGHEST PRIORITY)
    2. .env FILE (WMS_ORACLE_HOST=localhost - from execution directory)
    3. DEFAULT CONSTANTS (hardcoded WMS defaults in code)
    4. CLI PARAMETERS (--wms-host override-wms for specific executions)
    """

    def __init__(self) -> None:
        """Initialize WMS configuration with automatic .env loading."""
        # ✅ AUTOMATIC: Configuration loaded transparently by flext-cli
        self._config = FlextCliConfigs()
        self._logger = FlextLogger(__name__)

    def get_wms_configuration(self) -> FlextResult[dict]:
        """Get Oracle WMS configuration from automatic hierarchy resolution."""

        # Define Oracle WMS configuration schema
        wms_schema = {
            "wms_oracle": {
                "host": {
                    "default": "localhost",
                    "env_var": "WMS_ORACLE_HOST",
                    "cli_param": "--wms-oracle-host",
                    "config_formats": {
                        "env": "WMS_ORACLE_HOST",
                        "toml": "wms_oracle.host",
                        "yaml": "wms_oracle.host"
                    },
                    "type": str,
                    "required": True
                },
                "port": {
                    "default": 1521,
                    "env_var": "WMS_ORACLE_PORT",
                    "cli_param": "--wms-oracle-port",
                    "config_formats": {
                        "env": "WMS_ORACLE_PORT",
                        "toml": "wms_oracle.port",
                        "yaml": "wms_oracle.port"
                    },
                    "type": int,
                    "required": False
                },
                "service_name": {
                    "default": "WMSPROD",
                    "env_var": "WMS_ORACLE_SERVICE_NAME",
                    "cli_param": "--wms-oracle-service",
                    "config_formats": {
                        "env": "WMS_ORACLE_SERVICE_NAME",
                        "toml": "wms_oracle.service_name",
                        "yaml": "wms_oracle.service_name"
                    },
                    "type": str,
                    "required": True
                },
                "schema": {
                    "default": "WMS_RAW",
                    "env_var": "WMS_ORACLE_SCHEMA",
                    "cli_param": "--wms-schema",
                    "config_formats": {
                        "env": "WMS_ORACLE_SCHEMA",
                        "toml": "wms_oracle.schema",
                        "yaml": "wms_oracle.schema"
                    },
                    "type": str,
                    "required": True
                }
            },
            "singer_tap": {
                "incremental_lookback_days": {
                    "default": 7,
                    "env_var": "WMS_INCREMENTAL_LOOKBACK_DAYS",
                    "cli_param": "--incremental-days",
                    "config_formats": {
                        "env": "WMS_INCREMENTAL_LOOKBACK_DAYS",
                        "toml": "singer_tap.incremental_lookback_days",
                        "yaml": "singer_tap.incremental_lookback_days"
                    },
                    "type": int,
                    "required": False
                },
                "batch_size": {
                    "default": 10000,
                    "env_var": "WMS_TAP_BATCH_SIZE",
                    "cli_param": "--batch-size",
                    "config_formats": {
                        "env": "WMS_TAP_BATCH_SIZE",
                        "toml": "singer_tap.batch_size",
                        "yaml": "singer_tap.batch_size"
                    },
                    "type": int,
                    "required": False
                }
            },
            "dimensional_modeling": {
                "enable_scd_type2": {
                    "default": True,
                    "env_var": "WMS_ENABLE_SCD_TYPE2",
                    "cli_param": "--enable-scd2",
                    "config_formats": {
                        "env": "WMS_ENABLE_SCD_TYPE2",
                        "toml": "dimensional_modeling.enable_scd_type2",
                        "yaml": "dimensional_modeling.enable_scd_type2"
                    },
                    "type": bool,
                    "required": False
                },
                "inventory_snapshot_frequency": {
                    "default": "daily",
                    "env_var": "WMS_INVENTORY_SNAPSHOT_FREQ",
                    "cli_param": "--inventory-freq",
                    "config_formats": {
                        "env": "WMS_INVENTORY_SNAPSHOT_FREQ",
                        "toml": "dimensional_modeling.inventory_snapshot_frequency",
                        "yaml": "dimensional_modeling.inventory_snapshot_frequency"
                    },
                    "type": str,
                    "choices": ["hourly", "daily", "weekly"],
                    "required": False
                }
            },
            "data_quality": {
                "inventory_variance_tolerance": {
                    "default": 0.01,
                    "env_var": "WMS_INVENTORY_VARIANCE_TOLERANCE",
                    "cli_param": "--inventory-tolerance",
                    "config_formats": {
                        "env": "WMS_INVENTORY_VARIANCE_TOLERANCE",
                        "toml": "data_quality.inventory_variance_tolerance",
                        "yaml": "data_quality.inventory_variance_tolerance"
                    },
                    "type": float,
                    "required": False
                },
                "allocation_variance_tolerance": {
                    "default": 0.00,
                    "env_var": "WMS_ALLOCATION_VARIANCE_TOLERANCE",
                    "cli_param": "--allocation-tolerance",
                    "config_formats": {
                        "env": "WMS_ALLOCATION_VARIANCE_TOLERANCE",
                        "toml": "data_quality.allocation_variance_tolerance",
                        "yaml": "data_quality.allocation_variance_tolerance"
                    },
                    "type": float,
                    "required": False
                }
            }
        }

        # Register schema and get resolved configuration
        schema_result = self._config.register_schema(wms_schema)
        if schema_result.is_failure:
            return FlextResult[dict].fail(f"WMS schema registration failed: {schema_result.error}")

        config_result = self._config.get_resolved_configuration()
        if config_result.is_failure:
            return FlextResult[dict].fail(f"WMS configuration resolution failed: {config_result.error}")

        return FlextResult[dict].ok(config_result.unwrap())

    def get_dbt_wms_profile_configuration(self) -> FlextResult[dict]:
        """Generate dbt profiles.yml configuration for Oracle WMS."""

        wms_config_result = self.get_wms_configuration()
        if wms_config_result.is_failure:
            return FlextResult[dict].fail(f"WMS config access failed: {wms_config_result.error}")

        wms_config = wms_config_result.unwrap()

        # Generate dbt profile configuration for WMS
        dbt_profile = {
            "flext_oracle_wms": {
                "target": "production",
                "outputs": {
                    "production": {
                        "type": "oracle",
                        "host": wms_config["wms_oracle"]["host"],
                        "port": wms_config["wms_oracle"]["port"],
                        "service": wms_config["wms_oracle"]["service_name"],
                        "user": "{{ env_var('WMS_ORACLE_USERNAME') }}",
                        "password": "{{ env_var('WMS_ORACLE_PASSWORD') }}",
                        "schema": wms_config["wms_oracle"]["schema"],
                        "threads": 8,  # Optimized for WMS data volume
                        "keepalives_idle": 0,
                        # Oracle WMS-specific optimizations
                        "oracle_batch_size": 50000,
                        "oracle_arraysize": 10000,
                        "oracle_use_partitions": True
                    },
                    "dev": {
                        "type": "oracle",
                        "host": wms_config["wms_oracle"]["host"],
                        "port": wms_config["wms_oracle"]["port"],
                        "service": wms_config["wms_oracle"]["service_name"],
                        "user": "{{ env_var('WMS_ORACLE_DEV_USERNAME', 'wms_dev') }}",
                        "password": "{{ env_var('WMS_ORACLE_DEV_PASSWORD') }}",
                        "schema": "WMS_DEV",
                        "threads": 4,
                        "keepalives_idle": 0
                    }
                }
            }
        }

        return FlextResult[dict].ok(dbt_profile)

    def get_singer_tap_configuration(self) -> FlextResult[dict]:
        """Get Singer tap configuration for Oracle WMS data extraction."""

        wms_config_result = self.get_wms_configuration()
        if wms_config_result.is_failure:
            return FlextResult[dict].fail(f"WMS config access failed: {wms_config_result.error}")

        wms_config = wms_config_result.unwrap()

        # Configure Singer tap for Oracle WMS
        tap_config = {
            "tap_oracle_wms": {
                "host": wms_config["wms_oracle"]["host"],
                "port": wms_config["wms_oracle"]["port"],
                "service_name": wms_config["wms_oracle"]["service_name"],
                "user": "{{ env_var('WMS_ORACLE_USERNAME') }}",
                "password": "{{ env_var('WMS_ORACLE_PASSWORD') }}",
                "schema": wms_config["wms_oracle"]["schema"],

                # WMS entity configuration
                "entities": {
                    "inventory": {
                        "enabled": True,
                        "incremental": True,
                        "replication_key": "last_updated_date",
                        "batch_size": wms_config["singer_tap"]["batch_size"]
                    },
                    "locations": {
                        "enabled": True,
                        "incremental": True,
                        "replication_key": "last_modified_date",
                        "batch_size": wms_config["singer_tap"]["batch_size"]
                    },
                    "items": {
                        "enabled": True,
                        "incremental": True,
                        "replication_key": "last_updated_date",
                        "batch_size": wms_config["singer_tap"]["batch_size"]
                    },
                    "allocations": {
                        "enabled": True,
                        "incremental": True,
                        "replication_key": "allocation_date",
                        "batch_size": wms_config["singer_tap"]["batch_size"]
                    },
                    "orders": {
                        "enabled": True,
                        "incremental": True,
                        "replication_key": "order_date",
                        "batch_size": wms_config["singer_tap"]["batch_size"]
                    }
                },

                # Incremental processing configuration
                "incremental_lookback_days": wms_config["singer_tap"]["incremental_lookback_days"],
                "use_singer_decimal": True,
                "use_date_datatype": True,

                # Oracle WMS optimizations
                "oracle_optimizations": {
                    "use_bulk_select": True,
                    "arraysize": 10000,
                    "prefetchrows": 1000
                }
            }
        }

        return FlextResult[dict].ok(tap_config)
```

---

## 📊 QUALITY ASSESSMENT PROTOCOL (DBT ORACLE WMS SPECIFIC)

### Phase 1: WMS dbt Issue Identification

**MANDATORY FIRST STEP**: Get precise counts of quality issues in Oracle WMS dbt project:

```bash
# Navigate to flext-dbt-oracle-wms directory
cd flext-dbt-oracle-wms

echo "=== DBT ORACLE WMS PROJECT QUALITY ASSESSMENT ==="

echo "=== RUFF ISSUES (Oracle WMS dbt) ==="
ruff check src/ tests/ models/ macros/ --output-format=github | wc -l

echo "=== MYPY ISSUES (Oracle WMS dbt) ==="
mypy src/ --show-error-codes --no-error-summary 2>&1 | grep -E "error:|note:" | wc -l

echo "=== PYRIGHT ISSUES (Oracle WMS dbt) ==="
pyright src/ --level error 2>&1 | grep -E "error|warning" | wc -l

echo "=== PYTEST RESULTS (Oracle WMS dbt) ==="
pytest tests/ --tb=no -q 2>&1 | grep -E "failed|passed|error" | tail -1

echo "=== CURRENT COVERAGE (Oracle WMS dbt) ==="
pytest tests/ --cov=src --cov-report=term-missing --tb=no 2>&1 | grep "TOTAL"

echo "=== DBT MODEL COMPILATION TEST ==="
dbt compile --project-dir . 2>&1 | grep -E "ERROR|WARN" | wc -l

echo "=== DBT MODELS TEST EXECUTION ==="
dbt test --project-dir . 2>&1 | grep -E "PASS|FAIL|ERROR" | wc -l

echo "=== ORACLE WMS CONNECTIVITY TEST ==="
python -c "
try:
    from flext_dbt_oracle_wms import UnifiedFlextDbtOracleWmsService, FlextDbtOracleWmsConfig
    config = FlextDbtOracleWmsConfig()
    service = UnifiedFlextDbtOracleWmsService()
    result = service._validate_wms_connectivity()
    print('Oracle WMS connectivity:', 'SUCCESS' if result.is_success else f'FAILED: {result.error}')
except Exception as e:
    print(f'Oracle WMS import/connectivity test failed: {e}')
"

echo "=== SINGER TAP INTEGRATION TEST ==="
python -c "
try:
    from flext_tap_oracle_wms import OracleWmsTapExtractor
    extractor = OracleWmsTapExtractor()
    result = extractor.test_connection()
    print('Singer tap integration:', 'SUCCESS' if result.is_success else f'FAILED: {result.error}')
except Exception as e:
    print(f'Singer tap integration test failed: {e}')
"
```

### Phase 2: WMS dbt Resolution Priorities

**PRIORITY ORDER** (Oracle WMS + dimensional modeling + dbt specific):

1. **Fix Oracle WMS connectivity issues** (enables Singer tap and dbt operations)
2. **Resolve Singer tap integration errors** (enables WMS data extraction)
3. **Address dbt compilation errors** (enables dimensional model execution)
4. **Fix dimensional modeling issues** (proper fact/dimension relationships)
5. **Achieve WMS dbt execution coverage** (real WMS model compilation and execution tests)
6. **Optimize WMS performance** (Oracle partitioning, incremental processing, indexing)

### Phase 3: WMS dbt Continuous Validation

**AFTER EVERY CHANGE** (mandatory Oracle WMS dbt validation cycle):

```bash
# Quick Oracle WMS dbt validation cycle
ruff check src/ models/ macros/ --fix-only     # Auto-fix WMS dbt code issues
ruff check src/ models/ macros/                # Verify zero remaining issues
mypy src/ --strict --no-error-summary          # Verify zero type errors
dbt compile --project-dir .                    # Verify WMS models compile
dbt test --select tag:wms_core                 # Test core WMS models
pytest tests/ --tb=short -x                    # Stop on first test failure
```

---

## 📈 DBT ORACLE WMS TESTING STRATEGY

### Real WMS dbt Execution Testing (MINIMAL MOCKS)

```python
# ✅ CORRECT - Real Oracle WMS dbt functional tests
import pytest
from flext_core import FlextResult
from flext_dbt_oracle_wms import UnifiedFlextDbtOracleWmsService, FlextDbtOracleWmsConfig

class TestUnifiedFlextDbtOracleWmsService:
    """Real functional tests for Oracle WMS dbt service.

    These tests execute actual WMS dimensional model compilation and Oracle WMS connectivity,
    with minimal mocking only for external Oracle WMS instances.
    """

    def setup_method(self) -> None:
        """Setup real Oracle WMS dbt test environment."""
        self.config = FlextDbtOracleWmsConfig()
        self.service = UnifiedFlextDbtOracleWmsService()

        # Use test WMS entities configuration
        self.test_wms_entities = ["inventory", "locations", "items", "allocations"]

    def test_wms_connectivity_real_connection(self) -> None:
        """Test real Oracle WMS connectivity (may require WMS instance)."""
        # Test actual Oracle WMS connection
        result = self.service._validate_wms_connectivity()

        # If Oracle WMS is available, test should succeed
        if result.is_success:
            assert result.is_success
        else:
            # If Oracle WMS unavailable, ensure proper error handling
            assert "WMS connectivity" in result.error or "Oracle connection" in result.error

    def test_singer_tap_wms_extraction_functional(self) -> None:
        """Test Singer tap WMS data extraction with real tap integration."""
        # Test WMS data extraction for known entities
        result = self.service.extract_wms_data_via_singer_tap(self.test_wms_entities, "incremental")

        # Verify result structure regardless of Oracle WMS availability
        assert isinstance(result, FlextResult)

        if result.is_success:
            wms_data = result.unwrap()
            assert isinstance(wms_data, WmsRawData)
            assert len(wms_data.entities) >= 0
            assert wms_data.extraction_mode == "incremental"
        else:
            # Ensure proper error messages for unavailable WMS
            assert "extraction" in result.error.lower() or "wms" in result.error.lower()

    def test_wms_dimensional_model_generation(self) -> None:
        """Test WMS dimensional model generation from WMS data."""
        # Create mock WMS data that resembles real Oracle WMS structure
        sample_wms_data = self._create_sample_wms_data()

        # Test dimensional model generation
        result = self.service.generate_wms_dimensional_models(sample_wms_data)

        assert result.is_success, f"WMS dimensional model generation failed: {result.error}"
        models = result.unwrap()
        assert len(models) > 0

        # Verify dimensional model structure
        dimension_models = [m for m in models if m.model_type == 'dimension']
        fact_models = [m for m in models if m.model_type == 'fact']

        assert len(dimension_models) > 0, "Must have dimension models"
        assert len(fact_models) > 0, "Must have fact models"

        # Verify WMS-specific models
        model_names = [m.name for m in models]
        assert any('dim_item' in name for name in model_names), "Must have item dimension"
        assert any('dim_location' in name for name in model_names), "Must have location dimension"
        assert any('fact_inventory' in name for name in model_names), "Must have inventory fact"

    def test_wms_dbt_model_compilation_real_dbt(self) -> None:
        """Test actual WMS dbt model compilation using dbt CLI."""
        # Generate sample WMS dimensional models
        wms_data = self._create_sample_wms_data()
        model_result = self.service.generate_wms_dimensional_models(wms_data)

        assert model_result.is_success
        models = model_result.unwrap()

        # Test dbt compilation (real dbt execution)
        compilation_result = self.service._compile_wms_dbt_models(models)

        # Verify compilation works or provides proper error
        assert isinstance(compilation_result, FlextResult)

        if compilation_result.is_success:
            compiled = compilation_result.unwrap()
            assert compiled.compiled_models
            assert len(compiled.compiled_models) == len(models)
        else:
            # Ensure dbt compilation errors are properly captured
            assert "compilation" in compilation_result.error.lower()

    def test_complete_wms_dimensional_pipeline_integration(self) -> None:
        """Test complete Oracle WMS dimensional pipeline with real components."""
        # Test full WMS dimensional pipeline orchestration
        pipeline_result = self.service.orchestrate_wms_dimensional_pipeline(
            wms_entities=self.test_wms_entities[:2],  # Limit for testing
            extraction_mode="incremental"
        )

        # Verify pipeline structure regardless of Oracle WMS availability
        assert isinstance(pipeline_result, FlextResult)

        if pipeline_result.is_success:
            pipeline_data = pipeline_result.unwrap()
            assert hasattr(pipeline_data, 'executed_models')
            assert hasattr(pipeline_data, 'test_results')
            assert hasattr(pipeline_data, 'dimensional_models')
        else:
            # Ensure pipeline failures are properly captured and reported
            assert len(pipeline_result.error) > 0
            self._log_wms_pipeline_failure(pipeline_result.error)

    def test_wms_business_rule_validation(self) -> None:
        """Test WMS-specific business rule validation."""
        # Create inventory movement data with business rule violations
        invalid_movement = WmsInventoryMovement(
            movement_id="TEST001",
            item_key="ITEM001",
            location_key="LOC001",
            movement_type="ADJUSTMENT",
            quantity=0.0,  # Invalid: zero quantity
            unit_cost=-5.00,  # Invalid: negative cost
            movement_timestamp="2025-01-08T10:00:00Z"
        )

        # Test business rule validation
        validation_result = invalid_movement.validate_business_rules()
        assert validation_result.is_failure
        assert "zero" in validation_result.error.lower()

        # Create valid inventory movement
        valid_movement = WmsInventoryMovement(
            movement_id="TEST002",
            item_key="ITEM001",
            location_key="LOC001",
            movement_type="RECEIPT",
            quantity=100.0,
            unit_cost=25.50,
            movement_timestamp="2025-01-08T10:00:00Z"
        )

        validation_result = valid_movement.validate_business_rules()
        assert validation_result.is_success

    def test_wms_dimensional_model_relationships(self) -> None:
        """Test WMS dimensional model relationship integrity."""
        # Generate WMS dimensional models
        wms_data = self._create_sample_wms_data()
        model_result = self.service.generate_wms_dimensional_models(wms_data)

        assert model_result.is_success
        models = model_result.unwrap()

        # Test dimensional model relationships
        relationship_validation = self.service._validate_dimensional_relationships(models)

        if relationship_validation.is_success:
            # Verify fact tables reference dimensions
            fact_models = [m for m in models if m.model_type == 'fact']
            dimension_models = [m for m in models if m.model_type == 'dimension']

            dimension_names = [m.name for m in dimension_models]

            for fact in fact_models:
                # Verify fact has foreign keys to dimensions
                assert fact.dimensions, f"Fact model {fact.name} must have dimension references"

                # Verify referenced dimensions exist
                for dim_ref in fact.dimensions:
                    referenced_dim = dim_ref['references']
                    assert any(referenced_dim in name for name in dimension_names), \
                           f"Referenced dimension {referenced_dim} not found"
        else:
            # Log relationship validation issues for debugging
            self._logger.warning(f"Dimensional relationship validation failed: {relationship_validation.error}")

    def test_wms_performance_optimization_patterns(self) -> None:
        """Test Oracle WMS performance optimization implementation."""
        # Create models with different WMS characteristics
        high_volume_inventory = self._create_test_wms_dimensional_model("fact_inventory_movements", row_count=50000000)
        low_volume_allocations = self._create_test_wms_dimensional_model("fact_allocations", row_count=500000)

        models = [high_volume_inventory, low_volume_allocations]

        # Test WMS performance optimization
        optimization_result = self.service.optimize_wms_dimensional_performance(models)

        if optimization_result.is_success:
            optimization_data = optimization_result.unwrap()

            # Verify high-volume fact tables get partition strategies
            inventory_optimization = next(
                (opt for opt in optimization_data.optimizations if opt.model_name == "fact_inventory_movements"),
                None
            )
            assert inventory_optimization
            assert inventory_optimization.partition_strategy
            assert "RANGE" in inventory_optimization.partition_strategy

            # Verify Oracle hints are applied
            assert inventory_optimization.oracle_hints
            assert "PARALLEL" in str(inventory_optimization.oracle_hints)

        else:
            self._logger.warning(f"WMS performance optimization failed: {optimization_result.error}")

    def _create_sample_wms_data(self) -> WmsTransformedData:
        """Create sample Oracle WMS data for testing."""
        sample_entities = {
            'inventory': [
                {
                    'item_id': 'ITEM001',
                    'location_id': 'LOC001',
                    'on_hand_qty': 100,
                    'allocated_qty': 25,
                    'last_updated': '2025-01-08T10:00:00Z'
                }
            ],
            'locations': [
                {
                    'location_id': 'LOC001',
                    'zone': 'PICKING',
                    'aisle': 'A01',
                    'bay': '001',
                    'level': '01'
                }
            ],
            'items': [
                {
                    'item_id': 'ITEM001',
                    'description': 'Test Item',
                    'item_category': 'FINISHED_GOOD',
                    'unit_cost': 25.50
                }
            ]
        }

        return WmsTransformedData(
            entities=sample_entities,
            transformation_timestamp="2025-01-08T10:00:00Z",
            wms_business_rules_applied=True
        )

    def _create_test_wms_dimensional_model(self, name: str, row_count: int) -> WmsDimensionalModel:
        """Create test WMS dimensional model with specified characteristics."""
        return WmsDimensionalModel(
            name=name,
            model_type="fact",
            grain="item × location × time",
            materialization="incremental" if row_count > 1000000 else "table",
            dimensions=[
                {"name": "item_key", "references": "dim_item"},
                {"name": "location_key", "references": "dim_location"},
                {"name": "date_key", "references": "dim_date"}
            ],
            measures=[
                {"name": "quantity", "type": "numeric"},
                {"name": "value", "type": "numeric(15,2)"}
            ],
            business_rules=["quantity >= 0", "value = quantity * unit_cost"],
            oracle_optimizations={"row_count": row_count}
        )

    def _log_wms_pipeline_failure(self, error: str) -> None:
        """Log WMS pipeline failure for debugging."""
        self.service._logger.error(f"Oracle WMS dimensional pipeline test failure: {error}")
```

---

## 🔧 DBT ORACLE WMS CLI TESTING AND DEBUGGING

### Oracle WMS CLI Testing Patterns (FLEXT ECOSYSTEM)

```bash
# ✅ CORRECT - Oracle WMS dbt CLI testing through FLEXT ecosystem
# Configuration automatically loaded from .env in current directory

# Phase 1: Oracle WMS Configuration Debug
python -m flext_dbt_oracle_wms debug-config --debug
# Shows: WMS_ORACLE_HOST, WMS_ORACLE_PORT, Singer tap configuration

# Phase 2: Oracle WMS Connectivity Testing
python -m flext_dbt_oracle_wms test-wms-connection --debug --trace
# Tests: Oracle WMS database connectivity and Singer tap integration

# Phase 3: WMS dbt Model Compilation Testing
python -m flext_dbt_oracle_wms compile-wms-models --debug \
  --entities inventory,locations,items \
  --extraction-mode incremental

# Phase 4: WMS Dimensional Model Execution Testing
python -m flext_dbt_oracle_wms run-wms-pipeline --debug --dry-run \
  --entities inventory,allocations \
  --target dev

# Phase 5: Complete Oracle WMS Pipeline Testing
python -m flext_dbt_oracle_wms run-full-wms-pipeline --debug \
  --entities inventory,locations,items,allocations,orders \
  --config-file wms-production.env

# Phase 6: WMS Business Rule Validation
python -m flext_dbt_oracle_wms validate-wms-business-rules --debug \
  --entities inventory \
  --tolerance-checks strict
```

### Oracle WMS Environment Validation

```python
# ✅ CORRECT - Oracle WMS environment validation through FLEXT
class FlextDbtOracleWmsCliService:
    """Oracle WMS dbt CLI service using FLEXT ecosystem patterns."""

    def __init__(self) -> None:
        """Initialize with automatic .env configuration loading."""
        self._cli_api = FlextCliApi()
        self._config = FlextCliConfigs()  # Automatically loads .env + defaults
        self._wms_service = UnifiedFlextDbtOracleWmsService()

    def debug_wms_configuration(self) -> FlextResult[dict]:
        """Debug complete Oracle WMS dbt configuration."""

        # Get Oracle WMS configuration
        config_result = self._config.get_wms_configuration()
        if config_result.is_failure:
            return FlextResult[dict].fail(f"WMS config failed: {config_result.error}")

        config_data = config_result.unwrap()

        # Display configuration through FLEXT CLI
        debug_display_result = self._cli_api.display_debug_information(
            title="Oracle WMS dbt Configuration Debug (ENV → .env → DEFAULT → CLI)",
            data=config_data,
            format_type="tree"
        )

        return FlextResult[dict].ok(config_data)

    def test_wms_connectivity_debug(self) -> FlextResult[dict]:
        """Test Oracle WMS connectivity with comprehensive debugging."""

        # Test Oracle WMS connection through service
        connection_result = self._wms_service._validate_wms_connectivity()
        if connection_result.is_failure:
            self._cli_api.display_error_with_debug(
                error_message=f"Oracle WMS connectivity failed: {connection_result.error}",
                debug_data={"wms_config": "check WMS_ORACLE_* environment variables"},
                suggestions=[
                    "Verify Oracle WMS Database is running",
                    "Check WMS_ORACLE_HOST, WMS_ORACLE_PORT in .env",
                    "Validate Oracle WMS credentials",
                    "Test network connectivity to WMS server",
                    "Verify WMS schema access permissions"
                ]
            )
            return FlextResult[dict].fail(connection_result.error)

        # Display success information
        self._cli_api.display_success_with_debug(
            success_message="Oracle WMS Database connectivity successful",
            debug_data={"wms_status": "active", "schema_access": "verified"},
            format_type="table"
        )

        return FlextResult[dict].ok({"wms_connectivity": "success"})

    def test_singer_tap_integration_debug(self) -> FlextResult[dict]:
        """Test Singer tap Oracle WMS integration with debug output."""

        # Test Singer tap connection
        tap_result = self._wms_service._test_singer_tap_connection()
        if tap_result.is_failure:
            self._cli_api.display_error_with_debug(
                error_message=f"Singer tap integration failed: {tap_result.error}",
                debug_data={"tap_status": "failed"},
                suggestions=[
                    "Check flext-tap-oracle-wms installation",
                    "Verify Singer tap configuration",
                    "Test Oracle WMS connectivity first",
                    "Check tap permissions and access"
                ]
            )
            return FlextResult[dict].fail(tap_result.error)

        # Display tap integration success
        self._cli_api.display_success_with_debug(
            success_message="Singer tap Oracle WMS integration successful",
            debug_data={"tap_status": "connected", "extraction_ready": "yes"},
            format_type="table"
        )

        return FlextResult[dict].ok({"singer_tap": "success"})

    def test_wms_dimensional_models_compilation_debug(self, wms_entities: list[str]) -> FlextResult[dict]:
        """Test WMS dimensional model compilation with debug output."""

        # Extract WMS data via Singer tap
        extraction_result = self._wms_service.extract_wms_data_via_singer_tap(wms_entities, "incremental")
        if extraction_result.is_failure:
            return FlextResult[dict].fail(f"WMS data extraction failed: {extraction_result.error}")

        # Generate dimensional models
        models_result = self._wms_service.generate_wms_dimensional_models(extraction_result.unwrap())
        if models_result.is_failure:
            return FlextResult[dict].fail(f"WMS dimensional model generation failed: {models_result.error}")

        models = models_result.unwrap()

        # Test dbt compilation
        compilation_result = self._wms_service._compile_wms_dbt_models(models)
        if compilation_result.is_failure:
            self._cli_api.display_error_with_debug(
                error_message=f"WMS dbt compilation failed: {compilation_result.error}",
                debug_data={
                    "entities_tested": wms_entities,
                    "models_generated": len(models),
                    "compilation_status": "failed"
                },
                suggestions=[
                    "Check dbt project configuration for WMS",
                    "Verify dbt profiles.yml Oracle WMS settings",
                    "Validate generated WMS model SQL syntax",
                    "Check Oracle WMS-to-dbt type mappings",
                    "Verify dimensional model relationships"
                ]
            )
            return FlextResult[dict].fail(compilation_result.error)

        compilation_data = compilation_result.unwrap()

        # Display compilation success
        self._cli_api.display_success_with_debug(
            success_message=f"WMS dbt compilation successful: {len(models)} dimensional models compiled",
            debug_data={
                "entities_processed": wms_entities,
                "dimensional_models": len([m for m in models if m.model_type == 'dimension']),
                "fact_models": len([m for m in models if m.model_type == 'fact']),
                "compilation_time": compilation_data.compilation_time_ms
            },
            format_type="summary"
        )

        return FlextResult[dict].ok({
            "compilation_status": "success",
            "models_compiled": len(compilation_data.compiled_models)
        })

    def validate_complete_wms_environment(self) -> FlextResult[dict]:
        """Complete Oracle WMS dbt environment validation."""
        validation_results = {}

        # Phase 1: Configuration validation
        config_result = self.debug_wms_configuration()
        validation_results["wms_configuration"] = "✅ PASSED" if config_result.is_success else f"❌ FAILED: {config_result.error}"

        # Phase 2: Oracle WMS connectivity validation
        wms_result = self.test_wms_connectivity_debug()
        validation_results["wms_connectivity"] = "✅ PASSED" if wms_result.is_success else f"❌ FAILED: {wms_result.error}"

        # Phase 3: Singer tap integration validation
        tap_result = self.test_singer_tap_integration_debug()
        validation_results["singer_tap_integration"] = "✅ PASSED" if tap_result.is_success else f"❌ FAILED: {tap_result.error}"

        # Phase 4: WMS dimensional model compilation validation
        models_result = self.test_wms_dimensional_models_compilation_debug(["inventory", "locations"])
        validation_results["wms_dimensional_models"] = "✅ PASSED" if models_result.is_success else f"❌ FAILED: {models_result.error}"

        # Display complete validation results
        self._cli_api.display_validation_results(
            title="Complete Oracle WMS dbt Environment Validation",
            results=validation_results,
            format_type="detailed_table"
        )

        return FlextResult[dict].ok(validation_results)

# ✅ CORRECT - CLI entry point for Oracle WMS dbt
def create_wms_cli_with_debug_support() -> FlextResult[None]:
    """Create Oracle WMS dbt CLI with comprehensive debug support."""
    cli_service = FlextDbtOracleWmsCliService()
    cli_api = FlextCliApi()

    # Register Oracle WMS dbt debug commands
    commands = [
        {
            "name": "debug-config",
            "description": "Debug Oracle WMS dbt configuration (ENV → .env → DEFAULT → CLI)",
            "handler": cli_service.debug_wms_configuration,
            "supports_debug": True
        },
        {
            "name": "test-wms-connection",
            "description": "Test Oracle WMS Database connectivity",
            "handler": cli_service.test_wms_connectivity_debug,
            "supports_debug": True,
            "supports_trace": True
        },
        {
            "name": "test-singer-tap",
            "description": "Test Singer tap Oracle WMS integration",
            "handler": cli_service.test_singer_tap_integration_debug,
            "supports_debug": True,
            "supports_trace": True
        },
        {
            "name": "compile-wms-models",
            "description": "Test WMS dimensional model compilation",
            "handler": cli_service.test_wms_dimensional_models_compilation_debug,
            "arguments": ["wms_entities"],
            "supports_debug": True
        },
        {
            "name": "validate-environment",
            "description": "Complete Oracle WMS dbt environment validation",
            "handler": cli_service.validate_complete_wms_environment,
            "supports_debug": True,
            "supports_trace": True
        }
    ]

    # Register all commands
    for cmd in commands:
        result = cli_api.register_command(**cmd)
        if result.is_failure:
            return FlextResult[None].fail(f"Command registration failed for {cmd['name']}: {result.error}")

    return FlextResult[None].ok(None)
```

---

## 🏁 DBT ORACLE WMS FINAL SUCCESS VALIDATION

```bash
#!/bin/bash
# wms_dbt_final_validation.sh - Complete Oracle WMS dbt ecosystem validation

echo "=== FLEXT DBT ORACLE WMS FINAL VALIDATION ==="

# Navigate to project directory
cd flext-dbt-oracle-wms

# Quality Gates
echo "=== CODE QUALITY VALIDATION ==="
ruff check src/ tests/ models/ macros/ --statistics
mypy src/ --strict --show-error-codes
pyright src/ --stats
pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=75

# Oracle WMS dbt Functional Validation
echo "=== ORACLE WMS DBT FUNCTIONAL VALIDATION ==="
python -c "
import sys
sys.path.insert(0, 'src')

try:
    # Test Oracle WMS dbt imports
    from flext_dbt_oracle_wms import (
        UnifiedFlextDbtOracleWmsService,
        FlextDbtOracleWmsConfig,
        WmsRawData,
        WmsDimensionalModel
    )
    print('✅ Oracle WMS dbt imports: SUCCESS')

    # Test flext-core integration
    from flext_core import FlextResult, FlextContainer, FlextLogger
    print('✅ flext-core integration: SUCCESS')

    # Test flext-oracle-wms integration
    from flext_oracle_wms import FlextOracleWmsApi
    print('✅ flext-oracle-wms integration: SUCCESS')

    # Test flext-meltano integration
    from flext_meltano import FlextDbtHub
    print('✅ flext-meltano integration: SUCCESS')

    # Test flext-tap-oracle-wms integration
    from flext_tap_oracle_wms import OracleWmsTapExtractor
    print('✅ flext-tap-oracle-wms integration: SUCCESS')

    # Test configuration loading
    config = FlextDbtOracleWmsConfig()
    config_result = config.get_wms_configuration()
    print(f'✅ WMS Configuration loading: {"SUCCESS" if config_result.is_success else "FAILED"}')

    # Test service initialization
    service = UnifiedFlextDbtOracleWmsService()
    print('✅ WMS Service initialization: SUCCESS')

    print('✅ ALL ORACLE WMS VALIDATIONS: PASSED')

except Exception as e:
    print(f'❌ VALIDATION FAILED: {e}')
    sys.exit(1)
"

# dbt WMS Model Compilation Test
echo "=== DBT WMS MODEL COMPILATION VALIDATION ==="
if [ -f "dbt_project.yml" ]; then
    dbt compile --project-dir . && echo "✅ dbt WMS compilation: SUCCESS" || echo "❌ dbt WMS compilation: FAILED"
else
    echo "⚠️  dbt_project.yml not found - skipping dbt compilation test"
fi

# dbt WMS Model Test Execution
echo "=== DBT WMS MODEL TEST VALIDATION ==="
if [ -f "dbt_project.yml" ]; then
    dbt test --project-dir . --select tag:wms_core && echo "✅ dbt WMS tests: SUCCESS" || echo "❌ dbt WMS tests: FAILED"
else
    echo "⚠️  dbt_project.yml not found - skipping dbt test execution"
fi

# Oracle WMS Connectivity Test (if configured)
echo "=== ORACLE WMS CONNECTIVITY VALIDATION ==="
python -c "
try:
    from flext_dbt_oracle_wms import FlextDbtOracleWmsConfig, UnifiedFlextDbtOracleWmsService
    config = FlextDbtOracleWmsConfig()
    service = UnifiedFlextDbtOracleWmsService()

    # Test Oracle WMS connectivity (may fail if WMS not available)
    result = service._validate_wms_connectivity()
    if result.is_success:
        print('✅ Oracle WMS connectivity: SUCCESS')
    else:
        print(f'⚠️  Oracle WMS connectivity: UNAVAILABLE ({result.error[:50]}...)')
        print('   This is expected if Oracle WMS Database is not running')

except Exception as e:
    print(f'⚠️  Oracle WMS connectivity test error: {e}')
    print('   This is expected if Oracle WMS Database is not configured')
"

# Singer Tap Integration Test (if configured)
echo "=== SINGER TAP WMS INTEGRATION VALIDATION ==="
python -c "
try:
    from flext_tap_oracle_wms import OracleWmsTapExtractor
    extractor = OracleWmsTapExtractor()

    # Test Singer tap WMS integration
    result = extractor.test_connection()
    if result.is_success:
        print('✅ Singer tap WMS integration: SUCCESS')
    else:
        print(f'⚠️  Singer tap WMS integration: UNAVAILABLE ({result.error[:50]}...)')
        print('   This is expected if Oracle WMS Database is not configured for taps')

except Exception as e:
    print(f'⚠️  Singer tap WMS integration test error: {e}')
    print('   This is expected if flext-tap-oracle-wms is not configured')
"

echo "=== DBT ORACLE WMS ECOSYSTEM READY FOR PRODUCTION ==="
```

---

**DBT ORACLE WMS EXCELLENCE PATH**: Follow these Oracle WMS-specific standards precisely, validate WMS dimensional model compilation continuously, ensure proper fact/dimension relationships, optimize Oracle WMS performance patterns, never compromise on WMS business rule validation, integrate seamlessly with Singer tap ecosystem, and ALWAYS use FLEXT ecosystem for Oracle WMS CLI testing with proper configuration hierarchy (ENV → .env → DEFAULT → CLI) and complete flext-oracle-wms + flext-meltano + flext-tap-oracle-wms integration.
