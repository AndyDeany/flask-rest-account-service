from aloe import step, world

from features.helper import *


EXPECTED_MESSAGES = {
    "account creation was successful":
        "An account with username '{username}' was successfully created.",

    "the username is already in use":
        "An account already exists with username '{username}'.",

    "usernames cannot contain @ symbols":
        "The value of the 'username' field must not contain an '@' symbol.",

    "a required argument was missing":
        "The 'username', 'password' and 'email' arguments are required.",

    "an unexpected argument was given":
        "Unexpected arguments: {unexpected_argument}",

    "the user does not exist":
        "No account exists with username '{username}'.",

    "the password argument was missing":
        "The 'password' argument is required.",
}


@step("the response message should indicate that ((?:[\w@] ?)+)")
def check_message(self, message_purpose):
    expected_message = EXPECTED_MESSAGES[message_purpose]
    expected_message = expected_message.format(**world.__dict__)
    expect(world.response.json()["message"]).to(equal(expected_message))
