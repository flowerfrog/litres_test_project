import allure

from data.books import Book
from pages.book_page import BookPage
from pages.cart_page import CartPage


@allure.epic('Remove book from cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_removing_book_from_cart():
    book_page = BookPage()
    cart_page = CartPage()

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

    with allure.step("Open the cart page"):
        cart_page.open()

    with allure.step("Removing the selected book from cart"):
        cart_page.removing_book_to_cart()

    with allure.step("Checking that the book has been removed from cart"):
        cart_page.book_must_be_removed_from_cart()


@allure.epic('Remove book from cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_removing_book_from_cart_and_adding_to_favorites():
    book_page = BookPage()
    cart_page = CartPage()

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

    with allure.step("Open the cart page"):
        cart_page.open()

    with allure.step("Removing the selected book from cart and adding book to favorites"):
        cart_page.removing_book_to_cart_and_adding_to_favorites()

    with allure.step("Checking that the book has been removed from cart"):
        cart_page.book_must_be_removed_from_cart()

    with allure.step("Checking that the book has been removed from cart"):
        cart_page.book_must_be_removed_from_cart()

    with allure.step("Checking that the book has been added to favorites"):
        book_page.book_must_be_added_to_favorites(book)
