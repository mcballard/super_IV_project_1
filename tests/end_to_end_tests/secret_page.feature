Feature: Secret agents need to manage their reimbursement requests

  Scenario: As a secret agent, I should be able to login to my account
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Continue button
    Then  I should be on a page with the title {title}


  Scenario: As a secret agent, I should be able to create a reimbursement request
    Given I am on the home page
    When  I click "Create Reimbursement Request"
    When  I select the drop down menu for reason
    When  I select <reason> as my reason
    When  I enter <comment> as my comment
    When  I enter <amount> as my amount
    When  I click the Create Request button
    When  I click the Continue button
    Then  I should be on a page with the title {title}


  Scenario: As a secret agent, I should be able to view the total amount I have requested
    Given I am on the home page
    When  I click "View My Total Amount Requested"
    When  I click the View Total Amount button
    When  I click the Continue button
    Then  I should be on a page with the title {title}


  Scenario: As a secret agent, I should be able to cancel a reimbursement request
    Given I am on the home page
    When  I click "Cancel Reimbursement Request"
    When  I enter <reimbursement_request_id> of the request I would like to cancel
    When  I click the Cancel Request button
    When  I click the Continue button
    Then  I should be on a page with the title {title}


  Scenario: As a secret agent, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Continue button
    Then  I should be on a page with the title {title}

