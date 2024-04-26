# Write your MySQL query statement below
select e.name from Employee e,Employee v
where e.id=v.managerId
group by e.id
having count(v.managerId)>=5;