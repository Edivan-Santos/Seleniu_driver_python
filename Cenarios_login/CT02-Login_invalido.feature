Feature: Login invalido

Scenario: Unsuccessful Login with invalid credentials
    Given I am on the login page
    When I enter invalid username "invaliduser" and password "invalidpassword"
    And I click the login button
    Then I should see an error message "Invalid username or password"