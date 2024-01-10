from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("")
        return self

    def filling_authorization_form(self, user):
        browser.element('a[href="/pages/login/"]').should(be.visible).click()
        browser.element('input[name="email"]').should(be.visible).type(user.email)
        browser.element('div.AuthContent-module__form__submit_jot-u > button[type="submit"]').should(be.visible).click()
        browser.element('input[name="pwd"]').should(be.visible).type(user.password)
        browser.element('div.AuthContent-module__form__submit_jot-u > button[type="submit"]').should(be.visible).click()
        return self

    def user_must_be_authorized(self, user):
        browser.element('div.AuthContent-module__button_2yWRs > button[type="button"]').should(be.visible).click()
        browser.open("pages/personal_cabinet_about_me/")
        browser.element('span[class="user_header__name"]').should(have.text(user.name))
        return self

    def user_must_not_be_authorized(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.text('Неверное сочетание логина и '
                                                                                     'пароля'))
        return self
