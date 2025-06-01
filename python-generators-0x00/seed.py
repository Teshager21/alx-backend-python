import mysql.connector
import csv
import os
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
print("Current working directory:", os.getcwd())

# Environment configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = "ALX_prodev"


def connect_db():
    return mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)


def create_database(connection):
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()


def connect_to_prodev():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX idx_user_id (user_id)
        )
    """
    )
    cursor.close()


def insert_data(connection, data):
    cursor = connection.cursor()
    insert_query = """
        INSERT INTO user_data (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            email = VALUES(email),
            age = VALUES(age)
    """
    cursor.executemany(insert_query, data)
    connection.commit()
    cursor.close()


def load_csv_data(filename="user_data.csv"):
    data = []
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        print("CSV Columns:", reader.fieldnames)  # Debug print to check columns
        for row in reader:
            user_id = str(uuid.uuid4())  # Generate UUID for user_id
            name = row.get("name")
            email = row.get("email")
            age = float(row.get("age", 0))  # Convert age to float, default 0 if missing
            data.append((user_id, name, email, age))
    return data


if __name__ == "__main__":
    try:
        # Step 1: Create DB
        root_conn = connect_db()
        create_database(root_conn)
        root_conn.close()

        # Step 2: Connect to ALX_prodev
        conn = connect_to_prodev()
        create_table(conn)

        # Step 3: Load data and insert
        data = load_csv_data("data/3888260f107e3701e3cd81af49ef997cf70b6395.csv")
        insert_data(conn, data)

        conn.close()
        print("✅ Database seeded successfully.")
    except Exception as e:
        print("❌ Error:", e)
