from selene import browser, be, have


class BookPage:
    def open(self, book):
        browser.open(f"book/{book.url}")
        return self

    def adding_book_to_cart(self):
        browser.element('button[data-test-id="book__addToCartButton--desktop"]').should(be.visible).click()
        browser.element('div.Modal-module__content__header_3fkP_ > div > div > svg > use').should(be.visible).click()
        return self

    def book_must_be_added_to_cart(self, book):
        browser.open("my-books/cart/")
        browser.element('h3[data-test-id="cart__bookCardTitle--wrapper"]').should(have.text(book.name))
        browser.element('div[data-test-id="cart__bookCardAuthor--wrapper"]').should(have.text(book.author))
        browser.element('div[data-test-id="cart__bookCardDiscount--wrapper"]').should(have.text(book.price))
        return self

    def adding_books_to_cart(self):
        browser.element('button[data-test-id="book__addToCartButton--desktop"]').should(be.visible).click()
        browser.element('div.Modal-module__content__header_3fkP_ > div > div > svg > use').should(be.visible).click()
        return self

    def books_must_be_added_to_cart(self, book1, book2):
        browser.open("my-books/cart/")
        browser.element(f'h3 > a[href="/book/{book2.url}"]').should(have.text(book2.name))
        browser.element('div:nth-child(1) > div.Cart-module__bookCard__author_20vL8').should(have.text(book2.author))
        browser.element('div:nth-child(1) > div.Cart-module__bookCard__price_336CO').should(have.text(book2.price))
        browser.element(f'h3 > a[href="/book/{book1.url}"]').should(have.text(book1.name))
        browser.element('div:nth-child(2) > div.Cart-module__bookCard__author_20vL8').should(have.text(book1.author))
        browser.element('div:nth-child(2) > div.Cart-module__bookCard__price_336CO').should(have.text(book1.price))
        return self

    def adding_book_to_favorites(self):
        browser.element('ul > li:nth-child(2) > button > div').should(be.visible).click()
        return self

    def book_must_be_added_to_favorites(self, book):
        browser.open("my-books/liked/")
        browser.element('a[data-test-id="art__title--desktop"]').should(have.text(book.name))
        browser.element('a[data-test-id="art__authorName--desktop"]').should(have.text(book.author))
        return self

    def removing_book_from_favorites(self):
        browser.open("my-books/liked/")
        browser.element('div.ArtV2Default-module__like_button_1VLId > div').should(be.visible).click()
        browser.element('//*[@id=":r4:"]/div/div/div[3]').should(be.visible).click()
        return self

    def book_must_be_removed_from_favorites(self):
        browser.element('.EmptyState-module__empty__content_2lpJ-').should(have.text('Здесь будет все, что вы '
                                                                                     'отложите на потом'))
        return self
