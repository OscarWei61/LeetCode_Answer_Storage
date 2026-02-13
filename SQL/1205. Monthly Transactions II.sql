WITH approve_table AS (
  SELECT
    SUBSTR(trans_date, 1, 7) AS month,
    country,
    COUNT(*) AS approved_count,
    SUM(amount) AS approved_amount,
    0 AS chargeback_count,
    0 AS chargeback_amount
  FROM Transactions
  WHERE state = 'approved'
  GROUP BY SUBSTR(trans_date, 1, 7), country
),
Chargebacks_month_table AS (
  SELECT
    SUBSTR(c.trans_date, 1, 7) AS month,
    t.country,
    0 AS approved_count,
    0 AS approved_amount,
    COUNT(*) AS chargeback_count,
    SUM(t.amount) AS chargeback_amount
  FROM Chargebacks c
  JOIN Transactions t
    ON c.trans_id = t.id
  GROUP BY SUBSTR(c.trans_date, 1, 7), t.country
)

SELECT 
  month,
  country,
  SUM(approved_count) AS approved_count,
  SUM(approved_amount) AS approved_amount,
  SUM(chargeback_count) AS chargeback_count,
  SUM(chargeback_amount) AS chargeback_amount
FROM (
  SELECT * FROM approve_table
  UNION ALL
  SELECT * FROM Chargebacks_month_table
)
GROUP BY month, country
HAVING 
  SUM(approved_count) > 0 
  OR SUM(approved_amount) > 0 
  OR SUM(chargeback_count) > 0 
  OR SUM(chargeback_amount) > 0
ORDER BY month, country;