from behave import given, when, then


@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('https://p1-bucket-test-mcballard.s3.amazonaws.com/login.html')


@when(u'I enter {username} in the username')
def step_impl(context, username):
    context.secret_page_poms.username_input().send_keys(username)


@when(u'I enter {password} in the password')
def step_impl(context, password):
    context.secret_page_poms.password_input().send_keys(password)


@when(u'I click the Login button')
def step_impl(context):
    context.secret_page_poms.login_button().click()


@when(u'I click the Login Continue button')
def step_impl(context):
    context.secret_page_poms.login_continue_button().click()


@then(u'I should be on a page with the title Super Secret Agent Stuff')
def step_impl(context):
    assert context.driver.title == "Super Secret Agent Stuff"


@given(u'I am on the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the home page')


@when(u'I click "Create Reimbursement Request"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Create Reimbursement Request"')


@when(u'I select the drop down menu for reason')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the drop down menu for reason')


@when(u'I select {reason} as my reason')
def step_impl(context, reason):
    raise NotImplementedError(u'STEP: When I select <reason> as my reason')


@when(u'I enter {comment} as my comment')
def step_impl(context, comment: str):
    raise NotImplementedError(u'STEP: When I enter <comment> as my comment')


@when(u'I enter {amount} as my amount')
def step_impl(context, amount: float):
    raise NotImplementedError(u'STEP: When I enter <amount> as my amount')


@when(u'I click the Create Request button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Create Request button')


@when(u'I click the Create Request Continue button')
def step_impl(context):
    context.secret_page_poms.create_request_continue_button().click()


@when(u'I click "View My Total Amount Requested"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "View My Total Amount Requested"')


@when(u'I click the View Total Amount button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the View Total Amount button')


@when(u'I click the View Total Continue button')
def step_impl(context):
    context.secret_page_poms.view_total_continue_button().click()


@when(u'I click "Cancel Reimbursement Request"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Cancel Reimbursement Request"')


@when(u'I enter <reimbursement_request_id> of the request I would like to cancel')
def step_impl(context, reimbursement_request_id: int):
    raise NotImplementedError(u'STEP: When I enter <reimbursement_request_id> of the request I would like to cancel')


@when(u'I click the Cancel Request button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Cancel Request button')


@when(u'I click the Cancel Request Continue button')
def step_impl(context):
    context.secret_page_poms.cancel_request_continue_button().click()


@when(u'I click "Log Out"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Log Out"')


@when(u'I click the Log Out button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Log Out button')


@when(u'I click the Log Out Continue button')
def step_impl(context):
    context.secret_page_poms.log_out_continue_button().click()


@then(u'I should be on a page with the title Super Secret Login')
def step_impl(context, title):
    assert context.driver.title == "Super Secret Login"
