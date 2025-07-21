{{ 
  config(
    materialized='table',
    tags=['marts', 'metrics', 'kpi', 'dashboard'],
    indexes=[
      {'columns': ['company_code', 'facility_code', 'kpi_date'], 'unique': False},
      {'columns': ['kpi_category'], 'unique': False}
    ]
  ) 
}}

-- Enterprise KPI dashboard for Oracle WMS operations
-- Consolidates key performance indicators across all WMS functional areas

with allocation_kpis as (
    select 
        company_code,
        facility_code,
        business_date as kpi_date,
        'ALLOCATION' as kpi_category,
        
        -- Allocation performance metrics
        avg(pack_efficiency_percent) as avg_pack_efficiency,
        avg(avg_pick_time_hours) as avg_pick_time_hours,
        sum(daily_total_allocations) as total_allocations,
        sum(daily_outstanding_quantity) as total_outstanding_quantity,
        
        -- Allocation status distribution
        sum(case when allocation_status = 'PLANNED' then total_allocations else 0 end) as planned_allocations,
        sum(case when allocation_status = 'PICKING' then total_allocations else 0 end) as picking_allocations,
        sum(case when allocation_status = 'PICKED' then total_allocations else 0 end) as picked_allocations,
        sum(case when allocation_status = 'PACKED' then total_allocations else 0 end) as packed_allocations,
        
        -- Alert indicators
        count(case when operational_alert != 'NORMAL' then 1 end) as allocation_alerts_count
        
    from {{ ref('opr_wms__allocation_summary') }}
    group by company_code, facility_code, business_date
),

inventory_kpis as (
    select 
        company_code,
        facility_code,
        analysis_date as kpi_date,
        'INVENTORY' as kpi_category,
        
        -- Inventory value metrics
        sum(total_inventory_value) as total_inventory_value,
        avg(available_value_percent) as avg_available_value_percent,
        avg(damage_rate_percent) as avg_damage_rate_percent,
        
        -- Inventory classification
        count(case when abc_classification = 'A' then 1 end) as a_class_items,
        count(case when abc_classification = 'B' then 1 end) as b_class_items,
        count(case when abc_classification = 'C' then 1 end) as c_class_items,
        
        -- Turnover metrics
        count(case when inventory_turnover_category = 'FAST_MOVING' then 1 end) as fast_moving_items,
        count(case when inventory_turnover_category = 'MEDIUM_MOVING' then 1 end) as medium_moving_items,
        count(case when inventory_turnover_category = 'SLOW_MOVING' then 1 end) as slow_moving_items,
        count(case when inventory_turnover_category = 'DEAD_STOCK' then 1 end) as dead_stock_items,
        
        -- Risk indicators
        count(case when inventory_risk_level = 'HIGH' then 1 end) as high_risk_items,
        count(case when inventory_risk_level = 'MEDIUM' then 1 end) as medium_risk_items,
        
        -- Average days of supply
        avg(days_of_supply_30d) as avg_days_of_supply_30d,
        avg(annual_turnover_rate) as avg_annual_turnover_rate
        
    from {{ ref('ana_wms__inventory_analysis') }}
    group by company_code, facility_code, analysis_date
),

order_kpis as (
    select 
        oh.company_code,
        oh.facility_code,
        oh.business_date as kpi_date,
        'ORDERS' as kpi_category,
        
        -- Order volume metrics
        count(distinct oh.order_header_id) as total_orders,
        sum(oh.total_quantity) as total_order_quantity,
        sum(oh.total_value) as total_order_value,
        avg(oh.total_lines) as avg_lines_per_order,
        
        -- Order fulfillment metrics
        avg(od.fill_rate_percent) as avg_fill_rate_percent,
        sum(od.shortage_quantity) as total_shortage_quantity,
        
        -- Order type distribution
        count(case when oh.order_type = 'OUTBOUND' then 1 end) as outbound_orders,
        count(case when oh.order_type = 'INBOUND' then 1 end) as inbound_orders,
        count(case when oh.order_type = 'TRANSFER' then 1 end) as transfer_orders,
        
        -- Rush and special handling
        count(case when oh.is_rush_flag = true then 1 end) as rush_orders,
        count(case when oh.is_frozen_flag = true then 1 end) as frozen_orders,
        
        -- Data quality
        count(case when oh.data_quality_status != 'VALID' then 1 end) as invalid_order_headers,
        count(case when od.data_quality_status != 'VALID' then 1 end) as invalid_order_details
        
    from {{ ref('stg_wms__order_hdr') }} oh
    left join {{ ref('stg_wms__order_dtl') }} od 
        on oh.company_code = od.company_code
        and oh.facility_code = od.facility_code
        and oh.order_number = od.order_number
    group by oh.company_code, oh.facility_code, oh.business_date
),

inventory_position_kpis as (
    select 
        company_code,
        facility_code,
        business_date as kpi_date,
        'INVENTORY_POSITION' as kpi_category,
        
        -- Quantity metrics
        sum(on_hand_quantity) as total_on_hand_quantity,
        sum(available_quantity) as total_available_quantity,
        sum(allocated_quantity) as total_allocated_quantity,
        sum(damaged_quantity) as total_damaged_quantity,
        
        -- Location metrics
        count(distinct location_id) as total_locations,
        count(distinct case when on_hand_quantity > 0 then location_id end) as active_locations,
        
        -- Utilization metrics
        {{ calculate_wms_kpi('sum(available_quantity)', 'sum(on_hand_quantity)', 'availability_utilization_percent') }},
        {{ calculate_wms_kpi('sum(allocated_quantity)', 'sum(available_quantity)', 'allocation_utilization_percent') }},
        
        -- Quality metrics
        count(case when data_quality_status != 'VALID' then 1 end) as invalid_inventory_records
        
    from {{ ref('stg_wms__inventory') }}
    group by company_code, facility_code, business_date
),

