from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Coingecko_Automation.tests.pages.base_page import BasePage
from Coingecko_Automation.tests.pages.locators import HomePageLocators
import time


class HomePage(BasePage):

    @property
    def search_bar(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.SEARCH_BAR),
            'Search bar is not visible'
        )

    @property
    def search_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.SEARCH_INPUT),
            'Search input is not visible'
        )

    def search(self, text):
        search_bar = self.search_bar
        search_bar.click()
        time.sleep(10)
        search_input = self.search_input
        time.sleep(10)
        search_input.clear()
        time.sleep(10)
        search_input.send_keys(text)
        time.sleep(10)
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)


