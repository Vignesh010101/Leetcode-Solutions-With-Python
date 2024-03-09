# Write your MySQL query statement below
select email from Person group by 1 having count(*)>1;