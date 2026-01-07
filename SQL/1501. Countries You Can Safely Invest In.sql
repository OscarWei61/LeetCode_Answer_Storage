# Write your MySQL query statement below
with id_Country as (
    select 
        id, 
        Country.name as country
    from
        Person
    join
        Country
    on 
        left(Person.phone_number,3 ) = Country.country_code
), 
call_country as (
    select
        caller_id as call_id,
        duration,
        country
    from
        Calls
    join
        id_Country
    on 
        caller_id = id
    union all
    select
        callee_id as call_id,
        duration,
        country
    from
        Calls
    join
        id_Country
    on 
        callee_id = id
)
select 
    country
from
    call_country
group by
    country
having
    avg(duration) > (select avg(duration) from Calls);