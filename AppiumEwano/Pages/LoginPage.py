import time
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, mobile_no, otp):
        self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        time.sleep(10)
        self.driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/btnEnter").click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/textInputEt").send_keys(mobile_no)
        self.driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/btn").click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/etOtpNumber").send_keys(otp)
        time.sleep(11)
        self.driver.find_element(AppiumBy.ID, "com.ebcom.ewano:id/btn").click()
        time.sleep(5)