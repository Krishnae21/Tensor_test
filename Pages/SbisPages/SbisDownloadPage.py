from BasePage import BasePage
from selenium.webdriver.common.by import By
import re


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
        "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
    )


class SbisDownloadHelper(BasePage):
    def click_plugin(self):
        elem = self.find_element(SbisDownloadLocators.LOCATOR_PLUGIN)
        return self.action_click(elem)

    def click_windows_link(self):
        elem = self.find_element(SbisDownloadLocators.LOCATOR_WINDOWS)
        return self.action_click(elem)

    def get_plugin_download_link(self):
        return self.find_element(
            SbisDownloadLocators.LOCATOR_DOWNLOAD_LINK
        ).get_attribute("href")

    def get_plugin_size(self):
        text = self.find_element(SbisDownloadLocators.LOCATOR_DOWNLOAD_LINK).text
        pattern = r"\d+\.\d+"
        return float(re.findall(pattern, text)[0])
