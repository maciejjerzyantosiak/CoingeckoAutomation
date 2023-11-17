from tests.pages.base_page import BasePage
from tests.pages.locators import HomePageLocators
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    locators = {
                'search_bar': ('ID', 'search-bar')
    }

    def search(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, 'div.tw-flex tw-flex-row tw-items-center tw-px-2 2lg:tw-px-4 2lg:tw-py-2 tw-py-1 tw-shadow-sm 2lg:tw-shadow-none tw-rounded-lg')
        search_bar = self.driver.find_element(*HomePageLocators.SEARCH_BAR)
        search_bar.click()
        search = self.driver.find_element(*HomePageLocators.SEARCH_INPUT)
        search.clear()
        search.sendkeys('Bitcoin')
