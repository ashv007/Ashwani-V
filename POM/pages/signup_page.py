from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUpPage(BasePage):
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create an Account")
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[@title='Create an Account']")

    def open_signup_page(self):
        self.click(self.CREATE_ACCOUNT_LINK)

    def fill_signup_form(self, first_name, last_name, email, password):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, password)

    def submit_signup(self):
        self.click(self.CREATE_ACCOUNT_BTN)
