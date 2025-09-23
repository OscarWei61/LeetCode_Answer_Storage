# Write your MySQL query statement below
with num_split as (
    select num
    from MyNumbers
    group by num
    having count(*) = 1  
)

select MAX(num) as num
from num_split;