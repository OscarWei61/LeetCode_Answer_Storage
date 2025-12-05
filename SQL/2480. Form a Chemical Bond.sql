# Write your MySQL query statement below
select 
    metal_table.symbol as metal, nonmetal_table.symbol as nonmetal
from Elements as nonmetal_table
join Elements as metal_table
on nonmetal_table.type = "Nonmetal" and metal_table.type = "Metal";