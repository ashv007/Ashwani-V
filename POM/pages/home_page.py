from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    WELCOME_MSG = (By.XPATH, "//span[@class='logged-in']")

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MSG)
