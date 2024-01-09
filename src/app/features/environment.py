import sys

from pathlib import Path
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

SRC_DIR = Path(__file__).resolve().parent.parent.parent
LIBS_DIR = SRC_DIR / 'libs'

sys.path.append(str(LIBS_DIR))

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.close()
