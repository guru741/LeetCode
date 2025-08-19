select id,
    max(case when month = 'jan' then revenue end)as Jan_Revenue,
    max(case when month = 'feb' then revenue end)as Feb_Revenue,
    max(case when month = 'mar' then revenue end)as Mar_Revenue,
    max(case when month = 'apr' then revenue end)as Apr_Revenue,
    max(case when month = 'may' then revenue end)as May_Revenue,
    max(case when month = 'jun' then revenue end)as Jun_Revenue,
    max(case when month = 'jul' then revenue end)as Jul_Revenue,
    max(case when month = 'aug' then revenue end)as Aug_Revenue,
    max(case when month = 'sep' then revenue end)as Sep_Revenue,
    max(case when month = 'oct' then revenue end)as Oct_Revenue,
    max(case when month = 'nov' then revenue end)as Nov_Revenue,
    max(case when month = 'dec' then revenue end)as Dec_Revenue
    from Department
    group by id;