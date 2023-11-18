from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(options=options)
    #driver.maximize_window()
    driver.get('https://www.coingecko.com/')
    context.driver = driver


def after_scenario(context, scenario):
    sleep(10)
    context.driver.quit()
