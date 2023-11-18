from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
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

    @property
    def search_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.SEARCH_ITEM),
            'Search item is not visible'
        )

    @property
    def search_result(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(HomePageLocators.SEARCH_RESULTS),
            'Search results are not visible'
        )

    def select_item_from_result(self, element: WebElement, text: str) -> bool:
        WebDriverWait(self.driver, 10).until(EC.staleness_of(self.search_item))
        elem = self.search_item
        if text == elem.text:
            elem.click()
            return True
        else:
            return False

    def search(self, text):
        search_bar = self.search_bar
        search_bar.click()
        search_input = self.search_input
        search_input.clear()
        search_input.send_keys(text)

        elements = self.search_result
        for elem in elements:
            if self.select_item_from_result(elem, text):
                break
