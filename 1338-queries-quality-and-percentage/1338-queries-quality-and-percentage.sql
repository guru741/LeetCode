select query_name,
Round(Avg(cast(rating as decimal) / position),2) as quality,
Round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*) ,2) as poor_query_percentage
from Queries
group by query_name;