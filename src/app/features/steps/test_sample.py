import os

from time import sleep
from pytest_bdd import scenarios, given, when, then

from integrations.pages.sample import SamplePage

APP_PORT = os.environ.get('APP_PORT') or 7000
APP_SERVER = os.environ.get('APP_SERVER') or 'localhost'
TEST_APP_ADDRESS = 'http://' + APP_SERVER + ':' + str(APP_PORT) + '/app'

scenarios('../features/sample.feature')

@given('we are on the sample page', target_fixture='on_sample_page')
def step_impl(driver):
    url = TEST_APP_ADDRESS
    driver.get(url)
    return SamplePage(driver)

@when('we read the page text', target_fixture='hello_text')
def step_impl(on_sample_page):
    return on_sample_page.get_hello()

@then('we see the text "Hello world"')
def step_impl(hello_text):
    assert hello_text == "Hello world"
    sleep(5)
