{{ config(materialized='table') }}

with heatmap_data as (
    select
        type,
        lat,
        lon,
        count(*) as point_count
    from automobiles
    join traffic using (track_id)
    group by 1, 2, 3
)

select * from heatmap_data