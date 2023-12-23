{{ config(materialized='table') }}

with acceleration_data as (
    select
        id,
        track_id,
        lat_acc,
        lon_acc,
        time
    from automobiles
)

select * from acceleration_data