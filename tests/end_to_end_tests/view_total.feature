Feature: Secret agents need to view the total amount they have requested.

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

    Scenario Outline: As a secret agent, I should be able to login to my account
        Given I am on the login page
        When  I enter <username> in the username
        When  I enter <password> in the password
        When  I click the Login button
        When  I click the Login Continue button
        Then  I should be on a page with the title Super Secret Agent Stuff


        Examples:
            | username | password  |
            | jwick    | mypoordog |

    Scenario: As a secret agent, I should be not able to view the total amount I have requested if i have no requests
        Given I am on the home page
        When  I click "View My Total Amount Requested"
        When  I click the View Total Amount button
        When  I am shown an error i see an x icon
        When  I click the View Total Continue button
        Then  I should be on a page with the title Super Secret Agent Stuff


