from aloe import step, world


EXPECTED_MESSAGES = {
    "account creation was successful":
        "An account with username '{username}' was successfully created.",
}


@step("the response message should indicate that (\w+)")
def check_message(self, message_purpose):
    expected_message = EXPECTED_MESSAGES[message_purpose].format(world.__dict__)
    expect(world.response.json()["message"]).to(equal(expected_message))
