# Write your MySQL query statement below

select
    Signups.user_id,
    Round(IFNULL(SUM(Confirmations.action = 'confirmed') / COUNT(Confirmations.action), 0), 1) as confirmation_rate

from
    Signups

left join
    Confirmations
on
    Confirmations.user_id = Signups.user_id

group by
    Signups.user_id;    