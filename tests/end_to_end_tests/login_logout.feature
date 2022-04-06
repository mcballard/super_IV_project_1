Feature: Secret agents need to manage their reimbursement requests


  Scenario Outline: As a secret agent, I should not be able to login to my account with incorrect login info
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I am not logged in and see an error with an x icon
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
    When  I am not logged in and see an error with an x icon
    When  I click the Login Continue button
    Then  I should be on a page with the title Super Secret Login


    Examples:
      | username | password         |
      | jb007    | shakennotstirrup |

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


  Scenario: As a secret agent, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Log Out Continue button
    Then  I should be on a page with the title Super Secret Login