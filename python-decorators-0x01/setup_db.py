import sqlite3
from datetime import datetime
import os

# Path to create DB in the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "users.db")

# Connect to SQLite DB (creates it if it doesn't exist)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create 'users' table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
)
"""
)

# Insert a sample user
now = datetime.utcnow().isoformat()
cursor.execute(
    """
INSERT INTO users (email, password, first_name, last_name, created_at, updated_at)
VALUES (?, ?, ?, ?, ?, ?)
""",
    ("demo@example.com", "hashed_pw", "Demo", "User", now, now),
)

conn.commit()
conn.close()

print(f"✅ Database created successfully at: {db_path}")
