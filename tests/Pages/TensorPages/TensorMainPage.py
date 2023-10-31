from tests.BasePage import BasePage
from selenium.webdriver.common.by import By


class TensorMainLocators:
    LOCATOR_MAN_POWER_BLOCK = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[5]',
    )
    LOCATOR_MAN_POWER_ABOUT = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a',
    )


class TensorMainHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://tensor.ru/"

    def get_man_power_block(self):
        return self.find_element(TensorMainLocators.LOCATOR_MAN_POWER_BLOCK)

    def click_man_power_about(self):
        element = self.find_element(TensorMainLocators.LOCATOR_MAN_POWER_ABOUT)
        self.page_scroll(element)
        return self.find_element(TensorMainLocators.LOCATOR_MAN_POWER_ABOUT).click()
