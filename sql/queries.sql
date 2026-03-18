-- Total Revenue
SELECT SUM(sales) AS total_revenue FROM ecommerce;

-- Revenue by Region
SELECT region, SUM(sales) FROM ecommerce GROUP BY region;

-- Top Categories
SELECT category, SUM(sales) AS revenue
FROM ecommerce
GROUP BY category
ORDER BY revenue DESC;

-- Monthly Trend
SELECT strftime('%Y-%m', order_date) AS month, SUM(sales)
FROM ecommerce
GROUP BY month;