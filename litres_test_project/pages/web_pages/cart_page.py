from selene import browser, be, have


class CartPage:
    def open(self):
        browser.open('my-books/cart/')
        return self

    def removing_book_to_cart(self):
        browser.element('button[data-test-id="cart__listDeleteButton--desktop"] > div').should(be.visible).click()
        browser.element('//*[@id="modal"]/div[2]/div/div/div/div/div[3]/button[1]/div/div/div').should(be.visible).click()
        return self

    def book_must_be_removed_from_cart(self):
        browser.element('.EmptyState-module__empty__title_22qdT').should(have.text('Корзина пуста'))
        return self

    def removing_book_to_cart_and_adding_to_favorites(self):
        browser.element('button[data-test-id="cart__listDeleteButton--desktop"] > div').should(be.visible).click()
        browser.element('//*[@id="modal"]/div[2]/div/div/div/div/div[3]/button[2]/div/div/div').should(be.visible).click()
        return self
