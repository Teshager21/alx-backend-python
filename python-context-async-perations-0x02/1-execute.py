import sqlite3
import os

class ExecuteQuery:
    def __init__(self, query, params=(), db_name="users.db"):
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        # Get absolute path to the database in the same folder
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()  # Return query results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        print("✅ Database connection closed.")
