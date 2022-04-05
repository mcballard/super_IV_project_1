from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class SecretPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "username")
        return element

    def password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitInfo")
        return element

    def login_continue_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/button[1]")
        return element

    def create_reimbursement_request(self):
        element: WebElement = self.driver.find_element(By.ID, "createCollapseButton")
        return element

    def select_reason(self):
        element = Select(self.driver.find_element(By.ID, "reason"))
        return element

    def enter_comment(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursement_request_comment")
        return element

    def enter_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def create_request_button(self):
        element: WebElement = self.driver.find_element(By.ID, "create_request")
        return element

    def create_request_continue_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/button[1]")
        return element

    def view_total_amount_requested(self):
        element: WebElement = self.driver.find_element(By.ID, "viewCollapseButton")
        return element

    def view_total_amount_button(self):
        element: WebElement = self.driver.find_element(By.ID, "viewTotal")
        return element

    def view_total_continue_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/button[1]")
        return element

    def cancel_reimbursement_request(self):
        element: WebElement = self.driver.find_element(By.ID, "cancelCollapseButton")
        return element

    def enter_request_id_to_cancel(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursement_request_id")
        return element

    def cancel_request_button(self):
        element: WebElement = self.driver.find_element(By.ID, "cancelRequest")
        return element

    def cancel_request_continue_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/button[1]")
        return element

    def log_out(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutCollapseButton")
        return element

    def log_out_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logOut")
        return element

    def log_out_continue_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/button[1]")
        return element 
