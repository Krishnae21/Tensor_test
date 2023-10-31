import time
import re

from selenium.webdriver.common.by import By

from tests.BasePage import BasePage


class SbisDownloadLocators:
    LOCATOR_PLUGIN = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]",
    )
    LOCATOR_WINDOWS = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]",
    )
    LOCATOR_DOWNLOAD_LINK = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div["
        "2]/div/a",
    )


class SbisDownloadHelper(BasePage):
    def click_plugin(self):
        # Была проблема в интерактивности элемента,
        # пришлось добавить sleep(1) чтобы подождать отработку наведения мыши в драйвере
        elem = self.find_element(SbisDownloadLocators.LOCATOR_PLUGIN)
        self.move_to_element(elem)
        time.sleep(1)
        return elem.click()

    def click_windows_link(self):
        return self.find_element(SbisDownloadLocators.LOCATOR_WINDOWS).click()

    def get_plugin_download_link(self):
        return self.find_element(
            SbisDownloadLocators.LOCATOR_DOWNLOAD_LINK
        ).get_attribute("href")

    def get_plugin_size(self):
        text = self.find_element(SbisDownloadLocators.LOCATOR_DOWNLOAD_LINK).text
        pattern = r"\d+\.\d+"
        return float(re.findall(pattern, text)[0])
