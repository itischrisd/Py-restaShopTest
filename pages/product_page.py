from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class ProductPage(BasePage):
    __REGULAR_PRICE = (By.CSS_SELECTOR, ".regular-price")
    __DISCOUNT_PRICE = (By.CSS_SELECTOR, ".current-price-value")
    __SIZE_SELECT = (By.ID, "group_1")
    __QUANTITY_INPUT = (By.ID, "quantity_wanted")
    __ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart")
    __PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//div[@class='cart-content-btn']/a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_regular_price(self):
        return self.get_visible_element(self.__REGULAR_PRICE).text

    def get_discounted_price(self):
        return self.get_visible_element(self.__DISCOUNT_PRICE).text

    def select_size(self, size):
        size_element = Select(self.get_visible_element(self.__SIZE_SELECT))
        size_element.select_by_visible_text(size)

    def set_quantity(self, quantity):
        self.fill_input(self.__QUANTITY_INPUT, quantity)

    def click_add_to_cart_button(self):
        self.click_element(self.__ADD_TO_CART_BUTTON)

    def click_proceed_to_checkout_button(self):
        self.click_element(self.__PROCEED_TO_CHECKOUT_BUTTON)
