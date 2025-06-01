import sqlite3
import os

# Define database path
DB_FILENAME = "users.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../python-decorators-0x01", DB_FILENAME)

print("🔍 Using DB at:", DB_PATH)


class DatabaseConnection:
    """
    Custom context manager to handle opening and closing
    a SQLite database connection.
    """

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
            print("✅ Database connection closed.")


# Use the context manager to query the database
if __name__ == "__main__":
    with DatabaseConnection(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        print("📋 Users in the database:")
        for user in results:
            print(user)
