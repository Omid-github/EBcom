import time

import pytest
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login(self, driver):

        login_page = LoginPage(driver)
        login_page.login("09391010015", "3492")
        time.sleep(2)
