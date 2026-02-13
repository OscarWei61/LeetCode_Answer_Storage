# Write your MySQL query statement below
with total_amount_table as (
    select account, sum(amount) as total_amount 
    from Transactions
    group by account
)

select name, total_amount_table.total_amount as balance
from Users
join total_amount_table
on total_amount_table.account = Users.account
having total_amount_table.total_amount > 10000;