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

select * from trajectory_data
