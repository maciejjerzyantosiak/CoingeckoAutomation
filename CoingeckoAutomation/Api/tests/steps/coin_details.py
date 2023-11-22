from behave import *
import requests
import urllib.parse
import re


@given('I want to get information about "{coin}"')
def step_impl(context, coin):
    context.coin = coin


@when('I send get request')
def step_impl(context):
    context.coin_id = re.findall(r'\((.*?)\)', context.coin)[0]
    url = context.url + f'/coins/{context.coin_id}'
    context.response = requests.get(url)


@then('I should receive correct response')
def step_impl(context):
    response_body = context.response.json()
    assert response_body['id'] == context.coin_id
    assert context.coin.lower().split(' ')[0] in response_body['name'].lower()
    assert context.response.status_code == 200

