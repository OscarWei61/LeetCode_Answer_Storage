# Write your MySQL query statement below
with daily as (
    select visited_on, SUM(amount) as amount
    from Customer
    group by visited_on
),
period_amount as (
    select visited_on,
    SUM(amount) over (
        order by visited_on
        rows between 6 preceding and current row
    ) as total_amount,
    count(*) over (
        order by visited_on
        rows between 6 preceding and current row
    ) as period_count

    from daily
)

select 
    visited_on, 
    total_amount as amount, 
    ROUND(total_amount / 7, 2) as average_amount
from period_amount
where period_count = 7
order by visited_on;
