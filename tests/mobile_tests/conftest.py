import os

import allure
import allure_commons
import pytest
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver
from litres_test_project.helper import attach_mobile


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


context = os.getenv('context', 'bstack')
username = os.getenv('USER_NAME')
access_key = os.getenv('ACCESS_KEY')
remote_browser_url = os.getenv('REMOTE_BROWSER_URL')
bstack_app_id = os.getenv('BSTACK_APP_ID')


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",

        # Set URL of the application under test
        "app": f"bs://{bstack_app_id}",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-litres-build",
            "sessionName": "BStack litres_test",

            # Set your access credentials
            "userName": username,
            "accessKey": access_key
        }
    })

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            remote_browser_url,
            options=options
        )

    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    attach_mobile.screenshot()

    attach_mobile.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    attach_mobile.bstack_video(session_id)
