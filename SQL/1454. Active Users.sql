WITH DistinctLogins AS (
    SELECT DISTINCT id, login_date 
    FROM Logins
),
GroupedLogins AS (
    SELECT 
        id,
        login_date,
        DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date) DAY) AS diff
    FROM DistinctLogins
),
ConsecutiveCounts AS (
    SELECT id
    FROM GroupedLogins
    GROUP BY id, diff
    HAVING COUNT(*) >= 5
)
SELECT DISTINCT a.id, a.name
FROM Accounts a
JOIN ConsecutiveCounts c ON a.id = c.id
ORDER BY a.id;