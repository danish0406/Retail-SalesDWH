import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="danish@sql12345",
    database="retail_sdw"
)

cursor = conn.cursor()

# Load CSVs
customers_df = pd.read_csv("data/customers_raw.csv")
products_df = pd.read_csv("data/products_raw.csv")
sales_df = pd.read_csv("data/sales_raw.csv")

# ---- INSERT CUSTOMERS ----
for _, row in customers_df.iterrows():
    cursor.execute("""
        INSERT INTO staging_customers (customer_id, age, gender)
        VALUES (%s, %s, %s)
    """, (row['customer_id'], row['age'], row['gender']))

# ---- INSERT PRODUCTS ----
for _, row in products_df.iterrows():
    cursor.execute("""
        INSERT INTO staging_products (product_id, product_name, category, cost_price, selling_price)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row['product_id'],
        row['product_name'],
        row['category'],
        row['cost_price'],
        row['selling_price']
    ))

# ---- INSERT SALES ----
for _, row in sales_df.iterrows():
    cursor.execute("""
        INSERT INTO staging_sales (sale_id, date, customer_id, product_id, city, quantity, unit_price, discount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['sale_id'],
        row['date'],
        row['customer_id'],
        row['product_id'],
        row['city'],
        row['quantity'],
        row['unit_price'],
        row['discount']
    ))

conn.commit()
cursor.close()
conn.close()

print("Staging data loaded successfully.")