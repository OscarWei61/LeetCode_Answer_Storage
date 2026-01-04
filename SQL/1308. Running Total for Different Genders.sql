# Write your MySQL query statement belows
select
    gender,
    Scores.day,
    sum(score_points) over(
        partition by gender
        order by day
    ) as total
from 
    Scores
order by gender, day;