Feature: Verify POST Request Type

  Scenario: Creating user with POST
    Given User hits the endpoint with Request Type POST and payload {"name":"morpheus","job":"leader"}
    When The status code is 201
    Then The user validates the new data saved