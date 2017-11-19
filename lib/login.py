"""Module containing code for the /login endpoint."""
from flask_restful import Resource, abort
from flask import request
from werkzeug.security import check_password_hash

from lib.accounts import find_account


class Login(Resource):
    """Class representing the /login endpoint in the API."""

    def post(self):
        """Find out whether the given json credentials are valid."""
        json = request.get_json()

        login = json.pop("username", None) or json.pop("email", None)
        if login is None:
            abort(400, message="One of the following arguments are required: 'username', 'email'")
        try:
            password = json.pop("password")
        except KeyError:
            abort(400, message="The 'password' argument is required.")

        if json:
            abort(400, message=f"Unexpected arguments: {json}")

        account = find_account(login)

        if account is None:
            abort(404, message=f"No account exists with username '{username}'.")

        success = check_password_hash(account["password"], password)

        json = {"success": str(success).lower()}
        return json, 200 if success else 401
