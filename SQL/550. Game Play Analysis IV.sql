# Write your MySQL query statement below
with first_login_search as (
    select player_id, MIN(event_date) as first_login_day
    from Activity
    group by Activity.player_id
),

came_back_day as (
    select Activity.player_id
    from first_login_search
    join Activity
    on Activity.player_id = first_login_search.player_id
    and Activity.event_date = DATE_ADD(first_login_search.first_login_day, INTERVAL 1 DAY)
)

select 
    ROUND(
        (select count(*) from came_back_day) /
        (select COUNT(DISTINCT player_id) from Activity), 2
    ) as fraction;