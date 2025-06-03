# Write your MySQL query statement below
select
    Register.contest_id,
    ROUND(COUNT(Register.user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) as percentage
from 
    Register

left join
    Users 

on
    Users.user_id = Register.user_id

group by 
    Register.contest_id

order by 
    percentage desc, Register.contest_id;