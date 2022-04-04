Feature: Secret agents need to manage their reimbursement requests

  Scenario: As a secret agent, I should be able to login to my account
    Given I am on the login page
    When  I enter my username
    When  I enter my password
    When  I click the Login button
    Then  I am given the message "Successful login, click continue!", and then redirected to the home page


  Scenario: As a secret agent, I should be able to create a reimbursement request
    Given I am on the home page
    When  I click "Create Reimbursement Request"
    When  I select the drop down menu for reason
    When  I select the specific reason
    When  I enter the comment
    When  I enter the amount
    When  I click the Create Request button
    Then  I am given a message "Request successfully generated with ID number <reimbursement request id>",and left on the home page


  Scenario: As a secret agent, I should be able to view the total amount I have requested
    Given I am on the home page
    When  I click "View My Total Amount Requested"
    When  I click the View Total Amount button
    Then  I am given a message "Your total amount requested across all requests is <total requested amount>, and left on the home page


  Scenario: As a secret agent, I should be able to cancel a reimbursement request
    Given I am on the home page
    When  I click "Cancel Reimbursement Request"
    When  I enter the reimbursement request ID of the request I would like to cancel
    When  I click the Cancel Request button
    Then  I am given a message "The request with ID number <request ID number> has been successfully deleted", and I am left on the home page


  Scenario: As a secret agent, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    Then  I am given a message "Successfully logged out!", and I am redirected to the login page

