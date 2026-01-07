# Write your MySQL query statement below
with salary_rank as (
    select
    emp_id,
    dept,
    DENSE_RANK() over (partition by dept order by salary DESC) as rank_num
from
    Employees
)

select
    emp_id,
    dept
from 
    salary_rank
where
    rank_num = 2
order by emp_id ASC;