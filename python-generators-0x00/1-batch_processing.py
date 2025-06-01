import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = "ALX_prodev"


def stream_users_in_batches(batch_size):
    conn = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = conn.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute(
            "SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset)
        )
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    conn.close()
    return


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        # Single loop here to filter users over 25
        filtered = [user for user in batch if user.get("age", 0) > 25]
        yield filtered
    return
