from behave import *

from pages.account_page import AccountPage
from pages.addresses_page import AddressesPage
from pages.new_address_page import NewAddressPage
from utils.assertion import assert_equals
from utils.screenshot import take_screenshot

use_step_matcher("parse")


@when("User navigates to the Addresses Page")
def step_impl(context):
    account_page = AccountPage(context.browser)
    account_page.navigate_to_addresses()


@step("User clicks on the new address link")
def step_impl(context):
    addresses_page = AddressesPage(context.browser)
    addresses_page.click_new_address_link()


@step('User fills in the address form with {name}, {surname}, {alias}, {address}, {city}, {code}, {country}, {phone}')
def step_impl(context, name, surname, alias, address, city, code, country, phone):
    new_address_page = NewAddressPage(context.browser)
    new_address_page.set_alias(alias)
    new_address_page.set_first_name(name)
    new_address_page.set_last_name(surname)
    new_address_page.set_address(address)
    new_address_page.set_city(city)
    new_address_page.set_postcode(code)
    new_address_page.set_country(country)
    new_address_page.set_phone(phone)

    context.stored_address = f"{alias}\n{name} {surname}\n{address}\n{city}\n{code}\n{country}\n{phone}"


@step("User submits the new address")
def step_impl(context):
    new_address_page = NewAddressPage(context.browser)
    new_address_page.click_save_button()


@step('Address with {alias} should be visible in the address list')
def step_impl(context, alias):
    addresses_page = AddressesPage(context.browser)
    assert_equals(addresses_page.find_address_by_alias(alias).text, context.stored_address)


@when('User deletes the address with {alias}')
def step_impl(context, alias):
    addresses_page = AddressesPage(context.browser)
    addresses_page.delete_address_by_alias(alias)


@then('Message {message} should be displayed')
def step_impl(context, message):
    addresses_page = AddressesPage(context.browser)
    take_screenshot(context.browser, message)
    assert_equals(addresses_page.get_success_alert_text(), message)
