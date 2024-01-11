import os
import allure
from dotenv import load_dotenv
import jsonschema
from helper.load_schema import load_schema
from helper.api_requests import api_post


@allure.epic('Authorized API')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_authorization_registered_user():
    schema = load_schema('successful_authorization.json')

    url = "/foundation/api/auth/login"
    load_dotenv()
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    headers = {"Content-Type": "application/json"}

    result = api_post(url, headers=headers, json={"login": email, "password": password})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['error'] is None


@allure.epic('Authorized API')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_authorization_unregistered_user():
    schema = load_schema('unsuccessful_authorization.json')

    url = "/foundation/api/auth/login"
    load_dotenv()
    email = os.getenv('USER_EMAIL')
    invalid_password = os.getenv('UNREGISTERED_USER_PASSWORD')
    headers = {"Content-Type": "application/json"}

    result = api_post(url, headers=headers, json={"login": email, "password": invalid_password})

    assert result.status_code == 401
    jsonschema.validate(result.json(), schema)
    assert result.json()['error']['type'] == "Unauthorized"
    assert result.json()['error']['title'] == "Incorrect user data"
