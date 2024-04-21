# Write your MySQL query statement below
select v1.machine_id,round(avg(v2.timestamp-v1.timestamp),3) as processing_time from Activity v1, Activity v2
where v1.machine_id=v2.machine_id and v1.process_id=v2.process_id and v1.activity_type='start' and v2.activity_type='end'
group by v1.machine_id; 