Feature: User Registration and Login on Magento
  As a user
  I want to sign up and log in to my Magento account
  So that I can access my account dashboard

  Scenario: User successfully registers a new account
    Given I am on the Magento signup page
    When I enter valid first name, last name, email, and password
    And I click on "Create an Account"
    Then I should see a success message confirming my account creation

  Scenario: User logs out successfully
    Given I am logged in to my account
    When I click on the "Logout" button
    Then I should be redirected to the home page

  Scenario: User logs in with correct credentials
    Given I am on the Magento login page
    When I enter my registered email and password
    And I click on the "Sign In" button
    Then I should be redirected to my account dashboard

  Scenario: User fails to log in with an incorrect password
    Given I am on the Magento login page
    When I enter my registered email and an incorrect password
    And I click on the "Sign In" button
    Then I should see an error message saying "Invalid login credentials"

  Scenario: Capture screenshot on failure
    Given I am executing the Selenium test script
    When a test case fails
    Then the system should capture a screenshot and save it
