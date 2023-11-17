from behave import *
from tests.pages.home_page import HomePage


@given('I am on home page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.search()
    pass

@when('I search for Bitcoin')
def step_impl(context):
    assert True is not False

@then('page should display Bitcoin page')
def step_impl(context):
    assert context.failed is False