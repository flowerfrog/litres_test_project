import allure
from litres_test_project.pages.mobile_pages import AndroidMainPage
from litres_test_project.pages.mobile_pages import AndroidSearchBookPage


@allure.epic('Search')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the book search in mobile app")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_successful_searching_book(android_mobile_management):
    main_page = AndroidMainPage()
    book_page = AndroidSearchBookPage()

    with allure.step('Selecting the application language'):
        main_page.selecting_application_language()

    with allure.step('Hiding the adult content'):
        main_page.hiding_adult_content()

    with allure.step('Type search'):
        book_page.searching_book()

    with allure.step('Verify content found'):
        book_page.book_must_be_found()


@allure.epic('Search')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the book search in mobile app")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_unsuccessful_searching_book(android_mobile_management):
    main_page = AndroidMainPage()
    book_page = AndroidSearchBookPage()

    with allure.step('Selecting the application language'):
        main_page.selecting_application_language()

    with allure.step('Hiding the adult content'):
        main_page.hiding_adult_content()

    with allure.step('Type search'):
        book_page.searching_non_existent_book()

    with allure.step('Verify content not found'):
        book_page.book_must_not_be_found()
