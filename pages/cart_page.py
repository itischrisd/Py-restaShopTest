from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    __PROCEED_TO_CHECKOUT_BUTTON = (By.LINK_TEXT, "PROCEED TO CHECKOUT")
    __CONTINUE_ADDRESS_BUTTON = (By.NAME, "confirm-addresses")
    __DELIVERY_OPTION_RADIO = (By.CLASS_NAME, "carrier-name")
    __CONTINUE_DELIVERY_OPTION_BUTTON = (By.NAME, "confirmDeliveryOption")
    __PAYMENT_OPTION = (By.XPATH, "//div[@class='payment-option clearfix']/label/span")
    __TERMS_OF_SERVICE_CHECKBOX = (By.ID, "conditions_to_approve[terms-and-conditions]")
    __PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.center-block")
    __TOTAL_PRICE = (By.XPATH, "//tr[contains(@class, 'total-value')]/td[last()]")
    __ORDER_REFERENCE = (By.ID, "order-reference-value")

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed_to_checkout_button(self):
        self.click_element(self.__PROCEED_TO_CHECKOUT_BUTTON)

    def click_continue_address_button(self):
        self.click_element(self.__CONTINUE_ADDRESS_BUTTON)

    def select_delivery_option(self, delivery_option):
        delivery_options = self.get_visible_elements(self.__DELIVERY_OPTION_RADIO)
        for option in delivery_options:
            if option.text == delivery_option:
                option.click()
                break

    def click_continue_delivery_option_button(self):
        self.click_element(self.__CONTINUE_DELIVERY_OPTION_BUTTON)

    def select_payment_method(self, payment_method):
        payment_options = self.get_visible_elements(self.__PAYMENT_OPTION)
        for option in payment_options:
            if option.text == payment_method:
                option.click()
                break

    def click_terms_of_service_checkbox(self):
        checkbox = self._driver.find_element(*self.__TERMS_OF_SERVICE_CHECKBOX)
        checkbox.click()

    def click_place_order_button(self):
        self.click_element(self.__PLACE_ORDER_BUTTON)

    def get_total_price(self):
        return self.get_visible_element(self.__TOTAL_PRICE).text

    def get_order_reference(self):
        return self.get_visible_element(self.__ORDER_REFERENCE).text
