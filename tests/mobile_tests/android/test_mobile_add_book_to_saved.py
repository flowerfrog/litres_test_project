import allure
import pytest

from litres_test_project.pages.mobile_pages.main_page import main_page
from litres_test_project.pages.mobile_pages.books_to_read_page import book_search_page
from litres_test_project.pages.mobile_pages.book_page import book_page


@allure.epic('Add book to saved')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added to saved in mobile app")
@allure.severity('normal')
@allure.label('layer', 'mobile')
@pytest.mark.xfail(reason="App Automate testing time has expired")
def test_adding_book_to_saved(android_mobile_management):

    with allure.step('Selecting the application language'):
        main_page.selecting_application_language()

    with allure.step('Hiding the adult content'):
        main_page.hiding_adult_content()

    with allure.step('Type search'):
        book_search_page.searching_book()

    with allure.step('Choosing a book'):
        book_search_page.choosing_book()

    with allure.step('Adding a book to Saved'):
        book_page.adding_book_to_saved()

    with allure.step('Go to the Saved tab'):
        book_page.go_to_saved_tab()

    with allure.step('Checking that the selected book has been added to Saved'):
        book_page.book_must_be_added_to_saved()
