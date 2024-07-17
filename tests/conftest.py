import time

import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common.base import AppiumOptions


@pytest.fixture(scope="function")
def driver():
    # Capabilities dictionary
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "platformVersion": "14",
        "appPackage": "com.ebcom.ewano",
        "appActivity": "com.ebcom.ewano.ui.activity.MainActivity",
        "automationName": "UiAutomator2",
        "newCommandTimeout": "500000"
    }

    # URL for the Appium server
    url = 'http://127.0.0.1:4723/wd/hub'

    # Create the driver
    driver = webdriver.Remote(command_executor=url, options=AppiumOptions().load_capabilities(cap))
    time.sleep(2)
    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the driver after tests are done
    driver.quit()
