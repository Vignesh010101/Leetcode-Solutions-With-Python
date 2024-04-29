# Write your MySQL query statement below
with sample as(select requester_id id from RequestAccepted union all select accepter_id from RequestAccepted)
select id, count(*) num from sample group by 1 order by 2 desc limit 1