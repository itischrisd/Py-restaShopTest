from behave import given, use_step_matcher

from pages.home_page import HomePage
from pages.login_page import LoginPage

use_step_matcher("parse")


@given("User is logged into Presta shop")
def step_impl(context):
    context.browser.get("https://prod-kurs.coderslab.pl/")
    HomePage(context.browser).click_sign_in_button()
    LoginPage(context.browser).login_as("jankowalski01@mymail.de", "Pass1231")
