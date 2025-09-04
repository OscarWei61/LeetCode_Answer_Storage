# Write your MySQL query statement below
With count_reports as (
    select reports_to as employee_id, count(*) as reports_count, ROUND(AVG(age)) as average_age
    from Employees
    where reports_to is not null
    group by reports_to
)

select Employees.employee_id, Employees.name, count_reports.reports_count, count_reports.average_age
from Employees
join count_reports
on count_reports.employee_id = Employees.employee_id
order by Employees.employee_id;