# Write your MySQL query statement below
SELECT 
    state,
    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') AS cities,
    SUM(IF(LEFT(state, 1) = LEFT(city, 1), 1, 0)) AS matching_letter_count
FROM 
    cities
GROUP BY 
    state
HAVING 
    COUNT(city) >= 3 
    AND matching_letter_count >= 1
ORDER BY 
    matching_letter_count DESC, 
    state ASC;