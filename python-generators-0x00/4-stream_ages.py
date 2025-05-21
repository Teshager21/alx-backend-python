import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = "ALX_prodev"

def stream_user_ages():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:  # single loop yielding ages
        yield age

    cursor.close()
    conn.close()
    return

def calculate_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():  # second loop to consume generator
        total_age += age
        count += 1
    if count == 0:
        print("No users found.")
        return
    average = total_age / count
    print(f"Average age of users: {average:.2f}")

if __name__ == "__main__":
    calculate_average_age()
