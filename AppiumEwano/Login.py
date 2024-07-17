from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# Capabilities dictionary
cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "platformVersion": "14",
    "appPackage": "com.ebcom.ewano.sandbox",
    "appActivity": "com.ebcom.ewano.ui.activity.MainActivity",
    "automationName": "UiAutomator2",
    "newCommandTimeout": "500000"
}

# URL for the Appium server
url = 'http://127.0.0.1:4723/wd/hub'

# Create the driver
driver = webdriver.Remote(command_executor=url, options=AppiumOptions().load_capabilities(cap))


# Login function
def login(driver):
    driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/textInputEt").send_keys("09391010015")
    driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/btn").click()
    driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/etOtpNumber").send_keys("3492")
    driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/btn").click()


# Call the login function
login(driver)
