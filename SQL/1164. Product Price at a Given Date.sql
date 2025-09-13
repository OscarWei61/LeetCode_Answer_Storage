# Write your MySQL query statement below
with latest_price as (
    select product_id, new_price as price, max(change_date) as change_date
    from Products
    where change_date <= '2019-08-16'
    group by product_id
)

select p.product_id, COALESCE(pr.new_price, 10) as price
from (select distinct product_id from Products) p
LEFT JOIN latest_price lp
    ON p.product_id = lp.product_id
LEFT JOIN Products pr
    ON pr.product_id = lp.product_id 
   AND pr.change_date = lp.change_date;