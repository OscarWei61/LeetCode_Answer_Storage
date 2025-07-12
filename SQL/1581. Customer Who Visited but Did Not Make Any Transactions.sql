SELECT
    customer_id,
     COUNT(*) AS count_no_trans
from
    Visits
where
    visit_id NOT IN (select visit_id from transactions)
GROUP BY 
    customer_id;