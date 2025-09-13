# Write your MySQL query statement below
with cultimative as (
    select person_name, 
    turn,
    SUM(weight) OVER (ORDER BY turn) AS total_weight
    from Queue
)

select person_name
from cultimative
where total_weight <= 1000
order by turn Desc
limit 1;