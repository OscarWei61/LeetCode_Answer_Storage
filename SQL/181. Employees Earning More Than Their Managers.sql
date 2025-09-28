# Write your MySQL query statement below
select E1.name as Employee
from Employee E1
where managerId is not null
and salary > (
    select salary 
    from Employee E2
    where E1.managerId = E2.id);