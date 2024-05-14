from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class NewAddressPage(BasePage):
    __ALIAS_INPUT = (By.NAME, "alias")
    __FIRST_NAME_INPUT = (By.NAME, "firstname")
    __LAST_NAME_INPUT = (By.NAME, "lastname")
    __ADDRESS_INPUT = (By.NAME, "address1")
    __CITY_INPUT = (By.NAME, "city")
    __POSTCODE_INPUT = (By.NAME, "postcode")
    __PHONE_INPUT = (By.NAME, "phone")
    __COUNTRY_SELECT = (By.NAME, "id_country")
    __SAVE_BUTTON = (By.CLASS_NAME, "form-control-submit")

    def __init__(self, driver):
        super().__init__(driver)

    def set_alias(self, alias):
        self.fill_input(self.__ALIAS_INPUT, alias)

    def set_first_name(self, first_name):
        self.fill_input(self.__FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.fill_input(self.__LAST_NAME_INPUT, last_name)

    def set_address(self, address):
        self.fill_input(self.__ADDRESS_INPUT, address)

    def set_city(self, city):
        self.fill_input(self.__CITY_INPUT, city)

    def set_postcode(self, postcode):
        self.fill_input(self.__POSTCODE_INPUT, postcode)

    def set_phone(self, phone):
        self.fill_input(self.__PHONE_INPUT, phone)

    def set_country(self, country):
        country_element = Select(self.get_visible_element(self.__COUNTRY_SELECT))
        country_element.select_by_visible_text(country)

    def click_save_button(self):
        self.click_element(self.__SAVE_BUTTON)
