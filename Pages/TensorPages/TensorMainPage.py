from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TensorMainLocators:
    LOCATOR_MAN_POWER_BLOCK = (
        '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div'
    )
    LOCATOR_MAN_POWER_ABOUT = (
        '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
    )


class TensorMainHelper(BasePage):
    def get_man_power_block(self):
        return self.find_element(TensorMainLocators.LOCATOR_MAN_POWER_BLOCK)

    def click_man_power_about(self):
        return self.find_element(TensorMainLocators.LOCATOR_MAN_POWER_ABOUT).click()
