# Write your MySQL query statement below
with BaseData as (
    select
        car_id,
        lot_id,
        fee_paid,
        TIMESTAMPDIFF(second, entry_time, exit_time) / 3600.0 AS hours
    FROM ParkingTransactions
),
LotStatus as (
    select
        car_id, 
        lot_id,
        SUM(hours) as lot_total_hours,
        RANK() OVER(PARTITION BY car_id ORDER BY SUM(hours) DESC) as rnk
    FROM BaseData
    GROUP BY car_id, lot_id
),
CarStats AS (
    SELECT 
        car_id,
        SUM(fee_paid) as total_fee_paid,
        SUM(hours) as total_hours
    FROM BaseData
    GROUP BY car_id
)

SELECT 
    c.car_id,
    ROUND(c.total_fee_paid, 2) AS total_fee_paid,
    ROUND(c.total_fee_paid / c.total_hours, 2) AS avg_hourly_fee,
    l.lot_id AS most_time_lot
FROM CarStats c
JOIN LotStatus l ON c.car_id = l.car_id
WHERE l.rnk = 1
ORDER BY c.car_id ASC;