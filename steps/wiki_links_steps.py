from behave import given, when, then


@given(u'I am on the Wikipedia homepage')
def step_impl(context):
    context.driver.get("https://www.wikipedia.org/")


@when(u'I click on the Spanish link')
def step_impl(context):
    context.wiki_home.spanish().click()


@then(u'I am on the Spanish Wikipedia page')
def ste_impl(context):
    assert context.driver.title == "Wikipedia, la enciclopedia libre"
