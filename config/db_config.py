import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="danish@sql12345",
        database="retail_sdw"
    )
