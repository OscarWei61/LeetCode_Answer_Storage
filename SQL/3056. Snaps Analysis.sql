SELECT
    T.age_bucket,
    
    ROUND(
        SUM(CASE WHEN A.activity_type = 'send' THEN A.time_spent ELSE 0 END) * 100.0 / SUM(A.time_spent), 
        2
    ) AS send_perc,
    
    ROUND(
        SUM(CASE WHEN A.activity_type = 'open' THEN A.time_spent ELSE 0 END) * 100.0 / SUM(A.time_spent), 
        2
    ) AS open_perc
FROM 
    Activities A
INNER JOIN 
    Age T 
ON 
    A.user_id = T.user_id
GROUP BY 
    T.age_bucket
ORDER BY 
    T.age_bucket;