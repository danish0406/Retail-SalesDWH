import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# BASIC CONFIG
# -----------------------------
NUM_CUSTOMERS = 200
NUM_PRODUCTS = 20
NUM_TRANSACTIONS = 6000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

# -----------------------------
# STATIC MASTER DATA
# -----------------------------

cities = [
    ("Mumbai", "West"),
    ("Delhi", "North"),
    ("Bangalore", "South"),
    ("Hyderabad", "South"),
    ("Lucknow", "North")
]

categories = ["Laptops", "Smartphones", "Accessories", "Appliances"]

# -----------------------------
# GENERATE CUSTOMERS
# -----------------------------

customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": i,
        "age": random.randint(18, 60),
        "gender": random.choice(["Male", "Female"])
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# GENERATE PRODUCTS
# -----------------------------

products = []

for i in range(1, NUM_PRODUCTS + 1):
    category = random.choice(categories)

    cost_price = random.randint(500, 50000)
    selling_price = cost_price * random.uniform(1.1, 1.4)

    products.append({
        "product_id": i,
        "product_name": f"Product_{i}",
        "category": category,
        "cost_price": round(cost_price, 2),
        "selling_price": round(selling_price, 2)
    })

products_df = pd.DataFrame(products)

# -----------------------------
# GENERATE SALES TRANSACTIONS
# -----------------------------

sales = []

date_range = (END_DATE - START_DATE).days

for i in range(1, NUM_TRANSACTIONS + 1):

    product = products_df.sample(1).iloc[0]
    city = random.choice(cities)

    sale_date = START_DATE + timedelta(days=random.randint(0, date_range))

    quantity = random.randint(1, 3)

    discount = random.choice([0, 0.05, 0.1, 0.15])

    sales.append({
        "sale_id": i,
        "date": sale_date,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "product_id": product["product_id"],
        "city": city[0],
        "quantity": quantity,
        "unit_price": product["selling_price"],
        "discount": discount
    })

sales_df = pd.DataFrame(sales)

# -----------------------------
# SAVE RAW DATA
# -----------------------------

sales_df.to_csv("data/sales_raw.csv", index=False)
customers_df.to_csv("data/customers_raw.csv", index=False)
products_df.to_csv("data/products_raw.csv", index=False)

print("Data generation completed.")
