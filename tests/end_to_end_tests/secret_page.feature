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


  Scenario Outline: As a secret agent, I should not be able to login to my account with incorrect login info
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Login Continue button
    Then  I should be on a page with the title Super Secret Login


    Examples:
      | username | password         |
      | jb009    | shakennotstirred |


  Scenario Outline: As a secret agent, I should not be able to login to my account with incorrect login info
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Login Continue button
    Then  I should be on a page with the title Super Secret Login


    Examples:
      | username | password         |
      | jb007    | shakennotstirrup |


  Scenario Outline: As a secret agent, I should be able to create a reimbursement request
    Given I am on the home page
    When  I click "Create Reimbursement Request"
    When  I select 2 as my reason
    When  I enter <comment> as my comment
    When  I enter <amount> as my amount
    When  I click the Create Request button
    When  I click the Create Request Continue button
    Then  I should be on a page with the title Super Secret Agent Stuff

      Examples:
        | comment        | amount |
        | I am a comment | 550.50 |

  Scenario: As a secret agent, I should be able to view the total amount I have requested
    Given I am on the home page
    When  I click "View My Total Amount Requested"
    When  I click the View Total Amount button
    When  I click the View Total Continue button
    Then  I should be on a page with the title Super Secret Agent Stuff


  Scenario: As a secret agent, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Log Out Continue button
    Then  I should be on a page with the title Super Secret Login

