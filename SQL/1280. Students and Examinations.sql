# Write your MySQL query statement below
select
    student_table.student_id,
    student_table.student_name,
    subject_table.subject_name,
    count(exam_table.subject_name) as attended_exams

from 
    Students student_table

cross join
    Subjects subject_table

left join 
    Examinations exam_table

on
    exam_table.student_id = student_table.student_id and exam_table.subject_name = subject_table.subject_name
GROUP BY 
    student_table.student_id,
    student_table.student_name,
    subject_table.subject_name
ORDER BY
    student_table.student_id,
    subject_table.subject_name;