consolidated_kpis as (
    select * from allocation_kpis
    union all
    select 
        company_code, facility_code, kpi_date, kpi_category,
        avg_pack_efficiency, avg_pick_time_hours, total_allocations, total_outstanding_quantity,
        planned_allocations, picking_allocations, picked_allocations, packed_allocations,
        allocation_alerts_count,
        null as total_inventory_value, null as avg_available_value_percent, null as avg_damage_rate_percent,
        null as a_class_items, null as b_class_items, null as c_class_items,
        null as fast_moving_items, null as medium_moving_items, null as slow_moving_items, null as dead_stock_items,
        null as high_risk_items, null as medium_risk_items,
        null as avg_days_of_supply_30d, null as avg_annual_turnover_rate,
        null as total_orders, null as total_order_quantity, null as total_order_value, null as avg_lines_per_order,
        null as avg_fill_rate_percent, null as total_shortage_quantity,
        null as outbound_orders, null as inbound_orders, null as transfer_orders,
        null as rush_orders, null as frozen_orders,
        null as invalid_order_headers, null as invalid_order_details,
        null as total_on_hand_quantity, null as total_available_quantity, null as total_allocated_quantity, null as total_damaged_quantity,
        null as total_locations, null as active_locations,
        null as availability_utilization_percent, null as allocation_utilization_percent,
        null as invalid_inventory_records
    from inventory_kpis
    
    union all
    select 
        company_code, facility_code, kpi_date, kpi_category,
        null as avg_pack_efficiency, null as avg_pick_time_hours, null as total_allocations, null as total_outstanding_quantity,
        null as planned_allocations, null as picking_allocations, null as picked_allocations, null as packed_allocations,
        null as allocation_alerts_count,
        null as total_inventory_value, null as avg_available_value_percent, null as avg_damage_rate_percent,
        null as a_class_items, null as b_class_items, null as c_class_items,
        null as fast_moving_items, null as medium_moving_items, null as slow_moving_items, null as dead_stock_items,
        null as high_risk_items, null as medium_risk_items,
        null as avg_days_of_supply_30d, null as avg_annual_turnover_rate,
        total_orders, total_order_quantity, total_order_value, avg_lines_per_order,
        avg_fill_rate_percent, total_shortage_quantity,
        outbound_orders, inbound_orders, transfer_orders,
        rush_orders, frozen_orders,
        invalid_order_headers, invalid_order_details,
        null as total_on_hand_quantity, null as total_available_quantity, null as total_allocated_quantity, null as total_damaged_quantity,
        null as total_locations, null as active_locations,
        null as availability_utilization_percent, null as allocation_utilization_percent,
        null as invalid_inventory_records
    from order_kpis
    
    union all
    select 
        company_code, facility_code, kpi_date, kpi_category,
        null as avg_pack_efficiency, null as avg_pick_time_hours, null as total_allocations, null as total_outstanding_quantity,
        null as planned_allocations, null as picking_allocations, null as picked_allocations, null as packed_allocations,
        null as allocation_alerts_count,
        null as total_inventory_value, null as avg_available_value_percent, null as avg_damage_rate_percent,
        null as a_class_items, null as b_class_items, null as c_class_items,
        null as fast_moving_items, null as medium_moving_items, null as slow_moving_items, null as dead_stock_items,
        null as high_risk_items, null as medium_risk_items,
        null as avg_days_of_supply_30d, null as avg_annual_turnover_rate,
        null as total_orders, null as total_order_quantity, null as total_order_value, null as avg_lines_per_order,
        null as avg_fill_rate_percent, null as total_shortage_quantity,
        null as outbound_orders, null as inbound_orders, null as transfer_orders,
        null as rush_orders, null as frozen_orders,
        null as invalid_order_headers, null as invalid_order_details,
        total_on_hand_quantity, total_available_quantity, total_allocated_quantity, total_damaged_quantity,
        total_locations, active_locations,
        availability_utilization_percent, allocation_utilization_percent,
        invalid_inventory_records
    from inventory_position_kpis
),

final as (
    select 
        *,
        
        -- Generate composite key
        {{ dbt_utils.generate_surrogate_key([
            'company_code', 
            'facility_code', 
            'kpi_date',
            'kpi_category'
        ]) }} as kpi_key,
        
        current_timestamp as kpi_calculated_at
        
    from consolidated_kpis
)

select * from final

-- Add comprehensive data quality monitoring
{{ config(post_hook="
    {% if execute %}
        {% set data_quality_query %}
            select 
                kpi_category,
                count(*) as total_records,
                count(case when kpi_date < current_date - interval '1 day' then 1 end) as stale_records
            from {{ this }}
            group by kpi_category
        {% endset %}
        
        {% set results = run_query(data_quality_query) %}
        {% if results and results.rows %}
            {% for row in results.rows %}
                {% if row[2] > 0 %}
                    {{ log('WARNING: KPI category ' ~ row[0] ~ ' has ' ~ row[2] ~ ' stale records out of ' ~ row[1] ~ ' total', info=true) }}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endif %}
") }}