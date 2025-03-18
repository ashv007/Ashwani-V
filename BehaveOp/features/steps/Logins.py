from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

@given('I am on the Magento signup page')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize WebDriver
    context.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')  # Signup page
    time.sleep(2)  # Give time for page to load


@when('I enter valid first name, last name, email, and password')
def step_impl(context):
    context.driver.find_element(By.ID, 'firstname').send_keys('John')
    context.driver.find_element(By.ID, 'lastname').send_keys('Doe')
    context.driver.find_element(By.ID, 'email_address').send_keys('johndoe@gmail.com')
    context.driver.find_element(By.ID, 'password').send_keys('Password123!')
    context.driver.find_element(By.ID, 'password-confirmation').send_keys('Password123!')


@when('I click on "Create an Account"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.action.submit.primary').click()


@then('I should see a success message confirming my account creation')
def step_impl(context):
    time.sleep(3)  # Allow time for response
    success_message = context.driver.find_element(By.CSS_SELECTOR, '.message-success').text
    assert 'Thank you for registering' in success_message


@given('I am logged in to my account')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://magento.softwaretestingboard.com/customer/account/login/')  # Login page
    context.driver.find_element(By.ID, 'email').send_keys('johndoe@gmail.com')
    context.driver.find_element(By.ID, 'pass').send_keys('Password123!')
    context.driver.find_element(By.CSS_SELECTOR, 'button.action.login').click()
    time.sleep(3)  # Wait for login


@when('I click on the "Logout" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a.action.logout').click()


@then('I should be redirected to the home page')
def step_impl(context):
    time.sleep(2)
    assert context.driver.current_url == 'https://magento.softwaretestingboard.com/'  # Home page URL


@given('I am on the Magento login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://magento.softwaretestingboard.com/customer/account/login/')  # Login page


@when('I enter my registered email and password')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('johndoe@example.com')
    context.driver.find_element(By.ID, 'pass').send_keys('Password123!')


@when('I click on the "Sign In" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.action.login').click()


@then('I should be redirected to my account dashboard')
def step_impl(context):
    time.sleep(3)
    assert 'dashboard' in context.driver.current_url


@when('I enter my registered email and an incorrect password')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('johndoe@gmail.com')
    context.driver.find_element(By.ID, 'pass').send_keys('WrongPassword123!')


@then('I should see an error message saying "Invalid login credentials"')
def step_impl(context):
    time.sleep(2)
    error_message = context.driver.find_element(By.CSS_SELECTOR, '.error-msg').text
    assert 'Invalid login or password.' in error_message


@given('I am executing the Selenium test script')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://magento.softwaretestingboard.com/')  # Home page URL


@when('a test case fails')
def step_impl(context):
    # Trigger a failure intentionally for testing screenshot capture
    assert False


@then('the system should capture a screenshot and save it')
def step_impl(context):
    time.sleep(2)  # Allow time for failure to trigger
    screenshot_path = './screenshot.png'
    context.driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved to {screenshot_path}')
    context.driver.quit()
