from BasePage import BasePage
from selenium.webdriver.common.by import By


class SbisIndexLocators:
    LOCATOR_CONTACTS = (
        By.XPATH,
        '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a',
    )
    # LOCATOR_FOOTER = (
    #     By.XPATH,
    #     '',
    # )
    LOCATOR_DOWNLOAD = (
        By.LINK_TEXT,
        "Скачать СБИС",
    )


class SbisMainHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://sbis.ru/"

    def click_contacts(self):
        return self.find_element(SbisIndexLocators.LOCATOR_CONTACTS).click()

    def click_download(self):
        download_link_element = self.find_element(SbisIndexLocators.LOCATOR_DOWNLOAD)
        self.page_scroll(download_link_element)
        download_link_element.click()
