import allure
from data.books import Book
from pages.book_page import BookPage


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added or removed from favorites")
def test_adding_book_to_favorites():
    book_page = BookPage()

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price=''
    )

    with allure.step("Open the book page"):
        book_page.open(book)

    with allure.step("Adding a book to favorites"):
        book_page.adding_book_to_favorites()

    with allure.step("Checking that the book has been added to favorites"):
        book_page.book_must_be_added_to_favorites(book)


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added or removed from favorites")
def test_removing_book_from_favorites():
    book_page = BookPage()

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price=''
    )

    with allure.step("Open the book page"):
        book_page.open(book)

    with allure.step("Adding a book to favorites"):
        book_page.adding_book_to_favorites()

    with allure.step("Removing a book to favorites"):
        book_page.removing_book_from_favorites()

    with allure.step("Checking that the book has been removed from favorites"):
        book_page.book_must_be_removed_from_favorites()

