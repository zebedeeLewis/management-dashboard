import os
from time import sleep
from behave import *
from pages.sample import SamplePage

PORT = os.environ.get('PORT') or 7000
TEST_APP = os.environ.get('TEST_APP') or (
        'http://localhost:' + str(PORT) + '/')

@given('we are on the sample page')
def step_impl(context):
    url = TEST_APP
    context.driver.get(url)
    context.page = SamplePage(context.driver)

@when('we read the page text')
def step_impl(context):
    context.hello_text = context.page.get_hello()

@then('we see the text "Hello world"')
def step_impl(context):
    assert context.hello_text == "Hello world"
    sleep(5)
