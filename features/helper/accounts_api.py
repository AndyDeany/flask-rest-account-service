"""Module containing helper methods for accessing the /accounts endpoint of the API."""
from uuid import uuid4

from aloe import world
from requests import post

from features.helper import url


def generate_random_account_json():
    """Generate random credentials for creating an account with."""
    world.username = str(uuid4())
    world.password = str(uuid4())
    world.email = f"{world.username}@gmail.com"
    return {"username": world.username, "password": world.password, "email": world.email}


def post_account(json):
    """Send a POST request to the /accounts endpoint with the given json payload."""
    world.response = post(url("/accounts"), json=json)


def create_random_account():
    """Create a random account and return the credentials."""
    json = generate_random_account_json()
    post_account(json)
    return json
