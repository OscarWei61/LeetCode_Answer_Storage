# Write your MySQL query statement below
select
    e_table.name
from
    Employee e_table

where e_table.id in (
    select 
        managerId 
    
    from 
        Employee

    where 
        managerId IS NOT NULL
    
    GROUP by
        managerId
    having count(*) >= 5
);