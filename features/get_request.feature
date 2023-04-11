Feature: Verify GET Request Type

  Scenario: Get User by ID
    Given User hits the endpoint with Request Type GET and UserId 2
    When The status code is 200 and the response is retrieved with right data
    Then The user validates the data against the User