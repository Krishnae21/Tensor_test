import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from Pages.SbisPages.SbisMainPage import SbisMainHelper
from Pages.SbisPages.SbisContactsPage import SbisContactsHelper


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome(options)
    yield driver
    driver.quit()


def test_1(browser):
    sbis_main_page = SbisMainHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_contacts()
    sbis_contacts_page = SbisContactsHelper(browser)
    sbis_contacts_page.click_clients()
    sbis_contacts_page.click_tensor()
