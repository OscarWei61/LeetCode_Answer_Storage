# Write your MySQL query statement below

Select 
    id,
    movie,
    Cinema.description,
    rating

from
    Cinema

where
    MOD(id, 2) = 1 AND Cinema.description != 'boring'

order by
    rating DESC;