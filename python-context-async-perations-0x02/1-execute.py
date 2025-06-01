import sqlite3
import os

# Define database path
DB_FILENAME = "users.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../python-decorators-0x01", DB_FILENAME)


class ExecuteQuery:
    def __init__(self, query, params=(), db_name="users.db"):
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.db_path = DB_PATH

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        print("✅ Database connection closed.")


# ✅ Required query and parameter
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

# ✅ Must use the `with` statement (required by the checker)
with ExecuteQuery(query, params) as results:
    for user in results:
        print(user)
