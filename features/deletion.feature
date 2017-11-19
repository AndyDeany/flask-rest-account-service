Feature: Account deletion

  As a developer
  I want to be able to delete a user's account
  So that user's account can be deleted upon requested
  # This contributes to compliance with GDPR

  Scenario: Deleting a user's account
    When I try to delete a user's account
    Then I should get a 200 response
    And the user's account should be deleted

  Scenario: Deleting all accounts simulateously is not allowed
    When I try to delete all users' accounts
    Then I should get a 405 response
    And no accounts should be deleted
