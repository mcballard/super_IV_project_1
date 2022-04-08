from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait


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
    context.driver.get('https://p1-bucket-test-mcballard.s3.amazonaws.com/secretagentpage.html')


@when(u'I click "Create Reimbursement Request"')
def step_impl(context):
    context.secret_page_poms.create_reimbursement_request().click()


@when(u'I select 2 as my reason')
def step_impl(context):
    context.secret_page_poms.select_reason().select_by_value('2')


@when(u'I enter {comment} as my comment')
def step_impl(context, comment: str):
    context.secret_page_poms.enter_comment().send_keys(comment)


@when(u'I enter {amount} as my amount')
def step_impl(context, amount: float):
    context.secret_page_poms.enter_amount().send_keys(amount)


@when(u'I click the Create Request button')
def step_impl(context):
    context.secret_page_poms.create_request_button().click()


@when(u'I click the Create Request Continue button')
def step_impl(context):
    context.secret_page_poms.create_request_continue_button().click()


@when(u'I click "View My Total Amount Requested"')
def step_impl(context):
    context.secret_page_poms.view_total_amount_requested().click()


@when(u'I click the View Total Amount button')
def step_impl(context):
    context.secret_page_poms.view_total_amount_button().click()


@when(u'I am shown an error i see an x icon')
def step_impl(context):
    context.secret_page_poms.error_icon_div().click()


@when(u'I am not logged in and see an error with an x icon')
def step_impl(context):
    context.secret_page_poms.login_error_icon_div().click()


@when(u'I click the View Total Continue button')
def step_impl(context):
    context.secret_page_poms.view_total_continue_button().click()


@when(u'I click "Cancel Reimbursement Request"')
def step_impl(context):
    context.secret_page_poms.cancel_reimbursement_request().click()


@when(u'I enter {reimbursement_request_id} of the request I would like to cancel')
def step_impl(context, reimbursement_request_id: int):
    context.secret_page_poms.enter_request_id_to_cancel().send_keys(reimbursement_request_id)


@when(u'I click the Cancel Request button')
def step_impl(context):
    context.secret_page_poms.cancel_request_button().click()


@when(u'I click the Cancel Request Continue button')
def step_impl(context):
    context.secret_page_poms.cancel_request_continue_button().click()


@when(u'I click "Log Out"')
def step_impl(context):
    context.secret_page_poms.log_out().click()


@when(u'I click the Log Out button')
def step_impl(context):
    context.secret_page_poms.log_out_button().click()


@when(u'I click the Log Out Continue button')
def step_impl(context):
    context.secret_page_poms.log_out_continue_button().click()


@then(u'I should be on a page with the title Super Secret Login')
def step_impl(context):
    assert context.driver.title == "Super Secret Login"
