from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver


class SecretPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def create_reimbursement_request(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/button[1]")
        return element


    def view_total_amount_requested(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/button[2]")
        return element


    def cancel_reimbursement_request(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/button[3]")
        return element


    def log_out(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/button[4]")
        return element
