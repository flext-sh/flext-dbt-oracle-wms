"""DBT Oracle WMS protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextDbtOracleWmsProtocols:
    """DBT Oracle WMS protocols with explicit re-exports from FlextCore.Protocols foundation.

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

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # DBT ORACLE WMS-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtOracleWms:
        """DBT Oracle WMS domain protocols for warehouse management data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT operations with Oracle WMS data."""

            def run_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Run DBT models with Oracle WMS data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Test DBT models with Oracle WMS data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Compile DBT models for Oracle WMS data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT manifest with Oracle WMS model definitions.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextCore.Result[bool]:
                """Validate DBT project configuration for Oracle WMS integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextCore.Result[bool]: Validation status or error

                """

        @runtime_checkable
        class WmsIntegrationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle WMS data integration operations."""

            def extract_wms_inventory_data(
                self,
                wms_config: FlextCore.Types.Dict,
                extraction_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Extract inventory data from Oracle WMS for DBT processing.

                Args:
                    wms_config: Oracle WMS connection configuration
                    extraction_config: Data extraction parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Extracted WMS inventory data or error

                """

            def extract_wms_transaction_data(
                self,
                wms_config: FlextCore.Types.Dict,
                extraction_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Extract transaction data from Oracle WMS for DBT processing.

                Args:
                    wms_config: Oracle WMS connection configuration
                    extraction_config: Transaction extraction parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Extracted WMS transaction data or error

                """

            def transform_wms_to_dbt_format(
                self,
                wms_data: list[FlextCore.Types.Dict],
                transformation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Transform Oracle WMS data to DBT-compatible format.

                Args:
                    wms_data: Raw Oracle WMS data
                    transformation_config: Transformation parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def validate_wms_data_quality(
                self,
                data: list[FlextCore.Types.Dict],
                quality_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate Oracle WMS data quality for DBT processing.

                Args:
                    data: Oracle WMS data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality validation results or error

                """

            def sync_wms_to_warehouse(
                self,
                wms_data: list[FlextCore.Types.Dict],
                warehouse_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Sync Oracle WMS data to data warehouse for DBT processing.

                Args:
                    wms_data: Oracle WMS data to sync
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle WMS data modeling operations."""

            def create_inventory_dimension(
                self,
                wms_inventory: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create inventory dimension model from Oracle WMS inventory data.

                Args:
                    wms_inventory: Oracle WMS inventory data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Inventory dimension model or error

                """

            def create_location_dimension(
                self,
                wms_locations: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create location dimension model from Oracle WMS location data.

                Args:
                    wms_locations: Oracle WMS location data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Location dimension model or error

                """

            def create_warehouse_operations_models(
                self,
                wms_operations: list[FlextCore.Types.Dict],
                modeling_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create warehouse operations models from Oracle WMS operations data.

                Args:
                    wms_operations: Oracle WMS operations data
                    modeling_config: Operations modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Warehouse operations models or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[FlextCore.Types.Dict],
                fact_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Generate fact tables from Oracle WMS dimensions.

                Args:
                    dimensions: Oracle WMS dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle WMS data transformation operations."""

            def normalize_wms_inventory_data(
                self,
                wms_inventory: list[FlextCore.Types.Dict],
                normalization_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Normalize Oracle WMS inventory data for consistent processing.

                Args:
                    wms_inventory: Raw Oracle WMS inventory data
                    normalization_rules: Inventory normalization rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Normalized WMS inventory data or error

                """

            def process_wms_transactions(
                self,
                wms_transactions: list[FlextCore.Types.Dict],
                processing_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Process Oracle WMS transaction data for analytics.

                Args:
                    wms_transactions: Oracle WMS transaction data
                    processing_config: Transaction processing configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Processed transaction data or error

                """

            def apply_business_rules(
                self,
                data: list[FlextCore.Types.Dict],
                business_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Apply business rules to Oracle WMS data transformations.

                Args:
                    data: Oracle WMS data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def calculate_wms_kpis(
                self,
                wms_data: list[FlextCore.Types.Dict],
                kpi_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Calculate warehouse management KPIs from Oracle WMS data.

                Args:
                    wms_data: Oracle WMS operational data
                    kpi_config: KPI calculation configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Calculated WMS KPIs or error

                """

        @runtime_checkable
        class MacroProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT macro operations with Oracle WMS data."""

            def generate_wms_source_macro(
                self, source_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT macro for Oracle WMS data sources.

                Args:
                    source_config: Oracle WMS source configuration

                Returns:
                    FlextCore.Result[str]: Generated DBT macro or error

                """

            def create_wms_test_macro(
                self, test_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT test macro for Oracle WMS data validation.

                Args:
                    test_config: Oracle WMS test configuration

                Returns:
                    FlextCore.Result[str]: Generated test macro or error

                """

            def generate_wms_transformation_macro(
                self, transformation_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT transformation macro for Oracle WMS data.

                Args:
                    transformation_config: WMS transformation configuration

                Returns:
                    FlextCore.Result[str]: Generated transformation macro or error

                """

            def create_wms_snapshot_macro(
                self, snapshot_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT snapshot macro for Oracle WMS data versioning.

                Args:
                    snapshot_config: WMS snapshot configuration

                Returns:
                    FlextCore.Result[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle WMS data quality operations."""

            def validate_wms_inventory_accuracy(
                self,
                wms_data: list[FlextCore.Types.Dict],
                accuracy_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate Oracle WMS inventory accuracy for DBT processing.

                Args:
                    wms_data: Oracle WMS inventory data to validate
                    accuracy_rules: Inventory accuracy validation rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Accuracy validation results or error

                """

            def check_data_completeness(
                self,
                data: list[FlextCore.Types.Dict],
                completeness_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Check Oracle WMS data completeness for DBT processing.

                Args:
                    data: Oracle WMS data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[FlextCore.Types.Dict],
                anomaly_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Detect anomalies in Oracle WMS data for quality assurance.

                Args:
                    data: Oracle WMS data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[FlextCore.Types.Dict],
                report_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Generate data quality report for Oracle WMS DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT Oracle WMS performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: FlextCore.Types.Dict,
                performance_metrics: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize DBT models for Oracle WMS data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Optimization recommendations or error

                """

            def tune_wms_data_extraction(
                self,
                extraction_config: FlextCore.Types.Dict,
                tuning_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Tune Oracle WMS data extraction for improved performance.

                Args:
                    extraction_config: WMS data extraction configuration
                    tuning_config: Extraction tuning parameters

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Tuned extraction configuration or error

                """

            def monitor_dbt_performance(
                self, run_results: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor DBT performance with Oracle WMS data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Performance metrics or error

                """

            def optimize_warehouse_operations(
                self, operations_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize warehouse operations analysis for DBT processing.

                Args:
                    operations_config: Warehouse operations configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Operations optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT Oracle WMS monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]:
                """Track DBT run metrics for Oracle WMS data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextCore.Result[bool]: Metric tracking success status

                """

            def monitor_wms_data_freshness(
                self, freshness_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor Oracle WMS data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Data freshness status or error

                """

            def get_health_status(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT Oracle WMS integration health status.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create monitoring dashboard for DBT Oracle WMS operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Dashboard creation result or error

                """

            def track_inventory_metrics(
                self, inventory_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Track inventory management metrics for WMS analytics.

                Args:
                    inventory_config: Inventory tracking configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Inventory metrics or error

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
