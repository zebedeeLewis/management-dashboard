from selenium.webdriver.common.by import By

class SamplePage:
    def __init__(self, driver):
        self.driver = driver

    def get_hello(self):
        hello_element = self.driver.find_element(By.ID, "hello")
        return hello_element.text
