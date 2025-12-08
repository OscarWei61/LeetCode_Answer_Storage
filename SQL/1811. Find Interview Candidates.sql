with medals_records as (
  select user_id, contest_id from (
    select gold_medal as user_id, contest_id from Contests
    union all
    select silver_medal as user_id, contest_id from Contests
    union all
    select bronze_medal as user_id, contest_id from Contests
  )
),
consecutive_medals as (
  select user_id
  from (
    select 
      user_id, 
      contest_id,
      contest_id - row_number() over (partition by user_id order by contest_id) as group_id
    from medals_records 
  ) medal_group
  group by user_id, group_id
  having count(*) >= 3
),
gold_medals as (
  select gold_medal as user_id
  from Contests
  group by gold_medal
  having count(*) >= 3
)

select Users.name, Users.mail
from Users
where EXISTS (SELECT 1 FROM consecutive_medals WHERE user_id = Users.user_id)
   OR EXISTS (SELECT 1 FROM gold_medals WHERE user_id = Users.user_id);