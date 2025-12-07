# Write your MySQL query statement below
with friend_table as (
    select requester_id as id, accepter_id as friend_id
    from RequestAccepted
    union all
    select accepter_id as id, requester_id as friend_id
    from RequestAccepted
)

select id, count(*) as num
from friend_table
group by id
order by num DESC
limit 1;
    

