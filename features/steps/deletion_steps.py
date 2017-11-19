"""Module containing steps for sending POST requests to the /login endpoint."""
from uuid import uuid4

from aloe import step, world
from requests import get, delete

from features.helper import *
from features.helper.accounts_api import create_random_account


@step(r"I try to delete a user's account")
def delete_user_account(self):
    create_random_account()
    world.response = delete(url(f"/accounts/{world.username}"))


@step(r"I try to delete an account that doesn't exist")
def delete_non_existant_account(self):
    world.username = uuid4()
    world.response = delete(url(f"/accounts/{world.username}"))


@step(r"I try to delete all users' accounts")
def delete_all_accounts(self):
    create_random_account()
    world.initial_accounts = get(url("/accounts")).json()
    world.response = delete(url("/accounts"))


@step(r"the user's account should be deleted")
def check_user_account_deleted(self):
    expect(get(url(f"/accounts/{world.response}")).status_code).to(equal(404))


@step(r"no accounts should be deleted")
def check_response_login_status(self):
    accounts = get(url("/accounts")).json()
    expect(accounts).to(contain(*world.initial_accounts))
