import allure
from data.books import Book
from pages.web_pages.book_page import BookPage


@allure.epic('Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_book_to_cart():
    book_page = BookPage()

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price='339 ₽'
    )

    with allure.step("Open the book page"):
        book_page.open(book)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Checking that the book has been added to the cart"):
        book_page.book_must_be_added_to_cart(book)


@allure.epic('Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a books has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_books_to_cart():
    book_page = BookPage()

    book1 = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price='339 ₽'
    )

    book2 = Book(
        name='Семь сестер. Сестра тени',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-sestra-teni-57182608/',
        price='429 ₽'
    )

    with allure.step("Open the first book page"):
        book_page.open(book1)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Open the second book page"):
        book_page.open(book2)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Checking that the books has been added to the cart"):
        book_page.books_must_be_added_to_cart(book1, book2)
