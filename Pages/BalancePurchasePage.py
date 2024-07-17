import time
from appium.webdriver.common.appiumby import AppiumBy


class BalancePurchasePage:
    def __init__(self, driver):
        self.driver = driver

    def BalancePurchaseHamrahi(self):
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/first_value_proposition_tv").click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/source_card_select_btn").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/textInputEt").send_keys("09190714723")
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/confirmButton").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.ebcom.ewano:id/imageGreenTickIcon\"])[3]").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/secondTitleTv\" and @text=\"تا ۳۵٪\"]").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id=\"com.ebcom.ewano:id/button\" and @text=\"۵۰,۰۰۰\"]").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/btn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        successful_purchase_text_elm = self.driver.find_element(by=AppiumBy.XPATH,value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/tvStatus\" and @text=\"موفق\"]")
        assert successful_purchase_text_elm.is_displayed()

    def BalancePurchaseMTN(self):
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/first_value_proposition_tv").click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/source_card_select_btn").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/textInputEt").send_keys("09190714723")
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/confirmButton").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                     value="(//android.widget.ImageView[@resource-id=\"com.ebcom.ewano:id/imageGreenTickIcon\"])[3]").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                     value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/secondTitleTv\" and @text=\"تا ۳۵٪\"]").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                     value="//android.widget.Button[@resource-id=\"com.ebcom.ewano:id/button\" and @text=\"۵۰,۰۰۰\"]").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/btn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        successful_purchase_text_elm = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/tvStatus\" and @text=\"موفق\"]")
        assert successful_purchase_text_elm.is_displayed()

    def BalancePurchaseRtell(self):
        self.driver.find_element().click()
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/first_value_proposition_tv").click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/source_card_select_btn").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/textInputEt").send_keys("09190714723")
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/confirmButton").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="(//android.widget.ImageView[@resource-id=\"com.ebcom.ewano:id/imageGreenTickIcon\"])[3]").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/secondTitleTv\" and @text=\"تا ۳۵٪\"]").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.Button[@resource-id=\"com.ebcom.ewano:id/button\" and @text=\"۵۰,۰۰۰\"]").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/btn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        successful_purchase_text_elm = self.driver.find_element(by=AppiumBy.XPATH,
                                                                value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/tvStatus\" and @text=\"موفق\"]")
        assert successful_purchase_text_elm.is_displayed()

    def BalancePurchase_CachedMobileNo(self):
        self.driver.find_element().click()
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/first_value_proposition_tv").click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/source_card_select_btn").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/textInputEt").send_keys("09190714723")
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/confirmButton").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="(//android.widget.ImageView[@resource-id=\"com.ebcom.ewano:id/imageGreenTickIcon\"])[3]").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/secondTitleTv\" and @text=\"تا ۳۵٪\"]").click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.Button[@resource-id=\"com.ebcom.ewano:id/button\" and @text=\"۵۰,۰۰۰\"]").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/btn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ID, value="com.ebcom.ewano:id/payBtn").click()
        time.sleep(5)
        successful_purchase_text_elm = self.driver.find_element(by=AppiumBy.XPATH,
                                                                value="//android.widget.TextView[@resource-id=\"com.ebcom.ewano:id/tvStatus\" and @text=\"موفق\"]")
        assert successful_purchase_text_elm.is_displayed()



