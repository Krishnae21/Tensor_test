from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisIndexLocators:
    LOCATOR_CONTACTS = (
        By.XPATH,
        '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a',
    )


class SbisMainHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_handler = driver.current_window_handle

    def click_contacts(self):
        return self.find_element(SbisIndexLocators.LOCATOR_CONTACTS).click()
