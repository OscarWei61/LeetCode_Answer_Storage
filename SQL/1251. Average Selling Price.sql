# Write your MySQL query statement below

Select

    Prices.product_id,
    ROUND(IFNULL(SUM(UnitsSold.units * Prices.price) / SUM(UnitsSold.units), 0), 2) as average_price

from
    Prices

left join 
    UnitsSold
on
    Prices.product_id = UnitsSold.product_id AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
group by
    Prices.product_id;