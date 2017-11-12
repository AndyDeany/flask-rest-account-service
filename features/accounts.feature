Feature: Accounts API

  As a developer
  I want to be able to create accounts for my users
  So that they can be identified

  Scenario: Successful account creation
    When I try to create an account using an unused username
    Then I should get a 201 response
    And the response message should indicate that account creation was successful
    And an account with that username should be created

  Scenario: Desired username already in use
    When I try to create an account using a used username
    Then I should get a 409 response
    And the response message should indicate that the username is already in use

  Scenario: Missing account creation argument
    When I try to create an account without providing an email
    Then I should get a 400 response
    And the response message should indicate that a required argument was missing

  Scenario: Unexpected account creation argument
    When I try to create an account whilst providing an extra argument
    Then I should get a 400 response
    And the response message should indicate that an unexpected argument was given
