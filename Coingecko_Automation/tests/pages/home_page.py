from selenium.webdriver import Keys
from Coingecko_Automation.tests.pages.base_page import BasePage
from Coingecko_Automation.tests.pages.locators import HomePageLocators
import time


class HomePage(BasePage):

    def search(self, text):
        search_bar = self.driver.find_element(*HomePageLocators.SEARCH_BAR)
        search_bar.click()
        search_input = self.driver.find_element(*HomePageLocators.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(text)
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)


