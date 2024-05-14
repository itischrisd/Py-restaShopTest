from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddressesPage(BasePage):
    __SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    __ADDRESSES = (By.CLASS_NAME, "address-body")
    __NEW_ADDRESS_LINK = (By.XPATH, "//a[@data-link-action='add-address']")
    __DELETE_BUTTONS = (By.XPATH, "//a[@data-link-action='delete-address']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_new_address_link(self):
        self.click_element(self.__NEW_ADDRESS_LINK)

    def get_success_alert_text(self):
        return self.get_visible_element(self.__SUCCESS_ALERT).text

    def find_address_by_alias(self, alias):
        addresses = self.get_visible_elements(self.__ADDRESSES)
        for address in addresses:
            if address.text.startswith(alias):
                return address
        return None

    def delete_address_by_alias(self, alias):
        addresses = self.get_visible_elements(self.__ADDRESSES)
        delete_buttons = self.get_visible_elements(self.__DELETE_BUTTONS)
        for address, button in zip(addresses, delete_buttons):
            if address.text.startswith(alias):
                button.click()
                break
        else:
            raise ValueError(f"Address with alias '{alias}' not found")
