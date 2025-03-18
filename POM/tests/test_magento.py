import pytest
from selenium import webdriver
from pages.signup_page import SignUpPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_magento_signup_and_login(driver):
    signup = SignUpPage(driver)
    signup.open_signup_page()
    signup.fill_signup_form("Test", "User", "gmail.com", "Password123")
    signup.submit_signup()
    time.sleep(3)  # Wait for the page to load
    signup.take_screenshot("screenshots/signup_success.png")

    login = LoginPage(driver)
    login.open_login_page()
    login.login("testuser123@gmail.com", "Password123")
    time.sleep(3)
    login.take_screenshot("screenshots/login_success.png")

    home = HomePage(driver)
    assert "Welcome" in home.get_welcome_message()
