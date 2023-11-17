from selenium import webdriver
from time import sleep

def before_scenario(context, scenario):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.coingecko.com/')
    context.driver = driver


def after_scenario(context, scenario):
    sleep(10)
    context.driver.quit()
