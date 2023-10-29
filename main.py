import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver_conf():
    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome(options)
    return driver
