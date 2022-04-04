from behave.runner import Context
from selenium.webdriver.safari.webdriver import WebDriver

from POMS.wiki_home import WikiHome


def before_all(context: Context):
    context.driver = WebDriver()
    context.wiki_home = WikiHome(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.close()
