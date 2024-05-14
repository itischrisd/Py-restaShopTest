from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrdersPage(BasePage):
    __ORDER_STATUS = (By.CSS_SELECTOR, ".label.label-pill.bright")
    __ORDER_REFERENCE = (By.XPATH, "//th[@scope='row']")
    __ORDER_TOTAL_PRICE = (By.CSS_SELECTOR, ".text-xs-right")

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_order_status(self):
        order_statuses = self.get_present_elements(self.__ORDER_STATUS)
        return order_statuses[0].text

    def get_first_order_reference(self):
        order_references = self.get_visible_elements(self.__ORDER_REFERENCE)
        return order_references[0].text

    def get_first_order_total_price(self):
        order_total_prices = self.get_present_elements(self.__ORDER_TOTAL_PRICE)
        return order_total_prices[0].text
