from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign In")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    SIGN_IN_BTN = (By.ID, "send2")

    def open_login_page(self):
        self.click(self.SIGN_IN_LINK)

    def login(self, email, password):
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_IN_BTN)
