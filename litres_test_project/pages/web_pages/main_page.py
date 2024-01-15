from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("")
        return self

    def filling_authorization_form(self, user):
        browser.element('[href="/pages/login/"]').should(be.visible).click()
        browser.element('[name="email"]').should(be.visible).type(user.email)
        browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
        browser.element('[name="pwd"]').should(be.visible).type(user.password)
        browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
        return self

    def user_must_be_authorized(self, user):
        browser.element('.AuthContent-module__button_2yWRs > [type="button"]').should(be.visible).click()
        browser.open("pages/personal_cabinet_about_me/")
        browser.element('span[class="user_header__name"]').should(have.text(user.name))
        return self

    def user_must_not_be_authorized(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.text('Неверное сочетание логина и '
                                                                                     'пароля'))
        return self

    def search_book_by_title(self, book):
        browser.element('[data-test-id="header__search-input--desktop"]').should(be.visible).type(book.name)
        browser.element('[data-test-id="header__search-button--desktop"]').should(be.visible).click()
        return self

    def book_with_specified_title_must_be_found(self):
        browser.element('[data-test-id="art__title--desktop"]').should(have.text('Семь сестер'))
        return self

    def search_book_by_author(self, book):
        browser.element('[data-test-id="header__search-input--desktop"]').should(be.visible).type(book.author)
        browser.element('[data-test-id="header__search-button--desktop"]').should(be.visible).click()
        return self

    def book_with_specified_author_must_be_found(self, book):
        browser.element('[data-test-id="art__authorName--desktop"]').should(have.text(book.author))
        return self


main_page = MainPage()
