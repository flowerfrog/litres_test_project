from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class AndroidBookPage:

    def adding_book_to_saved(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/bookPostpone")).click()
        return self

    def go_to_saved_tab(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/nav_my_audiobooks")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "SAVED")).click()
        return self

    def book_must_be_added_to_saved(self):
        (browser.element((AppiumBy.ID, "ru.litres.android:id/bookName"))
         .should(have.text("The Adventures of Tom Sawyer")))
        return self

    def removing_book_from_saved(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/bookName")).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/bookPostpone")).click()
        return self

    def book_must_be_removed_from_saved(self):
        results = browser.all((AppiumBy.ID, 'ru.litres.android:id/empty_view'))
        results.should(have.size(1))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/action_button')).should(be.visible)
        return self


book_page = AndroidBookPage()
