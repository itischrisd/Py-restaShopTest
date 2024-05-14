from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    __LOGIN_INPUT = (By.NAME, "email")
    __PASSWORD_INPUT = (By.NAME, "password")
    __SIGN_IN_BUTTON = (By.ID, "submit-login")

    def __init__(self, driver):
        super().__init__(driver)

    def login_as(self, email, password):
        self.fill_input(self.__LOGIN_INPUT, email)
        self.fill_input(self.__PASSWORD_INPUT, password)
        self.click_element(self.__SIGN_IN_BUTTON)
