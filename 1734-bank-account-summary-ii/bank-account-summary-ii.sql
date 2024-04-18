# Write your MySQL query statement below
SELECT name, SUM(amount) AS balance
FROM Users
INNER JOIN Transactions ON Users.account = Transactions.account
GROUP BY name
HAVING SUM(amount) > 10000;