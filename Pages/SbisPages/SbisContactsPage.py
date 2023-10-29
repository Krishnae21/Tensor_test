from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisContactsLocators:
    LOCATOR_CLIENTS = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div',
    )
    LOCATOR_TENSOR_IMG = (
        By.XPATH,
        '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img',
    )


class SbisContactsHelper(BasePage):
    def click_clients(self):
        return self.find_element(SbisContactsLocators.LOCATOR_CLIENTS).click()

    def click_tensor(self):
        return self.find_element(SbisContactsLocators.LOCATOR_TENSOR_IMG).click()
