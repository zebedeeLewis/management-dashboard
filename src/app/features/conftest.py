import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from integrations.pages.sample import SamplePage
from integrations.utils.helpers import driver_ids, init_driver

APP_PORT = os.environ.get('APP_PORT') or 7000
APP_SERVER = os.environ.get('APP_SERVER') or 'localhost'
TEST_APP_ADDRESS = 'http://' + APP_SERVER + ':' + str(APP_PORT) + '/app'

WEBDRIVER_SERVER = os.environ.get('WEBDRIVER_SERVER') or ''
SELENIUM_HUB = 'http://' + WEBDRIVER_SERVER + ':4444/wd/hub'

@pytest.fixture(ids=driver_ids, params=[
    ('chome', ChromeOptions()),
    ('edge', FirefoxOptions()),
    ('firefox', EdgeOptions()),
    ])
def driver(request):
    driver = init_driver(
        bool(WEBDRIVER_SERVER),
        lambda o : webdriver.Remote(
            command_executor=SELENIUM_HUB, options=o),
        webdriver.Chrome,
        request.param[1] )

    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    return SamplePage(driver)
