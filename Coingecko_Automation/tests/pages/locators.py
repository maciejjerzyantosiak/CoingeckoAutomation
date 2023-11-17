from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_INPUT = By.ID, 'search-input-field'
    SEARCH_BAR = By.CSS_SELECTOR, 'div.tw-flex tw-flex-row tw-items-center tw-px-2 2lg:tw-px-4 2lg:tw-py-2 tw-py-1 tw-shadow-sm 2lg:tw-shadow-none tw-rounded-lg'
