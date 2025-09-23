# Write your MySQL query statement below
with product_sales as (
    select product_id, SUM(unit) as unit
    from Orders
    where order_date like '2020-02-%' 
    group by product_id
    having SUM(unit) >= 100
)

select Products.product_name, product_sales.unit
from Products
join product_sales
on Products.product_id = product_sales.product_id;
