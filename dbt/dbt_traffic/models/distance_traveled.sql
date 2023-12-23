{{ config(materialized='view') }}

with distance_summary as (
    select
        type,
        sum(traveled_d::numeric) AS total_distance
    from traffic
    group by 1
)

select * from distance_summary
