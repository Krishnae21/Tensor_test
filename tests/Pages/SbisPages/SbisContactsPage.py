from tests.BasePage import BasePage
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
    LOCATOR_REGION = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span',
    )
    LOCATOR_PARTNERS = (
        By.XPATH,
        '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div',
    )
    LOCATOR_REGIONS_SELECT = (
        By.XPATH,
        '//*[@id="popup"]/div[2]/div/div[2]/div/ul/li',
    )


class SbisContactsHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://sbis.ru/contacts/"

    def click_for_clients(self):
        return self.find_element(SbisContactsLocators.LOCATOR_CLIENTS).click()

    def click_for_clients_tensor(self):
        return self.find_element(SbisContactsLocators.LOCATOR_TENSOR_IMG).click()

    def get_region_element(self):
        return self.find_element(SbisContactsLocators.LOCATOR_REGION)

    def get_parters(self):
        return self.find_elements(SbisContactsLocators.LOCATOR_PARTNERS)

    def select_region(self, region):
        self.get_region_element().click()
        regions = self.find_elements(SbisContactsLocators.LOCATOR_REGIONS_SELECT)
        for reg in regions:
            if region in self.get_element_html(reg):
                reg.click()
                break
