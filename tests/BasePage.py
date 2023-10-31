from abc import ABC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = None

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def check_url(self):
        return self.base_url in self.driver.current_url

    @staticmethod
    def get_element_html(element):
        return element.get_attribute("outerHTML")

    def page_scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_handle(self):
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            if self.base_url in self.driver.current_url:
                break

    def get_actual_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def wait_url_pattern(self, pattern, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.url_matches(pattern),
            message=f"Reference pattern not found",
        )

    def js_click(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def move_to_element(self, element):
        self.visibility_wait(element, 10)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def visibility_wait(self, element, wait=1):
        return WebDriverWait(self.driver, wait).until(
            EC.visibility_of(element),
            message=f"Reference pattern not found",
        )
