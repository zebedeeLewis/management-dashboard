import os
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from dotenv import load_dotenv

load_dotenv()

SRC_DIR = Path(__file__).resolve().parent.parent.parent
LIBS_DIR = SRC_DIR / 'libs'

WEBDRIVER_SERVER = os.environ.get('WEBDRIVER_SERVER') or ''
SELENIUM_HUB = 'http://' + WEBDRIVER_SERVER + ':4444/wd/hub'
sys.path.append(str(LIBS_DIR))

def before_scenario(context, scenario):
    if WEBDRIVER_SERVER == '':
        driver = webdriver.Chrome()
    else:
        # options = FirefoxOptions()
        options = EdgeOptions()
        # options = ChromeOptions()

        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Remote(
                command_executor=SELENIUM_HUB,
                options=options,
                )

    context.driver = driver
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
