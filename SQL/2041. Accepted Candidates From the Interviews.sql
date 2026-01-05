# Write your MySQL query statement below
with count_interview_score as (
    select 
        interview_id,
        sum(score) as sum_score
    from Rounds
    group by interview_id
)
select 
    candidate_id
from 
    Candidates
left join 
    count_interview_score
on count_interview_score.interview_id = Candidates.interview_id
where 
    count_interview_score.sum_score > 15 and Candidates.years_of_exp >= 2;