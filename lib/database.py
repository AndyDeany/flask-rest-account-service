"""Module containing functions for accessing the database for the REST API."""
import sqlite3 as _sqlite


DATABASE_FILE = "api.db"

def sql(query):
    """Execute the given SQL query on the database."""
    with _sqlite.connect(DATABASE_FILE) as connection:
        return connection.cursor().execute(query)


def find_account(login):
    """Return the account with the given login or None if it doesn't exist."""
    login = login.casefold()
    login_type = "email" if "@" in login else "username"
    sql("SELECT email, username, password"
        "FROM accounts"
        f"WHERE {login_type} = {login}")


def add_account(username, password, email):
    """Add the given account information to the database."""
    sql("INSERT INTO accounts VALUES({username}, {password}, {email})")
