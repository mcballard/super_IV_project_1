Feature: Secret agents need to manage their reimbursement requests

  Scenario Outline: As a secret agent, I should be able to login to my account
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Login Continue button
    Then  I should be on a page with the title Super Secret Agent Stuff


    Examples:
      | username | password         |
      | jb007    | shakennotstirred |


  Scenario Outline: As a secret agent, I should be able to cancel a reimbursement request
    Given I am on the home page
    When  I click "Cancel Reimbursement Request"
    When  I enter <reimbursement_request_id> of the request I would like to cancel
    When  I click the Cancel Request button
    When  I click the Cancel Request Continue button
    Then  I should be on a page with the title Super Secret Agent Stuff

      Examples:
        | reimbursement_request_id |
        | 1                        |


  Scenario Outline: As a secret agent, I should not be able to cancel a reimbursement request with a bad id
    Given I am on the home page
    When  I click "Cancel Reimbursement Request"
    When  I enter <reimbursement_request_id> of the request I would like to cancel
    When  I click the Cancel Request button
    When  I click the Cancel Request Continue button
    Then  I should be on a page with the title Super Secret Agent Stuff

      Examples:
        | reimbursement_request_id |
        | 5000000                  |
