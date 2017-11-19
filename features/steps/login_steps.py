"""Module containing steps for sending POSt requests to the /login endpoint."""
from aloe import step, world
from requests import post

from features.helper import *
from features.helper.accounts_api import create_random_account


@step(r"I attempt to login with an? (in)?valid (\w+) and password combination")
def attempt_login(self, invalid, login):
    json = create_random_account()
    json = {key: json[key] for key in (login, "password")}
    if invalid:
        json["password"] = "very_wr0ng_pa$$w0rd"
    world.response = post(url("/login"), json=json)


@step(r"I attempt to login without providing a password")
def attempt_no_password_login(self):
    create_random_account()
    world.response = post(url("/login"), json={"username": world.username})


@step(r"I provide an extra argument whilst attempting to login")
def attempt_login_with_extra_arg(self):
    json = create_random_account()
    del json["email"]
    world.unexpected_argument = {"you": "can't login with this"}
    json.update(world.unexpected_argument)
    world.response = post(url("/login"), json=json)


@step(r"the response should contain a key suggesting that login was (un)?successful")
def check_response_login_status(self, unsuccessful):
    success = str(not bool(unsuccessful)).lower()
    expect(world.response.json()).to(equal({"success": success}))
