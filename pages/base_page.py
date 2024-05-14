from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    __LOGO_BUTTON = (By.CSS_SELECTOR, "a > img.logo")
    __ACCOUNT_BUTTON = (By.CLASS_NAME, "account")

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def get_visible_element(self, locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def get_visible_elements(self, locator):
        return self._wait.until(ec.visibility_of_all_elements_located(locator))

    def get_present_elements(self, locator):
        return self._wait.until(ec.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self._wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def click_logo_button(self):
        self.click_element(self.__LOGO_BUTTON)

    def click_account_button(self):
        self.click_element(self.__ACCOUNT_BUTTON)

    def fill_input(self, locator, text):
        element = self.get_visible_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
