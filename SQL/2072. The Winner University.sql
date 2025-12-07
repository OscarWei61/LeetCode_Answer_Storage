WITH excellent_student_count AS (
    SELECT
        (SELECT COUNT(*) FROM NewYork WHERE score >= 90) AS ny_count,
        (SELECT COUNT(*) FROM California WHERE score >= 90) AS ca_count
    FROM (SELECT 1) AS dummy_table
)
SELECT 
    CASE 
        WHEN ny_count > ca_count THEN 'New York University'
        WHEN ca_count > ny_count THEN 'California University'
        ELSE 'No Winner'
    END AS winner
FROM excellent_student_count;