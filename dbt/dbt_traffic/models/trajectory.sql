{{ config(materialized='table') }}

with trajectory_data as (
    select
        id,
        track_id,
        lat,
        lon,
        time
    from automobiles
)

select distinct on (lat, lon) *
from trajectory_data
order by lat, lon, time desc