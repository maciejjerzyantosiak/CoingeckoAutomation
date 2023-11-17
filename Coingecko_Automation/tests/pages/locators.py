from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_INPUT = By.ID, 'search-input-field'
    SEARCH_BAR = By.ID, 'search-bar'
    SEARCH_RESULTS = By.CSS_SELECTOR, 'li[class="tw-text-sm tw-font-medium tw-text-gray-700 dark:tw-text-white dark:tw-text-opacity-87"]'


class CoinPageLocators:
    COIN_TEXT = By.XPATH, '//span[@class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7 tw-ml-2 tw-mr-1"]'
