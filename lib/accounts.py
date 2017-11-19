"""This file contains code for the /accounts endpoint."""
from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser
from flask import request
from werkzeug.security import generate_password_hash


ACCOUNTS = []   # TODO: replace with a database (SQL Alchemy?)

def find_account(username):
    """Return the account with the given username or None if it doesn't exist."""
    username = username.casefold()
    for account in ACCOUNTS:
        if account["username"].casefold() == username:
            return account
    return None


class Accounts(Resource):
    """Class representing the /accounts/{username} endpoint in the REST API."""

    def get(self, username):
        """Get the details of the account with the given `username` parameter."""
        account = find_account(username)
        if account is None:
            abort(404, message=f"No account exists with username '{username}'.")

        # Remove email and password from response
        account.pop("email")
        account.pop("password")

        return account

    def delete(self, username):
        """Delete the account with the given username."""
        account = find_account(username)
        if account is None:
            abort(404, message=f"No account exists with username '{username}'.")

        ACCOUNTS.remove(account)


class AccountsList(Resource):
    """Class representing the base /accounts endpoint in the REST API."""

    def get(self):
        """Get all existing account usernames."""
        return [account["username"] for account in ACCOUNTS]

    def post(self):
        """Add a new account."""
        json = request.get_json()
        try:
            username = json.pop("username")
            password = json.pop("password")
            email = json.pop("email")
        except KeyError:
            abort(400, message="The 'username', 'password' and 'email' arguments are required.")

        if json:
            abort(400, message=f"Unexpected arguments: {json}")

        if "@" in username:
            abort(422, message="The value of the 'username' field must not contain an '@' symbol.")

        if find_account(username) is not None:
            abort(409, message=f"An account already exists with username '{username}'.")

        ACCOUNTS.append({
            "username": username,
            "password": generate_password_hash(password),
            "email": email,
        })

        json = {"message": f"An account with username '{username}' was successfully created."}
        return json, 201
