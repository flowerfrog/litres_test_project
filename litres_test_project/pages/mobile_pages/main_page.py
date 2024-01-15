from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


class AndroidMainPage:

    def selecting_application_language(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/title")).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/choosebutton")).click()
        return self

    def hiding_adult_content(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/btnDisableAdultContent")).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/btnConfirmDisableAdultContent")).click()
        return self
