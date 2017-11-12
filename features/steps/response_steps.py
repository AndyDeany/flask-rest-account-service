"""Module containing generic API response checking steps."""
from aloe import step, world


@step(r"I should get a (\d+) response")
def check_response(self, expected_response_code):
    expect(world.response.status_code).to(equal(int(expected_response_code)))
