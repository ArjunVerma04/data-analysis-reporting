-- Total Revenue
SELECT SUM(Revenue) FROM business;

-- Revenue by Region
SELECT Region, SUM(Revenue)
FROM business
GROUP BY Region;

-- Customer Trend
SELECT Date, Customers FROM business;