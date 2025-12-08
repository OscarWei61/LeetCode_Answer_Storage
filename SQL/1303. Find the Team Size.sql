# Write your MySQL query statement below
with team_size_count as (
    select team_id, count(*) as team_size
    from Employee
    group by team_id
)

select employee_id, team_size_count.team_size
from Employee
join team_size_count
on Employee.team_id = team_size_count.team_id;