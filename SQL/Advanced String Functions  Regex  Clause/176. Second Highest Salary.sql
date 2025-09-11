# Write your MySQL query statement below
with firsttwo_salary as (
    select distinct salary 
    from Employee
    order by salary DESC
    limit 2
)

select IFNULL(min(salary), NULL) as SecondHighestSalary
from firsttwo_salary
where salary < (select max(salary) from Employee);