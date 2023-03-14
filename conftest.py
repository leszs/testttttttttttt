import pytest
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    yield browser

    browser.quit()