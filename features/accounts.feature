Feature: Accounts API

  As a developer
  I want to be able to create accounts for my users
  So that they can be identified

  Scenario: Successful account creation
    When I try to create an account using an unused username
    Then I should get a 201 response
    And the response message should indicate that account creation was successful
    And an account with that username should be created
