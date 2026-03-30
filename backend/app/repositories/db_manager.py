from mysql.connector import pooling
import os

# Create a connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=5,
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


def get_connection():
    return connection_pool.get_connection()
