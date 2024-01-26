import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from integrations.pages.sample import SamplePage

APP_PORT = os.environ.get('APP_PORT') or 7000
APP_SERVER = os.environ.get('APP_SERVER') or 'localhost'
TEST_APP_ADDRESS = 'http://' + APP_SERVER + ':' + str(APP_PORT) + '/app'

WEBDRIVER_SERVER = os.environ.get('WEBDRIVER_SERVER') or ''
SELENIUM_HUB = 'http://' + WEBDRIVER_SERVER + ':4444/wd/hub'

def driver_ids(param):
    return param[0]

@pytest.fixture(ids=driver_ids, params=[
    ('chome', ChromeOptions()),
    ('edge', FirefoxOptions()),
    ('firefox', EdgeOptions()),
    ])
def driver(request):

    if WEBDRIVER_SERVER == '':
        driver = webdriver.Chrome()
    else:
        options = request.param[1]

        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Remote(
                command_executor=SELENIUM_HUB,
                options=options,
                )

    # url = TEST_APP_ADDRESS
    # driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    return SamplePage(driver)
