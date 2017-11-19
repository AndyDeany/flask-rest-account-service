"""Main file for running the accounts service API."""
from flask import Flask
from flask_restful import Api

from lib.accounts import Accounts, AccountsList
from lib.login import Login


app = Flask(__name__)
api = Api(app)


api.add_resource(AccountsList, "/accounts")
api.add_resource(Accounts, "/accounts/<username>")

api.add_resource(Login, "/login")


if __name__ == "__main__":
    app.run(debug=True)
