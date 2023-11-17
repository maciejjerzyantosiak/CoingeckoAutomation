from behave import *

from tests.pages import coin_page
from tests.pages.coin_page import CoinPage
from tests.pages.home_page import HomePage


@given('I am on home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)

    assert 'https://www.coingecko.com/' == context.home_page.url
    assert 'Cryptocurrency Prices, Charts, and Crypto Market Cap | CoinGecko' == context.home_page.title


@when('I search for "{coin}"')
def step_impl(context, coin):
    context.home_page.search(coin)


@then('page should display "{coin}" page')
def step_impl(context, coin):
    context.coin_page = CoinPage(context.driver)
    assert coin == context.coin_page.coin_name

