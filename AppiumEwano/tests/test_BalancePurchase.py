import time
import pytest
from Pages.LoginPage import LoginPage
from Pages.BalancePurchasePage import BalancePurchasePage


@pytest.mark.usefixtures("driver")
class TestBalancePurchase:

    def test_balancepurchaseHamrahi(self, driver):
        login_page = LoginPage(driver)
        login_page.login("09391010015", "3492")
        balancepurchase_page = BalancePurchasePage(driver)
        balancepurchase_page.BalancePurchaseHamrahi()

    def test_balancepurchaseMTN(self, driver):
        login_page = LoginPage(driver)
        login_page.login("09391010015", "3492")
        time.sleep(3)
        balancepurchase_page = BalancePurchasePage(driver)

    def test_balancepurchaseRtell(self, driver):
        login_page = LoginPage(driver)
        login_page.login("09391010015", "3492")
        time.sleep(3)
        balancepurchase_page = BalancePurchasePage(driver)

    def test_balancepurchase_CachedMobileNo(self, driver):
        login_page = LoginPage(driver)
        login_page.login("09391010015", "3492")
        time.sleep(3)
        balancepurchase_page = BalancePurchasePage(driver)
        



