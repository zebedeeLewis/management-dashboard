import os
from time import sleep
from behave import *
from integrations.pages.sample import SamplePage

APP_PORT = os.environ.get('APP_PORT') or 7000
APP_SERVER = os.environ.get('APP_SERVER') or 'localhost'
TEST_APP_ADDRESS = 'http://' + APP_SERVER + ':' + str(APP_PORT) + '/app'

@given('we are on the sample page')
def step_impl(context):
    url = TEST_APP_ADDRESS
    context.driver.get(url)
    context.page = SamplePage(context.driver)

@when('we read the page text')
def step_impl(context):
    context.hello_text = context.page.get_hello()

@then('we see the text "Hello world"')
def step_impl(context):
    assert context.hello_text == "Hello world"
    sleep(5)
