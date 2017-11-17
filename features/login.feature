Feature: Credential validation

  As a developer of an authentication microservice
  I want to be able to check if a user's credentials are correct
  So that I can decide whether to supply them with an authentication token

  Scenario: Valid username login
    When I attempt to login with a valid username and password combination
    Then I should get a 200 response
    And the response should contain a key suggesting that login was successful

  Scenario: Valid email address login
    When I attempt to login with a valid email and password combination
    Then I should get a 200 response
    And the response should contain a key suggesting that login was successful

  Scenario: Invalid username login
    When I attempt to login with an invalid username and password combination
    Then I should get a 401 response
    And the response should contain a key suggesting that login was unsuccessful

  Scenario: Invalid email address login
    When I attempt to login with an invalid email and password combination
    Then I should get a 401 response
    And the response should contain a key suggesting that login was unsuccessful
