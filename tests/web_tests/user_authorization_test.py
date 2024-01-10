import os
import allure
from dotenv import load_dotenv

from data.users import User
from pages.main_page import MainPage


@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_registered_user():
    main_page = MainPage()

    load_dotenv()
    user = User(
        name='Alexandra Osennyaya',
        email=os.getenv('USER_EMAIL'),
        password=os.getenv('USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has been authorized"):
        main_page.user_must_be_authorized(user)


@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_unregistered_user():
    main_page = MainPage()

    load_dotenv()
    user = User(
        name='test',
        email=os.getenv('UNREGISTERED_USER_EMAIL'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has not been authorized"):
        main_page.user_must_not_be_authorized()

