from selene import browser, be, have


class CartPage:
    def open(self):
        browser.open('my-books/cart/')
        return self

    def removing_book_to_cart(self):
        browser.element('[data-test-id="cart__listDeleteButton--desktop"]').should(be.visible).click()
        browser.element('.Modal-module__controls_1qN-h > .Button-module__button_primary_2FaKg').should(be.visible).click()
        return self

    def book_must_be_removed_from_cart(self):
        browser.element('.EmptyState-module__empty__title_22qdT').should(have.text('Корзина пуста'))
        return self

    def removing_book_to_cart_and_adding_to_favorites(self):
        browser.element('[data-test-id="cart__listDeleteButton--desktop"] > div').should(be.visible).click()
        browser.element('.Button-module__button_secondary_2G8Ew').should(be.visible).click()
        return self


cart_page = CartPage()
