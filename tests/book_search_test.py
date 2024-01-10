import allure
from data.books import Book
from pages.main_page import MainPage


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the book search on the main page")
def test_searching_of_book_by_title():
    main_page = MainPage()

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='',
        price=''
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Enter the name of the book in the search and click the Find button"):
        main_page.search_book_by_title(book)

    with allure.step("Checking that books with the specified title are found in the search"):
        main_page.book_with_specified_title_must_be_found()


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the book search on the main page")
def test_searching_of_book_by_author():
    main_page = MainPage()

    book = Book(
        name='',
        author='Люсинда Райли',
        url='',
        price=''
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Enter the author of the book in the search and click the Find button"):
        main_page.search_book_by_author(book)

    with allure.step("Checking that books with the specified author are found in the search"):
        main_page.book_with_specified_author_must_be_found(book)
