-- =========================
-- DIMENSION TABLES
-- =========================

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    month INT,
    quarter INT,
    year INT
);

CREATE TABLE dim_customer (
    customer_key INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE dim_product (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    cost_price DECIMAL(10,2),
    selling_price DECIMAL(10,2)
);

CREATE TABLE dim_city (
    city_key INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(50),
    region VARCHAR(50)
);

-- =========================
-- FACT TABLE
-- =========================

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    date_key INT,
    customer_key INT,
    product_key INT,
    city_key INT,
    quantity INT,
    revenue DECIMAL(12,2),
    cost DECIMAL(12,2),
    profit DECIMAL(12,2),

    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (city_key) REFERENCES dim_city(city_key)
);
