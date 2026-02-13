with total_user_count as (
select count(distinct user_id) as user_count
from (
    select user1 as user_id
    from Friends
    union
    select user2 as user_id
    from Friends
)
),
total_friend_count as (
select user_id, sum(total_count) as total_count
from(
    select user1 as user_id, count(*) as total_count
    from Friends
    group by user1
    union
    select user2 as user_id, count(*) as total_count
    from Friends
    group by user2
)
GROUP BY user_id
)

select user_id as user1, ROUND(total_count * 100 /  (select user_count from total_user_count), 2) as percentage_popularity 
from total_friend_count