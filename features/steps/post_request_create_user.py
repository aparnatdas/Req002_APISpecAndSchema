from behave import *

import requests as req
import constants
import json


@given('User hits the endpoint with Request Type POST and payload {string_payload}')
def hits_the_endpoint_post_with_payload(context, string_payload):
    # Posting the user data
    payload = json.loads(string_payload)
    context.payload = payload
    post_response = req.post(constants.endpoint, payload)
    print("POST ", post_response.json())
    context.post_response = post_response


@when('The status code is {status_code:d}')
def verifies_the_status_code(context, status_code):
    # Verifying the status code
    response = context.post_response
    assert (response.status_code == status_code), "Problem Posting Data"

    # Passing the json data
    data = response.json()
    print(data)
    context.user_data = data


@then('The user validates the new data saved')
def validates_the_post_response_data(context):
    # Verifying if data is empty
    user_data = context.user_data
    assert user_data, "User Data is Empty !!"

    # Confirming if the data posted correctly
    print("User Data ", user_data)
    print("Payload : ", context.payload)

    assert (user_data['name'] == context.payload['name']), "Names doesnt match"
    assert (user_data['job'] == context.payload['job']), "Jobs doesnt match"
    assert (user_data['id']), "No id available"
    assert (user_data['createdAt']), "No createdAt data available"
