import sqlite3
import functools
from datetime import datetime
import os

DB_FILENAME = "users.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILENAME)


def with_db_connection(func):
    """
    Decorator that opens a DB connection, passes it to the function,
    and ensures the connection is closed after function completes.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(DB_PATH)
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()

    return wrapper


def transactional(func):
    """
    Decorator to wrap DB operations in a transaction.
    Commits if no exception, rolls back on error.
    Assumes the first argument is a sqlite3.Connection.
    """

    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception:
            conn.rollback()
            raise

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Updates the email of the user with given user_id.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


if __name__ == "__main__":
    update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
    print("✅ Email updated successfully.")
