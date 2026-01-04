# Write your MySQL query statement below
with MatchStats as (
    select
        home_team_id as team_id,
        home_team_goals as g_for,
        away_team_goals as g_against,
        Case 
            when home_team_goals > away_team_goals then 3
            when home_team_goals = away_team_goals then 1
            else 0
        end as pts
    from
        Matches
    union all
    select
        away_team_id as team_id,
        away_team_goals as g_for,
        home_team_goals as g_against,
        Case 
            when home_team_goals < away_team_goals then 3
            when home_team_goals = away_team_goals then 1
            else 0
        end as pts
    from
        Matches
)
select
    t.team_name,
    Count(m.team_id) as matches_played,
    sum(m.pts) as points,
    sum(m.g_for) as goal_for,
    sum(m.g_against) as goal_against,
    sum(m.g_for) - sum(m.g_against) as goal_diff
from 
    Teams t
JOIN MatchStats m ON t.team_id = m.team_id
GROUP BY t.team_id
ORDER BY points DESC, goal_diff DESC, team_name ASC;