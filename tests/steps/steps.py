from behave import given, when, then

@given(u'I am on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the login page')


@when(u'I enter <username> in the username')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <username> in the username')


@when(u'I enter <password> in the password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <password> in the password')


@when(u'I click the Login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Login button')


@when(u'I click the Continue button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Continue button')


@then(u'I am directed to the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am directed to the home page')


@given(u'I am on the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the home page')


@when(u'I click "Create Reimbursement Request"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Create Reimbursement Request"')


@when(u'I select the drop down menu for reason')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the drop down menu for reason')


@when(u'I select <reason> as my reason')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select <reason> as my reason')


@when(u'I enter <comment> as my comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <comment> as my comment')


@when(u'I enter <amount> as my amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <amount> as my amount')


@when(u'I click the Create Request button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Create Request button')


@then(u'I am left on the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am left on the home page')


@when(u'I click "View My Total Amount Requested"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "View My Total Amount Requested"')


@when(u'I click the View Total Amount button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the View Total Amount button')


@when(u'I click "Cancel Reimbursement Request"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Cancel Reimbursement Request"')


@when(u'I enter <reimbursement_request_id> of the request I would like to cancel')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <reimbursement_request_id> of the request I would like to cancel')


@when(u'I click the Cancel Request button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Cancel Request button')


@when(u'I click "Log Out"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Log Out"')


@when(u'I click the Log Out button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Log Out button')


@then(u'I am redirected to the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am redirected to the login page')
