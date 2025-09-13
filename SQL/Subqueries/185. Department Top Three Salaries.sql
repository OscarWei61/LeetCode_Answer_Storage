# Write your MySQL query statement below
select Department.name as Department, Employee.name as Employee, Employee.salary as Salary
from Employee
join Department
on Department.id = Employee.departmentId
where (
    select count(distinct e2.salary)
    from Employee e2
    where Employee.departmentId = e2.departmentId
    and e2.salary > Employee.salary
) < 3;