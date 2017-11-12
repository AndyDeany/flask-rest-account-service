"""Module containing test execution steps for calling the accounts API."""
from uuid import uuid4

from requests import get, post
from aloe import step, world

from features.helper import *


@step(r"I try to create an account using an? (used|unused) username")
def create_account_valid(self, use):
    world.username = str(uuid4())
    world.password = str(uuid4())
    world.email = f"{world.username}@gmail.com"
    json = {"username": world.username, "password": world.password, "email": world.email}
    world.response = post(url("/accounts"), json=json)
    if use == "used":
        world.response = post(url("/accounts"), json=json)


@step(r"I should get a (\d+) response")
def check_response(self, expected_response_code):
    expect(world.response.status_code).to(equal(int(expected_response_code)))


@step("an account with that username should be created")
def confirm_account_created(self):
    expect(get(url(f"/accounts/{world.username}")).status_code).to(equal(200))
