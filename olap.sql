CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    date DATE,
    year INT,
    month INT
);

CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(30)
);

CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(30)
);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    date_key INT,
    product_key INT,
    customer_key INT,
    quantity INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key)
);

INSERT INTO dim_date VALUES (1,'2024-01-01',2024,1),(2,'2024-02-01',2024,2),(3,'2024-03-01',2024,3);
INSERT INTO dim_product VALUES (1,'Laptop','Electronics'),(2,'Chair','Furniture'),(3,'Mouse','Electronics');
INSERT INTO dim_customer VALUES (1,'John','NYC'),(2,'Sarah','LA'),(3,'Mike','Chicago');
INSERT INTO fact_sales VALUES (1,1,1,1,2,2400),(2,1,2,2,1,350),(3,2,3,3,5,125),(4,3,1,1,1,1200);

SELECT p.name, SUM(s.amount) total FROM fact_sales s
JOIN dim_product p ON s.product_key=p.product_key
WHERE p.category='Electronics' GROUP BY p.name;

SELECT d.month, p.category, SUM(s.amount) total FROM fact_sales s
JOIN dim_date d ON s.date_key=d.date_key
JOIN dim_product p ON s.product_key=p.product_key
WHERE d.year=2024 AND p.category='Electronics' GROUP BY d.month, p.category;

SELECT d.year, p.category, SUM(s.amount) total FROM fact_sales s
JOIN dim_date d ON s.date_key=d.date_key
JOIN dim_product p ON s.product_key=p.product_key
GROUP BY d.year, p.category;

SELECT d.month, p.name, c.city, SUM(s.amount) total FROM fact_sales s
JOIN dim_date d ON s.date_key=d.date_key
JOIN dim_product p ON s.product_key=p.product_key
JOIN dim_customer c ON s.customer_key=c.customer_key
GROUP BY d.month, p.name, c.city;