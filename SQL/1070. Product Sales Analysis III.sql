# Write your MySQL query statement below
with first_year_sale as (
    select product_id, MIN(year) as first_year
    from Sales
    group by product_id
)

select Sales.product_id, first_year_sale.first_year, quantity, price
from Sales
join first_year_sale
on Sales.product_id = first_year_sale.product_id and Sales.year = first_year_sale.first_year;