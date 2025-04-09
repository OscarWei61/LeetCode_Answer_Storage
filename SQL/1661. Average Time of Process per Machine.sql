# Write your MySQL query statement below
select
    table1.machine_id,
    ROUND(AVG(table2.timestamp - table1.timestamp), 3) as processing_time
from
    Activity table1
join
    Activity table2
    on table1.machine_id = table2.machine_id
    and table1.process_id = table2.process_id
    and table1.activity_type = 'start'
    and table2.activity_type = 'end'
group BY
    table1.machine_id;