"""Run this file using python to run the RESTful API.

Created: 2017-08-07
Author: Andrew Dean
"""
from flask import Flask
from flask_restful import Api

from lib.accounts import Accounts, AccountsList


app = Flask(__name__)
api = Api(app)


api.add_resource(AccountsList, "/accounts")
api.add_resource(Accounts, "/accounts/<username>")


if __name__ == "__main__":
    app.run(debug=True)
