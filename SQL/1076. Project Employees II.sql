WITH ProjectCounts AS (
    SELECT
        project_id,
        COUNT(employee_id) AS employee_count,
        RANK() OVER (ORDER BY COUNT(employee_id) DESC) AS rank_num
    FROM
        Project
    GROUP BY
        project_id
)
SELECT
    project_id
FROM
    ProjectCounts
WHERE
    rank_num = 1;