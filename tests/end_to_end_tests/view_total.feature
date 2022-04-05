Feature: Secret agents need to view the total amount they have requested.

    Scenario: As a secret agent, I should be able to view the total amount I have requested
    Given I am on the home page
    When  I click "View My Total Amount Requested"
    When  I click the View Total Amount button
    When  I click the View Total Continue button
    Then  I should be on a page with the title Super Secret Agent Stuff


