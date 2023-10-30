import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Pages.TensorPages.TensorAboutPage import TensorAboutHelper
from Pages.TensorPages.TensorMainPage import TensorMainHelper
from Pages.SbisPages.SbisContactsPage import SbisContactsHelper
from Pages.SbisPages.SbisMainPage import SbisMainHelper
from Pages.SbisPages.SbisDownloadPage import SbisDownloadHelper
from OtherFunctions import Functions

if "__main__" == __name__:
    options = Options()
    options.add_argument("--start-maximized")
    browser = Chrome(options)
    sbis_main_page = SbisMainHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_download()
    sbis_download_page = SbisDownloadHelper(browser)
    sbis_download_page.click_plugin()
    sbis_download_page.click_windows_link()
    link = sbis_download_page.get_plugin_download_link()
    size = sbis_download_page.get_plugin_size()
    file_size = round(Functions.download_file(link).__sizeof__() / 1048576, 2)
    assert file_size == size
    input()
