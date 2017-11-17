"""Module containing steps for sending GET requests to the /accounts endpoint."""
from uuid import uuid4

from aloe import step, world
from requests import get

from features.helper import *
from features.helper.accounts_api import create_random_account


@step("I try to get the details of an existing account")
def get_exisiting_account_details(self):
    create_random_account()
    world.response = get(url(f"/accounts/{world.username}"))


@step(r"the response should contain the user's public details")
def check_response_contains_user_details(self):
    expect(world.response.json()).to(equal({"username": world.username}))


@step(r"I try to get the details of an account that doesn't exist")
def get_non_existant_account(self):
    world.response = get(url(f"/accounts/{uuid4()}"))

@step(r"I try to get all the usernames that are currently in use")
def get_all_usernames(self):
    world.usernames = [create_random_account()["username"] for _ in range(10)]
    world.response = get(url("/accounts"))

@step(r"the response should contain a list of all used usernames")
def check_response_contains_existing_usernames(self):
    expect(world.response.json()).to(contain(*world.usernames))
