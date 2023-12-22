{{ config(materialized='view') }}

with type_distribution as (
    select
        type,
        count(*) as vehicle_count
    from traffic
    group by 1
)

select * from type_distribution