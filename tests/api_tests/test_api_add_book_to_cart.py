import allure
import jsonschema
from helper.load_schema import load_schema
from helper.api_requests import api_put


@allure.epic('API. Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added to cart")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_adding_book_to_cart():
    schema = load_schema('successful_adding_book_to_cart.json')

    url = "/cart/arts/add"
    art_ids = [69175546]
    headers = {"Content-Type": "application/json"}

    result = api_put(url, headers=headers, json={"art_ids": art_ids})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['payload']['data']['added_art_ids'] == art_ids
    assert result.json()['payload']['data']['failed_art_ids'] == []

