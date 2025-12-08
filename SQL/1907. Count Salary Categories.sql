# Write your MySQL query statement below
with category_table as (
    select 'Low Salary' as category, count(*) accounts_count
    from Accounts
    where income < 20000
    union
    select 'Average Salary' as category, count(*) accounts_count
    from Accounts
    where income >= 20000 and income <= 50000
    union
    select 'High Salary' as category, count(*) accounts_count
    from Accounts
    where income > 50000
)

select category, accounts_count
from category_table;