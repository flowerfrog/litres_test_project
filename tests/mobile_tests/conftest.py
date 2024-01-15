import allure
import allure_commons
import pytest
from tests.mobile_tests import config
from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver
from litres_test_project.helper import attach_mobile


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",

        # Set URL of the application under test
        "app": "bs://0e40d78b8dd17360e059300c7b471a9477db3d5d",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-litres-build",
            "sessionName": "BStack litres_test",

            # Set your access credentials
            "userName": config.username,
            "accessKey": config.access_key
        }
    })

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_browser_url,
            options=options
        )

    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    attach_mobile.screenshot( )

    attach_mobile.page_source_xml( )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    attach_mobile.bstack_video(session_id)
