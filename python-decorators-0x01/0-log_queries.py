import os
import sqlite3
import functools
from datetime import datetime

# Absolute path to the SQLite database file
DB_FILENAME = "users.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILENAME)


def log_sql_queries(func):
    """
    Decorator that logs the SQL query before executing the decorated function.
    Assumes the decorated function accepts a 'query' argument as the first positional
    or keyword argument.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query") or (args[0] if args else None)
        if query:
            print(f"📥 Executing SQL Query:\n{query}\n")
        else:
            print("⚠️ Warning: No SQL query provided to log.")
        return func(*args, **kwargs)

    return wrapper


@log_sql_queries
def fetch_all_users(query):
    """
    Executes the provided SQL query against the users database
    and returns all fetched results.
    """
    print(f"📂 Connecting to database at: {DB_PATH}")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
    return results


def main():
    """
    Main function to fetch and display all users from the database.
    """
    sql_query = "SELECT * FROM users;"
    users = fetch_all_users(query=sql_query)
    print(f"📋 Retrieved {len(users)} user(s):")
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
