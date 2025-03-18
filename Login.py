import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver (Ensure chromedriver.exe is in your path)
driver = webdriver.Chrome()
driver.maximize_window()


# Generate a random email to avoid duplicate accounts
def generate_email():
    return "testuser" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + "@gmail.com"


test_email = generate_email()
test_password = "Test@1234"

try:
    # Open Magento Signup Page
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

    # Fill Signup Form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstname"))).send_keys("Test")
    driver.find_element(By.ID, "lastname").send_keys("User")
    driver.find_element(By.ID, "email_address").send_keys(test_email)
    driver.find_element(By.ID, "password").send_keys(test_password)
    driver.find_element(By.ID, "password-confirmation").send_keys(test_password)
    driver.find_element(By.CSS_SELECTOR, "button[title='Create an Account']").click()

    # Wait for account creation success
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "message-success")))
    print("Account created successfully with email:", test_email)

    # Log Out
    driver.get("https://magento.softwaretestingboard.com/customer/account/logout/")
    time.sleep(3)

    # Open Login Page
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

    # Perform Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(test_email)
    driver.find_element(By.ID, "pass").send_keys(test_password)
    driver.find_element(By.ID, "send2").click()

    # Validate Login Success
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "logged-in")))
    print("Login successful!")

except Exception as e:
    print("Test Failed:", e)


finally:
    time.sleep(20)
    driver.quit()
