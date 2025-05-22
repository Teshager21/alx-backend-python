import time
from datetime import datetime
import sqlite3
import functools
import os

DB_FILENAME = 'users.db'
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILENAME)

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

def retry_on_failure(retries=3, delay=2):
    """
    Decorator factory that retries the decorated function up to `retries` times
    with `delay` seconds pause if an exception is raised.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"⚠️ Attempt {attempt} failed with error: {e}")
                    if attempt == retries:
                        print("❌ All retry attempts failed.")
                        raise
                    print(f"⏳ Retrying after {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetches all users from the database with automatic retry on failure.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

if __name__ == "__main__":
    users = fetch_users_with_retry()
    print(f"📋 Fetched {len(users)} users:")
    for user in users:
        print(user)
