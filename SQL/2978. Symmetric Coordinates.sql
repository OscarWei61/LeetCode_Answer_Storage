# Write your MySQL query statement below
WITH RankedCoordinates AS (
    SELECT X, Y, ROW_NUMBER() OVER() as id
    FROM Coordinates
)

select distinct
    r1.X,
    r1.Y
from
    RankedCoordinates r1
join 
    RankedCoordinates r2
on 
    r1.X = r2.Y AND r1.Y = r2.X
where
    r1.id != r2.id
    and
    r1.X <= r1.Y
order by
    r1.X asc, r1.Y asc;