# Write your MySQL query statement below
select s1.student_id, s1.subject, s1.score as first_score, s2.score as latest_score
from (
    select student_id, subject, score, exam_date
    from Scores
    where (student_id, subject, exam_date) in (
        select student_id, subject, min(exam_date)
        from Scores
        group by student_id, subject
    )
) s1
join (
    select student_id, subject, score, exam_date
    from Scores
    where (student_id, subject, exam_date) in (
        select student_id, subject, max(exam_date)
        from Scores
        group by student_id, subject
    )
) s2
on s1.student_id = s2.student_id and s1.subject = s2.subject
and s2.score > s1.score
order by student_id, subject;