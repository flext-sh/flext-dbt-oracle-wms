"""DBT Oracle WMS protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import (
    FlextProtocols,
    FlextResult,
)


class FlextDbtOracleWmsProtocols:
    """DBT Oracle WMS protocols with explicit re-exports from FlextProtocols foundation.

    This class provides protocol definitions for DBT operations with Oracle WMS integration,
    warehouse management data transformation, inventory analytics, and enterprise WMS patterns.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in DbtOracleWms namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    # ============================================================================
    # DBT ORACLE WMS-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtOracleWms:
        """DBT Oracle WMS domain protocols for warehouse management data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT operations with Oracle WMS data."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Run DBT models with Oracle WMS data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextResult[dict[str, object]]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Test DBT models with Oracle WMS data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextResult[dict[str, object]]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Compile DBT models for Oracle WMS data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextResult[dict[str, object]]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextResult[dict[str, object]]:
                """Get DBT manifest with Oracle WMS model definitions.

                Returns:
                    FlextResult[dict[str, object]]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextResult[bool]:
                """Validate DBT project configuration for Oracle WMS integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextResult[bool]: Validation status or error

                """

        @runtime_checkable
        class WmsIntegrationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle WMS data integration operations."""

            def extract_wms_inventory_data(
                self,
                wms_config: dict[str, object],
                extraction_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Extract inventory data from Oracle WMS for DBT processing.

                Args:
                    wms_config: Oracle WMS connection configuration
                    extraction_config: Data extraction parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Extracted WMS inventory data or error

                """

            def extract_wms_transaction_data(
                self,
                wms_config: dict[str, object],
                extraction_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Extract transaction data from Oracle WMS for DBT processing.

                Args:
                    wms_config: Oracle WMS connection configuration
                    extraction_config: Transaction extraction parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Extracted WMS transaction data or error

                """

            def transform_wms_to_dbt_format(
                self,
                wms_data: list[dict[str, object]],
                transformation_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Transform Oracle WMS data to DBT-compatible format.

                Args:
                    wms_data: Raw Oracle WMS data
                    transformation_config: Transformation parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def validate_wms_data_quality(
                self,
                data: list[dict[str, object]],
                quality_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate Oracle WMS data quality for DBT processing.

                Args:
                    data: Oracle WMS data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextResult[dict[str, object]]: Quality validation results or error

                """

            def sync_wms_to_warehouse(
                self,
                wms_data: list[dict[str, object]],
                warehouse_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Sync Oracle WMS data to data warehouse for DBT processing.

                Args:
                    wms_data: Oracle WMS data to sync
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextResult[dict[str, object]]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle WMS data modeling operations."""

            def create_inventory_dimension(
                self,
                wms_inventory: list[dict[str, object]],
                dimension_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create inventory dimension model from Oracle WMS inventory data.

                Args:
                    wms_inventory: Oracle WMS inventory data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Inventory dimension model or error

                """

            def create_location_dimension(
                self,
                wms_locations: list[dict[str, object]],
                dimension_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create location dimension model from Oracle WMS location data.

                Args:
                    wms_locations: Oracle WMS location data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Location dimension model or error

                """

            def create_warehouse_operations_models(
                self,
                wms_operations: list[dict[str, object]],
                modeling_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create warehouse operations models from Oracle WMS operations data.

                Args:
                    wms_operations: Oracle WMS operations data
                    modeling_config: Operations modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Warehouse operations models or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[dict[str, object]],
                fact_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Generate fact tables from Oracle WMS dimensions.

                Args:
                    dimensions: Oracle WMS dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle WMS data transformation operations."""

            def normalize_wms_inventory_data(
                self,
                wms_inventory: list[dict[str, object]],
                normalization_rules: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Normalize Oracle WMS inventory data for consistent processing.

                Args:
                    wms_inventory: Raw Oracle WMS inventory data
                    normalization_rules: Inventory normalization rules

                Returns:
                    FlextResult[list[dict[str, object]]]: Normalized WMS inventory data or error

                """

            def process_wms_transactions(
                self,
                wms_transactions: list[dict[str, object]],
                processing_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Process Oracle WMS transaction data for analytics.

                Args:
                    wms_transactions: Oracle WMS transaction data
                    processing_config: Transaction processing configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Processed transaction data or error

                """

            def apply_business_rules(
                self,
                data: list[dict[str, object]],
                business_rules: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Apply business rules to Oracle WMS data transformations.

                Args:
                    data: Oracle WMS data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def calculate_wms_kpis(
                self,
                wms_data: list[dict[str, object]],
                kpi_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Calculate warehouse management KPIs from Oracle WMS data.

                Args:
                    wms_data: Oracle WMS operational data
                    kpi_config: KPI calculation configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Calculated WMS KPIs or error

                """

        @runtime_checkable
        class MacroProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT macro operations with Oracle WMS data."""

            def generate_wms_source_macro(
                self, source_config: dict[str, object]
            ) -> FlextResult[str]:
                """Generate DBT macro for Oracle WMS data sources.

                Args:
                    source_config: Oracle WMS source configuration

                Returns:
                    FlextResult[str]: Generated DBT macro or error

                """

            def create_wms_test_macro(
                self, test_config: dict[str, object]
            ) -> FlextResult[str]:
                """Create DBT test macro for Oracle WMS data validation.

                Args:
                    test_config: Oracle WMS test configuration

                Returns:
                    FlextResult[str]: Generated test macro or error

                """

            def generate_wms_transformation_macro(
                self, transformation_config: dict[str, object]
            ) -> FlextResult[str]:
                """Generate DBT transformation macro for Oracle WMS data.

                Args:
                    transformation_config: WMS transformation configuration

                Returns:
                    FlextResult[str]: Generated transformation macro or error

                """

            def create_wms_snapshot_macro(
                self, snapshot_config: dict[str, object]
            ) -> FlextResult[str]:
                """Create DBT snapshot macro for Oracle WMS data versioning.

                Args:
                    snapshot_config: WMS snapshot configuration

                Returns:
                    FlextResult[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle WMS data quality operations."""

            def validate_wms_inventory_accuracy(
                self,
                wms_data: list[dict[str, object]],
                accuracy_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate Oracle WMS inventory accuracy for DBT processing.

                Args:
                    wms_data: Oracle WMS inventory data to validate
                    accuracy_rules: Inventory accuracy validation rules

                Returns:
                    FlextResult[dict[str, object]]: Accuracy validation results or error

                """

            def check_data_completeness(
                self,
                data: list[dict[str, object]],
                completeness_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Check Oracle WMS data completeness for DBT processing.

                Args:
                    data: Oracle WMS data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextResult[dict[str, object]]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[dict[str, object]],
                anomaly_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Detect anomalies in Oracle WMS data for quality assurance.

                Args:
                    data: Oracle WMS data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[dict[str, object]],
                report_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Generate data quality report for Oracle WMS DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextResult[dict[str, object]]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT Oracle WMS performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: dict[str, object],
                performance_metrics: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Optimize DBT models for Oracle WMS data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextResult[dict[str, object]]: Optimization recommendations or error

                """

            def tune_wms_data_extraction(
                self,
                extraction_config: dict[str, object],
                tuning_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Tune Oracle WMS data extraction for improved performance.

                Args:
                    extraction_config: WMS data extraction configuration
                    tuning_config: Extraction tuning parameters

                Returns:
                    FlextResult[dict[str, object]]: Tuned extraction configuration or error

                """

            def monitor_dbt_performance(
                self, run_results: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Monitor DBT performance with Oracle WMS data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextResult[dict[str, object]]: Performance metrics or error

                """

            def optimize_warehouse_operations(
                self, operations_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Optimize warehouse operations analysis for DBT processing.

                Args:
                    operations_config: Warehouse operations configuration

                Returns:
                    FlextResult[dict[str, object]]: Operations optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT Oracle WMS monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: dict[str, object]
            ) -> FlextResult[bool]:
                """Track DBT run metrics for Oracle WMS data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextResult[bool]: Metric tracking success status

                """

            def monitor_wms_data_freshness(
                self, freshness_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Monitor Oracle WMS data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextResult[dict[str, object]]: Data freshness status or error

                """

            def get_health_status(self) -> FlextResult[dict[str, object]]:
                """Get DBT Oracle WMS integration health status.

                Returns:
                    FlextResult[dict[str, object]]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Create monitoring dashboard for DBT Oracle WMS operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextResult[dict[str, object]]: Dashboard creation result or error

                """

            def track_inventory_metrics(
                self, inventory_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Track inventory management metrics for WMS analytics.

                Args:
                    inventory_config: Inventory tracking configuration

                Returns:
                    FlextResult[dict[str, object]]: Inventory metrics or error

                """

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    # DBT operations
    DbtProtocol = DbtOracleWms.DbtProtocol

    # WMS integration
    WmsIntegrationProtocol = DbtOracleWms.WmsIntegrationProtocol

    # Data modeling
    ModelingProtocol = DbtOracleWms.ModelingProtocol

    # Transformations
    TransformationProtocol = DbtOracleWms.TransformationProtocol

    # DBT macros
    MacroProtocol = DbtOracleWms.MacroProtocol

    # Data quality
    QualityProtocol = DbtOracleWms.QualityProtocol

    # Performance optimization
    PerformanceProtocol = DbtOracleWms.PerformanceProtocol

    # Monitoring
    MonitoringProtocol = DbtOracleWms.MonitoringProtocol

    # Convenience aliases for downstream usage
    DbtOracleWmsProtocol = DbtOracleWms.DbtProtocol
    DbtWmsIntegrationProtocol = DbtOracleWms.WmsIntegrationProtocol
    DbtWmsModelingProtocol = DbtOracleWms.ModelingProtocol
    DbtWmsTransformationProtocol = DbtOracleWms.TransformationProtocol
    DbtWmsMacroProtocol = DbtOracleWms.MacroProtocol
    DbtWmsQualityProtocol = DbtOracleWms.QualityProtocol
    DbtWmsPerformanceProtocol = DbtOracleWms.PerformanceProtocol
    DbtWmsMonitoringProtocol = DbtOracleWms.MonitoringProtocol


__all__ = [
    "FlextDbtOracleWmsProtocols",
]
