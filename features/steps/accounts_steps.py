"""Module containing test execution steps for calling the accounts API."""
from uuid import uuid4

from requests import get, post
from aloe import step, world

from features.helper import *


def post_account(json):
    """Send a POST request to the /accounts endpoint with the given json payload."""
    world.response = post(url("/accounts"), json=json)


@step(r"I try to create an account ((?:\w ?)+)")
def create_account_valid_request(self, condition):
    world.username = str(uuid4())
    world.password = str(uuid4())
    world.email = f"{world.username}@gmail.com"
    json = {"username": world.username, "password": world.password, "email": world.email}

    if condition.startswith("without providing a"):
        argument_name = condition.split()[-1]
        del json[argument_name]

    elif condition == "whilst providing an extra argument":
        world.unexpected_argument = {"well,": "this is unexpected"}
        json.update(world.unexpected_argument)

    elif condition == "using a used username":
        post_account(json)  # Post account an extra time

    post_account(json)


@step(r"I should get a (\d+) response")
def check_response(self, expected_response_code):
    expect(world.response.status_code).to(equal(int(expected_response_code)))


@step("an account with that username should be created")
def confirm_account_created(self):
    expect(get(url(f"/accounts/{world.username}")).status_code).to(equal(200))
