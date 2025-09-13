# Write your MySQL query statement below
with primary_flag_n as (
    select employee_id, department_id
    from Employee
    group by employee_id
    having count(*) = 1
)

select employee_id, department_id
from Employee
where Employee.primary_flag = 'Y'
union
select employee_id, department_id
from primary_flag_n;