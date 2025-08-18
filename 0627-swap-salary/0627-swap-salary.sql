update Salary 
set sex = case
            when sex = 'm' then 'f'
            else 'm'
        end;
-- select id,name,sex,salary from Salary;