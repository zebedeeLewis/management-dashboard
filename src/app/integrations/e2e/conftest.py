import os
import pytest
from selenium import webdriver
from integrations.pages.sample import SamplePage

PORT = os.environ.get('PORT') or 7000
TEST_APP = os.environ.get('TEST_APP') or (
        'http://localhost:' + str(PORT) + '/')

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    url = TEST_APP
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture
def page(driver):
    return SamplePage(driver)
