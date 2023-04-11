from behave import *

import requests as req
import constants


@given('User hits the endpoint with Request Type GET and UserId {user_id:d}')
def hits_the_endpoint_get_user(context, user_id):
    context.user_id = user_id
    params = {"id": user_id}
    response = req.get(constants.endpoint, params)
    context.response = response


@when('The status code is {status_code:d} and the response is retrieved with right data')
def verifies_the_response_code(context, status_code):
    # Verifying the response code
    response = context.response
    assert (response.status_code == status_code), "Problem Fetching Data"

    # Passing the json data
    data = response.json()
    print(data)
    context.user_data = data


@then('The user validates the Data against the User')
def validates_the_data_against_the_user(context):
    # Verifying if data is empty
    user_data = context.user_data
    assert user_data, "User Data is Empty !!"

    # Confirming if the User ID's match
    expected_user_id = context.user_id
    actual_user_id = user_data['data']['id']
    print("Expected UserID = ", expected_user_id)
    print("Actual UserID = ", actual_user_id)
    assert (expected_user_id == actual_user_id), "User ID's doesnt match !!"

    # Validating the User Data
    user_specific_data = user_data['data']
    print("User Data :- ")
    print("User ID : ", user_specific_data['id'])
    print("Email : ", user_specific_data['email'])
    print("First Name : ", user_specific_data['first_name'])
    print("Last Name : ", user_specific_data['last_name'])

    # Checking if support data is available or not
    assert user_data['support'], "Support data not available"
