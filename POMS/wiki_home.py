from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class WikiHome:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def spanish(self):
        element: WebElement = self.driver.find_element(By.ID, "js-link-box-es")
        return element

    def search_input(self):
        element: WebElement = self.driver.find_element(By.ID, "searchInput")
        return element

    def lang_selector(self):
        element: Select = Select(self.driver.find_element(By.ID, "searchLanguage"))
        return element

    def search_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[3]/form/fieldset/button")
        return element
