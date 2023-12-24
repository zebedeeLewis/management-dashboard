import pytest
from selenium import webdriver
from pages.sample import SamplePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    url = 'http://localhost:4200/'
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture
def page(driver):
    return SamplePage(driver)
