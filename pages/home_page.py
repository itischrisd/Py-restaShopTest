from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    __SIGN_IN_BUTTON = (By.XPATH, "//a[@title='Log in to your customer account']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in_button(self):
        self.click_element(self.__SIGN_IN_BUTTON)

    def click_product(self, product_name):
        locator = (By.LINK_TEXT, product_name)
        self.click_element(locator)
