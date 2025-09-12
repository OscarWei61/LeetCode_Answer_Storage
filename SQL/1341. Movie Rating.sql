# Write your MySQL query statement below
(
select name as results
from Users
join (
    select user_id, count(*) as times
    from MovieRating
    group by user_id
) users_times
on users_times.user_id = Users.user_id
order by times DESC, name ASC
limit 1
)
union all
(
select title as results
from Movies
join (
    select movie_id, AVG(rating) as avg_rating
    from MovieRating
    where created_at like '2020-02-%'
    group by movie_id
    order by avg_rating DESC
) Movie_rating
on Movie_rating.movie_id = Movies.movie_id
order by avg_rating desc, title asc
limit 1
);