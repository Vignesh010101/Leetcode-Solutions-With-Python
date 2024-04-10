SELECT project_id, ROUND( AVG(experience_years), 2) AS average_years
FROM (
SELECT employee_id, name, experience_years, project_id
FROM project p
JOIN employee e USING (employee_id)) a
GROUP BY project_id