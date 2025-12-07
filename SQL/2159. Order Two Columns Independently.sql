with first_col_asc as (
  select 
  
    first_col,
    ROW_NUMBER() OVER (ORDER BY first_col ASC) AS rn
  
  from Data
),
  second_col_desc as (
  select 
    second_col,
    ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rn 
  
  from Data
  
)

select first_col_asc.first_col, second_col_desc.second_col
from first_col_asc
join second_col_desc
on first_col_asc.rn = second_col_desc.rn;