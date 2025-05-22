import time
from datetime import datetime
import sqlite3
import functools
import os

DB_FILENAME = 'users.db'
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILENAME)

query_cache = {}

def with_db_connection(func):
    """
    Opens a SQLite connection, passes it to the decorated function,
    and closes the connection afterwards.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(DB_PATH)
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """
    Decorator to cache query results based on the SQL query string.
    Assumes the decorated function receives `conn` as first argument,
    and the SQL query string as the second argument.
    """
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("⚡ Using cached result for query:")
            print(f"    {query}")
            return query_cache[query]

        print("📥 Executing and caching query:")
        print(f"    {query}")
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Executes the provided SQL query and returns all results.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    # First call - executes and caches result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"First call fetched {len(users)} users.")

    # Second call - should use cached result
    users_cached = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Second call fetched {len(users_cached)} users (from cache).")
