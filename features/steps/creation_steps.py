"""Module containing test execution steps for calling the accounts API."""
from requests import get, post
from aloe import step, world

from features.helper import *   # pylint: disable=wildcard-import,unused-wildcard-import
from features.helper.accounts_api import post_account, generate_random_account_json


@step(r"I try to create an account ((?:\w ?)+)")
def create_account_valid_request(self, condition):
    json = generate_random_account_json()

    if condition.startswith("without providing a"):
        argument_name = condition.split()[-1]
        del json[argument_name]

    elif condition == "whilst providing an extra argument":
        world.unexpected_argument = {"well,": "this is unexpected"}
        json.update(world.unexpected_argument)

    elif condition == "using a used username":
        post_account(json)  # Post account an extra time

    post_account(json)


@step("an account with that username should be created")
def confirm_account_created(self):
    expect(get(url(f"/accounts/{world.username}")).status_code).to(equal(200))
