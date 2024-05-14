from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    __ADDRESS_BUTTON = (By.ID, "addresses-link")
    __ORDERS_BUTTON = (By.ID, "history-link")
    __LOGOUT_BUTTON = (By.CLASS_NAME, "logout")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_addresses(self):
        self.click_element(self.__ADDRESS_BUTTON)

    def navigate_to_order_history(self):
        self.click_element(self.__ORDERS_BUTTON)

    def click_logout(self):
        self.click_element(self.__LOGOUT_BUTTON)
