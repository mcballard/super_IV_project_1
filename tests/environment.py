from behave.runner import Context
from selenium.webdriver.firefox.webdriver import WebDriver
from tests.secret_page_POMS.secret_page_poms import SecretPage


def before_all(context: Context):
    context.driver = WebDriver()
    context.secret_page_poms = SecretPage(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.close()
