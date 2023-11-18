from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument('--window-size=1920,1080')
    options.add_argument('headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.coingecko.com/')
    context.driver = driver


def after_scenario(context, scenario):
    context.driver.quit()
