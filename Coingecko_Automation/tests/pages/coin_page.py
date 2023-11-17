from Coingecko_Automation.tests.pages.base_page import BasePage
from Coingecko_Automation.tests.pages.locators import CoinPageLocators


class CoinPage(BasePage):
    @property
    def coin_name(self):
        return self.driver.find_element(*CoinPageLocators.COIN_TEXT).text
