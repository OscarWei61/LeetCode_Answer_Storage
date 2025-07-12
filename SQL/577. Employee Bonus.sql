# Write your MySQL query statement below
select
    e_table.name,
    b_table.bonus
from
    Employee e_table
left join
    Bonus b_table ON e_table.empId = b_table.empId
where
    b_table.bonus < 1000 OR b_table.bonus IS NULL;