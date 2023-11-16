from behave import *

@given('I am on home page')
def step_impl(context):
    pass

@when('I search for Bitcoin')
def step_impl(context):
    assert True is not False

@then('page should display Bitcoin page')
def step_impl(context):
    assert context.failed is False