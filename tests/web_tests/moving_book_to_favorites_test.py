import allure
from litres_test_project.data.books import Book
from litres_test_project.pages.web_pages.book_page import book_page


@allure.epic('Move book to/from favorites')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added or removed from favorites")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_book_to_favorites():

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


@allure.epic('Move book to/from favorites')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added or removed from favorites")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_removing_book_from_favorites():

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
