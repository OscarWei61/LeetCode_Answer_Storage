# Write your MySQL query statement below
with alldriver as (
    select 
        distinct driver_id
    from 
        Rides
),
passenger_count as (
    select
        passenger_id,
        count(*) as passenger_cnt
    from
        Rides
    group by 
        passenger_id
)

select 
    driver_id,
    IFNULL(passenger_count.passenger_cnt, 0) as cnt
from
    alldriver
left join
    passenger_count
on
    alldriver.driver_id = passenger_count.passenger_id;