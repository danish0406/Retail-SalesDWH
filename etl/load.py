import pandas as pd
from config.db_config import get_connection

def load_customers():
    conn = get_connection()
    cursor = conn.cursor()

    df = pd.read_csv("data/customers_raw.csv")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO dim_customer (customer_id, age, gender)
            VALUES (%s, %s, %s)
        """, (int(row["customer_id"]), int(row["age"]), row["gender"]))

    conn.commit()
    cursor.close()
    conn.close()

    print("Customers loaded successfully.")

   
