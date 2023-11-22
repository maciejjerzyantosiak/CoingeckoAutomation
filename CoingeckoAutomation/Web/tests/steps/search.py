from behave import *
from CoingeckoAutomation.Web.tests.pages.coin_page import CoinPage
from CoingeckoAutomation.Web.tests.pages.home_page import HomePage


@given('I am on home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)

    print('Starting')
    assert 'https://www.coingecko.com/' == context.home_page.url
    assert 'Cryptocurrency Prices, Charts, and Crypto Market Cap | CoinGecko' == context.home_page.title


@when('I search for "{coin}"')
def step_impl(context, coin):
    context.home_page.search(coin)


@then('page should display "{coin}" page')
def step_impl(context, coin):
    context.coin_page = CoinPage(context.driver)
    print(context.coin_page.url)
    coin = coin.lower().split(' ')[0]
    assert f'https://www.coingecko.com/en/coins/{coin.lower()}' == context.coin_page.url
    assert coin == context.coin_page.coin_name.text.lower()

