from BasePage import BasePage
from selenium.webdriver.common.by import By


class TensorAboutLocators:
    LOCATOR_WORK_BLOCK = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')
    LOCATOR_WORK_IMAGES_BLOCK = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[4]/div[2]',
    )
    LOCATOR_WORK_IMAGES_BLOCKS = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[4]/div[2]/div',
    )


class TensorAboutHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://tensor.ru/about"

    def get_work_block(self):
        return self.find_element(TensorAboutLocators.LOCATOR_WORK_BLOCK)

    def get_work_images_block(self):
        return self.find_element(TensorAboutLocators.LOCATOR_WORK_IMAGES_BLOCK)

    def get_work_images_blocks(self):
        blocks = self.find_elements(TensorAboutLocators.LOCATOR_WORK_IMAGES_BLOCKS)
        return [image.find_element(By.XPATH, "//a/div[1]/img") for image in blocks]
