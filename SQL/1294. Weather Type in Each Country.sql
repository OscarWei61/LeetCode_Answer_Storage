# Write your MySQL query statement below
with weather_avarage_table as (
    select 
        country_id, 
        avg(weather_state) as weather_state_avg
    from Weather
    WHERE YEAR(day) = 2019 AND MONTH(day) = 11
    GROUP BY country_id
)

select 
    country_name, 
    (
        case 
            when weather_state_avg >= 25 then "Hot"
            when weather_state_avg <= 15 then 'Cold'
            else "Warm"
        end
    ) as weather_type

from Countries
join weather_avarage_table
on weather_avarage_table.country_id = Countries.country_id;