from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Coingecko_Automation.tests.pages.base_page import BasePage
from Coingecko_Automation.tests.pages.locators import CoinPageLocators


class CoinPage(BasePage):

    @property
    def coin_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CoinPageLocators.COIN_TEXT),
            'Coin name is not visible'
        )

