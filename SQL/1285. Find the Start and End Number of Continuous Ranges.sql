# Write your MySQL query statement below
with group_log as (
    select
        log_id,
        log_id - row_number() over(order by log_id) as diff
    from
        Logs
)
select
    min(log_id) as start_id,
    max(log_id) as end_id
from group_log
group by diff
order by start_id;