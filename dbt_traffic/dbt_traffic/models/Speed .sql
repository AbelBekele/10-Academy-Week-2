-- File: speed_analysis.sql
{{ config(materialized='view') }}

with speed_summary as (
    select
        track_id,
        type,
        time,
        speed::numeric as numeric_speed
    from automobiles
    join traffic using (track_id)
)

select
    type,
    time,
    numeric_speed
from speed_summary
