import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")
print(f"Inspecting DB at: {db_path}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Count users
if ("users",) in tables:
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"Number of users in 'users' table: {count}")
else:
    print("No 'users' table found!")

conn.close()
