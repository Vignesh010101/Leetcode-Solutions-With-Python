# Write your MySQL query statement below
SELECT
    product_id,
    IF(SUM(units) > 0, ROUND(SUM(revenue) / SUM(units), 2), 0) AS average_price
FROM (
    SELECT
        p.product_id,
        p.start_date,
        p.end_date,
        p.price,
        u.purchase_date,
        u.units,
        p.price * u.units AS revenue
    FROM Prices p
    JOIN UnitsSold u ON p.product_id = u.product_id
    WHERE u.purchase_date BETWEEN p.start_date AND p.end_date
) AS merged_data
GROUP BY product_id

UNION

SELECT
    p.product_id,
    0 AS average_price
FROM Prices p
LEFT JOIN (
    SELECT DISTINCT product_id
    FROM UnitsSold
) AS sold_products ON p.product_id = sold_products.product_id
WHERE sold_products.product_id IS NULL;