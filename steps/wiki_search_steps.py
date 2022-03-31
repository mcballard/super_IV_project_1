from behave import when, then
from selenium.webdriver.support.select import Select


@when(u'I enter {criteria} into the search bar')
def step_impl(context, criteria: str):
    context.wiki_home.search_input().send_keys(criteria)


@when(u'I select {language} as my language option')
def step_impl(context, language: str):
    select_element: Select = context.wiki_home.lang_selector()
    select_element.select_by_value(language)


@when(u'I click the search button')
def step_impl(context):
    context.wiki_home.search_button().click()


@then(u'I should be on a page with the title {title}')
def step_impl(context, title: str):
    assert context.driver.title == title
