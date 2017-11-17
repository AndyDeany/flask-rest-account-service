Feature: Account retrieval

  As a developer
  I want to be able to get the details of a user's account
  So that it can be displayed on their profile

  Scenario: Successful account retrieval
    When I try to get the details of an existing account
    Then I should get a 200 response
    And the response should contain the user's public details

  Scenario: Account does not exist
    When I try to get the details of an account that doesn't exist
    Then I should get a 404 response
    And the response message should indicate that the requested user does not exist

  Scenario: Retrieving all used usernames
    When I try to get all the usernames currently in used
    Then I should get a 200 response
    And the response should contain a list of all used usernames
