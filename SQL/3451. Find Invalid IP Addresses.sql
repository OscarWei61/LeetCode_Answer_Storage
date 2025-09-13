# Write your MySQL query statement below
select ip, count(*) as invalid_count
from logs
where 
    length(ip) - length(replace(ip, '.', "")) + 1 != 4 

    or

    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 1), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 4), '.', -1) AS UNSIGNED) > 255
    

    or

    ip REGEXP '(^|\\.)(0[0-9]+)(\\.|$)'

group by ip
order by invalid_count DESC, ip DESC;