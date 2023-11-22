from selenium.webdriver.remote.webelement import WebElement

from CoingeckoAutomation.Web.tests.helpers.page_loader import get_visible_element, get_visible_elements, \
    wait_until_not_stale
from CoingeckoAutomation.Web.tests.pages.base_page import BasePage
from CoingeckoAutomation.Web.tests.pages.locators import HomePageLocators


class HomePage(BasePage):

    @property
    def search_bar(self):
        return get_visible_element(self.driver, HomePageLocators.SEARCH_BAR)

    @property
    def search_input(self):
        return get_visible_element(self.driver, HomePageLocators.SEARCH_INPUT)

    @property
    def search_item(self):
        return get_visible_element(self.driver, HomePageLocators.SEARCH_ITEM)

    @property
    def search_result(self):
        return get_visible_elements(self.driver, HomePageLocators.SEARCH_RESULTS)

    def select_item_from_result(self, element: WebElement, text: str) -> bool:
        elem = element.find_element(*HomePageLocators.SEARCH_ITEM)
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

        wait_until_not_stale(self.driver, HomePageLocators.SEARCH_ITEM)
        elements = self.search_result
        for elem in elements:
            if self.select_item_from_result(elem, text):
                break
