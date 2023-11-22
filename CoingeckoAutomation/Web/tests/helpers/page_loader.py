from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_visible_element(driver, locator):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator),
        f'{locator[0]} is not visible'
    )


def get_visible_elements(driver, locator):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(locator),
        f'{locator[0]} is not visible'
    )


def wait_until_not_stale(driver, locator):
    try:
        WebDriverWait(driver, 15).until(EC.staleness_of(get_visible_element(driver, locator)))
    except TimeoutException as e:
        print('Timeout occurred while waiting for item results')
        pass
